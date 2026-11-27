"""Publish the tool-first directory tree, canonical part pages and inventory."""
from collections import defaultdict
import json
import os
from pathlib import Path

import yaml

from holder_catalogue import ROOT, natural_key, write_file
from holder_assembly import print_instruction

NAV = ROOT / "navigation_oobb"
DISCOVERY = NAV / "oobb" / "part" / "holder_tool"
BEGIN = "<!-- oobb-presentation:start -->"
END = "<!-- oobb-presentation:end -->"
NOTICE = "AI-generated CAD images and instructions. Errors possible."
PROJECT_ORIGIN = (
    "This is an entirely AI-generated coding project. The generated outputs are included "
    "and usually work. The project is published so others can modify and regenerate "
    "the designs with their own AI tools."
)
VERTICAL = "https://github.com/oomlout/oomlout_oobb_part_tool_holder_vertical"
VERSION_4 = "https://github.com/oomlout/oomlout_oobb_version_4"


def relative(folder, target):
    return Path(os.path.relpath(target, folder)).as_posix() + ("/" if target.is_dir() else "")


def write_block(path, content):
    original = path.read_text(encoding="utf-8") if path.exists() else ""
    if BEGIN in original or END in original:
        if original.count(BEGIN) != 1 or original.count(END) != 1 or original.index(BEGIN) > original.index(END):
            raise ValueError(f"Check generated block markers in {path}")
        before, _, rest = original.partition(BEGIN)
        _, _, after = rest.partition(END)
    else:
        before, after = "", "\n" + original if original else "\n"
    write_file(path, before + BEGIN + "\n" + content.strip() + "\n" + END + after)


def assembly_instructions(**kwargs):
    part = kwargs["part"]
    folder = kwargs["folder"]
    recipe = part["assembly_details"]
    assembly = ROOT / "parts" / part["id"] / "assembly"
    source_file = ROOT / "source_file" / "tool_models" / recipe["tool_id"] / "source.json"
    source = json.loads(source_file.read_text(encoding="utf-8"))
    single_piece = part["construction"]["mode"] in ("block", "stand")
    placement = " Place the holder upright with its openings facing up." if single_piece else " The dark teal half sits against the wall and the light teal half faces the room."
    lines = [
        print_instruction(part=part) + placement,
        "",
    ]
    for number, step in enumerate(recipe["steps"], start=1):
        picture = assembly / "render" / "raw" / (step["key"] + ".png")
        action = f"{number}. {step['action']}"
        if picture.is_file():
            action += f" [View step {number}]({relative(folder, picture)})"
        lines.append(action)
    manifest = assembly / "assembly_manifest.json"
    if manifest.is_file():
        pages = json.loads(manifest.read_text(encoding="utf-8"))["book_pages"]
        lines.extend(["", "<details><summary>Illustrated assembly steps</summary>", ""])
        for number, page in enumerate(pages, start=1):
            if page["kind"] == "instructions":
                picture = assembly / "pages" / f"page_{number:02d}.png"
                lines.append(f"![Assembly steps for the {recipe['label'].lower()} holder]({relative(folder, picture)})")
        lines.extend(["", "</details>"])
    lines.extend([
        "",
        f"{source['model_note']} The digital model was checked against the printed holder. Physical fit remains unverified. "
        f"[OOMP tool record](https://github.com/oomlout/oomp_tool_version_5/tree/main/parts/{recipe['tool_id']})",
    ])
    for extra in recipe.get("additional_tools", []):
        extra_file = ROOT / "source_file" / "tool_models" / extra["tool_id"] / "source.json"
        extra_source = json.loads(extra_file.read_text(encoding="utf-8"))
        lines.extend([
            "",
            f"{extra_source['model_note']} [OOMP tool record](https://github.com/oomlout/oomp_tool_version_5/tree/main/parts/{extra['tool_id']})",
        ])
    if part.get("layered"):
        lines.extend([
            "",
            "The seven staggered front positions are open-face grooves. Retention of the bits in those grooves has not been physically tested.",
        ])
    return "\n".join(lines)


