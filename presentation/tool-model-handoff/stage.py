"""Refresh Terra's local modelling packets from the two active catalogue manifests."""
from collections import defaultdict
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import sys

from PIL import Image
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from holder_catalogue import write_file

BAHCO = "https://www.bahco.com/int_en/metric-flat-combination-wrenches-with-chrome-finish-pb_111m_.html"


def read_records(root):
    ids = (root / "parts_source/catalogue.txt").read_text().splitlines()
    return {
        key: yaml.safe_load((root / "parts" / key / "working.yaml").read_text(encoding="utf-8"))
        for key in ids
    }


def brief_for(**kwargs):
    tool = kwargs["tool"]
    briefs = kwargs["briefs"]
    key = tool["key"]
    dimensions = tool.get("parameters", {})
    if tool["model_kind"] == "hex_key":
        return (f"Use the existing {dimensions['across_flats_mm']} mm across-flats hex section. "
                f"Check the {dimensions['long_arm_mm']} mm and {dimensions['short_arm_mm']} mm arm lengths. "
                "Seat the long arm in the matching bore, then orient the short arm to clear adjacent sizes. "
                "Derive the order independently for the forward and reversed sets.")
    if key.startswith("tool_screwdriver_hex_m"):
        return (f"Use the {dimensions['across_flats_mm']} mm hex tip and {dimensions['shaft_diameter_mm']} mm "
                "shaft from this record's own datasheet. Compare the grip to the local photograph. "
                "Seat the shaft down and leave the rotating cap clear. Use screwdriver_precision_tall in holder taxonomy.")
    return briefs[key]


def stage(**kwargs):
    tools_root = kwargs.get("tools_root", ROOT.parent / "oomp_tool_version_5")
    briefs = yaml.safe_load((HERE / "briefs.yaml").read_text(encoding="utf-8"))
    references = yaml.safe_load((HERE / "references.yaml").read_text(encoding="utf-8"))
    tools = read_records(tools_root)
    holders = read_records(ROOT)
    memberships = defaultdict(dict)
    for tool_id, tool in tools.items():
        for holder in tool["holders"]:
            memberships[holder["id"]][tool_id] = holder["quantity"]
    if memberships.keys() != holders.keys():
        raise ValueError(f"Unmapped holder IDs: {memberships.keys() ^ holders.keys()}")
    layouts = {}
    for holder_id, part in sorted(holders.items()):
        manifest = ROOT / "parts" / holder_id / "assembly/assembly_manifest.json"
        loaded_ids = []
        if manifest.is_file():
            guide = json.loads(manifest.read_text(encoding="utf-8"))
            loaded_ids = [item["id"] for key, item in guide["parts"].items() if key not in guide["printed_keys"]]
        layouts[holder_id] = {
            "construction": part["construction"],
            "members_and_quantities": memberships[holder_id],
            "published_guide_tools": loaded_ids,
            "occupancy": "alternate tools in one pocket" if part["profile"] == "tool_knife_utility_17_mm_blade" else "simultaneous",
            "source": f"parts/{holder_id}/working.yaml",
            "production_stl": f"parts/{holder_id}/3dpr.stl",
            "positioned_pockets_and_repeat_settings": part["oobb_details"],
        }
    write_file(HERE / "layouts.yaml", yaml.safe_dump(layouts, sort_keys=False, allow_unicode=True))
    index = [
        "# Tool modelling queue", "",
        f"{len(tools)} tool packets cover {len(layouts)} production layouts. Each packet includes the tool brief, evidence, dimensional inputs, holder IDs, quantities and outstanding views.",
        "", "[Agent instructions](AGENTS.md) · [Launch prompt](LAUNCH.md) · [Layout placements and dependencies](layouts.yaml) · [Outstanding evidence](OUTSTANDING.md)", "",
        "| Tool packet | Model | Loaded layouts for this tool |", "| --- | --- | ---: |",
    ]
    for tool_id, tool in sorted(tools.items()):
        key = tool["key"]
        folder = tools_root / "parts" / tool_id
        drawing = f"resources/{key}.svg"
        write_file(HERE / drawing, (folder / "working.svg").read_bytes())
        evidence = []
        for path in sorted(folder.iterdir()):
            if path.suffix.lower() in (".jpg", ".cdr", ".pdf") or path.name.startswith(("measurements.", "photo_overlay.", "research_")):
                evidence.append({
                    "path_from_tools_repo": path.relative_to(tools_root).as_posix(),
                    "sha256": sha256(path.read_bytes()).hexdigest(),
                })
        images = sorted(folder.glob("*.jpg"))
        preview = None
        if images:
            preview = f"resources/{key}.jpg"
            with Image.open(images[0]) as raw:
                raw.thumbnail((640, 640))
                output = BytesIO()
                raw.convert("RGB").save(output, format="JPEG", quality=88)
            write_file(HERE / preview, output.getvalue())
        pending = []
        guided = []
        for holder in tool["holders"]:
            target = guided if tool_id in layouts[holder["id"]]["published_guide_tools"] else pending
            target.append({
                "id": holder["id"],
                "quantity": holder["quantity"],
                "layout": holder["layout"],
            })
        leads = list(references.get(key, []))
        if key.startswith("tool_wrench_"):
            leads.append({
                "title": "Bahco 111M size table",
                "url": BAHCO,
                "use": "Compare head widths and thicknesses against the positioned pocket.",
            })
        for lead in leads:
            if "staged_file" in lead:
                lead["sha256"] = sha256((HERE / lead["staged_file"]).read_bytes()).hexdigest()
        packet = {
            "title": tool["title"],
            "oomp_id": tool_id,
            "populate_key": key,
            "model_kind": tool["model_kind"],
            "model_task": "Build an external tool model" if tool["model_kind"] == "holder_envelope" else "Reuse the existing external model",
            "modelling_and_seating_instructions": brief_for(tool=tool, briefs=briefs),
            "existing_model_note": tool["model_note"],
            "declared_tool_parameters": tool.get("parameters", {}),
            "pocket_reference_only_mm": tool["holder_profile"],
            "staged_drawing_from_handoff": drawing,
            "staged_photo_from_handoff": preview,
            "local_originals": evidence,
            "source_record_from_tools_repo": f"parts/{tool_id}/working.yaml",
            "model_files_from_tools_repo": f"parts/{tool_id}/three_d_model",
            "source_evidence": tool["sources"],
            "additional_manufacturer_references": leads,
            "existing_loaded_guides": guided,
            "remaining_holder_views": pending,
        }
        write_file(HERE / "packets" / f"{key}.yaml", yaml.safe_dump(packet, sort_keys=False, allow_unicode=True))
        index.append(f"| [{tool['title']}](packets/{key}.yaml) | {tool['model_kind'].replace('_', ' ')} | {len(guided)} / {len(tool['holders'])} |")
    write_file(HERE / "README.md", "\n".join(index) + "\n")


if __name__ == "__main__":
    stage()
