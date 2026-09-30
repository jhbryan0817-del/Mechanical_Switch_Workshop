# Validation — v0.6 Fusion revision, 2026-09-30

The Mechanical Switch cloud document was saved successfully with `isModified=false`. This repository update changes documentation only. Existing geometry, images, scripts and JSON reports remain v0.4; no revised 3D files were exported or uploaded.

## Checks on the revised live design

- Each of the four PRINT components contains exactly one solid body and one lump.
- Final pairwise temporary-BRep checks among chassis, servo/horn, PCB bodies, stop, neutral actuator, cover and nominal battery found no intersections above 0.001 mm³. Pairs within the same reference component were excluded.
- Maximum battery envelope (63 × 22 × 34 mm in assembly XYZ) has zero calculated intersection volume with chassis and cover.
- Actuator rotations at −15, −12, −8, 0, 8, 12 and 15 degrees about the relocated shaft axis (X direction, Y=4.8, Z=22) have zero calculated intersection volume with chassis, stop, maximum battery envelope and cover.
- Assumed servo-header plug and battery lead-storage volumes have zero calculated intersection volume with chassis and cover.
- Open, populated and closed views were inspected. The saved inspection view shows chassis, stop and battery, with PCB, servo, actuator and cover hidden to expose the edits.
- Chassis and cover end at Y=-41; enclosure envelope is 90 × 82 × 54.8 mm. Servo ends at Y=37.65, leaving 0.35 mm to the front wall.

## Limits and unresolved items

The fixed tilted-rocker reference still overlaps the chassis: **251.30 mm³** in this revision. This is an unresolved interference, not a passing switch-fit result. The actuator moved +4.8 mm with the servo while the switch reference stayed fixed. Contact position, force, travel and real mounting alignment require revalidation before use.

Angle samples do not establish a continuous collision-free sweep or an operating range. No slicing, mesh export, print trial, structural analysis, electrical test or physical assembly was performed. Removing one PCB tab reduces corner support; check board flex, remaining rail strength, screw engagement and cover-pad pressure in the selected print material.

Servo and cable/connector references are simplified. Verify actual lead exit, bend radius, plug access and insertion sequence. The stock DC jack remains close to the left wall; compact power-pigtail fit is unresolved. Fuse and low-voltage-protection hardware is not modeled.

The maximum battery envelope includes documented dimensional tolerance, but tabs, wrapping, leads and connector exits need measurement. Check soft-strap threading and retention, deburr contact surfaces and use the insulating pad. Old STL closure reports do not validate this revision.
