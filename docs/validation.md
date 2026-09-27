# Validation — v0.3

This revision is a CAD prototype. No physical strength, latching, fatigue, adhesive or powered-cycle test has been performed.

Completed geometric checks are recorded in validation/fusion_checks.json:

- Nine components, twelve single-lump solids.
- No positive-volume neutral overlap above 0.001 mm³.
- No sampled collisions during 27 horizontal positions (−26 to +26 mm in 2 mm steps) against the modeled fixed parts.
- No sampled shoe/horn collision with surrounding modeled structure at 31 angles (−30 to +30° in 2° steps).
- Shoe intersections with the static rocker are recorded as required switch displacement, **not passed clearance or demonstrated latching**.

Checks exclude removed fasteners, tape and unmeasured electronics envelopes. There is no compliance, moving-switch, stress or continuous swept-volume analysis. Component transforms are identity in the verified model. The displayed simplified servo/PCB references omit real ears, leads and connectors.

STL manifold/volume results are in stl_checks.json. Native archive round-trip checks are in archive_reimport.json. Export status is in exports.json. These reports must describe v0.3; earlier revision results cannot qualify this geometry.

Required physical checks: actual switch identification and dimensions, clearance in both latched states, measured force/travel, horn attachment/tool clearance, print layer and screw strength, actual hardware fit, mount peel/creep, conservative torque/current calibration and repeated on/off operation. See mechanics.md for the conditional load estimate and limited travel budget.

All six current STL files passed closed-edge and positive-volume checks. F3D and STEP exports succeeded. Reimporting the F3D confirmed all nine component names and twelve body names/volumes within 0.01 mm³. The original Fusion document save returned success.
