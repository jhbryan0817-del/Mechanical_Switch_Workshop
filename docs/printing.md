# Printing — current v0.7 parts, exported 2026-10-02

The three STLs at the top level of `stl/` are current exports of the active Mechanical Switch document, including its unsaved changes on top of Fusion cloud version 9. Old meshes are under `stl/historical/v0.4/`; do not combine that broad clamp or actuator placeholder with these parts. Files in `cad/` remain historical v0.4 and do not describe the current assembly.

| Quantity | File | Orientation supplied | Print envelope (mm) |
|---:|---|---|---|
| 1 | [01_integrated_chassis.stl](../stl/01_integrated_chassis.stl) | Flat enclosure floor down, open cavity up | 90 × 82 × 52 |
| 1 | [02_horizontal_servo_stop.stl](../stl/02_horizontal_servo_stop.stl) | Outer flat flange face down; rotated -90° about assembly Y | 22.2 × 14 × 8.65 |
| 1 | [03_cover_and_pcb_capture.stl](../stl/03_cover_and_pcb_capture.stl) | Exterior down, PCB capture pads up; rotated 180° about assembly X | 82 × 82 × 16.85 |

Each mesh is centered in XY with its lowest vertex at Z=0. STL carries no unit metadata: select **millimetres** and **100% scale** in the slicer. The orientations are starting choices, not tested slicing profiles. The cover's exterior details may need support or an alternative orientation after previewing bed contact.

Fusion export used binary STL and High mesh refinement. Postprocessing applies rotations/translations to vertices and normals only; no scaling, smoothing, hole repair or design changes. [The manifest](../validation/exports.json) records source components/bodies, assembly bounds, CAD volumes, transforms and SHA-256 checksums. The cover component is PRINT 03 even though its body retains the historical PRINT 04 name.

Fusion contains three single-solid print components: chassis, horizontal servo stop and cover; actuator design is reserved for manual work. Battery, electronics and wiring references are not printable parts.

The obstructing upper-right PCB tab and its cover pad are removed. The lower-right support has a continuous connection to its flange. The battery-side exterior is flat. These edits remove the identified obstruction and placement mismatch; they are not physical print-strength validation.

Before printing, preview every layer and choose supports for the remaining rail, blind pilots, cable-pocket ceiling, rounded actuator opening and cover pads. The old broad clamp's orientation is not applicable.

The previous untested starting profile remains PETG or ASA, 0.2 mm layers and 5–6 perimeters, with local reinforcement around screw mounts. Verify pilot fit in actual material; do not globally scale the design to correct holes. Deburr battery-contact surfaces and use an insulating pad and a physically verified removable retention method; the old strap tunnels are removed.

All three meshes passed binary-file integrity, finite-coordinate, closed-edge, consistent-winding, normal-direction, single-shell, nondegenerate-triangle, positive-volume and Z=0 checks. Mesh volume differs from the source solid by less than 0.006%. Run `python validation/check_stl.py` from the repository to reproduce these checks. No self-intersection analysis, slicing, print trials or FEA were performed. Actual board retention, battery/connector fit and switch/actuator alignment remain to be checked.
