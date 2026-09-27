# Validation record and release gates

**Release: v0.1 mechanical bench prototype, 2026-09-27. No physical build or powered test has been performed.**

## Completed checks

- The live Fusion document was inspected before editing; it contained no bodies.
- The delivered model contains individually named printed bodies and explicitly labeled reference envelopes.
- All 25 STL files have closed mesh edges (each undirected edge belongs to two triangles), positive signed volume and valid binary STL lengths. See `stl_checks.json`.
- Fusion neutral-position intersection checks found no positive-volume overlap between printed solids, excluding the detached coupon. See `fusion_checks.json`.
- Nine combinations of X = −28.5/0/+28.5 mm and Y = −12/0/+12 mm are checked in `xy_sample_checks.json`. These are discrete neutral-cam samples, not a continuous motion simulation.
- Native Fusion archive export succeeded and was reimported into a fresh Fusion document: all 34 bodies were solid. See `archive_reimport.json`. STEP export returned false; no usable STEP deliverable is claimed.

These checks do not establish print tolerances, strength, adhesive life, electrical suitability, spring performance, exact cam contact under rotation, or compatibility with actual hardware. STL closed-edge checks are not a full self-intersection analysis. Reference hardware is simplified and was excluded from the printed-part interference checks.

## Before printing the complete set

| Measurement | Actual value | Gate |
|---|---|---|
| Faceplate width / height | ____ / ____ mm | Fits bezel and tape map |
| Flat plastic bonding regions | ____ | All six strips seat fully |
| Screw cap diameter / projection | ____ / ____ mm | Clears reliefs |
| Faceplate projection | ____ mm | Record for depth setup |
| Rocker centre X / Y | ____ / ____ mm | Within X/Y range |
| Rocker width / height | ____ / ____ mm | 22 mm contacts land on useful areas |
| Rocker protrusion / press travel | ____ / ____ mm | Neutral gap and stroke available |
| Measured actuation force | ____ N | Spring stack can latch without coil bind |
| Servo axis offset | ____ mm | Matches cradle assumption |
| Horn bolt circle / hole pattern | ____ | Matches cam; revise if different |
| Horn stack / screw engagement | ____ mm | No bottoming or cradle rubbing |
| Servo and board connector clearance | ____ | Cable accessible with service loop |
| Primary spring rate / solid height | ____ / ____ | Required force and ≥0.5 mm bind margin |
| Return spring rate / solid height | ____ / ____ | Reliable return and bind margin |
| Coupon-selected M3 pilot | ____ mm | No splitting or stripping |

## Staged physical acceptance

1. **Fit gauge:** bezel and bridge fit every intended switch; all six lands contact flat plastic. Verify the extreme-X shoe does not scrape the bezel. No tape or powered servo yet.
2. **Free mechanism:** all guides move freely; clips remain seated; sleeves capture the guide; screws have adequate engagement. Check manual cam movement before servo coupling.
3. **Compliance:** block each stem and move its cup through the intended displacement. Measure force versus displacement and verify both spring solid heights remain clear. Never use a powered servo for this check.
4. **Manual switch test:** on an unpowered training switch, confirm upper/lower latching and complete neutral release. Set 0.5–1.0 mm tip clearance.
5. **Adhesive coupon:** test the chosen tape on representative plastic, using its specified preparation and dwell. Inspect peel and creep with an equivalent mass and offset. Nominal bonded area alone does not establish a safe load.
6. **Mounted static hold:** support the device during initial placement, mark the bezel position, and monitor over a workshop-length interval and then at least 24 hours. Stop on edge lift or drift; no powered cycling until this passes.
7. **Powered bench test:** current-limited supply, conservative travel and speed, 20 alternating cycles. Record peak current, force, temperature trend, clip retention and mount movement. Stop immediately on rubbing, missed return, heating or adhesive movement.
8. **Repeatability:** extend to 100 cycles only after the first 20 pass. Recheck after an overnight rest. Record failures, not just successful cycles.

## Deliberate limitations / next iteration

- Only 22 mm contact spacing is modeled; 18 and 26 mm require new matched guides/cups/track geometry, not simply moving holes.
- The assembly is roughly 91 mm proud of the nominal faceplate, rather than the compact proposal target.
- Actual servo axis, disc mounting, springs and rocker dimensions remain unverified.
- The open sidecar uses dimensions, not an imported official board STEP model. No sealed enclosure, connector-specific cover or OLED window is supplied.
- No full protective cam cover, instant manual bypass, implemented firmware, continuous motion simulation or structural analysis is supplied.
- Printed stops and clips are prototype parts, not rated protective devices.
- Tape may damage plastic during removal, and long-term creep/peel performance is unknown.

## Re-run checks

Run `python validation/check_stl.py` from any folder; it resolves the repository location. This uses Python's standard library only. In Fusion, run `cad/check_xy.py` and `cad/verify_export.py` against the built model after setting their output directory. Do not run the builder over an existing design; it intentionally refuses to overwrite one.

