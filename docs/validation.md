# Validation — current print export, 2026-10-02

The three current PRINT bodies were exported from the active Mechanical Switch document using Fusion MCP. The source was Fusion cloud version 9 with `isModified=true`; the unsaved geometry was included. The export did not save the document or edit its geometry, and `isModified` remained true afterwards. Current manifests and mesh results are in `validation/exports.json` and `validation/stl_checks.json`. Old STL/report files are archived in their respective `historical/v0.4/` folders. CAD/STEP and images remain v0.4.

## Checks on the exported meshes

Each source PRINT component has exactly one solid BRep body and one lump. Each exported mesh has one connected shell, positive signed volume, no boundary/nonmanifold edges, no winding errors, no degenerate triangles and normals consistent with triangle winding. Coordinates are finite; the lowest vertex is at Z=0; SHA-256 hashes match the manifest. Printed envelopes match the source CAD extents after the documented rotations within 0.01 mm.

| Part | Triangles | Print envelope (mm) | Mesh/CAD volume difference |
|---|---:|---|---:|
| Chassis | 9,176 | 90 × 82 × 52 | 0.00530% |
| Horizontal stop | 852 | 22.2 × 14 × 8.65 | 0.00374% |
| Cover | 5,856 | 82 × 82 × 16.85 | 0.00049% |

Run `python validation/check_stl.py` to reproduce the mesh checks using Python's standard library. No geometry repairs were applied. Mesh checks do not test self-intersections, support requirements or physical fit.

## Previously recorded v0.7 design checks — 2026-09-30

The following design/interference checks were recorded during the v0.7 cleanup. They were not rerun as part of this export; the export checks above cover the three current print solids and their meshes.

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

No slicing, print trial, structural analysis, electrical test or physical assembly was performed. Compact power-pigtail, lead bend radii, protection hardware and real battery wrapping/tab fit remain unverified. Historical STL reports do not validate this revision; current mesh checks validate only the exported meshes.
