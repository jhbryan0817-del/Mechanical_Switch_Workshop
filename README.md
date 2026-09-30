# IoT Beyond Lab — Mechanical Switch v0.7

The **Mechanical Switch** Fusion cloud document contains the saved v0.7 revision (2026-09-30). The live design is the source of truth.

The battery ribs and their tunnels are removed, both battery-floor slots are sealed, and the floor is flat. Print 02's two holes now match the Ø2.6 mm M3 self-threading pilots. Small obsolete recesses are cleaned up while retaining the large servo-wire passage. The through-floor actuator opening has four tangent R3 mm corners.

Overall enclosure envelope: **90 × 82 × 54.8 mm**, excluding adhesive and switch plate. The main enclosure remains 82 mm wide, with the existing 8 mm side cable pocket. Walls remain 3 mm nominal; the floor remains 3.2 mm.

**Documentation-only repository update:** CAD, STEP, STL, screenshots, scripts and JSON reports remain the **v0.4 baseline**. They do not represent v0.7 and must not be used to print this assembly. No revised 3D files were exported or uploaded; the revision is saved in Fusion only.

- [Mechanics](docs/mechanics.md) · [Assembly](docs/assembly.md) · [BOM](docs/bom.md)
- [Battery and wiring](docs/wiring.md) · [Printing status](docs/printing.md)
- [Validation and remaining checks](docs/validation.md) · [References](reference/README.md)

No actuator is present in the current live document; actuator design is reserved for manual work. The existing switch-rocker/chassis overlap remains unresolved. CAD checks are not physical fit or print validation.

## Historical v0.4 exports

[CAD and STEP](cad) · [STLs](stl). These images also show v0.4.

![Historical v0.4 closed enclosure](assets/fusion-assembly.png)
![Historical v0.4 internal assembly](assets/fusion-internal.png)

The historical export script is not part of this revision's workflow; it modifies geometry and overwrites v0.4-named files.
