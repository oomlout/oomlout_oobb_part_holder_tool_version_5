"""Blender worker for the four photographed tools. World units are metres."""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_holder import aim, material


def corners(objects):
    bpy.context.view_layer.update()
    return [obj.matrix_world @ Vector(corner) for obj in objects for corner in obj.bound_box]


def shoot(scene, camera, **kwargs):
    points = kwargs["bounds"]
    output = kwargs["output"]
    eye = Vector(kwargs.get("eye", [0.95, -1.25, 1.75])).normalized()
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
    bpy.ops.wm.stl_import(filepath=kwargs["holder"])
    holder = bpy.context.object
    holder.scale = [0.001]*3
    holder.data.materials.append(material("Turquoise PLA", [0, 177, 183]))
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
    holder_bounds = corners([holder])
    tool_bounds = corners(meshes)
    full_bounds = holder_bounds + tool_bounds
    lift = max(step["lift_mm"] for step in spec["steps"])/1000
    step_bounds = full_bounds + [p + Vector([0,0,lift]) for p in tool_bounds]
    holder.hide_render = True
    shoot(scene, camera, bounds=tool_bounds, output=folder/"part_tool.png")
    holder.hide_render = False
    for obj in meshes:
        obj.hide_render = True
    shoot(scene, camera, bounds=holder_bounds, output=folder/"part_holder.png")
    shown = set()
    for step in spec["steps"]:
        shown.update(step["add"])
        for obj in meshes:
            obj.hide_render = "tool" not in shown
        assembly.location = position + Vector([0,0,step["lift_mm"]/1000])
        shoot(scene, camera, bounds=step_bounds, output=folder/(step["key"]+".png"))
    shoot(scene, camera, bounds=full_bounds, output=folder/"book_cover.png")
    shoot(scene, camera, bounds=full_bounds, eye=[0,0,1], output=folder/"loaded_top.png")


if __name__ == "__main__":
    for job in json.loads(Path(sys.argv[sys.argv.index("--")+1]).read_text()):
        render(**job)

