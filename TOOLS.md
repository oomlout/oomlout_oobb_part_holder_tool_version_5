<!-- oobb-presentation:start -->
# Tool inventory

64 printable layouts in 18 tool categories. Sizes are width × height in 15 mm grid units, followed by the source design depth in millimetres.

## Hierarchy

```mermaid
flowchart LR
    root["OOBB tool holders"] --> family["Tool type"] --> model["Model or size"] --> layout["Layout"] --> size["Grid and design depth"] --> part["Part folder"]
```

```text
oobb / part / holder_tool
├── blade_disposal  olfa_dc3
├── caliper         mitutoyo_500_196_30
├── drill_cleaner   tdpb_m3 · tdpb_m6
├── driver_bit      driver_bit_60mm · quarter_inch
├── glue_stick      prit_medium
├── hex_key         small_metric_set
├── knife           utility_17mm
├── marker          bic_clear_lid · german_big · ikea_mala · patterned_thick · sharpie · sharpie_style_13mm
├── mixed_tools     basic_stand
├── nozzle_changer  tdpb
├── pliers          needle_nose_130mm
├── screwdriver     picquic_teeny_turner · quikpik_200mm
├── screwdriver_precision_tall  hex_60mm
├── side_cutters    generic_110mm
├── spanner         m7 · m8 · m10 · m13 · m13_m10_m8_m7 · m21
├── tape_measure    stanley_1_30_696
├── timer           round_80mm
└── wire_strippers  generic_120mm
```

Each model opens into layout, then size, then the canonical part folder.

## Tools and layouts

| Tool type | Tools | Print layouts |
| --- | --- | ---: |
| [Blade disposal](navigation_oobb/oobb/part/holder_tool/blade_disposal/) | OLFA DC-3 blade disposal can | 1 |
| [Caliper](navigation_oobb/oobb/part/holder_tool/caliper/) | Mitutoyo 500-196-30 digital caliper, 150 mm | 1 |
| [Drill cleaner](navigation_oobb/oobb/part/holder_tool/drill_cleaner/) | TDPB M3 drill cleaner<br>TDPB M6 drill cleaner | 2 |
| [Driver bit](navigation_oobb/oobb/part/holder_tool/driver_bit/) | Driver bit, 60 mm profile<br>Quarter-inch drive bit<br>Quarter-inch drive bit block, 3 rows<br>Quarter-inch drive bit block, 5 rows<br>Quarter-inch drive bit block, 7 rows | 13 |
| [Glue stick](navigation_oobb/oobb/part/holder_tool/glue_stick/) | Medium Prit glue stick<br>Medium Prit glue stick and utility knife | 2 |
| [Hex key](navigation_oobb/oobb/part/holder_tool/hex_key/) | Small metric hex keys, 1.5–5 mm | 2 |
| [Knife](navigation_oobb/oobb/part/holder_tool/knife/) | Utility knife, 17 mm blade | 1 |
| [Marker](navigation_oobb/oobb/part/holder_tool/marker/) | BIC clear-lid marker<br>IKEA MÅLA marker<br>Large German marker<br>Sharpie marker, 13 mm v4 profile<br>Sharpie-style felt-tip pen, 13 × 137 mm<br>Thick patterned marker | 18 |
| [Mixed tools](navigation_oobb/oobb/part/holder_tool/mixed_tools/) | Basic mixed-tool bench stand | 1 |
| [Nozzle changer](navigation_oobb/oobb/part/holder_tool/nozzle_changer/) | TDPB nozzle changer | 1 |
| [Pliers](navigation_oobb/oobb/part/holder_tool/pliers/) | Blue needle-nose pliers, 130 mm | 1 |
| [Screwdriver](navigation_oobb/oobb/part/holder_tool/screwdriver/) | Picquic Teeny Turner precision multi-driver<br>Quikpik 200 mm multi-driver and utility knife | 2 |
| [Screwdriver precision tall](navigation_oobb/oobb/part/holder_tool/screwdriver_precision_tall/) | Tall precision screwdriver, 1.5 mm hex, 60 mm<br>Tall precision screwdriver, 2 mm hex, 60 mm<br>Tall precision screwdriver, 2.5 mm hex, 60 mm | 6 |
| [Side cutters](navigation_oobb/oobb/part/holder_tool/side_cutters/) | Red side cutters, 110 mm | 1 |
| [Spanner](navigation_oobb/oobb/part/holder_tool/spanner/) | M7 spanner<br>M8 spanner<br>M10 spanner<br>M13 spanner<br>M13, M10, M8 and M7 spanners<br>M21 spanner | 9 |
| [Tape measure](navigation_oobb/oobb/part/holder_tool/tape_measure/) | Stanley 1-30-696 tape measure, 5 m | 1 |
| [Timer](navigation_oobb/oobb/part/holder_tool/timer/) | Black round timer, 80 mm | 1 |
| [Wire strippers](navigation_oobb/oobb/part/holder_tool/wire_strippers/) | Red wire strippers, 120 mm | 1 |

[Illustrated loading guides and print booklets](README.md#assembly)
<!-- oobb-presentation:end -->
