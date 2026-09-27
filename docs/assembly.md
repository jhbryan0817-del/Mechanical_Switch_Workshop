# Print, fit and assemble

Use the numbered STL filenames with the BOM. STLs are in millimetres and are individually translated to their minimum XYZ corner. They retain the assembly axis orientation; **choose print orientation in the slicer**. Never import as inches.

## 1. Measure and print the fit set

Record the measurements in `validation.md`. Print the pilot coupon, bezel and bridge first. The bezel must fit without forcing or opening the switch. Place paper templates matching the six tape strips on the plate; verify full flat contact and clear screw caps. Trial the carriage at both X extremes and all needed rocker locations.

Suggested PETG starting settings: 0.20 mm layers, 0.4 mm nozzle, four walls, five top/bottom layers, 35–45% infill, locally solid fastener bosses. Use 0.16 mm layers and five walls for cam/follower parts. These are untested starting settings; inspect the slicer for bridges and unsupported geometry.

| Parts | Suggested bed face / support notes |
|---|---|
| Bezel | Flat adhesive back down; raised rails need support in the nut-access gaps. Keep tape lands smooth. |
| Bridge | Broad flat face down; no support expected. |
| Lower guide and pillars | Broad lower plate down; tall pillars upward. |
| Follower guide, sleeves | Flat ends down; no support expected. |
| Contact stems | Flange on bed, shaft upward (flip STL); keep bores vertical. |
| Retaining clips | Flat on bed, solid; print spares and inspect for splitting. |
| Spring cups | Closed roof on bed, cavity up (flip STL); the narrow external follower pin needs support underneath the roof. Remove support fully and polish the follower. |
| Servo cradle | Broad base on bed; downward stop pins require support or a carefully chosen alternate orientation. |
| Servo cap | Broad flat face down. |
| Face cam | Flat back on bed, lobes upward (flip STL); smooth ramps without changing profile. |
| Sidecar | Broad back down; support the raised attachment arms. |
| TPU shoes | Flat contact face down, recess upward; avoid support in head recess. |

Do not leave support scars on tape lands or moving surfaces. Deburr every slot. Hand-fit guides so stems and cups move freely under light finger pressure. Reject cracked bosses, warped tape lands or clips that do not retain the stems. Do not lubricate adhesive surfaces.

## 2. Assemble the adjusters off the switch

1. Put two M3 nuts and washers under the raised bezel rails. Fit the bridge using two M3 × 12 screws and head washers. Leave loose enough to slide.
2. Fit the lower guide/pillar body to the bridge with four M3 × 12 screws, washers and nuts through the Y slots. Access the nuts from behind while off the faceplate.
3. Test all adjustment positions, then tighten gently. Screw heads and washers must bridge the slots. Check screw lengths do not bottom or approach the tape plane.
4. Fit the right sidecar with two M3 × 12 screws into its blind bezel pilots. The sidecar can be left off during mechanical testing.

## 3. Assemble compliant plungers

1. Place each light return spring over a stem, under its flange. Insert the stem down through the lower guide, leaving the spring between flange and guide top.
2. Snap the retaining clip into the stem groove below the guide. Check it engages completely. It must limit upward escape without binding against the plate.
3. Fit an M3 contact screw from the wall-facing end. Start with a short projection and at least 8 mm thread engagement. Add the TPU shoe after depth adjustment; use a small compatible adhesive if its head recess does not grip securely.
4. Place the primary spring above each stem flange, then lower the follower cup over it. The primary spring sits between stem flange and cup roof.
5. Slide four short sleeves over the pillars. Lower the follower guide over the cups and pillar slots. Add the four long retaining sleeves.
6. Check free motion, spring seating and return by hand. The cup must move 4 mm while the stem can pause against a test block and compress the primary spring. Neither spring may go solid. The clip must remain engaged.

Do not mistake the two spring types. With no cam contact, the primary spring can push the cup out; retain the parts by hand until the cam/cradle is installed. Keep small parts contained on the bench.

## 4. Fit the servo, horn and cam

1. Compare your servo to the reference envelope. Check shaft offset, output disc bolt pattern, connector location and cap clearance. Revise parts if these differ.
2. Set the servo to a known neutral position **with the horn/cam detached**, following the controller documentation. Disconnect servo power before mechanical assembly.
3. Install the supplied metal horn and its manufacturer-specified centre screw. Fit the printed cam with correctly sized screws. The cam tab points along +X at neutral; followers lie on the unraised track.
4. Feed the cam/servo assembly through the cradle, aligning the stop tab between the two stop pins. Inspect the horn-to-cradle opening and the full cam sweep.
5. Lower the cradle onto the pillar stack. Fit four M3 × 14 screws and washers. The long sleeves capture the follower guide; add thin noncompressible shims if your print leaves play.
6. Fit foam shims around the servo body, then the retaining cap with four M3 × 14 screws and washers. Tighten only until secure; do not crush the servo case.
7. With power disconnected, check neutral and limited manual movement. Do not force the geared servo. Check cam rotation before coupling it to the horn where possible.

The mechanism is open in v0.1. Keep fingers, hair and cables clear during supervised bench tests. A protective cover is a future design task.

## 5. Controller and wiring

Seat the board on its locating pegs. The pegs are not screws. Retain it with light ties over protected, component-free edges; do not press on the display or antenna. Route the bus cable in a loose service loop, allowing full X/Y adjustment. Secure the external power lead to the tray so a tug does not pull on the board connector or bezel.

Follow `wiring.md`. Keep all wiring external to the faceplate. Bench-test with an unpowered training switch before mounting on an installed accessory.

## 6. Attach and calibrate

1. Verify the actual plate's surface is compatible with the selected tape. Follow the tape manufacturer's cleaning, application pressure, temperature and dwell guidance. Do not assume all plastics tolerate the same cleaner.
2. Apply the six strips to the defined plastic-contact lands. Do not bridge curved edges, screw caps, seams or gaps. The reference assumes 1 mm tape; adjust the neutral tip position for actual thickness.
3. Position the bezel without loading the rocker. Let the adhesive reach its specified bond strength before fitting or operating the heavy cassette. Support the assembly during fitting.
4. Align the cassette to rocker centre, tighten X/Y locks and set both tips clear of the rocker by 0.5–1.0 mm at neutral. The reference faceplate has no modeled rocker protrusion, so this gap must be measured on the actual switch.
5. Manually characterize switch travel and force. Start powered calibration at small travel (about ±10–15°), low speed and a conservative current limit. Increase only until reliable latching occurs; return to neutral after each brief press.
6. If travel or force is insufficient, stop and revise spring/geometry selection. Do not solve a mechanical mismatch by driving harder into a stop.

## Removal and maintenance

Disconnect power and support the device before releasing the cassette screws. The four Y fasteners remove the cassette; this is a service operation, not an instant manual bypass. Do not depend on it for emergency switching. Remove the tape using its manufacturer's method, supporting the faceplate and avoiding force on its fixing system. Recheck clips, cup wear, screw threads and tape edges before each workshop.
