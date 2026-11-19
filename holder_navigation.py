"""Publish the tool-first directory tree, canonical part pages and inventory."""
from collections import defaultdict
import json
import os
from pathlib import Path

import yaml

from holder_catalogue import ROOT, natural_key, write_file

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
HERO = "oobb_part_holder_tool_mixed_tools_basic_stand_bench_7x10x66"


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
    lines = [
        "Print two copies of the holder STL. The dark teal half sits against the wall and the light teal half faces the room.",
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
        f"{source['model_note']} The digital model was checked against both halves. Physical fit remains unverified. "
        f"[OOMP tool record](https://github.com/oomlout/oomp_tool_version_5/tree/main/parts/{recipe['tool_id']})",
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
    thickness = depth if stand else depth / 2
    metadata = yaml.safe_dump(part, sort_keys=False, allow_unicode=True).strip()
    source = VERSION_4 + "/blob/41f5386997faef4473c959dfb8c929864d7bf697/oobb_make_sets.py#L626"
    if part["body_style"] == "vertical_project":
        source = VERTICAL + "/tree/93a962a09e0c275c3cfa62187182ac3203bde1b2/parts/" + part["source_id"]
    instruction = "The stand prints as one piece. Tools enter the pockets from the top." if stand else "Print two copies of the holder half. Turn one over, face the pockets inward and line up the mounting holes and open ends."
    if part["construction"]["mirror_second_print_x"]:
        instruction = "Print one half as supplied and mirror the second copy along X in the slicer before printing. Turn one half over and bring the matching pockets and mounting holes together."
    if part["body_style"] == "paired_v4":
        instruction = "Print the supplied two-body layout once. Move the right-hand half onto the left-hand half, keeping the pocket faces together and the openings aligned."
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
        instruction += f" [Illustrated guides for the four photo-modelled tools]({guide_index})"
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
        single = next(h["id"] for h in tool["holders"] if h["layout"] == "1_place")
        path = root/"parts"/single
        if (path/"assembly/assembly_manifest.json").is_file():
            for holder in tool["holders"]:
                related[holder["id"]].append((tool["title"], path))
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
    featured = next((p["id"] for p in guides if p["tool_type"] == "pliers"), HERO)
    hero_id = featured if featured in parts else sorted(parts)[0]
    hero = parts[hero_id]
    destination = f"parts/{hero_id}/"
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

{NOTICE}

## Summary

Printable holders for workshop hand tools on the 15 mm OOBB grid. These designs come from Oomlout’s [vertical tool holders]({VERTICAL}) and [OOBB version 4]({VERSION_4}).

{PROJECT_ORIGIN}

[![CAD views of {hero['title']}]({destination}3dpr_presentation.png)]({destination}README.md)

[{hero['title']}]({destination}README.md)

## Details

**[Browse by tool type]({relative(root, DISCOVERY)})** or see the [hierarchy and tool list](TOOLS.md). The catalogue contains {len(parts)} layouts across {len(groups)} categories. Choose a tool type, model, layout and size.

Run `python working.py` to rebuild. The [build notes](presentation/README.md) cover dependencies, filtered builds and source comparisons.

## Parts

Width and height use 15 mm grid units. A 3 × 5 holder has a nominal footprint of 44 × 74 mm. The last size value is the source design depth in millimetres. Vertical holders use two half-depth pieces. Stack them with the pockets facing inward and the holes aligned. Each part page gives its printed thickness, a section drawing and a CAD preview.

## Assembly

Four single-place holders have two-piece assembly and loading instructions illustrated with the original OOMP photo-based tool models. Each viewer opens offline. The print booklets use landscape A4 pages. Physical fit remains unverified.

For future renders, show vertical holders as they sit on the wall, with the opening and tool handles pointing up. Show the halves touching in the assembled view and move the front half outward along the mounting holes for the exploded view. The combined Prit and knife layout supplies both halves in one print. The mixed-tool bench stand prints as one piece.

{guide_links}

{guide_steps}
"""
    write_block(root / "README.md", landing)

