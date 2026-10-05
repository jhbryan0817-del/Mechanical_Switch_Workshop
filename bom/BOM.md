# Bill of materials

| Qty | Item | Notes |
|---:|---|---|
| 1 each | Chassis, servo stop, cover | Current [STLs](../3d/stl/); millimetres, 100% scale |
| 1 | STS3215/ST3215 servo and stock horn | Confirm actual voltage variant and case/lead dimensions |
| 1 | Waveshare Servo Driver with ESP32 | Manufacturer PCB model included in the CAD assembly |
| 1 | Gens ace GEA8502S60E2 850 mAh 2S 7.4 V battery, EC2 | Nominal 58 × 32 × 20 mm reference envelope |
| 1 | Mating EC2 internal harness | Match polarity, insulation and load rating |
| 1 each | Inline fuse/holder and suitable 2S low-voltage protection | Select for measured load; hardware fit is not yet modelled |
| 1 | Compact DC power pigtail | Board input: 5.5 × 2.1 mm; check connector fit |
| 1 | External 2S LiPo balance charger | Compatible discharge and balance connectors |
| 1 set | Insulating pad and removable battery retention | Flat battery floor; retention method remains to be chosen |
| 4 | M3 cover screws | Approximately 12 mm starting length; verify engagement |
| 2 | M3 servo-stop screws | Approximately 8 mm starting length; 3.2 mm flange and Ø2.6 mm pilots; verify bottoming |
| 2 | Left PCB screws | Verify actual Ø2.75 mm board-hole clearance before using M3 |
| As needed | Servo leads, adhesive, actuator and actuator hardware | Actuator remains to be designed |

The servo reference is lowered 5.15 mm. The floor-to-case gap is 0.30 mm, both hold-down surfaces have 0.25 mm clearance above the case, and the horizontal stop has 0.35 mm side clearance. The stop's screw base and chassis pilots retain their original positions. These are CAD clearances; confirm them on printed parts.

The actuator and real switch interface remain unfinished. The existing tilted-rocker reference overlap with the chassis is not resolved by this revision. The battery model represents its nominal envelope; connector, protection hardware and cable routing require physical fit checks.
