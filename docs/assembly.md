# Assembly — v0.7 Fusion prototype

Use the three [current STLs](printing.md) exported on 2026-10-02: chassis, horizontal servo stop and cover. Archived v0.4 files do not build this revision. These parts still require physical fit checks; no actuator is included.

1. Verify the purchased servo voltage variant, battery dimensions and connectors. Dry-fit the real switch; the reference-rocker/shielding overlap remains unresolved.
2. With the PCB and new Print 02 stop removed, lower the servo into the open bay and slide it under the remaining lowered right support. Route the lead into the pocket opposite the horn and up through its internal passage. Do not force the case under a rail.
3. Fit the small L-shaped horizontal stop with two M3 screws at X=-3, Y=24.8 and 32.8. Start with approximately 8 mm under-head length; the flange is 3.2 mm thick and pilots extend from Z=11.8 to 5.0. Both stop holes and chassis pilots are Ø2.6 mm for M3 thread forming. Seat the stop against its mounts while tightening; check engagement, screw jacking and bottoming on the actual print.
4. Install the PCB at its lowered, forward-shifted position. Two left screws secure it; the remaining lower-right locating pin and matching cover pads capture the opposite edge; the cable-side tab and its pad have been removed. The board reference has Ø2.75 mm holes: check actual fastener clearance before using M3.
5. Fit an insulating pad on the flat battery floor. The ribs, tunnels and floor slots have been removed, so the old strap-threading route is unavailable. Choose and verify a removable retention method; the unchanged battery reference has 2.5 mm clearance above the floor. Restrain the pack without crushing it.
6. Connect the servo at the board top. The prior 6 mm plug allowance and above-battery lead allowance remain design assumptions; dedicated clearance bodies are absent from the current live model. Keep all cables away from the horn, actuator and cover screws.
7. Connect the fused battery harness and low-voltage protection to the board power input. Verify polarity and connector fit with the cover open. The stock DC jack is close to the left wall; a conventional straight barrel plug is not fit-validated. Select and physically check a compact right-angle pigtail before final printing.
8. Close the cover with four M3 screws. Confirm that extended pads capture the PCB without bending it and that no battery leads are pinched. Open the cover to disconnect/remove the battery for external balance charging.
9. Test low-speed, limited-travel actuation only after resolving physical switch fit and finalizing the actuator and rechecking its contact position after the +4.8 mm relocation.

No cable is intended to pass through an external service hole. The remaining ventilation holes are not charging ports. Screw lengths and assembly access still require a physical trial.
