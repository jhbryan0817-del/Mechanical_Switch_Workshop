# Print and assemble

STL units are millimetres. Each mesh is translated to its own origin but retains assembly axes; choose the print orientation in the slicer. Print the pilot coupon before the full set. PETG starting settings: 0.2 mm layers, four walls, five solid top/bottom layers, 35–45% infill and solid fastener bosses. These settings have not been physically qualified.

| Part | Printing notes |
|---|---|
| Base | Adhesive side down; keep lands flat and smooth |
| Chassis | Floor down; inspect supports beneath elevated slot bars and pillars |
| Servo clamp / controller shelf | Broad underside down; keep PCB pins accurate |
| Horn paddle | Horn-facing side down; support the cantilever shelf as needed |
| TPU insert | Centre mounting face toward bed, contact ends up; inspect flexible leaves and remove support without tearing them |
| Cover | Closed front face down; hollow interior up; inspect roof vent bridging |

1. **Fit the base.** Compare the printed base to the square plastic plate. Check tape lands and fixing-cap clearance. Keep adhesive off the switch and wall. Dry-fit the mechanism before applying tape.
2. **Prepare threads.** Select the M3 pilot using the coupon, then form the main printed threads gently. Clear swarf. Check screw length against blind depth.
3. **Fit servo and direct paddle.** Set servo neutral while detached from the mechanism, then remove power. Fit its supplied metal horn. Attach the yellow paddle through its two radial slots; use screws that match the metal horn. Fit one TPU insert using the M3 × 6 screw. Leave clearance between the insert leaves and rigid paddle.
4. **Install servo in chassis.** Route its cable away from the moving insert. Shim the body lightly and fit the cap with two low-profile M3 × 10 screws (heads no higher than 2 mm). Check the actual mounting ears and connectors clear the pocket. No reference solid includes their exact shape.
5. **Set horizontal position.** Put two M3 × 10 screws and washers through the horizontal slots into the base pilots. Align the insert centre with the rocker. Travel is ±26 mm. The setting is static, not motorized. Remove the cap temporarily if it blocks screwdriver access at the selected position. Tighten without stripping; support the loose carriage.
6. **Check contact depth.** Select standard, long or short TPU insert so both ends clear the rocker in both latched states by approximately 0.5–1 mm at neutral. Never force the geared servo by hand. Inspect the uncoupled paddle's limited rotation first. If all three inserts miss the fit, adjust `PAD_CONTACT_Z` and regenerate part 05.
7. **Install controller.** Seat the board on its four locating pins. Retain with light ties through shelf slots across protected, component-free edges. Pass the bus cable through the shelf opening. Check actual connector and cable heights with the cover, not just the PCB outline.
8. **Fit cover.** Four low-profile M3 × 25 screws (heads no higher than 2 mm) pass through recessed cover holes and shelf into the chassis. They secure the cover and shelf together. For uncovered checks, four temporary M3 × 10 screws can hold the shelf instead. Keep cables out of the seam and moving paddle; add strain relief to the shelf's available tie slots.
9. **Bond the base.** Apply the six tape strips to flat plastic regions using the tape manufacturer's preparation and dwell instructions. Support the assembly during bonding. Do not bridge curved edges or fixing caps.
10. **Calibrate on an isolated switch.** Start with small movements and low force/current settings. Increase only enough to latch, then return to neutral. ±30° is the checked CAD sweep boundary, not a ready-to-run command. Validate the compliant insert with a force gauge before relying on it to protect the switch.

The cover is removable; the device is not sealed. To regain manual switch access, disconnect power, support the assembly, remove the cover/shelf as needed and remove the two carriage screws. The adhesive base remains on the plastic plate.
