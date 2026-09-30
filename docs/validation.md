# Validation — v0.5 Fusion revision, 2026-09-30

The revised Mechanical Switch document was saved in Fusion. No geometry or new JSON reports were exported to the repository. The existing files under `validation/` describe v0.4 only.

## Checks performed in Fusion

- Each of the four PRINT components contains one solid lump.
- Pairwise temporary-BRep intersections among chassis, servo/horn, PCB bodies, horizontal stop, neutral actuator, cover and nominal battery reported no positive volumes above 0.001 mm³.
- The maximum vendor battery envelope, 63 × 34 × 22 mm, has zero calculated intersection volume with chassis or cover.
- The unchanged actuator was rotated about the modeled shaft axis at −15, −12, −8, 0, 8, 12 and 15 degrees. At every sample, calculated intersection volume with chassis, new stop and maximum battery envelope was zero.
- Open and closed assembly views were inspected. The board and battery are present; the cover is left hidden for internal inspection.
- Fusion reported the active document saved with `isModified=false`.

## Limits and unresolved items

This is a fit-test prototype. The angle samples are not a continuous sweep or a validated working travel range. No physical assembly, print trial, thermal/load test, firmware calibration, battery-runtime measurement or FEA was performed.

The pre-existing switch-rocker/shielding overlap was not changed or revalidated; v0.4 recorded approximately 242.9 mm³. Real switch fit and final actuator geometry remain unresolved.

The servo model is simplified. Cable/connector references are assumed clearance volumes, not detailed manufacturer geometry. Verify actual servo lead exit, bend radius, board connector headroom and the insertion sequence. The stock board DC jack is close to the left wall; actual internal power-pigtail fit is unresolved.

The battery bay accounts for the vendor's stated dimensional maxima, but cell tabs, wrapping, connector exits and pack condition must be measured. Confirm the actual servo voltage variant before using a fully charged 2S pack. Fuse and low-voltage protection hardware are required for the proposed wiring architecture but have not been selected, modeled or electrically tested.

Check Ø2.75 mm PCB holes against actual fasteners, printed pilot strength, cover-pad pressure, battery strap retention, and adhesive loading with the added battery mass. Do not interpret old STL closure checks as validation of this revision.
