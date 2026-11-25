"""Publish OOBB studio sheets made from the canonical print meshes."""
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont
import trimesh

import holder_layers
from holder_catalogue import ROOT, records, write_file, cli_options


def render_parts(**kwargs):
    selected = kwargs.get("filter", "")
    force = kwargs.get("force", False)
    executable = kwargs.get("blender") or os.environ.get("BLENDER_EXE") or shutil.which("blender")
    worker = ROOT / "presentation" / "render_holder.py"
    cache = ROOT / "build" / "renders"
    jobs = []
    sheets = []
    cache.mkdir(parents=True, exist_ok=True)
    for part_id, folder, part in records(filter=selected):
        if part.get("assembly_details"):
            continue
        mesh = folder / "3dpr.stl"
        construction = part["construction"]
        label = f"{part['title']}  ·  {part['layout'].replace('_', ' ')}"
        key = hashlib.sha256(mesh.read_bytes() + worker.read_bytes() + Path(__file__).read_bytes()
                             + Path(holder_layers.__file__).read_bytes() + json.dumps(construction).encode() + label.encode()).hexdigest()
        directory = cache / key
        sheet = folder / "3dpr_presentation.png"
        stamp = directory / "image.sha256"
        if not force and sheet.exists() and stamp.exists():
            if stamp.read_text() == hashlib.sha256(sheet.read_bytes()).hexdigest():
                continue
        directory.mkdir(exist_ok=True)
        layers = holder_layers.assembled_layers(mesh=trimesh.load_mesh(mesh), construction=construction)
        sources = []
        for number, layer in enumerate(layers, start=1):
            path = directory / f"layer_{number}.stl"
            write_file(path, layer.export(file_type="stl"))
            sources.append(str(path))
        job = {
            "sources": sources,
            "directory": str(directory),
        }
        jobs.append(job)
        sheets.append((directory, sheet, label, layers))
    if not jobs:
        return
    if not executable:
        installed = sorted(Path("C:/Program Files/Blender Foundation").glob("Blender */blender.exe"))
        if not installed:
            raise FileNotFoundError("Set BLENDER_EXE or add Blender to PATH")
        executable = str(installed[-1])
    print(f"Rendering {len(jobs)} tool holders", flush=True)
    with tempfile.TemporaryDirectory(dir=cache) as scratch:
        batch = Path(scratch) / "jobs.json"
        batch.write_text(json.dumps(jobs))
        log_path = cache / "blender.log"
        with log_path.open("w") as log:
            subprocess.run([executable, "--background", "--python-exit-code", "1",
                            "--python", str(worker), "--", str(batch)], check=True,
                           stdout=log, stderr=subprocess.STDOUT)
    for directory, sheet, label, layers in sheets:
        canvas = Image.new("RGB", (1280, 724), "#f6f4ef")
        for index, view in enumerate(("angle", "detail")):
            with Image.open(directory / f"{view}.png") as source:
                image = source.convert("RGBA")
                canvas.paste(image, (640 * index, 24), image)
        draw = ImageDraw.Draw(canvas)
        draw.text((26, 15), label, font=ImageFont.load_default(size=26), fill="#243a3b")
        dimensions = " x ".join(f"{v:.1f}".removesuffix(".0") for v in trimesh.util.concatenate(layers).extents)
        caption = "Wall-mounted holder" if len(layers) == 2 else "Assembled holder"
        draw.text((26, 615), caption, font=ImageFont.load_default(size=21), fill="#243a3b")
        legend = "Exploded view - two printed halves" if len(layers) == 2 else "Top view - single-piece holder"
        draw.text((665, 615), legend, font=ImageFont.load_default(size=21), fill="#243a3b")
        draw.text((26, 655), f"Assembled dimensions   {dimensions} mm",
                  font=ImageFont.load_default(size=21), fill="#243a3b")
        draw.text((26, 692), "AI-generated CAD illustration. Errors possible.",
                  font=ImageFont.load_default(size=15), fill="#536361")
        buffer = io.BytesIO()
        canvas.save(buffer, format="PNG")
        binary = buffer.getvalue()
        write_file(sheet, binary)
        write_file(directory / "image.sha256", hashlib.sha256(binary).hexdigest())


if __name__ == "__main__":
    from holder_assembly import build_assemblies
    options = cli_options()
    render_parts(**options)
    build_assemblies(**options)

