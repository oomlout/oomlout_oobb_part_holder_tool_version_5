"""Blender worker for the four photographed tools. World units are metres."""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_holder import WALL_VIEW, aim, import_layers, orient_for_wall


def corners(objects):
    bpy.context.view_layer.update()
    return [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]


def shoot(scene, camera, **kwargs):
    points = kwargs["bounds"]
    output = kwargs["output"]
    eye = Vector(kwargs.get("eye", WALL_VIEW)).normalized()
    low = Vector([min(p[i] for p in points) for i in range(3)])
    high = Vector([max(p[i] for p in points) for i in range(3)])
    centre = (high + low) / 2
    camera.location = centre + eye * 0.6
    aim(camera, centre)
    bpy.context.view_layer.update()
    projected = [camera.matrix_world.inverted() @ p for p in points]
    limits = [(min(p[i] for p in projected), max(p[i] for p in projected)) for i in (0, 1)]
    middle = Vector([(a+b)/2 for a,b in limits] + [0])
    camera.location += camera.rotation_euler.to_matrix() @ middle
    aspect = scene.render.resolution_x / scene.render.resolution_y
    camera.data.ortho_scale = max(limits[0][1]-limits[0][0], aspect*(limits[1][1]-limits[1][0])) * 1.11
    scene.render.filepath = str(output)
    bpy.ops.render.render(write_still=True)


def render(**kwargs):
    folder = Path(kwargs["output"])
    spec = kwargs["recipe"]
    position = Vector(spec["translation_mm"]) / 1000
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.engine = "CYCLES"
    scene.cycles.samples = 18
    scene.cycles.use_denoising = True
    prefs = bpy.context.preferences.addons["cycles"].preferences
    try:
        prefs.compute_device_type = "OPTIX"
        prefs.get_devices()
        for device in prefs.devices:
            device.use = device.type == "OPTIX"
        if any(d.use for d in prefs.devices):
            scene.cycles.device = "GPU"
    except (RuntimeError, TypeError):
        pass
    scene.render.resolution_x = 920
    scene.render.resolution_y = 700
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.view_settings.exposure = -0.65
    scene.render.image_settings.color_mode = "RGBA"
    scene.world = bpy.data.worlds.new("Studio")
    scene.world.use_nodes = True
    scene.world.node_tree.nodes["Background"].inputs[1].default_value = 0.55
    lower, upper = import_layers(sources=kwargs["sources"])
    existing = set(scene.objects)
    bpy.ops.import_scene.gltf(filepath=kwargs["tool"])
    imported = set(scene.objects) - existing
    meshes = [obj for obj in imported if obj.type == "MESH"]
    assembly = bpy.data.objects.new("OOMP tool pose", None)
    scene.collection.objects.link(assembly)
    for obj in imported:
        if obj.parent is None:
            obj.parent = assembly
    assembly.rotation_euler = [math.radians(v) for v in spec["rotation_deg"]]
    assembly.location = position
    orient_for_wall(objects=[lower, upper, assembly])
    for name, xyz, power in [
        ("Key", [-0.24,-0.30,0.42], 8), ("Fill", [0.32,-0.07,0.32], 4),
        ("Rim", [0,0.31,0.36], 6),
    ]:
        light = bpy.data.lights.new(name, "AREA")
        light.energy = power
        light.shape = "DISK"
        light.size = 0.28
        obj = bpy.data.objects.new(name, light)
        scene.collection.objects.link(obj)
        obj.location = xyz
        aim(obj, [0,0.03,0.01])
    camera = bpy.data.objects.new("Orthographic camera", bpy.data.cameras.new("Lens"))
    scene.collection.objects.link(camera)
    camera.data.type = "ORTHO"
    camera.data.clip_start = 0.001
    scene.camera = camera
    folder.mkdir(parents=True, exist_ok=True)
    lower_bounds = corners([lower])
    tool_bounds = corners(meshes)
    full_bounds = corners([lower, upper, *meshes])
    lower.hide_render = upper.hide_render = True
    shoot(scene, camera, bounds=tool_bounds, output=folder/"part_tool.png")
    lower.hide_render = False
    for obj in meshes:
        obj.hide_render = True
    shoot(scene, camera, bounds=lower_bounds, output=folder/"part_holder.png")

    half_count = 0
    tool_visible = False
    for step in spec["steps"]:
        half_count += step["add"].count("holder")
        tool_visible = tool_visible or "tool" in step["add"]
        upper.hide_render = half_count < 2
        upper.location.z = step["upper_lift_mm"] / 1000
        assembly.location = position + Vector([0, step["withdraw_mm"] / 1000, 0])
        for obj in meshes:
            obj.hide_render = not tool_visible
        visible = [obj for obj in [lower, upper, *meshes] if not obj.hide_render]
        shoot(scene, camera, bounds=corners(visible), output=folder/(step["key"]+".png"))

    shoot(scene, camera, bounds=full_bounds, output=folder/"book_cover.png")
    # The original top-of-print view is the front elevation on the wall.
    shoot(scene, camera, bounds=full_bounds, eye=[0,-1,0], output=folder/"loaded_top.png")
    upper.location.z = max(step["upper_lift_mm"] for step in spec["steps"]) / 1000
    shoot(scene, camera, bounds=corners([lower, upper, *meshes]), output=folder/"exploded.png")


if __name__ == "__main__":
    for job in json.loads(Path(sys.argv[sys.argv.index("--")+1]).read_text()):
        render(**job)

