# Mechanical design — v0.5

Saved in the live Mechanical Switch Fusion document; repository geometry remains v0.4. Coordinates below are assembly coordinates in millimetres, with Z normal to the switch plate.

| Feature | Revised geometry |
|---|---|
| Overall enclosure envelope | X=-41..49, Y=-42..41, Z=1..55.8; 90 × 83 × 54.8 mm |
| Main walls / floor | 3 / 3.2 mm nominal |
| Large service apertures | Three closed with solid wall material |
| New aesthetic vents | 36 circular Ø2.4 mm bores; 9 columns × 2 rows on each of two opposite walls |
| Vent centres | X=-24..24 at 6 mm pitch; Z=44 and 48 |
| PCB underside | Z=37.2, lowered 3.2 mm from 40.4 |
| PCB right rail underside | Z=34.6, 0.25 mm above modeled servo top |
| Highest PCB component | Approximately Z=46.1; 6.9 mm to lid underside |
| Right PCB lid pads | Bottom Z=38.95; 0.15 mm above board top |
| Servo case / location | Preserved; X=3..38, Y=-12.35..32.85, Z=9.65..34.35 |
| Servo support clearance | Bed Z=9.35; rail underside Z=34.6; 0.55 mm total vertical play |
| New Print 02 | L-shaped horizontal stop; X=-6..2.65, Y=17..31, Z=12..34.2 |
| Clamp fasteners | Two vertical M3 screws at X=-3, Y=20 and 28; Ø3.3 clearance / Ø2.6 blind pilots |
| Servo horizontal stop gap | 0.35 mm at X=3 case face |
| Cable pocket exterior | X=37.9..49, Y=-2..24, Z=10..47 |
| Cable pocket main cavity | X=38.35..46, Y=1..21, Z=13..44 |
| Battery nominal reference | 58 × 32 × 20 mm, oriented 58 X × 20 Y × 32 Z |
| Battery reference bounds | X=-29..29, Y=-37.5..-17.5, Z=6.7..38.7 |
| Battery bay | X=-32..32, Y=-39..-16; cavity to Z=41 |
| Battery support ribs | Top Z=6.2; two internal strap tunnels at X=±18 |

The right PCB rails mechanically limit upward servo travel; the board is not used as a clamp pressing on the servo. Left platform height and underside-component relief were adjusted, and the cover capture pads were extended down to match.

Print 02 is entirely on the stationary case side at Y=17..31, beyond the horn and sampled actuator sweep. Removing two screws opens the horizontal insertion path. The former broad top clamp and its lower mounting boss are removed. The gap behind the servo enclosure at Y=33.2..38 is filled to join it to the outer wall. Sliding clearances around the actual motor are deliberately retained.

The approved outward cable pocket gives the side opposite the horn an internal escape volume and a passage above the right PCB rail. Its opening to the enclosure is above Z=37.2; the outer wall remains closed. No servo/actuator relocation was needed.

The battery bay includes manufacturer dimensional tolerance: maximum reference 63 X × 22 Y × 34 Z mm, placed at X=±31.5, Y=-38.5..-16.5, Z=6.7..40.7. The 64 × 23 mm pocket leaves 0.5 mm per side. A 0.5 mm insulating pad is allowed over support ribs. Use a soft strap through the internal tunnels; do not clamp the pouch with screws. Pack leads are stored above the battery. Verify the supplied pack, tabs and connector exits before printing.

The actuator, horn, switch reference, rear window and branding remain unchanged. The existing rocker/shielding overlap is still a known limitation.
