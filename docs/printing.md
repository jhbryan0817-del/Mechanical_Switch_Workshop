# Printing status — v0.6

**No revised 3D files were exported.** Files in `stl/` and `cad/` remain v0.4 and do not match the live Fusion v0.6 assembly. Do not print this revision from historical files or combine the old broad clamp with the current chassis.

Fusion contains four single-solid print components: chassis, horizontal servo stop, relocated actuator placeholder and revised cover. Battery, electronics and wiring references are not printable parts.

The obstructing upper-right PCB tab and its cover pad are removed. The lower-right support has a continuous connection to its flange. The battery-side exterior is flat. These edits remove the identified obstruction and placement mismatch; they are not physical print-strength validation.

A future print-preparation pass must choose orientations and check supports for the remaining rail, blind pilots, cable-pocket ceiling, strap tunnels and cover pads. The old broad clamp's orientation is not applicable.

The previous untested starting profile remains PETG or ASA, 0.2 mm layers and 5–6 perimeters, with local reinforcement around screw mounts. Verify pilot fit in actual material; do not globally scale the design to correct holes. Deburr battery-contact surfaces and use the intended insulating pad and soft strap.

No slicing, mesh validation, print trials or FEA were performed. Actual board retention, battery/connector fit and switch/actuator alignment remain to be checked.
