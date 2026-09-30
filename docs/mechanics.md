# Mechanical design — v0.7

Saved in the live Mechanical Switch Fusion document on 2026-09-30. Repository geometry remains v0.4. Coordinates are assembly millimetres; Z is normal to the switch plate. **Front** means the +Y wall opposite the battery, confirmed against the user's open-enclosure view.

## Layout and clearances

| Feature | Current geometry |
|---|---|
| Overall enclosure | X=-41..49, Y=-41..41, Z=1..55.8; 90 × 82 × 54.8 mm |
| Main walls / floor | 3 / 3.2 mm nominal |
| Servo case | X=3..38, Y=-7.55..37.65, Z=9.65..34.35 |
| Servo front clearance | 0.35 mm to inner wall Y=38 |
| Servo bed | Top Z=9.35; case-bottom clearance 0.30 mm |
| Remaining right support | Underside Z=34.6; case-top clearance 0.25 mm |
| PCB board | X=-32.5..32.5, Y≈-10.211..19.811, Z=37.2..38.8 |
| Highest PCB component | Approximately Z=46.1; 6.9 mm to lid underside |
| Remaining right lid pad | Bottom Z=38.95; 0.15 mm above board top |
| Print 02 stop | X=-6..2.65, Y=21.8..35.8, Z=12..34.2 |
| Stop screws | X=-3, Y=24.8 and 32.8; Ø2.6 through-holes in stop / Ø2.6 blind chassis pilots |
| Stop-to-case gap | 0.35 mm at X=3 case face |
| Actuator | Not present in current live design; to be designed manually |
| Servo shaft axis | Parallel to X through Y=4.8, Z=22 |
| Through-floor actuator window | X=-24..3, Y=-8..17.6, Z=1..4.2; 27 × 25.6 mm, four R3 mm corners |
| Cable pocket cavity | X=38.35..46, Y=1..21, Z=13..44 |
| Clear upper cable passage | Y=1..21, Z=34.6..44; obstructing tab and thin divider removed |
| Nominal battery | X=-29..29, Y=-32.7..-12.7, Z=6.7..38.7 |
| Maximum battery envelope | X=-31.5..31.5, Y=-33.7..-11.7, Z=6.7..40.7 |
| Battery pocket | 64 mm wide; forward clearance face Y=-11.2; upper relief Z=41 |
| Battery floor | Flat at Z=4.2; both ribs/tunnels removed and both floor slots sealed |

## Changes from v0.6

Removed both battery ribs at X=±18 and their internal tunnels. Sealed both rectangular floor slots with continuous 3.2 mm floor thickness. The nominal battery reference remains at Z=6.7, leaving 2.5 mm to the new flat floor; pad thickness and retention must be chosen for the actual pack. The previous strap-threading method no longer applies.

Reduced both Print 02 holes from Ø3.3 to Ø2.6 mm, matching the existing chassis pilots. The centers, 3.2 mm stop flange, and blind chassis pilot depth are unchanged. These are undersized plain holes for M3 thread forming, not modeled helical threads.

Removed the shallow PCB footprint impressions, flattened support tops to Z=37.19 (about 0.01 mm below the PCB), and replaced the localized left capacitor notch with a straight support edge at X=-25.8. The entire edge was inset 1 mm to preserve underside-component clearance without a small isolated indentation. The right locating pin remains connected.

Flattened the 0.1 mm stepped surround of the large wire passage, aligned the remaining right support underside to Z=34.6, filled the obsolete upper-right support recess, and closed the two old narrow left-wall slots. The large cable cavity, ventilation bores, mounting pilots, cover screw counterbores and functional servo clearances remain.

Rounded all four corners of the through-floor actuator opening to R3 mm through the full floor thickness. Both faces of this same opening now have a rounded-rectangle outline. No actuator was created or modified; none was present when this revision was inspected.

The prior +4.8 mm layout shift and 90 × 82 × 54.8 mm enclosure envelope are retained. The fixed rocker/chassis interference remains unresolved; see [validation](validation.md).