def part_page(**kwargs):
    part = kwargs["part"]
    folder = kwargs["folder"]
    canonical = kwargs["canonical"]
    leaf = kwargs["leaf"]
    guide_holders = kwargs.get("guide_holders", [])
    title = part["title"]
    layout = part["layout"].replace("_", " ")
    depth = part["depth"]
    stand = part["body_style"] == "stand"
    block = part["body_style"] == "bit_block"
    thickness = depth if stand or block else depth / 2
    metadata = yaml.safe_dump(part, sort_keys=False, allow_unicode=True).strip()
    source = VERSION_4 + "/blob/41f5386997faef4473c959dfb8c929864d7bf697/oobb_make_sets.py#L626"
    if part["body_style"] == "vertical_project":
        source = VERTICAL + "/tree/93a962a09e0c275c3cfa62187182ac3203bde1b2/parts/" + part["source_id"]
    instruction = "The stand prints as one piece. Tools enter the pockets from the top." if stand else "Print two copies of the holder half. Turn one over, face the pockets inward and line up the mounting holes and open ends."
    if part["construction"]["mode"] == "handed_pair":
        instruction = "Print the supplied layout once with both pockets facing up. Flip the right-hand piece over the left, face the pockets inward and align the holes."
    if block:
        rows = part["row_count"]
        capacity = part["count"] * rows - rows // 2
        instruction = f"Print the block once with its pockets opening upward. Its {rows} staggered rows hold {capacity} quarter-inch bits."
    if part["body_style"] == "paired_v4":
        instruction = "Print the supplied two-body layout once. Move the right-hand half onto the left-hand half, keeping the pocket faces together and the openings aligned."
    if "bottom_m6_clearance_mm" in part:
        instruction += f" The pocket floors stop {part['bottom_m6_clearance_mm']:g} mm above the rim of the bottom M6 mounting holes."
    if block or part["profile"] == "four_spanners":
        source = relative(folder, ROOT / "working_oomp_populate.py")
    guide_index = relative(folder, ROOT / "README.md") + "#assembly"
    if part.get("assembly_details"):
        assembly = canonical / "assembly"
        instruction = assembly_instructions(part=part, folder=folder)
        instruction += (
            f"\n\n[Offline HTML viewer]({relative(folder, assembly/'assembly_instructions.html')}) · "
            f"[Print booklet (PDF)]({relative(folder, assembly/'assembly_instructions.pdf')})"
        )
    elif guide_holders:
        references = [f"[{label}]({relative(folder, path/'README.md')}#assembly)"
                      for label, path in guide_holders]
        instruction += "\n\nThese tools also have illustrated single-place holder guides. " + " · ".join(references)
    else:
        instruction += f" [Illustrated tool-loading guides]({guide_index})"
    return f"""# {title}

{NOTICE}

## Summary

OOBB {part['tool_type'].replace('_', ' ')} holder · {layout}.

{PROJECT_ORIGIN}

![CAD views of {title}]({relative(folder, canonical / '3dpr_presentation.png')})

## Details

| Grid (width × height) | Assembled thickness | Thickness per printed piece |
| --- | --- | --- |
| {part['width']} × {part['height']} | {depth:g} mm | {thickness:g} mm |

The grid pitch is 15 mm. The dashed line on the plan locates the cross section. [Section drawing]({relative(folder, canonical / 'working.svg')})

OOMP ID `{part['id']}`

[Part folder]({relative(folder, canonical)}) · [OOBB navigation]({relative(folder, leaf.parent)}) · [Source design]({source})

<details><summary>Complete part metadata</summary>

```yaml
{metadata}
```

</details>

## Parts

Use the print mesh in the part folder. Tool and mounting hardware are supplied separately.

## Assembly

{instruction}
"""


