# IoT Beyond Lab — Mechanical Switch v0.4

Current four-part design exported from the edited **Mechanical Switch** Fusion document. **82 × 82 mm** footprint; **54.8 mm** enclosure depth, excluding adhesive and the wall-switch plate.

![Closed branded enclosure](assets/fusion-assembly.png)

The integrated chassis has wall-connected corner screw blocks and a full-height left PCB platform with two blind M3 pilots. The right PCB edge rests on ledges and is captured by solid rectangular cover pads. Display and button openings are closed; ventilation, wiring and fastening openings remain.

**The meshes are ready to slice, but the assembly remains a fit-test prototype.** The actuator is a placeholder. The preserved rear shielding overlaps the switch-rocker reference; physical fit and actuation are not validated.

- [Four print-oriented STLs](stl), in millimetres, centered in XY and seated on Z=0.
- [Fusion archive](cad/Mechanical_Switch_v04.f3d) · [STEP assembly](cad/Mechanical_Switch_v04.step).
- [Printing](docs/printing.md) · [Assembly](docs/assembly.md) · [BOM](docs/bom.md) · [Mechanics](docs/mechanics.md) · [Wiring](docs/wiring.md) · [Validation](docs/validation.md).

![Internal assembly](assets/fusion-internal.png)

The Fusion archive is the source of truth, including manual edits. The [export script](cad/export_current_fusion.py) exports an already-open design; it does not rebuild geometry. Superseded six-part v0.3 files are in [archive/v0.3](archive/v0.3). Do not mix them with v0.4.
