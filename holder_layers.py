"""Place production STL bodies in their assembled positions, in millimetres."""
import numpy as np
import trimesh


def assembled_layers(**kwargs):
    source = kwargs["mesh"]
    settings = kwargs["construction"]
    mode = settings["mode"]
    if mode == "stand":
        return [source.copy()]
    if mode == "paired_layout":
        lower, upper = sorted(source.split(), key=lambda body: body.bounds[0, 0])
        upper.apply_translation([
            lower.bounds[0, 0] - upper.bounds[0, 0],
            0,
            lower.bounds[1, 2] - upper.bounds[0, 2],
        ])
        return [lower, upper]

    lower = source.copy()
    # Turning about the tool's long axis keeps the pocket entrance at +Y.
    turn_over = np.diag([-1.0, 1.0, -1.0, 1.0])
    if settings["pocket_on_underside"]:
        lower.apply_transform(turn_over)
    upper = lower.copy()
    if settings["mirror_second_print_x"]:
        upper.apply_transform(np.diag([-1.0, 1.0, 1.0, 1.0]))
    upper.apply_transform(turn_over)
    upper.apply_translation([0, 0, lower.bounds[1, 2] - upper.bounds[0, 2]])
    return [lower, upper]