def publish_catalogue(**kwargs):
    root = ROOT
    manifest = root / "parts_source/catalogue.txt"
    nodes = defaultdict(dict)
    groups = defaultdict(list)
    parts = {}
    leaves = set()
    related = defaultdict(list)
    for source in sorted((root/"source_file/tool_models").glob("*/source.json")):
        tool = json.loads(source.read_text(encoding="utf-8"))
        single = next((h["id"] for h in tool["holders"] if h["layout"].endswith("1_place")
                       and (root/"parts"/h["id"]/"assembly/assembly_manifest.json").is_file()), None)
        if single is None:
            continue
        path = root/"parts"/single
        if (path/"assembly/assembly_manifest.json").is_file():
            single_part = yaml.safe_load((path / "working.yaml").read_text(encoding="utf-8"))
            label = single_part["assembly_details"]["label"]
            for holder in tool["holders"]:
                related[holder["id"]].append((label, path))
    for part_id in manifest.read_text().splitlines():
        canonical = root / "parts" / part_id
        if not (canonical / "3dpr_presentation.png").is_file() or not (canonical / "working.svg").is_file():
            continue
        part = yaml.safe_load((canonical / "working.yaml").read_text(encoding="utf-8"))
        parts[part_id] = part
        groups[part["tool_type"]].append(part)
        branch = NAV
        for level in range(1, 8):
            segment = part[f"taxonomy_{level}"]
            child = branch / segment
            nodes[branch][segment] = canonical if level == 7 else child
            branch = child
        leaf = branch
        leaves.add(leaf)
        leaf.mkdir(parents=True, exist_ok=True)
        for folder in (canonical, leaf):
            details = {
                "part": part,
                "folder": folder,
                "canonical": canonical,
                "leaf": leaf,
                "guide_holders": related[part_id],
            }
            write_block(folder / "README.md", part_page(**details))
        write_file(leaf / "oomp_id.txt", part_id + "\n")
    if not parts:
        raise ValueError("Build the holder drawings and renders before publishing navigation")
    for branch, children in nodes.items():
        branch.mkdir(parents=True, exist_ok=True)
        lines = [f"# {branch.name.replace('_', ' ').capitalize()}", ""]
        for label in sorted(children, key=natural_key):
            choice = label.replace("_", " ")
            if children[label].parent == root / "parts":
                part = parts[children[label].name]
                choice = f"{part['width']} × {part['height']} grid · {part['depth']:g} mm design depth"
            lines.append(f"- [{choice}]({relative(branch, children[label])})")
        if branch != NAV:
            lines.extend(["", "[Parent category](../)"])
        write_block(branch / "README.md", "\n".join(lines))
    # Retire only generated navigation files when a definition moves or is removed.
    active = set(nodes) | leaves
    for page in NAV.rglob("README.md"):
        if page.parent not in active:
            content = page.read_text(encoding="utf-8").strip()
            if content.startswith(BEGIN) and content.endswith(END):
                page.unlink()
                (page.parent / "oomp_id.txt").unlink(missing_ok=True)
    for directory in sorted(NAV.rglob("*"), key=lambda path: len(path.parts), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            directory.rmdir()
    inventory = [
        "# Tool inventory", "",
        f"{len(parts)} printable layouts in {len(groups)} tool categories. Sizes are width × height in 15 mm grid units, followed by the source design depth in millimetres.", "",
        "## Hierarchy", "",
        "```mermaid", "flowchart LR",
        '    root["OOBB tool holders"] --> family["Tool type"] --> model["Model or size"] --> layout["Layout"] --> size["Grid and design depth"] --> part["Part folder"]',
        "```", "", "```text", "oobb / part / holder_tool",
    ]
    categories = sorted(groups, key=natural_key)
    for index, category in enumerate(categories):
        branch = "└──" if index == len(categories) - 1 else "├──"
        models = sorted({p["model"] for p in groups[category]}, key=natural_key)
        inventory.append(f"{branch} {category:<14}  {' · '.join(models)}")
    inventory.extend(["```", "", "Each model opens into layout, then size, then the canonical part folder.", "",
                      "## Tools and layouts", "", "| Tool type | Tools | Print layouts |", "| --- | --- | ---: |"])
    for category in categories:
        titles = sorted({p["title"] for p in groups[category]}, key=natural_key)
        link = relative(root, DISCOVERY / category)
        inventory.append(f"| [{category.replace('_', ' ').capitalize()}]({link}) | {'<br>'.join(titles)} | {len(groups[category])} |")
    inventory.extend(["", "[Illustrated loading guides and print booklets](README.md#assembly)"])
    write_block(root / "TOOLS.md", "\n".join(inventory))
    guides = [p for p in parts.values() if p.get("assembly_details")]
    guide_table = [
        "| Holder README | Offline viewer | Print booklet |",
        "| --- | --- | --- |",
    ]
    sequences = []
    for guide in guides:
        part_path = f"parts/{guide['id']}"
        path = f"{part_path}/assembly"
        label = guide["assembly_details"]["label"]
        guide_table.append(f"| [{label}]({part_path}/README.md#assembly) | [Offline HTML]({path}/assembly_instructions.html) | [Download PDF]({path}/assembly_instructions.pdf) |")
        sequences.extend([f"### {label}", assembly_instructions(part=guide, folder=root)])
    guide_links = "\n".join(guide_table) if guides else ""
    guide_steps = "\n\n".join(sequences)
    landing = f"""# OOBB tool holders

[![Yellow and turquoise tool holders mounted on a black captive nut plate, with round covers on the mounting bolts](source_file/image_main/working_1024.jpg)](source_file/image_main/working.jpg)

Print files for the [bolt covers](https://github.com/oomlout/oomlout_oobb_part_cosmetic_nut_screw_adapter_version_5) and the [black captive nut plate behind the holders](https://github.com/oomlout/oomlout_oobb_part_plate_captive_nut_version_5) are available in their respective repositories.

{NOTICE}

## Summary

Printable holders for workshop hand tools on the 15 mm OOBB grid. These designs come from Oomlout’s [vertical tool holders]({VERTICAL}) and [OOBB version 4]({VERSION_4}).

{PROJECT_ORIGIN}

## Details

**[Browse by tool type]({relative(root, DISCOVERY)})** or see the [hierarchy and tool list](TOOLS.md). The catalogue contains {len(parts)} layouts across {len(groups)} categories. Choose a tool type, model, layout and size.

Run `python working.py` to rebuild. The [build notes](presentation/README.md) cover dependencies and filtered builds. The [tool modelling queue](presentation/tool-model-handoff/README.md) maps each OOMP tool to its holder layouts and staged references.

## Parts

Width and height use 15 mm grid units. A 3 × 5 holder has a nominal footprint of 44 × 74 mm. The last size value is the assembled depth in millimetres. Two-piece wall holders use half-depth pieces. Stack them with the pockets facing inward and the holes aligned. Each part page gives its printed thickness, a section drawing and a CAD preview.

## Assembly

{len(guides)} holders have illustrated assembly and loading instructions using OOMP tool models. Each viewer opens offline. The print booklets use landscape A4 pages. Physical fit remains unverified.

For future renders, show vertical holders as they sit on the wall, with the opening and tool handles pointing up. Show the halves touching in the assembled view and move the front half outward along the mounting holes for the exploded view. Print the Quikpik combination, utility knife, Prit combination, metric hex-key sets and four-size spanner layout once to obtain both halves. The quarter-inch bit blocks and mixed-tool bench stand each print as one piece.

{guide_links}

{guide_steps}
"""
    write_block(root / "README.md", landing)

