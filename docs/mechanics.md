# Mechanical design — v0.6

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
| Stop screws | X=-3, Y=24.8 and 32.8; Ø3.3 clearance / Ø2.6 blind pilots |
| Stop-to-case gap | 0.35 mm at X=3 case face |
| Actuator placeholder | X=-23..-2.3, Y=-7.2..16.8, Z=6.8..33 |
| Actuator shaft axis | Parallel to X through Y=4.8, Z=22 |
| Rear actuator window | X=-24..3, Y=-8..17.6 |
| Cable pocket cavity | X=38.35..46, Y=1..21, Z=13..44 |
| Clear upper cable passage | Y=1..21, Z=34.6..44; obstructing tab and thin divider removed |
| Nominal battery | X=-29..29, Y=-32.7..-12.7, Z=6.7..38.7 |
| Maximum battery envelope | X=-31.5..31.5, Y=-33.7..-11.7, Z=6.7..40.7 |
| Battery pocket | 64 mm wide; forward clearance face Y=-11.2; upper relief Z=41 |
| Battery support ribs | X=±18, top Z=6.2; internal soft-strap tunnels retained |

## Changes from v0.5

Removed the upper-right PCB locating tab and matching cover pad to eliminate the fragile obstruction across the wire escape. The existing closed outward cable pocket remains. Its upper passage is open uniformly across the 20 mm groove width, without the projecting tab or narrow divider.

Removed the 4.8 mm filled region at Y=33.2..38 ahead of the servo bay. The servo/horn, bed and rear flange, stop and pilots, PCB and platform, remaining right support and cover pads, actuator and rear clearance window all move +4.8 mm in Y. The lower-right support has a continuous connection to its flange instead of the previous 0.2 mm height mismatch. Servo sliding clearances remain 0.30 mm below and 0.25 mm above at the retained rail.

The battery, maximum envelope, lead-storage allowance and support layout move +4.8 mm. The bay keeps at least 0.5 mm side and forward clearance around the maximum envelope; extra space remains behind the pack. The 0.5 mm insulating-pad allowance remains. Chassis and cover end at Y=-41, removing the former battery-side bump, with a 3 mm lower rear wall to Y=-38.

Two left PCB screws, the remaining lower-right locating pin/support, and matching cover capture retain the board. The deleted corner is intentionally unsupported. Verify board flex and support strength in a physical print. The cover screw pattern, branding, vents and fixed switch reference are retained.

The actuator shape is unchanged but its position is not. Recheck contact location and travel against the real fixed switch; the existing rocker/chassis interference remains unresolved. See [validation](validation.md).
