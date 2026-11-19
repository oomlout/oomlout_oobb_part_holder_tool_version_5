"""Draw two measured sections through each printable tool holder."""
from xml.etree import ElementTree as ET

import trimesh

from holder_catalogue import cli_options, records, write_file
from holder_geometry import build_mesh


def section_path(mesh, **kwargs):
    origin = kwargs.get("origin", [0, 0, 0])
    normal = kwargs.get("normal", [0, 0, 1])
    axes = kwargs.get("axes", [0, 1])
    section = mesh.section(plane_origin=origin, plane_normal=normal)
    if section is None:
        raise ValueError(f"Section misses the holder at {origin}")
    rings = []
    for curve in section.discrete:
        coordinates = curve[:, axes].copy()
        coordinates[:, 1] *= -1
        rings.append("M " + " L ".join(f"{x:.3f},{y:.3f}" for x, y in coordinates) + " Z")
    return " ".join(rings)


def draw_sections(folder, **kwargs):
    part = kwargs["part"]
    drawing = part["svg_details"]
    near_face = drawing.get("near_face_fraction", 0.08)
    cross_section = drawing.get("cross_section_y_fraction", 0.82)
    mesh = trimesh.load_mesh(folder / "3dpr.stl")
    lo, hi = mesh.bounds
    width, height, thickness = mesh.extents
    z = lo[2] + thickness * (near_face if drawing["show_underside"] else 1 - near_face)
    y = lo[1] + height * cross_section
    # Keep both sections at the same scale. SVG Y increases down the page.
    page_width = max(width + 14, 105)
    page_height = height + thickness + 46
    document = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "width": f"{page_width:g}mm",
        "height": f"{page_height:g}mm",
        "viewBox": f"0 0 {page_width:g} {page_height:g}",
        "font-family": "sans-serif",
        "fill": "#243a3b",
    })
    ET.SubElement(document, "title").text = f"{part['title']} — tool holder sections"
    xshift = (page_width - width) / 2 - lo[0]
    sections = [
        {
            "origin": [0, 0, z],
            "normal": [0, 0, 1],
            "axes": [0, 1],
            "label": f"Plan section · {z-lo[2]:.2f} mm above base",
            "baseline": 7,
            "shift": 12 + hi[1],
        },
        {
            "origin": [0, y, 0],
            "normal": [0, 1, 0],
            "axes": [0, 2],
            "label": f"Cross section · Y = {y:.2f} mm",
            "baseline": height + 26,
            "shift": height + 31 + hi[2],
        },
    ]
    for section in sections:
        ET.SubElement(document, "text", {
            "x": "5",
            "y": str(section["baseline"]),
            "font-size": "3.6",
        }).text = section["label"]
        ET.SubElement(document, "path", {
            "d": section_path(mesh, **section),
            "transform": f"translate({xshift:g} {section['shift']:g})",
            "fill": "#a8dcda",
            "fill-rule": "evenodd",
            "stroke": "#16565a",
            "stroke-width": "0.24",
            "stroke-linejoin": "round",
        })
    cut_line = 12 + hi[1] - y
    ET.SubElement(document, "path", {
        "d": f"M {xshift+lo[0]-2:g},{cut_line:g} h {width+4:g}",
        "stroke": "#616966",
        "stroke-width": "0.25",
        "stroke-dasharray": "2 1",
    })
    ET.SubElement(document, "text", {
        "x": "5",
        "y": f"{page_height-4:g}",
        "font-size": "2.8",
    }).text = f"{part['width']} × {part['height']} grid · {thickness:g} mm print thickness · scale 1:1"
    ET.indent(document)
    write_file(folder / "working.svg", ET.tostring(document, encoding="utf-8", xml_declaration=True))


def main(**kwargs):
    selected = kwargs.get("filter", "")
    render = kwargs.get("render", True)
    publish = kwargs.get("publish", True)
    for _, folder, part in records(filter=selected):
        options = {
            **kwargs,
            "oobb_details": part["oobb_details"],
        }
        build_mesh(folder, **options)
        draw_sections(folder, part=part)
    if render:
        from holder_render import render_parts
        from holder_assembly import build_assemblies
        render_parts(**kwargs)
        build_assemblies(**kwargs)
    if publish:
        from holder_navigation import publish_catalogue
        publish_catalogue(**kwargs)


if __name__ == "__main__":
    main(**cli_options())

