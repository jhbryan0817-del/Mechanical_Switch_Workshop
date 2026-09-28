# Validation — v0.4

All four fabricated parts are single solid lumps in Fusion. All four STL exports pass closed-edge checks and have positive signed volume. Print meshes are seated on Z=0.

- [Fusion checks](../validation/fusion_checks.json)
- [Export dimensions and volumes](../validation/exports.json)
- [STL mesh checks](../validation/stl_checks.json)
- Repeat with `python validation/check_stl.py` (Python standard library only).

No positive-volume intersections remain among chassis, servo/horn, clamp, PCB components, cover and neutral actuator. **Known exception:** the switch-rocker reference overlaps the user-preserved rear shielding by approximately 242.9 mm³. Real-switch installation fit remains unresolved; the shielding was retained as requested.

The actuator/chassis clearance was sampled at -15, -12, -8, 0, 8, 12 and 15 degrees with no intersection. This is not a continuous sweep, safe operating-angle range or actuation proof. The actuator remains a placeholder.

No print trials, FEA, force/adhesive tests, thermal measurements or firmware calibration were performed. Actual PCB M3-hole clearance, servo/plug fit, print tolerances, screw engagement, board capture and switch travel require physical checks. Slicer-ready does not mean production-qualified.

Old v0.3 checks/reimport reports are archived and do not validate v0.4. Current geometry comes from `cad/Mechanical_Switch_v04.f3d`; the export script does not recreate manual edits.
