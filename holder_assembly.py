"""Build tool-loaded CAD sheets and the four OOBB loading booklets."""
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont
import trimesh

from holder_catalogue import ROOT, records, write_file
from presentation import assembly_booklet, assembly_viewer

STUDIO = ROOT / "presentation"
REFERENCES = ROOT / "source_file" / "tool_models"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_pose(**kwargs):
    holder = trimesh.load_mesh(kwargs["holder"])
    tool = trimesh.load_mesh(kwargs["tool"])
    recipe = kwargs["recipe"]
    rotation = trimesh.transformations.euler_matrix(*np.radians(recipe["rotation_deg"]))
    tool.apply_transform(rotation)
    tool.apply_translation(recipe["translation_mm"])
    if not (holder.is_volume and tool.is_volume):
        raise ValueError("The pose check requires closed production solids")
    overlap = trimesh.boolean.intersection([holder, tool], engine="manifold")
    volume = abs(float(overlap.volume)) if len(overlap.faces) else 0.0
    if volume > 0.0001:
        raise ValueError(f"{recipe['label']} intersects the printed holder by {volume:g} mm³")
    # A lifted or misplaced tool can also have zero overlap. Check that its nose
    # occupies the recessed space below the rim, inside the holder footprint.
    half = holder.extents / 2
    probe = trimesh.creation.box([holder.extents[0], holder.extents[1], holder.bounds[1,2]])
    probe.apply_translation([0, 0, holder.bounds[1,2] / 2])
    seated = trimesh.boolean.intersection([probe, tool], engine="manifold")
    occupied = float(seated.volume) if len(seated.faces) else 0.0
    if occupied < 1:
        raise ValueError(f"{recipe['label']} misses the pocket")
    return {
        "holder_intersection_mm3": volume,
        "tool_volume_inside_pocket_mm3": round(occupied, 3),
        "physical_fit": "Unverified. The OOMP model uses provisional photograph-based dimensions.",
    }


