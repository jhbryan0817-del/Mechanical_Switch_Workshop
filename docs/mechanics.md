# Mechanical audit — v0.3

## Decision

Use one thick printed rocking shoe directly on the stock metal servo horn. Custom CNC metal is not required as a starting design choice. Keep the bought metal spline/horn interface; do not print the spline. PETG is the prototype material. A strength rating cannot be assigned from infill percentage: layer direction, local section, notches, creep, fasteners and actual contact force control this design.

The old shoe fed load through a 3 mm shelf and a small screwed TPU stem with 1.6 mm leaves. This could consume useful stroke in flex and concentrate stress. The new shoe has a 6.2 mm horn web, 5 mm-thick broad bridge and two integral rounded 8 × 4 mm contact lands at Y=±6.5 mm. There is no central contact screw, leaf, linkage or fine printed joint. Two radial M3-clearance slots retain the previous assumed 12–16 mm horn bolt circle. The centre access hole remains 7 mm. Two full-depth 11.7 mm bolt bosses provide front screw-head seating and unobstructed axial tool access; the slotted passages extend through the complete boss.

This is a more robust prototype, **not a qualified automatic actuator**. No FEA or physical fatigue test has been performed. The horn pattern, screw heads, servo mounting ears, connector envelopes and real switch geometry must be verified.

## Load budget and material

The cited 7.4 V STS3215 datasheet gives 19.5 kgf·cm stall torque (about 1.91 N·m), and 5 kgf·cm rated torque (about 0.49 N·m). Neither value is a safe switch actuation setting. At a 6.5 mm effective lever arm, stall torque corresponds to roughly 294 N; effective leverage changes through the stroke and can produce still higher normal force. A metal shoe would transmit that overload into the switch and mounting instead of solving it.

For scale only, assume a 20 N measured press load and a 6 mm cantilever arm on an ideal 8 × 5 mm rectangular ligament: sigma=6FL/(bh²)=3.6 MPa. At 294 N the same idealized stress is about 53 MPa, before notch, hole, layer and fatigue effects. This calculation is **not the shoe's stress analysis or allowable load**, and 20 N is a provisional test target, not a measured switch requirement. The perforated horn web needs physical proof testing as well.

Print the shoe with the horn-facing YZ face on the bed, six or more perimeters and solid local sections. Inspect bonding around the slots and centre bore. Use PETG initially; PLA may be used for fit-only checks but is not selected for warm, sustained service. 100% infill does not eliminate layer weakness or creep. Use broad screw-head load distribution, correct metal-thread engagement and modest tightening. Screw length must account for the new 11.7 mm bolt bosses (previously 3 mm).

Fit optional 0.5 mm silicone/rubber facing to the two contact lands after dry fitting. It is unmodeled consumable material, not a structural leaf or calibrated overload device. Do not rely on default servo overload protection: the datasheet describes delayed protection, which can allow damage first. Calibrate force with a gauge and configure low torque/current, slow motion, timeout and return-to-neutral. No firmware or controller settings were changed in this CAD revision. If reliable latching needs more force than the tested printed assembly can tolerate, redesign and retest rather than simply applying stall torque or replacing the shoe with metal.

## Kinematics and fit limits

X is horizontal, Y vertical, Z outward from the faceplate; shaft axis is X through Y=0, Z=16 mm. The rigid lands start at Z=7.3 mm. With 0.5 mm facing, nominal contact Z=6.8 mm, giving 0.8 mm gap to the assumed 6 mm-high flat rocker.

For the descending contact centre: Z(theta)=16−6.5 sin(theta)−9.2 cos(theta), and Y(theta)=−6.5 cos(theta)+9.2 sin(theta). At 20° approach is about 1.67 mm, leaving 0.87 mm after the nominal gap. At 30° approach is about 2.02 mm, leaving 1.22 mm. Facing compression consumes some of this travel. Bare rigid lands have less travel available after clearance. The contact slides toward the rocker centre (Y≈−1.03 mm at 30°); this reduces leverage on the switch. Avoid approaching the geometric minimum near 35°.

These values do not prove latching. A real pivoting rocker may have different face height in each latched state and require more travel. Measure both states, pivot orientation, press force and latch displacement. Adjust PAD_CONTACT_Z in the builder only after measuring; re-run all geometry checks after changes. Neutral must clear both states. ±30° is a collision-study boundary, not an operating command. If the switch cannot latch inside the available motion with suitable margin, this geometry must be revised before operation.

## Mounting and remaining interfaces

The original 86 mm printed frame, ±26 mm carriage adjustment, clamp, controller shelf and cover are retained. Six physical adhesive lands total 1,500 mm² nominal area with 1 mm tape clearance. Adhesive and screw reference solids were removed at the user's request; actual fasteners and adhesive remain essential. Peel resistance, curved plate contact and mounting creep are untested.

The servo body reference is 45.2 × 24.7 × 35 mm. Shaft offset and simplified stock horn geometry still require physical measurement. The driver is a 65 × 30 mm PCB reference, not a detailed electronics model. Its unmeasured component keepout was removed, so its absence is not evidence of connector clearance. Cover size is 89 × 92 mm, front Z=53 mm.

## CAD organization

Nine named Fusion components contain twelve connected solids. Six are printed parts, the servo component contains body/shaft/horn references, the driver contains one PCB, and the switch reference contains plate and rocker. Components are organized solids, not a constrained joint simulation. The rotor body attribute identifies the horn independently from the fixed servo body for checks.

Run cad/build_fusion.py in an empty Mechanical Switch design, then cad/verify_export.py in a separate Fusion transaction. Replacement is disabled by default. Archive any existing design before explicitly enabling REPLACE_EXISTING. The verifier currently assumes all occurrence transforms are identity; do not move components manually and interpret its native-body results as assembly checks.

Sources: [FEETECH STS3215 datasheet](https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf), [Schneider Hong Kong S-Classic](https://www.se.com/hk/en/product/E31_1_2AR_WE/sclassic-1way-switch-1-gang-white/).
