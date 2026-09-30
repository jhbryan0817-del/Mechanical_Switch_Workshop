# IoT Beyond Lab — Mechanical Switch v0.5

Battery-powered enclosure revision saved in the **Mechanical Switch** Fusion cloud document on 2026-09-30. The live Fusion document is the source of truth for v0.5.

The three large external service apertures are closed. Two rows of small circular vents replace their visual role. A lowered PCB platform captures the servo vertically; a small two-screw L-shaped stop (Print 02) blocks horizontal withdrawal without crossing the horn. An outward cable pocket preserves the servo and actuator positions, and an internal removable battery bay holds a compact 2S pack.

Overall envelope: **90 × 83 × 54.8 mm**, excluding adhesive and the switch plate. The main enclosure remains 82 mm wide; the approved cable pocket projects 8 mm to one side. The battery wall extends 1 mm on its side.

**Documentation-only repository update:** CAD, STEP, STL, screenshots, scripts and JSON reports in this repository remain the **v0.4 baseline**. They do not represent v0.5 and must not be used to print the new clamp or battery chassis. No v0.5 CAD was exported or uploaded.

- [Mechanics](docs/mechanics.md) · [Assembly](docs/assembly.md) · [BOM](docs/bom.md)
- [Battery and wiring](docs/wiring.md) · [Printing status](docs/printing.md)
- [Validation and remaining checks](docs/validation.md) · [References](reference/README.md)

The actuator remains a placeholder. The existing switch-rocker/shielding overlap remains unresolved. CAD clearance checks are not physical fit, electrical, thermal, or operating-life validation.

## Historical v0.4 exports

[CAD and STEP](cad) · [STLs](stl). The images below show v0.4, not the battery revision.

![Historical v0.4 closed enclosure](assets/fusion-assembly.png)
![Historical v0.4 internal assembly](assets/fusion-internal.png)

Do not run the historical export script for this documentation-only revision: it writes geometry and overwrites v0.4-named files.
