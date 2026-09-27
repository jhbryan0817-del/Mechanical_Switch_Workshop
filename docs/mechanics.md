# Mechanical design — v0.2

## Switch reference

The supplied photograph shows a short, rounded-square rocker, with two circular fixing caps on the faceplate. It does not show a long paddle switch. Scaling the button's roughly 66 px width against the plate's roughly 334 px width gives about 17 mm on an 86 mm plate. This is a **photo estimate**, not a manufacturer-controlled dimension or a confirmed SKU. The reference solid is 17 × 17 mm with rounded corners and a nominal 6 mm projection. No source established the actual press travel or force.

The device presses the existing rocker externally. It does not grip the button, remove the faceplate or use its fixing screws. The 6 mm-wide TPU contact regions sit within the small button. Three insert depths accommodate different projection: standard contact plane 6.8 mm, long 4.8 mm, short 8.8 mm above the faceplate reference. Select for clearance in both latched switch states; alter `PAD_CONTACT_Z` for intermediate fit.

## Direct actuation

Coordinates: X horizontal, Y up, Z out from the plastic faceplate. Servo shaft axis is X at Y=0, Z=16 mm. The servo turns in the same plane in which the rocker tilts. Its horn directly carries the rigid paddle; only the TPU insert lies between paddle and rocker.

The two flexible contact ends belong to one insert, with a shared central M3 attachment. Positive rotation brings the negative-Y end toward the faceplate and lifts the other; negative rotation reverses that motion. Return to neutral after latching. No cam, guide, follower, separate return spring or sliding contact stem remains.

For a contact centre initially at Y=−7.5 mm, Z=6.8 mm:

`Z(theta) = 16 − 7.5 sin(theta) − 9.2 cos(theta)`

At 20°, its nominal approach is about 2.01 mm; at 30°, 2.52 mm. After a nominal 0.8 mm neutral gap this leaves about 1.21 / 1.72 mm for switch movement plus insert deflection. The contact also slides toward the rocker centre. This is a geometric travel budget, **not demonstrated latching**. A taller or stiffer rocker may need a different insert or geometry.

The 1.6 mm TPU leaves flex under excess displacement. TPU grade, print direction and temperature determine actual stiffness. They are not a calibrated force limiter. Use low speed, calibrated angular limits and the servo/controller's applicable torque/current protections. No printed stop is intended to absorb full servo stall torque.

## Mounting and adjustment

The base is 86 × 86 mm. Its rear plane is 1 mm from the nominal faceplate front to allow foam adhesive. Tape: two 70 × 9 mm strips plus four 4 × 15 mm strips = **1,500 mm²**. All lands lie on faceplate plastic; curvature can reduce actual contact area. Side screw caps have clearance.

Two 3.4 mm-wide slots in the carriage provide ±26 mm positioning on fixed M3 screws at Y=±39 mm. The screws thread into blind 2.7 mm pilots in the base. The fixed rails clear the moving chassis and cover throughout the sampled travel. Alignment is an assembly setting: remove the cover and controller shelf; the servo clamp may also need removal for tool access at some positions. Support the carriage while loose.

The enclosure moves with the servo and controller. Cover dimensions are 89 × 92 × 50.7 mm; its front is Z=53 mm. Including the base, the centred footprint is 99 × 92 mm. At X=+26 mm it is 125 × 92 mm. It is smaller than v0.1's approximately 146 × 98 mm footprint and 91 mm projection, but the retained servo and 65 mm controller prevent a button-sized housing.

## Hardware interfaces

The STS3215 reference body is 45.2 × 24.7 × 35 mm. Shaft offset 12.35 mm and the simplified 18 mm horn diameter are assumptions inherited from the hardware envelope, not a measured servo. Foam-lined body clamping avoids invented mounting-ear holes. The printed horn adapter has two radial 3.4 mm slots for a 12–16 mm opposed-hole bolt circle and centre-screw access. Use the supplied metal spline/horn and correct metal-thread screws.

The PCB shelf uses the published 65 × 30 mm outline and 58 × 23 mm hole pattern. Its 2.4 mm locating pins fit 2.75 mm PCB holes; ties retain the board. Do not force M3 screws through PCB holes. Side service openings and an internal cable passage are provided. The 10.1 mm component envelope is provisional; real plugs, mounting ears and cable bend radii require fit checking.

## Editing

The Fusion file contains named direct solids, not a constrained jointed assembly. `build_fusion.py` is the dimensioned, repeatable source. In an empty design named `Mechanical Switch`, run it using Fusion Python/MCP; it refuses to overwrite an existing design by default. Run `verify_export.py` after the build transaction commits. Keep `REPLACE_EXISTING=False` for normal use. Existing output directories must contain only this version's files; the builder does not erase old meshes.
