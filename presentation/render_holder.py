"""Blender worker: render unchanged STL geometry in millimetres, two views per mesh."""
import json
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector


# World Z is vertical. The camera looks at the front and the open top edge.
WALL_VIEW = (1.0, -1.8, 0.72)


def orient_for_wall(**kwargs):
    objects = kwargs["objects"]
    mount = bpy.data.objects.new("Wall mounting plane", None)
    bpy.context.scene.collection.objects.link(mount)
    # Local +Y is the tool opening. Local +Z points out of the wall.
    mount.rotation_euler.x = math.radians(90)
    for obj in objects:
        obj.parent = mount
    bpy.context.view_layer.update()
    return mount


def linear(v):
    return v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4


def material(name, colour, roughness=.4):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    shader = m.node_tree.nodes.get('Principled BSDF')
    shader.inputs['Base Color'].default_value = (*[linear(v / 255) for v in colour], 1)
    shader.inputs['Roughness'].default_value = roughness
    return m


def aim(obj, point):
    obj.rotation_euler = (Vector(point) - obj.location).to_track_quat('-Z', 'Y').to_euler()


def import_layers(**kwargs):
    sources = kwargs["sources"]
    colours = (
        ("Deep teal PLA", (0, 115, 123)),
        ("Turquoise PLA", (0, 177, 183)),
    )
    layers = []
    for source, (name, colour) in zip(sources, colours, strict=False):
        bpy.ops.wm.stl_import(filepath=source)
        layer = bpy.context.object
        layer.scale = (0.001, 0.001, 0.001)
        layer.data.materials.append(material(name, colour))
        layers.append(layer)
    bpy.context.view_layer.update()
    return layers


def render(**kwargs):
    sources = kwargs["sources"]
    directory = Path(kwargs["directory"])
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 12
    scene.cycles.use_denoising = True
    prefs = bpy.context.preferences.addons['cycles'].preferences
    try:
        prefs.compute_device_type = 'OPTIX'
        prefs.get_devices()
        for d in prefs.devices:
            d.use = d.type == 'OPTIX'
        if any(d.use for d in prefs.devices):
            scene.cycles.device = 'GPU'
            # Keep the same studio style; denoise on the GPU during large batches.
            scene.cycles.denoising_use_gpu = True
    except Exception:
        pass
    scene.render.resolution_x = 640
    scene.render.resolution_y = 640
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    scene.render.image_settings.color_mode = 'RGBA'
    scene.render.film_transparent = True
    scene.view_settings.view_transform = 'AgX'
    scene.world = bpy.data.worlds.new('Studio')
    scene.world.use_nodes = True
    scene.world.node_tree.nodes['Background'].inputs[0].default_value = (.8, .8, .8, 1)
    scene.world.node_tree.nodes['Background'].inputs[1].default_value = .35
    layers = import_layers(sources=sources)
    mount = orient_for_wall(objects=layers) if len(layers) == 2 else None
    corners = [part.matrix_world @ Vector(v) for part in layers for v in part.bound_box]
    lo = Vector([min(v[i] for v in corners) for i in range(3)])
    hi = Vector([max(v[i] for v in corners) for i in range(3)])
    centre = (hi + lo) / 2
    size = hi - lo
    # No remeshing, bevel modifier or smoothing of real holes and sharp edges.
    # An open background keeps through-holes legible; floor shadows can resemble hardware.
    span = max(size)
    for name, pos, energy, radius in [
        ('Key', (-2, -3, 5), 22, 4), ('Fill', (3, -1, 3), 12, 3),
        ('Rim', (0, 4, 4), 18, 3),
    ]:
        data = bpy.data.lights.new(name, 'AREA')
        data.energy = energy * .07 * (span / .1) ** 2
        data.shape = 'DISK'
        data.size = span * radius
        light = bpy.data.objects.new(name, data)
        scene.collection.objects.link(light)
        light.location = Vector(pos) * span
        aim(light, (0, 0, 0))
    data = bpy.data.cameras.new('Camera')
    data.type = 'ORTHO'
    cam = bpy.data.objects.new('Camera', data)
    scene.collection.objects.link(cam)
    scene.camera = cam
    for view in ("angle", "detail"):
        eye = Vector(WALL_VIEW if mount else (0.8, 1.65, 1.0))
        focus = centre.copy()
        if view == "detail" and len(layers) == 2:
            lift = span * 0.48
            layers[1].location.z += lift
            focus += mount.matrix_world.to_3x3() @ Vector((0, 0, lift / 2))
        elif view == "detail":
            eye = Vector((0, 0, 3))
        cam.location = focus + eye * span
        aim(cam, focus)
        bpy.context.view_layer.update()
        bounds = [cam.matrix_world.inverted() @ (part.matrix_world @ Vector(v)) for part in layers for v in part.bound_box]
        extent = max(max(v[i] for v in bounds) - min(v[i] for v in bounds) for i in (0, 1))
        data.ortho_scale = extent * 1.23
        data.clip_start = .0001
        scene.render.filepath = str(directory / (view + '.png'))
        bpy.ops.render.render(write_still=True)
    print('OOBB rendered ' + directory.name, flush=True)


if __name__ == '__main__':
    jobs = json.loads(Path(sys.argv[sys.argv.index('--') + 1]).read_text())
    for job in jobs:
        render(**job)
