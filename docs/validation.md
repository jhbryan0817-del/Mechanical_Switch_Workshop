# Validation — v0.2

CAD and export checks completed on 2026-09-27. **No physical print, fit, adhesive-load, force or powered-cycle test has been performed.**

## Completed

- Inspected the existing live `Mechanical Switch` model and archived it before replacement.
- Built 25 named, connected solid bodies, including clearly named hardware references and hidden alternative contact inserts.
- Checked neutral intersections between assembled printed bodies and the modeled hardware: **no positive-volume overlap above 0.001 mm³**.
- Checked 27 horizontal offsets, −26 to +26 mm in 2 mm increments, against the fixed base, faceplate, adhesive and modeled X-lock screw/washer envelopes: **no unintended overlaps**.
- Checked 31 paddle angles, −30 to +30° in 2° increments: **no rigid interference**. The TPU insert's intentional intersections with the stationary rocker reference are recorded separately; they represent required switch movement and/or insert flex, not a physical compliance simulation.
- Checked the provisional controller component envelope against printed parts: **no overlap**. The envelope excludes the PCB's mounting holes.
- Exported **10 STL files**: seven assembled pieces, one pilot coupon, two substitute-depth inserts. All have valid binary lengths, closed two-triangle mesh edges and positive signed volume.
- Exported native F3D and STEP successfully. Reimported the F3D into a separate document, confirming 25 solid bodies and matching names/volumes within 0.01 mm³. Closed the verification copy and retained the original document.

Reports: [Fusion checks](../validation/fusion_checks.json), [mesh checks](../validation/stl_checks.json), [archive check](../validation/archive_reimport.json), [exports](../validation/exports.json), [dimension/body manifest](../validation/build_manifest.json).

## What these checks establish

They establish the modeled solids, nominal clearance samples and export integrity. They are not continuous-motion, stress, thread-strength or TPU deformation analyses. The switch is a static rounded reference, not a jointed simulation of its internal latch. Contact force and latching cannot be derived from a successful Boolean test. Hidden alternative inserts are excluded from the assembled interference checks.

The X-lock fastener heads/washer envelopes are included. Other fastener heads, mounting ears, real connectors, component shapes and cable bends are not fully modeled. The controller component height, servo shaft offset and switch depth remain explicit assumptions. The 17 mm rocker outline is photo-scaled, not an exact identified SKU.

## Physical acceptance still required

1. Base lands contact flat plastic and clear the fixing caps; adhesive area alone does not establish holding capacity.
2. Selected M3 pilot forms a durable thread without splitting. Screw tips stay within blind depths; the actual horn matches the slots.
3. Servo body, ears, cable and controller fit with the enclosure installed. Nothing loads a connector or restricts the paddle.
4. In both switch states, neutral clears both contact ends. Determine the smallest reliable stroke and correct insert depth.
5. Measure TPU force/deflection, check available flex before hard contact and inspect permanent set. Do not infer protection from material softness alone.
6. On an isolated switch, perform low-speed, conservatively limited actuation; return to neutral after each latch. Record missed latches, peak load/current and adhesive movement before increasing cycle count.

## Repeat checks

Run `python validation/check_stl.py` outside Fusion. In Fusion run `cad/verify_export.py` after the build transaction. The latter writes reports, captures views and exports only after the interference assertions pass. It targets the document named `Mechanical Switch`, even when another document was active.
