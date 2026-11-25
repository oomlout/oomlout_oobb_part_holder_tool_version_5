"""OOBB component recipe for the print layouts and their tool envelopes."""
from copy import deepcopy
import hashlib
import shutil
import subprocess
import tempfile
from pathlib import Path

import opsc
import trimesh

from holder_catalogue import ROOT, write_file


def mounting_holes(**kwargs):
    width = kwargs.get("width", 3)
    height = kwargs.get("height", 5)
    corners_only = kwargs.get("corners_only", False)
    pitch = kwargs.get("pitch_mm", 15)
    radii = kwargs.get("hole_radii_mm", [3.25, 1.8])
    # The legacy U opens at +Y. Half-grid holes coincident with M6 are redundant.
    centres = {}
    for subdivision, radius in enumerate(radii, start=1):
        columns = (width - 1) * subdivision
        rows = (height - 1) * subdivision
        for column in range(columns + 1):
            for row in range(rows + 1):
                side = column in (0, columns)
                corner = side and row in (0, rows)
                if (corner if corners_only else side or row == 0):
                    point = (
                        (column - columns / 2) * pitch / subdivision,
                        (row - rows / 2) * pitch / subdivision,
                    )
                    centres.setdefault(point, radius)
        if corners_only:
            break
    return centres


def get_holder_tool(thing, **kwargs):
    width = kwargs.get("width", 3)
    height = kwargs.get("height", 5)
    depth = kwargs.get("depth", 15)
    style = kwargs.get("body_style", "vertical_v4")
    count = kwargs.get("count", 1)
    spacing = kwargs.get("spacing_mm", 15)
    offset = kwargs.get("offset_mm", [0, 0, 0])
    profile = kwargs.get("profile", [])
    layered = kwargs.get("layered", False)
    pitch = kwargs.get("pitch_mm", 15)
    corner_radius = kwargs.get("corner_radius_mm", 5)
    edge_reduction = kwargs.get("edge_reduction_mm", 1)
    clearance = kwargs.get("bottom_m6_clearance_mm")
    hole_radii = kwargs.get("hole_radii_mm", [3.25, 1.8])
    row_count = kwargs.get("row_count", 1)
    row_pitch = kwargs.get("row_pitch_mm", 6)
    profile_z = kwargs.get("profile_z_mm", 0)
    stand = style == "stand"
    bottom = -1
    if stand:
        bottom = -depth / 2
    elif style in ("vertical_project", "bit_block"):
        bottom = 0
    printed_depth = depth if stand or style == "bit_block" else depth / 2
    faces = [[0, profile_z]]
    if style == "paired_v4":
        faces.append([width * pitch + 5, -printed_depth])
    rows = [[count, 0]]
    if layered:
        rows.append([count - 1, depth / 2])
    if style == "bit_block":
        first_row = (depth - (row_count - 1) * row_pitch) / 2
        rows = [(count - row % 2, first_row + row * row_pitch) for row in range(row_count)]
    hole_options = {
        "width": width,
        "height": height,
        "corners_only": stand,
        "pitch_mm": pitch,
        "hole_radii_mm": hole_radii,
    }
    holes = mounting_holes(**hole_options)
    for face_x, tool_z in faces:
        body = {
            "type": "positive",
            "shape": "rounded_rectangle",
            "size": [width * pitch - edge_reduction, height * pitch - edge_reduction, printed_depth],
            "r": corner_radius,
            "pos": [face_x, 0, bottom],
        }
        thing["components"].append(body)
        for (x, y), radius in holes.items():
            hole = {
                "type": "negative",
                "shape": "cylinder",
                "r": radius,
                "h": printed_depth + 2,
                "pos": [face_x + x, y, bottom - 1],
            }
            thing["components"].append(hole)
        for places, row_z in rows:
            for index in range(places):
                shift_x = (index - (places - 1) / 2) * spacing
                for segment in profile:
                    x, y, z = segment["pos"]
                    pocket_y = y + offset[1]
                    if clearance is not None:
                        pocket_y = -(height - 1) * pitch / 2 + hole_radii[0] + clearance
                    cutter = {
                        **deepcopy(segment),
                        "type": "negative",
                        "pos": [face_x + x + offset[0] + shift_x, pocket_y, z + offset[2] + row_z + tool_z],
                    }
                    thing["components"].append(cutter)


def build_mesh(directory, **kwargs):
    geometry = kwargs["oobb_details"]
    force = kwargs.get("force", False)
    export_mesh = kwargs.get("export_mesh", True)
    executable = kwargs.get("openscad") or shutil.which("openscad")
    resolution = kwargs.get("facets", 50)
    source = directory / "3dpr.scad"
    mesh_file = directory / "3dpr.stl"
    cache = ROOT / "build" / "meshes" / directory.name
    thing = {
        "components": [],
    }
    get_holder_tool(thing, **geometry)
    with tempfile.TemporaryDirectory() as temporary:
        scratch = Path(temporary)
        scad = scratch / "3dpr.scad"
        opsc.opsc_make_object(str(scad), thing["components"], mode="3dpr", resolution=resolution)
        if geometry["body_style"] in ("handed_pair", "paired_face_up"):
            shift = geometry["width"] * geometry["pitch_mm"] + 5
            thickness = geometry["depth"] / 2
            # Turn a face over about Y, leaving its flat back on the print plane.
            turn = f"translate([0,0,{thickness - 2:g}]) rotate([0,180,0])"
            first = scad.read_text()
            if geometry["body_style"] == "handed_pair":
                # The hex-key source pocket opens on the underside.
                scad.write_text(f"module rear() {{ {turn} {{\n{first}\n}} }}\nrear();\n"
                                f"translate([{shift},0,0]) mirror([1,0,0]) rear();\n")
            else:
                second = {
                    "components": [],
                }
                get_holder_tool(second, **geometry, profile_z_mm=-thickness)
                opsc.opsc_make_object(str(scad), second["components"], mode="3dpr", resolution=resolution)
                front = scad.read_text()
                scad.write_text(f"{first}\ntranslate([{shift},0,0]) {turn} {{\n{front}\n}}\n")
        elif geometry["body_style"] == "bit_block":
            height_mm = geometry["height"] * geometry["pitch_mm"] - geometry["edge_reduction_mm"]
            body = scad.read_text()
            scad.write_text(f"translate([0,{geometry['depth']/2:g},{height_mm/2:g}]) rotate([90,0,0]) {{\n{body}\n}}\n")
        content = scad.read_bytes()
        if not export_mesh:
            write_file(source, content)
            return
        digest = hashlib.sha256(content).hexdigest()
        if not force and cache.is_file() and mesh_file.is_file():
            mesh_hash = hashlib.sha256(mesh_file.read_bytes()).hexdigest()
            if cache.read_text() == f"{digest} {mesh_hash}":
                write_file(source, content)
                return
        if not executable:
            raise FileNotFoundError("OpenSCAD is required to export STL")
        output = scratch / "3dpr.stl"
        subprocess.run([executable, "--backend=Manifold", "--export-format=binstl",
                        "-o", str(output), str(scad)], check=True, capture_output=True)
        mesh = trimesh.load_mesh(output)
        if mesh.is_empty or not mesh.is_volume:
            raise ValueError(f"Invalid print mesh for {directory.name}")
        binary = output.read_bytes()
        write_file(source, content)
        write_file(mesh_file, binary)
        write_file(cache, f"{digest} {hashlib.sha256(binary).hexdigest()}")

