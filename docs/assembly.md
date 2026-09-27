# Print and assemble — v0.3

Print only the six current STL files, in millimetres. STL files are translated to their own origins but retain assembly axes; orient in the slicer.

1. Measure the actual rocker width, height and neutral clearance in both states, press force and travel. Check servo shaft location, metal horn bolt circle, mounting ears, board connectors and available wiring space against the references.
2. Print the PETG shoe with its horn-facing YZ face toward the bed (rotate 90° from exported axes). Use at least six walls and solid sections around the web and bridge. Support overhangs as needed; inspect slot bridges, layer fusion and dimensional fit. Other parts can start at four walls and 35–45% infill, with solid screw bosses; settings remain unqualified.
3. Dry-fit frame, carriage, servo shims and clamp. Hand-form the 2.7 mm printed pilots gently and check screw tips do not bottom. Screw and tape solids have been removed only for visual clarity.
4. Establish servo neutral while detached; disconnect power. Fit the stock metal horn and screw the integral shoe directly to it through the two slots. Select screws for a 11.7 mm printed boss plus any washer and actual horn thread depth. Check head/tool access and do not crush the print. No separate TPU insert or centre contact screw is used.
5. Align the carriage to the rocker using the ±26 mm slots. If desired, add 0.5 mm soft facing to the two lands. Check clearance in both latched states and move the uncoupled shoe through the intended limited sweep. Do not force the geared servo by hand. Adjust contact depth in CAD if needed and rerun checks.
6. Mount the controller on the shelf pins and secure with ties across component-free edges. Route and restrain cables away from the shoe. Fit the cover and inspect real connector clearances; the PCB alone is an incomplete hardware envelope.
7. Bond the mounting frame to suitable plastic faceplate regions with the specified tape, following its manufacturer's surface preparation and dwell. Check curvature, fixing-cap clearance and peel resistance. No backbox or mains connection is part of this assembly.
8. On an isolated switch, measure contact force while increasing a low-speed, torque-limited stroke only enough to latch, then return to neutral. Do not use ±30° as a preset command. Stop if reliable actuation requires excessive force or the contact slides too near the rocker pivot.
9. Proof-test the printed shoe and mounting under a controlled load above the measured operating load, then cycle both directions. Record force, missed latches, temperature, cracks, screw loosening and mounting movement. Choose a justified service load and cycle target before unattended use; no such test has yet been completed.

In Fusion the cover is hidden for inspection. Enable component 06 to see it; hide component 05 and the driver temporarily for unobstructed mechanism inspection. The reference board includes both faceplate and rocker.
