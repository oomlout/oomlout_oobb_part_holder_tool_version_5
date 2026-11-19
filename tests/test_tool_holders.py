"""Regression checks for the source-profile mix-up and the two multi-row layouts."""
from copy import deepcopy

import numpy as np
import trimesh
from shapely.ops import unary_union

from holder_catalogue import records
from holder_geometry import get_holder_tool
from holder_layers import assembled_layers
from working_oomp_populate import get_options, get_profiles


def tool_cutters(**kwargs):
    thing = {
        "components": [],
    }
    get_holder_tool(thing, **kwargs)
    return [component for component in thing["components"] if "rot" in component]


def test_new_tools_have_independent_cutouts():
    profiles = get_profiles()
    expected = {
        "quarter_inch": [4, 100],
        "picquic_teeny_turner": [4.75, 28],
        "sharpie_style_13mm": [7, 137],
    }
    for name, dimensions in expected.items():
        cylinder = profiles[name][0]
        assert [cylinder["r"], cylinder["h"]] == dimensions


def test_layered_driver_bits_have_two_staggered_rows():
    example = next(p for p in get_options() if p.get("layered") and p["height"] == 3)
    options = {
        **example,
        "profile": get_profiles()[example["profile"]],
    }
    original = deepcopy(options)
    cutters = tool_cutters(**options)
    assert options == original
    assert [c["pos"][0] for c in cutters[:8]] == [-52.5, -37.5, -22.5, -7.5, 7.5, 22.5, 37.5, 52.5]
    assert [c["pos"][0] for c in cutters[8:]] == [-45, -30, -15, 0, 15, 30, 45]
    assert [c["pos"][2] for c in cutters] == [0] * 8 + [6] * 7


def test_glue_and_knife_faces_use_complementary_depths():
    example = next(p for p in get_options() if p["body_style"] == "paired_v4")
    options = {
        **example,
        "profile": get_profiles()[example["profile"]],
    }
    cutters = tool_cutters(**options)
    assert len(cutters) == 4
    for first, second in zip(cutters[:2], cutters[2:]):
        assert second["pos"][0] - first["pos"][0] == 80
        assert second["pos"][2] - first["pos"][2] == -15


def test_all_vertical_holder_layers_meet_with_matching_pockets():
    for identifier, folder, part in records():
        source = trimesh.load_mesh(folder / "3dpr.stl")
        layers = assembled_layers(mesh=source, construction=part["construction"])
        if part["body_style"] == "stand":
            assert len(layers) == 1
            continue
        lower, upper = layers
        seam = lower.bounds[1, 2]
        assert np.isclose(upper.bounds[0, 2], seam), identifier
        assert np.isclose(upper.bounds[1, 2] - lower.bounds[0, 2], part["depth"]), identifier
        # Use the same world XY frame for both cross sections. Matching outlines
        # alone would miss offset pockets or mounting holes in the wrong half.
        sections = []
        for layer, offset in ((lower, -0.002), (upper, 0.002)):
            section = layer.section(plane_normal=[0, 0, 1], plane_origin=[0, 0, seam + offset])
            flat, _ = section.to_2D(to_2D=np.eye(4), check=False)
            sections.append(unary_union(flat.polygons_full))
        assert sections[0].symmetric_difference(sections[1]).area < 2, identifier

