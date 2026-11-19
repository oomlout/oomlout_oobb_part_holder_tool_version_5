# Building the tool-holder catalogue

Run the three stages below, or run `python working.py` for the full sequence. Pass the same `--filter` to each stage to build one model or layout. For example, `python working.py --filter picquic_teeny_turner` rebuilds the precision multi-driver holder.

```powershell
python working_oomp_populate.py
python working_oomp.py
python working_svg.py
```

Use Python 3.11 or newer. Put the OOBB v5 and OOMP v5 checkouts on `PYTHONPATH`, with their Python dependencies installed. The first supplies `opsc` and the second supplies `oomp` and `oomp_populate_helper`. The catalogue also uses PyYAML, trimesh, NumPy, SciPy and Pillow. Use an OpenSCAD build with the Manifold backend on `PATH`. Put Blender on `PATH` or set `BLENDER_EXE` to its executable. On Windows the renderer also searches the Blender Foundation install directory. The migration was built with Python 3.12.2, OpenSCAD 2026.04.16 and Blender 5.2.2 LTS.

## Editing a holder

1. Edit the tool envelope in `get_profiles()` in [working_oomp_populate.py](../working_oomp_populate.py). Each dictionary describes a negative cylinder or extruded polygon. Positions, radii, lengths and points are in millimetres. Rotation is in degrees. A cylinder starts at its position and extends along its rotated local Z axis.
2. Edit a variant in `get_options()` in the same file. The record names its tool type, model, layout, grid dimensions, source design depth and profile. Multi-tool rows use a centre-to-centre spacing. Layered bit holders add a second row with one fewer bit, offset by half a pitch. The basic stand uses upright profiles and corner mounting holes.
3. Regenerate. Populate writes an active ID manifest and source YAML. OOMP resolves the IDs and writes canonical part metadata. The SVG stage builds the OpenSCAD print layout and STL, sections that mesh, renders the studio views and publishes navigation. A full build updates the catalogue after changing a taxonomy name. Historical part directories can be retained independently of the active navigation.

The part page gives both **design depth** and **printed thickness**. A vertical layout prints one half-depth face. The combined medium Prit glue-stick and craft-knife layout includes two complementary faces, side by side. The bench stand uses its full 66 mm depth. Studio sheets show the full assembled holder and an exploded view of its two halves. The SVG shows a horizontal section near that face and a cross section through the dashed line. Section positions can be set with `near_face_fraction` and `cross_section_y_fraction` in the populate record.

Source settings live in populate. To add local metadata for a canonical part, use its `working_manual.yaml`. Keep hand-written README text outside the generated block. `build/` contains disposable render and mesh caches. A rebuild from an empty cache recreates them.

## Rendering the two-piece holder

Repeat this convention for every vertical holder. Render it upright as mounted on a wall, with the pocket mouth at the top and the tool handles above it. Use dark teal for the wall-side half and light teal for the front half. Show the halves seated rim to rim, then draw the front half outward perpendicular to the wall for the exploded view. Keep the mounting holes aligned. In the assembly steps the tool enters downward from above. The studio rotates the entire assembly together by 90° about its local X axis. The bench stand sits level on the bench.

The construction settings come from `get_construction()` in populate. Most holders use two copies of one STL. For handed pocket patterns (metric hex keys and the Quikpik combination), mirror the second copy along X in the slicer before turning it over. The Prit and knife print layout already contains the complementary pieces and needs one copy of the layout. Render the bench stand as a single piece. The build uses the same layer placement for the studio sheets, guide illustrations and digital fit checks.

## Tool-loaded assembly guides

The project README and each guided holder's main README include the numbered actions and illustrated steps. The catalogue links to those READMEs. Edit the step definitions in populate and regenerate to update both locations. The offline HTML and printable PDF are also available from each README.

The [four loading guides](../README.md#assembly) use the coloured GLB models from the OOMP tool catalogue. Each guide pairs one model with its single-place production STL. The poses, loading instructions and page style are editable in `get_tool_assemblies()`, `get_loading_steps()` and `get_book_style()` in [the populate file](../working_oomp_populate.py). Translations use millimetres and rotations use degrees.

Run `python working.py --filter needle_nose_130mm` to rebuild the pliers guide, or `python working.py` to rebuild the catalogue. The assembly stage also uses manifold3d for mesh intersections, ReportLab and svglib for booklet artwork, and PyMuPDF for page review. Each modelled part has an `assembly/` directory with the offline HTML viewer, printable PDF, illustrated sequence, inventory and source hashes. The presentation sheet shows the tool in the closed holder alongside an exploded view.

The renderer preserves each tool’s original scale. The build checks that the tool enters the pocket and measures its overlap with both halves at 15 positions along the insertion path. The tool dimensions come from photographs. In particular, the wire stripper carries a 120 mm OOMP label, and its source model uses a provisional 130 mm reference. Physical fit awaits a print test.

After revising the models in the sibling OOMP tool checkout, run the following from this repository. The import refreshes the local source meshes and metadata. The export copies the finished booklets into the base OOBB and OOMP tool catalogues, updates the tool pages, and refreshes the base README thumbnail.

```powershell
python presentation/sync_tool_guides.py import-models
python working.py
python presentation/sync_tool_guides.py export-guides
```

## Migration checks

- The vertical project has 12 active variants in its generator and one historical 3 × 1 Sharpie-style holder in its part folders. All 13 are included. Its tool dictionary reused the same mutable object for the bit, multi-driver and marker. The last definition gave the saved bit and multi-driver models the marker’s 14 × 137 mm cutter. The v5 profiles use the original declared cutouts of 8 × 100 mm for the bits, 9.5 × 28 mm for the Teeny Turner and 14 × 137 mm for the marker. These are cutter diameters and lengths. All 13 migrated meshes were checked against the source recipe with independent tool dictionaries, including the seven staggered upper pockets on both layered layouts. [Vertical source recipe](https://github.com/oomlout/oomlout_oobb_part_tool_holder_vertical/blob/93a962a09e0c275c3cfa62187182ac3203bde1b2/scad.py)
- The v4 tool-holder set contains 47 vertical layouts and one mixed-tool stand. Each one was compared with a fresh STL export of its published OpenSCAD file. All 48 matched in bounds and connected body count. The symmetric volume difference was below 0.0001 mm³ in each comparison. The crimper entries are commented out in v4 and have no released holder in this set. [V4 catalogue definitions](https://github.com/oomlout/oomlout_oobb_version_4/blob/41f5386997faef4473c959dfb8c929864d7bf697/oobb_make_sets.py#L626) · [V4 released geometry](https://github.com/oomlout/oomlout_oobb_version_4_generated_parts/tree/654a21d735523b3a7b14c07f2363fa6f108d15d5/navigation_oobb/)
- All 61 generated meshes were checked as closed positive-volume solids. Physical tool fit and print testing remain unverified. Run `python -m pytest -q tests` for the project tests, including the profile and layered-layout regressions. The two-piece regression uses Shapely and Rtree to compare the actual pocket and mounting-hole outlines on each side of the seam for every vertical holder.


## Rebuild verification

During the original migration, the three entry points were run from a different working directory against a clean copy with empty output folders. The source YAML, canonical metadata, OpenSCAD, STL, SVG and navigation pages matched the original build byte for byte. All 61 holder sheets regenerated. The two GPU render runs differed by at most one level per 8-bit colour channel.
