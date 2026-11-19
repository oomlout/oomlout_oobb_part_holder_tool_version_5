<!-- oobb-presentation:start -->
# Tool inventory

61 printable layouts in 17 tool categories. Sizes are width × height in 15 mm grid units, followed by the source design depth in millimetres.

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
├── knife           exacto_17mm · utility_17mm
├── marker          bic_clear_lid · german_big · ikea_mala · patterned_thick · sharpie · sharpie_style_13mm
├── mixed_tools     basic_stand
├── nozzle_changer  tdpb
├── pliers          needle_nose_130mm
├── screwdriver     picquic_teeny_turner · quikpik_200mm · wera_hex_60mm
├── side_cutters    generic_110mm
├── tape_measure    stanley_1_30_696
├── timer           round_80mm
├── wire_strippers  generic_120mm
└── wrench          m7 · m8 · m10 · m13 · m21
```

Each model opens into layout, then size, then the canonical part folder.

## Tools and layouts

| Tool type | Tools | Print layouts |
| --- | --- | ---: |
| [Blade disposal](navigation_oobb/oobb/part/holder_tool/blade_disposal/) | OLFA DC-3 blade disposal can | 1 |
| [Caliper](navigation_oobb/oobb/part/holder_tool/caliper/) | Mitutoyo 500-196-30 digital caliper, 150 mm | 1 |
| [Drill cleaner](navigation_oobb/oobb/part/holder_tool/drill_cleaner/) | TDPB M3 drill cleaner<br>TDPB M6 drill cleaner | 2 |
| [Driver bit](navigation_oobb/oobb/part/holder_tool/driver_bit/) | Driver bit, 60 mm profile<br>Quarter-inch drive bit | 10 |
| [Glue stick](navigation_oobb/oobb/part/holder_tool/glue_stick/) | Medium Prit glue stick<br>Medium Prit glue stick and craft knife | 2 |
| [Hex key](navigation_oobb/oobb/part/holder_tool/hex_key/) | Small metric hex keys, 1.5–5 mm | 2 |
| [Knife](navigation_oobb/oobb/part/holder_tool/knife/) | Black Exacto craft knife, 17 mm<br>Utility knife, 17 mm blade | 2 |
| [Marker](navigation_oobb/oobb/part/holder_tool/marker/) | BIC clear-lid marker<br>IKEA MÅLA marker<br>Large German marker<br>Sharpie marker, 13 mm v4 profile<br>Sharpie-style felt-tip pen, 13 × 137 mm<br>Thick patterned marker | 18 |
| [Mixed tools](navigation_oobb/oobb/part/holder_tool/mixed_tools/) | Basic mixed-tool bench stand | 1 |
| [Nozzle changer](navigation_oobb/oobb/part/holder_tool/nozzle_changer/) | TDPB nozzle changer | 1 |
| [Pliers](navigation_oobb/oobb/part/holder_tool/pliers/) | Blue needle-nose pliers, 130 mm | 1 |
| [Screwdriver](navigation_oobb/oobb/part/holder_tool/screwdriver/) | Picquic Teeny Turner precision multi-driver<br>Quikpik 200 mm multi-driver and craft knife<br>Wera 1.5 mm hex screwdriver, 60 mm<br>Wera 2 mm hex screwdriver, 60 mm<br>Wera 2.5 mm hex screwdriver, 60 mm | 8 |
| [Side cutters](navigation_oobb/oobb/part/holder_tool/side_cutters/) | Red side cutters, 110 mm | 1 |
| [Tape measure](navigation_oobb/oobb/part/holder_tool/tape_measure/) | Stanley 1-30-696 tape measure, 5 m | 1 |
| [Timer](navigation_oobb/oobb/part/holder_tool/timer/) | Black round timer, 80 mm | 1 |
| [Wire strippers](navigation_oobb/oobb/part/holder_tool/wire_strippers/) | Red wire strippers, 120 mm | 1 |
| [Wrench](navigation_oobb/oobb/part/holder_tool/wrench/) | M7 wrench<br>M8 wrench<br>M10 wrench<br>M13 wrench<br>M21 wrench | 8 |

[Illustrated loading guides and print booklets](README.md#assembly)
<!-- oobb-presentation:end -->
