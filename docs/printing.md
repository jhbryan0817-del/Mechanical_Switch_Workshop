# Printing — v0.4

Import the four binary STLs in **millimetres at 100% scale**. They are centered in XY and seated on Z=0 in the intended orientation. CAD/STEP retain assembly coordinates. STL does not encode units.

| STL | Applied orientation | Size in print axes, mm |
|---|---|---|
| 01_integrated_chassis.stl | Adhesive floor down, open side up | 82 × 82 × 52 |
| 02_servo_clamp.stl | Broad face down | 31 × 60.1 × 3.2 |
| 03_actuator_PLACEHOLDER.stl | Horn mating face down | 26.2 × 24 × 20.7 |
| 04_closed_branded_cover.stl | Exterior face down, pads up | 82 × 82 × 13.65 |

Print one of each enclosure part; the actuator is optional for fit experiments and is not a finalized working part. Suggested untested starting profile: PETG or ASA, 0.2 mm layers, 5–6 perimeters, 6 top/bottom layers, 35–50% infill and local higher infill around screw mounts. Follow the material/printer requirements.

Inspect sliced layers before printing. Local supports may be needed under elevated right PCB ledges and wiring openings. Avoid supports inside blind pilot bores where possible. Cover lettering faces the bed; use a clean flat surface and inspect first-layer detail. Inspect the placeholder actuator separately for supports.

Test Ø2.6 mm pilot fit with the actual filament and screw. Do not globally scale the model to correct a hole. Fit-test the servo, PCB, connectors and real switch before a final build. Mesh closure is not a strength or physical-fit certification.
