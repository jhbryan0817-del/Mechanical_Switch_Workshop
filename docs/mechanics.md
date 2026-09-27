# Mechanical design · v0.1

## Coordinate system and references

All dimensions are millimetres. The wall is Z=0; positive Z points into the room. X=0 and Y=0 are the faceplate centre. Positive Y points toward the top of the modeled plate. A nominal 87 × 87 × 10 mm faceplate is a simplified reference only. For the proposal's left-edge coordinates, add 43.5 mm to X. Thus the shaft moves from X=15 to 72 mm on an 87 mm plate (14.5 to 71.5 mm on an 86 mm plate).

The supplied Fusion document was empty. The screenshot supplied with the request showed MCP settings, not measured switch geometry. No dimensions have been inferred from that screenshot.

## Tape bezel

The frame is 98 × 98 mm. Its rear bonding plane is Z=11, nominally 1 mm in front of the reference faceplate. The central aperture is 69 × 63 mm, with side screw-cap reliefs at mid-height. The bezel overhangs the faceplate; **only the six defined lands contact the plastic**. It does not depend on the wall surface for attachment.

Tape cuts:

| Quantity | Size | Centre X | Centre Y |
|---:|---|---|---|
| 2 | 70 × 10 mm | 0 | ±37.5 |
| 4 | 8 × 14 mm | ±38.5 | ±23 |

Total nominal area = 2×70×10 + 4×8×14 = **1,848 mm²**. This is a geometric area, not a holding-force rating. At the extreme X position, the 10 mm contact shoe has 1 mm nominal clearance to the aperture edge in projection. Verify the clearance on the actual print and switch.

There is no recessed tape pocket: the broad back surface is easy to clean and re-tape. Reference tape bodies show where to apply strips. Check that every strip lies on flat plastic, away from screw caps and curved edges. If it does not, revise the base or tape map before loading it. A very strong adhesive may mark or damage the faceplate during removal.

Raised slotted rails leave access below for standard M3 nuts. Fasteners never pass through the adhesive plane. Sidecar blind pilots have 8.5 mm available depth; verify the selected screw does not bottom.

## Adjustment and load path

Two horizontal rail slots provide ±28.5 mm carriage travel. Four vertical slots provide ±12 mm cassette travel. The axes use bolts, washers and nuts rather than a printed dovetail: this makes the first workshop build easier to inspect and avoids relying on a printer-specific sliding fit.

Normal force travels from rocker → shoe → contact stem → primary spring → follower cup → face cam → supplied metal horn → servo cradle → cassette pillars → bridge → bezel → tape → faceplate.

The spring is **in series** with the contact load. A single rigid follower with only a return spring would not provide this compliance.

## Plungers and springs

Only the **22 mm centre spacing** is implemented. Each 4.8 mm stem runs in a 5.3 mm guide. A 9.6 mm flange slides inside the 10.2 mm follower-cup bore. The cup OD is 13 mm and its guide bore is 13.5 mm. These are starting FDM clearances; print and hand-fit before assembly.

Each stem has a light snap retaining clip below the lower guide. The clip is a positional retainer, not a force-rated safety device. A small M3 screw threads into the bottom pilot and carries a soft TPU shoe. Maintain at least 8 mm screw engagement. Bond the shoe to the screw head after setting depth; allow access for later adjustment.

There are **two different springs per plunger**:

- Primary spring above the stem flange, inside the cup: nominal installed length 7 mm, preliminary free length 8 mm, target rate 0.5 N/mm, OD ≤8 mm, ID ≥5.2 mm, solid height ≤2.5 mm.
- Light return spring below the stem flange: nominal installed length 4 mm, preliminary free length 8 mm, target rate 0.2 N/mm, OD ≤8 mm, ID ≥5.2 mm, solid height ≤1.5 mm for up to 2 mm stem travel.

These are **procurement/measurement targets**, not an identified spring product. Reject a spring that reaches solid height in the intended travel. A longer spring package may be necessary after actual switch-force measurement. The nominal spring combination gives roughly 0.3 N upward return bias at neutral; with the stem blocked and 4 mm cup travel, net contact force is roughly 1.7 N, ignoring friction. Actual force will differ with switch travel and spring preload. Measure it. Do not infer 2–4 N simply from a 4 mm cam lift.

Four lower sleeves position the follower guide; four upper sleeves capture it beneath the servo cradle. Cups can translate 4 mm without their lower ends hitting the lower guide in the nominal model. Check this manually after printing.

## Cam and servo interface

The cam has a 38 mm base disc, 3 mm thick, with two 4 mm lobes centred at rotor angles ±50°. Each lobe has a ±6° dwell and a 22° cosine rise/fall, modeled with 2° loft stations. Followers lie at ±90° on an 11 mm radius. Nominal commands are neutral, +40° and −40°; physical phasing determines which rocker end moves.

The disc includes four 3.4 mm holes on an **assumed 14 mm bolt circle**, a 7 mm centre access hole, and a radial stop tab. Two cradle pins stop the tab at approximately ±46°. These printed stops are sacrificial overtravel backups and cannot withstand full servo stall torque. Verify contact angle by hand; never drive the servo hard into a stop.

The horn bolt circle, screw lengths, horn stack height, shaft offset and connector clearance are **not confirmed for your hardware**. Use the supplied metal 25T horn, never a printed spline. Dry-fit it before printing the final cam/cradle. Screws must engage the horn without bottoming or touching the servo case.

The servo reference uses the published 45.2 × 24.7 × 35 mm envelope. The shaft is assumed 12.35 mm from one end of the long side. The clamp retains the body with foam shims and a removable cap; there are no invented mounting-ear holes. Keep pressure away from connectors and moving output parts.

## Packaging trade-offs

The full layout is approximately **146 × 98 × 101 mm from the wall reference**, including the sidecar and cap. It projects about **91 mm beyond the nominal faceplate front**. This is significantly larger than the proposal's 48–55 mm target: the accessible spring stack, raised bolt rails and open clamp take priority in this first demonstrator. Do not describe this as the compact final enclosure.

The sidecar is open for USB, power, bus cable, display and button access. Its 58 × 23 mm peg pattern follows Waveshare dimensions; 2.5 mm locating pegs fit nominal 2.75 mm PCB holes. Retain the PCB with loose ties over safe board edges and insulating foam, avoiding components and the antenna. The tray can be mirrored for a left-side variant; only the right-side build is delivered. A measured connector envelope and protective cover remain future work.

## CAD editing

The F3D contains individually named **solid bodies in the existing single-part design**, not a jointed assembly or a feature-parameter model. Hide the `REF_` bodies before examining printed parts. The coupon is hidden in the assembled view. The Python builder records the dimensions and construction, including analytic solids and lofted cam surfaces. It is the repeatable design source, but dimension edits may require coordinated changes; the pilot setting and inline dimensions are not a complete parameter system.

To rebuild, set the builder's output directory, create its `cad`, `stl`, `assets` and `validation` subfolders, activate an empty Fusion document named `Mechanical Switch`, and run the script through Fusion's Python script interface or MCP. It refuses a non-empty model. Fusion lengths are converted from mm to cm internally; STL exports are explicitly in mm. Run `verify_export.py` after the build transaction commits. STEP export returned false in this session; the invalid file is intentionally excluded.

