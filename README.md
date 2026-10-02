# IoT Beyond Lab — Mechanical Switch v0.7

The **Mechanical Switch** Fusion document is the source of truth. The three printable parts in this repository were exported from its current in-memory geometry on **2026-10-02**, including unsaved changes on top of Fusion cloud version 9. The part names identify the v0.7 design; the Fusion version number is a separate cloud revision counter.

The battery ribs and their tunnels are removed, both battery-floor slots are sealed, and the floor is flat. Print 02's two holes now match the Ø2.6 mm M3 self-threading pilots. Small obsolete recesses are cleaned up while retaining the large servo-wire passage. The through-floor actuator opening has four tangent R3 mm corners.

Overall enclosure envelope: **90 × 82 × 54.8 mm**, excluding adhesive and switch plate. The main enclosure remains 82 mm wide, with the existing 8 mm side cable pocket. Walls remain 3 mm nominal; the floor remains 3.2 mm.

## Current print files

Print one of each. These are binary STLs exported in **millimetres** with Fusion's High mesh refinement, then rigidly oriented and placed at Z=0. Import at 100% scale. No geometry was rebuilt or repaired.

| Part | STL | Print envelope (X × Y × Z) |
|---|---|---|
| Chassis and internal cable pocket | [01_integrated_chassis.stl](stl/01_integrated_chassis.stl) | 90 × 82 × 52 mm |
| Horizontal servo stop | [02_horizontal_servo_stop.stl](stl/02_horizontal_servo_stop.stl) | 22.2 × 14 × 8.65 mm |
| Cover and PCB capture | [03_cover_and_pcb_capture.stl](stl/03_cover_and_pcb_capture.stl) | 82 × 82 × 16.85 mm |

All three meshes pass closed-edge, winding, connected-shell, volume and dimensional checks. See [printing](docs/printing.md), [export provenance](validation/exports.json) and [mesh results](validation/stl_checks.json). Mesh checks do not establish physical fit or a support-free print.

The incompatible v0.4 STLs and validation reports are archived under `stl/historical/v0.4/` and `validation/historical/v0.4/`. CAD/STEP and screenshots remain historical v0.4 references. This export did not save or modify the Fusion geometry.

- [Mechanics](docs/mechanics.md) · [Assembly](docs/assembly.md) · [BOM](docs/bom.md)
- [Battery and wiring](docs/wiring.md) · [Printing status](docs/printing.md)
- [Validation and remaining checks](docs/validation.md) · [References](reference/README.md)

No actuator is present in the current live document; actuator design is reserved for manual work. The existing switch-rocker/chassis overlap remains unresolved. CAD checks are not physical fit or print validation.

## Historical v0.4 exports

[CAD and STEP](cad) · [Archived STLs](stl/historical/v0.4). These images also show v0.4.

![Historical v0.4 closed enclosure](assets/fusion-assembly.png)
![Historical v0.4 internal assembly](assets/fusion-internal.png)

The historical export script is not part of this revision's workflow; it modifies geometry and overwrites v0.4-named files.
