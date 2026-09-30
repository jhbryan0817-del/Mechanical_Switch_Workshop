# Validation — v0.7 Fusion revision, 2026-09-30

The Mechanical Switch cloud document was saved successfully and verified with `isModified=false`. This update changes repository Markdown documentation only. CAD, STEP, STL, images, scripts and JSON reports remain the historical v0.4 baseline. No 3D files were exported.

## Checks on the current live design

- Three PRINT components are present: chassis, horizontal stop and cover. Each has exactly one solid body and one lump. There is no actuator in the inspected live model; none was created.
- Temporary-BRep intersection checks of the revised chassis against all other live bodies found no overlap above 0.001 mm³ with the servo/horn, manufacturer PCB bodies, stop, cover or nominal battery.
- A temporary 63 × 22 × 34 mm maximum battery envelope at X=-31.5..31.5, Y=-33.7..-11.7, Z=6.7..40.7 has zero chassis intersection.
- The retained cable cavity X=38.35..46, Y=1..21, Z=13..44 has zero chassis intersection.
- The former rib region above Z=4.2 is empty. The former floor-slot region contains its full expected 190.4 mm³ of solid floor material.
- Both Print 02 holes and both corresponding chassis pilots measure Ø2.6 mm. The actuator opening has four cylindrical R3 mm corner faces through the full floor thickness.
- Top, underside and oblique views were inspected; the saved view exposes the cleaned chassis and stop.

## Limits and remaining checks

The fixed tilted-rocker reference still overlaps the chassis by **254.83 mm³**. The v0.6 documentation reported 251.30 mm³; rounding the window corners adds material at the corners and increases that unresolved overlap. This is not a passing switch-fit result. Final actuator shape, contact position, travel and actual mounting alignment remain manual design and fit tasks.

Earlier actuator-angle and assumed connector-volume checks are historical and do not validate v0.7. The current model has no actuator or dedicated maximum-battery/lead-clearance reference component; the maximum battery test above used temporary geometry only.

The battery ribs and strap tunnels are gone. The nominal pack remains 2.5 mm above the flat floor, so pad thickness and a removable retention method need physical validation. Screw thread forming, simultaneous engagement through stop and chassis, PCB support stiffness and cover-pad pressure also need a print trial. The straight inset left support preserves modeled capacitor clearance.

No slicing, mesh export, print trial, structural analysis, electrical test or physical assembly was performed. Compact power-pigtail, lead bend radii, protection hardware and real battery wrapping/tab fit remain unverified. Historical STL reports do not validate this revision.
