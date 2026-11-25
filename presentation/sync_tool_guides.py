"""Refresh source models or distribute finished guides to sibling catalogues."""
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
    recipes = list(get_tool_assemblies().values())
    recipes.extend(extra for recipe in list(recipes) for extra in recipe.get("additional_tools", []))
    for recipe in recipes:
        tool_id = recipe["tool_id"]
        folder = tools_root / "parts" / tool_id
        source = yaml.safe_load((folder/"working.yaml").read_text(encoding="utf-8"))
        expected_kind = recipe.get("model_kind", "photo_reference")
        if source["model_kind"] != expected_kind or expected_kind == "holder_envelope" or source["id"] != tool_id:
            raise ValueError(f"Expected the OOMP {expected_kind} model for {tool_id}")
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
        "Each guide shows OOMP tool models in their printed holder. Two-piece wall holders include an exploded view, and bit blocks include a top view. The booklets print on landscape A4 paper. Physical fit is unverified.", "",
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
        write_file(base_index/(identifier+".pdf"), guide)
        write_file(tools_refs/(identifier+".pdf"), guide)
        tool = recipe["tool_id"]
        tool_ids = [tool, *(extra["tool_id"] for extra in recipe.get("additional_tools", []))]
        tool_links = " · ".join(
            f"[OOMP record](https://github.com/oomlout/oomp_tool_version_5/tree/main/parts/{tool_id})"
            for tool_id in tool_ids
        )
        readme = f"{project_url}/blob/main/parts/{identifier}/README.md#assembly"
        index.append(f"| [{recipe['label']}]({readme}) | [Download PDF]({identifier}.pdf) | {tool_links} |")
    write_file(base_index/"README.md", "\n".join(index)+"\n")
    subprocess.run([
        sys.executable, "-c",
        "import sys; from import_tool_references import collect_holders; "
        "collect_holders(holder_root=sys.argv[1], include_previews=False)",
        str(ROOT),
    ], cwd=tools_root, check=True)
    for stage in ("working_oomp_populate.py", "working_oomp.py"):
        subprocess.run([sys.executable, stage], cwd=tools_root, check=True)
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

