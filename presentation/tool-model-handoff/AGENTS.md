# Modelling OOMP tools in their OOBB holders

Use this directory from the holder checkout. Its sibling checkouts are `../oomp_tool_version_5` (tool identity, evidence and geometry) and `../oomlout_oobb_version_5` (base catalogue). The [queue](README.md) is an inventory of the active manifests. Each tool has one packet. Each production holder has one entry in [layouts.yaml](layouts.yaml), even when several tools share it. Paths inside packets are labelled with their starting directory.

## Plan and order of work

1. **Prove a single model and holder.** The M10 and M13 single-place guides are the completed examples. Start with the [60 mm driver bit](packets/tool_screwdriver_driver_bit.yaml). Its packet identifies a representative HiKOKI PH2/PZ2 bit and a real single-place holder. Build that guide before repeating the bit. The separate quarter-inch record has a staged 89 mm PH2 datasheet and starts at seven places. The existing Teeny Turner, Mitutoyo caliper and tall precision drivers also have local dimensional references and can go directly to pose verification.
2. **Build the remaining external models.** Filter the queue for `holder envelope`. Open each packet's drawing and evidence. Follow its individual modelling and seating instructions. For unidentified markers and TDPB tools, record the specific missing photograph or dimension and continue with an evidenced item. New identities belong in OOMP populate only if auditing a new layout reveals a genuinely unrepresented tool.
3. **Integrate reusable models.** For packets that already have a tool model, preserve the sourced dimensions and use the production STL for digital fitting. Start with an individual seat where available. Inspect the ring, jaw, grip, cap, slider or other seating feature named in the packet.
4. **Publish repeated and shared layouts once per holder ID.** Finish individual models first. Then build homogeneous rows, staggered rows and blocks, mixed spanner and hex sets, the paired tool holders, and finally the bench stand. Use every member and quantity in the layout entry. The closed utility knives are alternatives for one slot in their single-place holder. Keep their views separate. The Prit and Quikpik combinations have two distinct tools.

## Complete one tool

- Open the source record, the staged SVG and any `staged_file`, thumbnail, measurement sheet, CDR or datasheet listed in the packet. A staged SVG for `holder_envelope` depicts the pocket. Use a manufacturer drawing, a scaled photograph or a measured specimen for tool dimensions. Identify any representative article and label estimated dimensions on the tool page.
- Edit the tool's existing multiline dictionary in `../oomp_tool_version_5/working_tool_declarations.py`. Retain the existing `key` and OOMP ID. Include `model_kind`, a multiline `parameters` dictionary, `model_note` and individual source dictionaries with `title`, `url` and `supports`. Put routine defaults at the top. Assemble named dictionaries and pass them as `**kwargs`. Keep physical dimensions editable in millimetres.
- Build geometry in `working_tool_geometry.py` or reuse an existing recipe. Follow `combination_spanner` for dimensional solids and `working_photo_tools.py` plus the side-cutter packet for calibrated outlines, grip contours, materials and photo overlays. Give each coloured section a name and material. Preserve one watertight positive-volume STL and an equivalent full-scale GLB. Extend the studio render selection in `working_blender.py` for a new model kind.
- In this holder project's `working_oomp_populate.py`, declare the exact model, layout, canonical OOMP ID, label, translation, XYZ rotation, loading action and seated check. The pilots use a translation in mm, ring down at negative Y and thickness centred on the seam. Measure other poses on their own production solids. Select by complete holder ID where model/layout pairs could collide.
- Use the build sequence below. Inspect the studio view, assembled and exploded sheet, final loading frame and booklet. The part README should identify the tool, link the OOMP record, show the new render and include assembly steps in the main page. Check links from the root holder catalogue, tool page and base project README.

## Build sequence

Run PowerShell from the holder repo. Replace both values with the packet's canonical OOMP ID and the target layout's exact ID. These values reproduce the M10 pilot. The first build uses OOMP populate, OOMP materialization, model generation, SVG, Blender and documentation. Import reads the sibling model files, so run it after the OOMP build.

```powershell
$toolId = 'tool_wrench_m10'
$holderId = 'oobb_part_holder_tool_spanner_m10_1_place_3x5x9'
Push-Location ../oomp_tool_version_5
python working.py --filter $toolId --render-blender
Pop-Location
python presentation/sync_tool_guides.py import-models
python working.py --filter $holderId
python presentation/sync_tool_guides.py export-guides
python presentation/tool-model-handoff/stage.py
```

Check each command's exit status before advancing. Export once per finished batch. The staging script works offline against both checkouts and regenerates packets, local drawing copies, previews and the layout inventory. Edit the packet guidance in `briefs.yaml`, and add supplemental sources to `references.yaml`. Put durable dimensional evidence in the OOMP declaration as well.

## Repeated and mixed layouts

The guide worker accepts one tool type in one or more positions and additional individual tool types. The two- and three-place M10 guides exercise repeated instances in two-piece holders. The quarter-inch bit blocks exercise one-piece holders and staggered rows. The Pritt and closed-knife guide exercises two distinct tool types. Preserve the current single-place input as a one-instance default. Extend the instance representation for repeated quantities of additional tool types before using it for the bench stand.

- Derive stations from the positioned pockets, pitch, offsets and row settings in the holder's canonical geometry. Store each tool's ID and transform with its seat. Load each source GLB once and instance it at full scale. Check each tool against printed solids and against previously seated tools along its insertion path.
- Use `holder_layers.assembled_layers` for printed bodies. Show two contacting halves on wall holders, separate the front half along the mounting axis in the exploded view, and keep the opening up. Blocks and the bench stand use one solid and their own upright frame.
- Count instances in the inventory, steps and pictures. The M13/M10/M8/M7 pockets have a defined left-to-right order. The metric hex sets reverse station order in one variant. The stand contains two M10s. The bit blocks alternate rows of eight and seven. Use the production geometry to verify these cases.
- Key exported booklets by full holder ID before multiple layouts share a model name. Update guide discovery in `holder_navigation.py`, `presentation/sync_tool_guides.py` and the sibling `working_action.py` so each page links to the correct layout, including guides with multiple tools or no single-place equivalent. Extend `stage.py`'s loaded-layout audit when the guide manifest records alternate scenes or multiple instances.

## Verify and resume

The pilot manifests in `parts/<holder ID>/assembly/assembly_manifest.json` record tool and holder hashes, measured pocket occupancy, 15 sampled insertion positions and overlap with both halves. Check the imported mesh hashes against OOMP. Keep the physical fit marked unverified until someone tests the actual tool and print. If an independently sourced model collides, document the measured mismatch and investigate the specimen and pose. Keep its original scale.

Run `python -m pytest -q tests` in both repositories. Refresh the queue before handing off. Report finished holder IDs, unfinished external models, and the specific evidence or incompatible dimension blocking any remaining view. The two single-place pilots can be inspected directly in the [10 mm guide](../../parts/oobb_part_holder_tool_spanner_m10_1_place_3x5x9/README.md#assembly) and [13 mm guide](../../parts/oobb_part_holder_tool_spanner_m13_1_place_3x5x10/README.md#assembly).
