"""Check that the combined holder guide accounts for both physical tools."""
from pathlib import Path

import trimesh
import yaml

import holder_layers
from holder_assembly import REFERENCES, verify_pose


def test_glue_and_knife_pose_and_inventory():
    root = Path(__file__).resolve().parents[1]
    identifier = "oobb_part_holder_tool_glue_stick_prit_medium_with_knife_5x5x30"
    folder = root / "parts" / identifier
    part = yaml.safe_load((folder / "working.yaml").read_text(encoding="utf-8"))
    recipe = part["assembly_details"]
    layers = holder_layers.assembled_layers(
        mesh=trimesh.load_mesh(folder / "3dpr.stl"),
        construction=part["construction"],
    )
    result = verify_pose(
        layers=layers,
        tool=REFERENCES / recipe["tool_id"] / "working.stl",
        recipe=recipe,
    )
    assert result["tool_count"] == 2
    assert result["holder_intersection_mm3"] == 0
    assert sum(step["add"].count("knife") for step in recipe["steps"]) == 1
    assert sum(step["add"].count("tool") for step in recipe["steps"]) == 1