def make_sheet(**kwargs):
    raw = kwargs["raw"]
    title = kwargs["title"]
    sheet = Image.new("RGB", (1280, 724), "#f6f4ef")
    for index, name in enumerate(("book_cover", "loaded_top")):
        with Image.open(raw / (name + ".png")) as source:
            image = source.convert("RGBA")
            box = image.getchannel("A").getbbox()
            image = image.crop(box)
            image.thumbnail((590, 518), Image.Resampling.LANCZOS)
            sheet.paste(image, (320 + 640*index - image.width//2, 332-image.height//2), image)
    draw = ImageDraw.Draw(sheet)
    draw.text((25, 16), title, font=ImageFont.load_default(size=29), fill="#243a3b")
    draw.text((26, 615), "Seated tool", font=ImageFont.load_default(size=21), fill="#243a3b")
    draw.text((665, 615), "Pocket alignment", font=ImageFont.load_default(size=21), fill="#243a3b")
    draw.text((26, 682), "OOMP photo-based tool model · Physical fit unverified · AI-generated CAD illustration.",
              font=ImageFont.load_default(size=17), fill="#536361")
    buffer = io.BytesIO()
    sheet.save(buffer, format="PNG")
    return buffer.getvalue()


def publish_book(**kwargs):
    folder = kwargs["folder"]
    part = kwargs["part"]
    output = kwargs["output"]
    recipe = part["assembly_details"]
    reference = REFERENCES / recipe["tool_id"]
    source = json.loads((reference / "source.json").read_text(encoding="utf-8"))
    source_url = "https://github.com/oomlout/oomp_tool_version_5/tree/main/parts/" + source["id"]
    fit = verify_pose(holder=folder/"3dpr.stl", tool=reference/"working.stl", recipe=recipe)
    parts = {
        "holder": {
            "key": "holder",
            "id": part["id"],
            "name": "Printed holder",
            "quantity": 1,
        },
        "tool": {
            "key": "tool",
            "id": source["id"],
            "name": recipe["label"],
            "quantity": 1,
            "md5": source["md5"],
            "md5_6_alpha": source["md5_6_alpha"],
            "short_label": "oom.lt/a/" + source["md5_6_alpha"],
            "short_url": "https://oom.lt/a/" + source["md5_6_alpha"],
            "identity_source": source_url,
        },
    }
    steps = []
    added = []
    for number, step in enumerate(recipe["steps"], start=1):
        added.extend(step["add"])
        steps.append({
            **step,
            "title": f"Loading operation {number}",
            "number": number,
            "loose_parts": dict.fromkeys(step["add"], 1),
        })
    if sorted(added) != sorted(parts):
        raise ValueError("Each physical item must enter the assembly once")
    title = recipe["label"] + " holder"
    details = [
        f"{part['width']} × {part['height']} OOBB grid. Printed thickness {part['depth']/2:g} mm.",
        "Use one printed holder and one tool. These views show loading the pocket face-up.",
        recipe["alignment"], recipe["check"], source["model_note"],
        "Digital check: the seated tool occupies the pocket with no measurable solid overlap.",
        "AI-generated CAD images and instructions. Physical fit has yet to be tested.",
    ]
    data = {
        "configuration_title": title,
        "style": recipe["style"],
        "book": {
            "cover_title": title,
            "cover_subtitle": "Loading the tool into its single-place OOBB holder",
            "project_name": ROOT.name + " / OOMP tool reference",
            "project_url": source_url,
            "details_title": "Tool and holder",
            "details": details,
            "summary_title": "Printed part",
            "hardware_title": "Workshop tool",
            "summary_view": "loaded_top",
            "signature_pages": 4,
            "summary_step": True,
            "viewer_start": "step-01",
            "logo_svg": "source_file/tool_models/oomlout-LOGO-unshaded-vector.svg",
            "logo_symbol_subpaths": 3,
        },
        "parts": parts,
        "steps": steps,
        "physical_item_count": 2,
        "printed_keys": ["holder"],
        "pose": {
            "rotation_deg": recipe["rotation_deg"],
            "translation_mm": recipe["translation_mm"],
        },
        "fit_check": fit,
        "source_sha256": {
            "holder_stl": digest(folder / "3dpr.stl"),
            "tool_glb": digest(reference / "working.glb"),
            "tool_stl": digest(reference / "working.stl"),
            "logo": digest(REFERENCES / "oomlout-LOGO-unshaded-vector.svg"),
        },
    }
    assembly_booklet.publish(output=output, data=data)
    assembly_booklet.review_outputs(output=output, data=data)
    assembly_viewer.publish(output=output, data=data)
    sequence = "\n".join(f"{s['number']}. {s['action']}" for s in steps)
    notes = f"""# {title}

AI-generated CAD images and instructions. Errors possible.

[Offline step viewer](assembly_instructions.html) · [Print booklet](assembly_instructions.pdf) · [Holder files](../)

![Tool seated in the printed holder](../3dpr_presentation.png)

## Loading sequence

{sequence}

## Model and fit

{source['model_note']} The illustrated pose was checked against the production STL at the original model scale. Physical fit remains unverified. [OOMP tool record]({source_url})

The PDF uses eight landscape A4 pages in reader order. Choose booklet printing for folded copies.
"""
    write_file(output / "ASSEMBLY.md", notes)
    inventory = io.StringIO(newline="")
    writer = csv.writer(inventory)
    writer.writerow(["item", "id", "quantity", "source", "short_url"])
    for item in parts.values():
        writer.writerow([item["name"], item["id"], item["quantity"], item.get("identity_source", ""), item.get("short_url", "")])
    write_file(output / "parts.csv", inventory.getvalue())
    return make_sheet(raw=output/"render/raw", title=title)


def build_assemblies(**kwargs):
    selected = kwargs.get("filter", "")
    force = kwargs.get("force", False)
    blender = kwargs.get("blender") or os.environ.get("BLENDER_EXE") or shutil.which("blender")
    scripts = [Path(__file__), STUDIO/"assembly_booklet.py", STUDIO/"assembly_viewer.py",
               STUDIO/"assembly_viewer.html", STUDIO/"render_loaded.py", STUDIO/"render_holder.py"]
    inputs = [digest(p) for p in scripts]
    for _, folder, part in records(filter=selected):
        recipe = part.get("assembly_details")
        if not recipe:
            continue
        reference = REFERENCES / recipe["tool_id"]
        assets = [folder/"3dpr.stl", reference/"working.glb", reference/"working.stl", reference/"source.json",
                  REFERENCES/"oomlout-LOGO-unshaded-vector.svg"]
        key = hashlib.sha256(json.dumps([inputs, [digest(p) for p in assets], part], sort_keys=True).encode()).hexdigest()
        cache = ROOT / "build" / "assembly" / folder.name
        cache.mkdir(parents=True, exist_ok=True)
        stamp = cache / "outputs.json"
        previous = json.loads(stamp.read_text()) if stamp.is_file() else {}
        if not force and previous.get("key") == key and all(
            (folder/name).is_file() and digest(folder/name) == value for name, value in previous["files"].items()
        ):
            continue
        if not blender:
            installed = sorted(Path("C:/Program Files/Blender Foundation").glob("Blender */blender.exe"))
            if not installed:
                raise FileNotFoundError("Set BLENDER_EXE to render the tool in its holder")
            blender = str(installed[-1])
        with tempfile.TemporaryDirectory(dir=cache) as scratch:
            work = Path(scratch)
            output = work / "assembly"
            job = {
                "holder": str(folder/"3dpr.stl"),
                "tool": str(reference/"working.glb"),
                "output": str(output/"render/raw"),
                "recipe": recipe,
            }
            batch = work/"job.json"
            batch.write_text(json.dumps([job]))
            print(f"Building illustrated guide for {recipe['label']}", flush=True)
            with (cache/"blender.log").open("w") as log:
                subprocess.run([blender,"--background","--python-exit-code","1","--python",str(STUDIO/"render_loaded.py"),
                                "--",str(batch)],stdout=log,stderr=subprocess.STDOUT,check=True)
            sheet = publish_book(folder=folder, part=part, output=output)
            write_file(work/"3dpr_presentation.png", sheet)
            published = {}
            for src in [work/"3dpr_presentation.png", *sorted(output.rglob("*"))]:
                if src.is_file():
                    name = src.relative_to(work).as_posix()
                    write_file(folder/name, src.read_bytes())
                    published[name] = digest(src)
            result = {
                "key": key,
                "files": published,
            }
            write_file(stamp, json.dumps(result, indent=2))

