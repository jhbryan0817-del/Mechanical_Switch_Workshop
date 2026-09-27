# Parts and hardware

Print one of every file in `stl/`. Duplicate stems, cups, shoes, clips and sleeves are already separate files. There are 25 files, including the coupon; 24 printed pieces enter the assembly.

| Part / group | Quantity | Material | Role |
|---|---:|---|---|
| 01 tape bezel | 1 | PETG | Bonding lands and X rails |
| 02 XY bridge | 1 | PETG | Horizontal carriage, Y adjustment |
| 03 lower guide and pillars | 1 | PETG | Stem guide and structural frame |
| 04 follower guide | 1 | PETG | Guides the cups |
| 05 lower sleeves | 4 | PETG | Support guide |
| 05b upper sleeves | 4 | PETG | Retain guide |
| 06 contact stems | 2 | PETG | Sliding switch contacts |
| 06b retaining clips | 2 | PETG | Light axial retainers; print spares |
| 07 spring cups | 2 | PETG or nylon | Cam followers and spring seats |
| 08 shoes | 2 | 95A TPU | Soft switch contact |
| 09 servo cradle | 1 | PETG | Servo location and stop pins |
| 10 retaining cap | 1 | PETG | Servo retention |
| 11 face cam | 1 | PETG or nylon | Two-lobe drive |
| 12 controller tray | 1 | PETG | Open electronics mount |
| 13 coupon | 1 | PETG | Pilot-hole selection |

## Purchased items

| Item | Quantity | Selection / fit check |
|---|---:|---|
| FEETECH STS3215, 7.4 V variant | 1 | Confirm label; body, axis and cable clearance |
| Supplied metal 25T output disc and centre screw | 1 set | Centre screw per manufacturer, nominal M3 × 6; verify actual hardware |
| Waveshare Servo Driver with ESP32, SKU 21593 | 1 | 65 × 30 mm PCB; 58 × 23 mm mounting pattern |
| M3 × 12 machine screws | 8 | 2 X locks, 4 Y locks, 2 sidecar screws |
| M3 × 14 machine screws | 8 | 4 cradle-to-pillar, 4 cap; verify 8–10 mm engagement after washers |
| M3 × 12 contact adjuster screws | 2 | At least 8 mm engagement in stems |
| M3 cam-to-disc screws | 4 | Length depends on your metal horn; measure before buying |
| M3 hex nuts | 6 | X/Y locks; do not use nyloc where clearance is insufficient |
| M3 flat washers | Approximately 22 | Heads, slot clamps and nut-bearing faces; check stack heights |
| Primary compression springs | 2 | Characterize to `mechanics.md`; do not substitute by appearance |
| Return compression springs | 2 | Lighter than primary springs; verify coil-bind margin |
| Acrylic foam double-sided tape | Six cuts | Nominal 1 mm thick, compatible with actual plastic; total 1,848 mm² |
| Insulating foam shims | As needed | Servo fit, PCB edge protection |
| Small cable ties | 4–6 | PCB retention and external strain relief |
| Compatible 3-wire ST-series bus cable | 1 | Confirm pin order and connector keying |
| Regulated 7.4 V DC supply | 1 | ≥3 A; 5 A headroom is a design recommendation, not a tested requirement |
| DC lead, strain relief and inline protection | As appropriate | Match board polarity and cable/supply ratings |

M3 lengths are starting assembly selections, not permission to bottom screws. Measure stack thickness and available depth. The coupon holes are 2.5, 2.6, 2.7 and 2.8 mm, ordered left-to-right in the source model; mark the printed coupon. Production pilots currently use 2.7 mm. If your coupon selects another diameter, revise the CAD before printing the main parts.

Tools: calipers, small screwdrivers/hex keys, deburring tools, fine abrasive, spring scale or force gauge, multimeter, 3D printer, and preferably a current-limited bench supply. No tools for opening a mains accessory are needed.
