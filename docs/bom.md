# Bill of materials — v0.7

| Qty | Item | Notes |
|---:|---|---|
| 1 each | Revised chassis, horizontal stop, cover | Current 2026-10-02 STLs in `stl/`; archived v0.4 meshes are incompatible |
| 1 | Manually designed actuator | Not present in current live model; user will design it |
| 1 | STS3215/ST3215 servo and stock horn | Confirm actual voltage variant and case/lead geometry |
| 1 | Waveshare Servo Driver with ESP32 | Manufacturer PCB reference; lowered 3.2 mm and moved +4.8 mm in Y |
| 1 | Gens ace GEA8502S60E2 850 mAh 2S 7.4 V 60C battery, EC2 | 58 × 32 × 20 mm nominal; 63 × 34 × 22 mm published upper dimensions |
| 1 | Mating EC2 internal harness | Correct polarity, insulation, strain relief and current rating |
| 1 | Inline fuse and holder | Size from measured load/inrush and wire rating; no fuse value validated |
| 1 | Suitable 2S low-voltage disconnect/protection | No integrated pack BMS assumed; hardware size not yet modeled |
| 1 | Compact internal DC power pigtail | Match board's 5.5 × 2.1 mm input; physical fit unresolved |
| 1 | External 2S LiPo balance charger | For EC2 discharge and JST-XHR-3P balance leads |
| 1 set | Insulating pad and removable battery retention | Flat floor; 2.5 mm to unchanged nominal battery reference. Old strap tunnels removed; retention method and pad thickness require validation |
| 4 | M3 cover screws | Existing approximately 12 mm starting length; verify |
| 2 | M3 horizontal-stop screws | Approximately 8 mm starting length; verify pilot depth |
| 2 | Left PCB screws | Verify Ø2.75 mm board-hole clearance before using M3 |
| As needed | Actuator hardware, adhesive, servo leads | Finalize after fit and force tests |

Battery choice: [manufacturer specification](https://genstattu.com/gens-ace-850mah-2s-60c-7-4v-lipo-battery-ec2-plug-car-classic-non-g-tech/). The 850 mAh pack is close to the requested 1000 mAh and leaves a useful tolerance allowance within the compact enclosure. The researched Gens ace 1000 mAh alternative is 72 mm long nominal, with a stated ±5 mm length tolerance, too long for the 76 mm nominal internal span without further enlargement.

The battery reference is a dimensional envelope, not an imported detailed vendor CAD assembly. Protection hardware and connector bodies need selection and fit verification before a powered build.
