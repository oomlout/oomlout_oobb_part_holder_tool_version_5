"""Refresh the four source models or distribute finished guides to sibling catalogues."""
import argparse
import io
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from holder_catalogue import records, write_file
from working_oomp_populate import get_tool_assemblies


def import_models(**kwargs):
    tools_root = kwargs["tools_root"]
    fields = ["id", "title", "model_kind", "model_note", "md5", "md5_6_alpha", "holders"]
    for recipe in get_tool_assemblies().values():
        tool_id = recipe["tool_id"]
        folder = tools_root / "parts" / tool_id
        source = yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))
        if source["model_kind"] != "photo_reference" or source["id"] != tool_id:
            raise ValueError(f"Expected the OOMP photo model for {tool_id}")
        destination = ROOT / "source_file/tool_models" / tool_id
        for name in ("working.glb", "working.stl"):
            write_file(destination/name, (folder/"three_d_model"/name).read_bytes())
        metadata = {key: source[key] for key in fields}
        write_file(destination/"source.json", json.dumps(metadata, indent=2, ensure_ascii=False)+"\n")


def export_guides(**kwargs):
    tools_root = kwargs["tools_root"]
    base_root = kwargs["base_root"]
    base_index = base_root / "presentation/tool-holders"
    tools_refs = tools_root / "source_file/tool_references/holders"
    project_url = "https://github.com/oomlout/oomlout_oobb_part_holder_tool_version_5"
    index = [
        "# Tool-holder loading guides", "",
        "Each guide shows a photo-based OOMP tool model lowered into a two-piece wall holder. In the exploded view the front half moves away from the wall to reveal the pocket. The booklets print on landscape A4 paper. Physical fit is unverified.", "",
        f"[Tool-holder project README and assembly instructions]({project_url}#assembly)", "",
        "| Holder README | Print booklet | Tool model |", "| --- | --- | --- |",
    ]
    for identifier, folder, part in records():
        recipe = part.get("assembly_details")
        buffer = io.BytesIO()
        with Image.open(folder/"3dpr_presentation.png") as img:
            img.thumbnail((880,550), Image.Resampling.LANCZOS)
            img.convert("RGB").save(buffer, format="JPEG", quality=92)
        write_file(tools_refs/(identifier+".jpg"), buffer.getvalue())
        if not recipe:
            continue
        guide = (folder/"assembly/assembly_instructions.pdf").read_bytes()
        write_file(base_index/(part["model"]+".pdf"), guide)
        write_file(tools_refs/(identifier+".pdf"), guide)
        tool = recipe["tool_id"]
        url = "https://github.com/oomlout/oomp_tool_version_5/tree/main/parts/" + tool
        readme = f"{project_url}/blob/main/parts/{identifier}/README.md#assembly"
        index.append(f"| [{recipe['label']}]({readme}) | [Download PDF]({part['model']}.pdf) | [OOMP record]({url}) |")
    write_file(base_index/"README.md", "\n".join(index)+"\n")
    subprocess.run([sys.executable, "working_action.py"], cwd=tools_root, check=True)
    subprocess.run([sys.executable, "presentation/scripts/build_project_thumbnails.py", "--filter", "tool-holders",
                    "--projects-root", str(ROOT.parent)], cwd=base_root, check=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["import-models", "export-guides"])
    parser.add_argument("--tools-root", type=Path, default=ROOT.parent/"oomp_tool_version_5")
    parser.add_argument("--base-root", type=Path, default=ROOT.parent/"oomlout_oobb_version_5")
    args = vars(parser.parse_args())
    action = args.pop("action")
    if action == "import-models":
        import_models(**args)
    else:
        export_guides(**args)

