# Current v0.7 print export — 2026-10-02

- Export the active Mechanical Switch document's three single-solid PRINT components, including unsaved changes on top of Fusion cloud version 9.
- Publish millimetre binary STLs at High mesh refinement for the chassis, horizontal servo stop and cover.
- Orient each mesh for printing, center it in XY and set minimum Z=0 using rigid transforms only.
- Verify closed edges, consistent winding/normals, one connected shell, nondegenerate triangles, positive volume, dimensions and checksums. All three pass; mesh/CAD volume differences are below 0.006%.
- Archive incompatible v0.4 meshes, actuator placeholder and validation reports under historical folders.
- Update printing, assembly, BOM, provenance and validation documentation. Preserve known fit limitations and label prior interference checks by date.
- Leave Fusion geometry unsaved and unchanged; retain historical CAD/STEP and screenshots.

# v0.7 — 2026-09-30

- Save cleanup in the live Mechanical Switch Fusion document; update Markdown documentation only.
- Remove both battery ribs/tunnels and seal both floor slots flush with the 3.2 mm floor.
- Reduce Print 02's two Ø3.3 mm holes to Ø2.6 mm, matching the M3 self-threading chassis pilots.
- Flatten PCB support impressions, replace the small capacitor notch with a straight inset edge, clean the cable-opening surround, align the right support underside, and close obsolete recesses/left-wall slots.
- Preserve the large servo-wire passage, vents and functional mounting clearances.
- Round all four through-floor actuator-window corners to R3 mm. Leave actuator design to the user; none is present in the live document.
- Verify three single-solid PRINT components, chassis/component clearances, maximum battery clearance, sealed floor, hole diameters and window radii.
- Record the remaining rocker/chassis overlap at 254.83 mm³ and the need to revise battery retention after removing the tunnels.
- Leave all 3D files, repository images, scripts and JSON reports unchanged.

# v0.6 — 2026-09-30

- Save the revised layout in the live Mechanical Switch Fusion document; update documentation only.
- Remove the upper-right PCB tab and matching cover pad; open the cable groove uniformly.
- Align the remaining lower-right PCB support and join its flange continuously.
- Remove 4.8 mm of front filler and move servo/horn, stop, PCB, actuator, supporting geometry and battery forward by 4.8 mm (+Y).
- Move the actuator clearance window and cover capture pads with the relocated components.
- Flatten the battery-side wall and matching cover edge; enclosure envelope becomes 90 × 82 × 54.8 mm.
- Verify single-solid print parts, assembly intersections, maximum battery clearance, assumed lead volumes and seven actuator-angle samples.
- Record remaining fixed-rocker/chassis overlap (251.30 mm³) and the need to recheck actuator contact alignment and physical PCB retention.
- Leave all CAD, STEP, STL, images, export scripts and JSON reports unchanged at v0.4. No revised 3D files exported or uploaded.
# v0.5 — 2026-09-30

- Save the battery revision in the live Mechanical Switch Fusion document; update repository documentation only.
- Close three large external service apertures and add 36 Ø2.4 mm aesthetic vents.
- Lower PCB mounting by 3.2 mm, rebuild right capture rails and extend lid pads.
- Replace Print 02 with a small two-screw L-shaped horizontal servo stop.
- Join the servo-enclosure rear gap to the outer wall and add the approved closed cable pocket opposite the horn.
- Add an internal Gens ace 850 mAh 2S battery reference, tolerance-aware bay and soft-strap tunnels.
- Overall envelope becomes 90 × 83 × 54.8 mm; servo, horn and actuator coordinates are preserved.
- Check solid lumps, assembly intersections, maximum battery envelope and sampled actuator clearance.
- Mark all existing repository geometry, images and JSON reports as historical v0.4. No new geometry exports.
- Document unresolved connector/protection fit, voltage-variant confirmation and physical validation.

# v0.4 — 2026-09-28

- Synchronize repository to current manually edited Fusion assembly: four parts, 82 mm footprint.
- Add branded closed cover, integrated wall-connected screw blocks, solid left PCB platform with two M3 pilots and solid right PCB capture pads.
- Close display and button openings; retain wiring/ventilation openings.
- Preserve user actuator placeholder and shifted rear window, previously reduced 20% in height.
- Export high-resolution, print-oriented STLs at Z=0 plus current F3D and STEP.
- Document assembly, print settings, mesh checks and unresolved reference-rocker/PCB-hole fit.
- Archive superseded v0.3 files separately.

# v0.3 — 2026-09-27

- Simplified 25 loose bodies into nine named components containing twelve solids; removed tape, screw, alternate insert, coupon and keepout models.
- Replaced the thin paddle/TPU leaf assembly with one integral PETG rocking shoe: 6.2 mm horn web with 11.7 mm bolt bosses, 5 mm bridge, two broad contact lands; stock metal horn retained.
- Kept six printed assembly pieces and hid the cover by default for inspection.
- Updated source, exports, print meshes, views and geometric reports. Documented limited travel, torque overload risk, material rationale and outstanding physical tests.

# Change record

## v0.2 — 2026-09-27

- Replaced the two-lobe face cam and two separate spring plungers with a sideways servo, direct horn paddle and one compliant TPU leaf insert.
- Added the short rounded-square rocker reference from the supplied photograph, with explicit dimensional assumptions and alternative insert depths.
- Added a rounded removable enclosure and internal controller shelf; removed the open sidecar.
- Reduced nominal front projection from approximately 91 mm to 53 mm; seven printed parts now enter the assembly instead of 24.
- Changed horizontal adjustment to 52 mm total and retained faceplate-only adhesive mounting.
- Used M3 screws in undersized printed pilots for base locks, servo retention and enclosure attachment; removed adjustment nuts.
- Replaced current CAD, STL, images and validation reports. Previous files remain recoverable in Git history.
- Removed the workshop plan, promotional cover and lesson material. Documentation now describes the actual design, assembly and outstanding physical checks.

## v0.1

Superseded cam/plunger concept. See commit `d75feed` for its files and original documentation.
