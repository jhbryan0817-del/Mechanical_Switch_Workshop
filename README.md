# Mechanical Switch

A removable, adhesive-mounted servo actuator for the **small rounded rocker** on a square wall-switch faceplate.

![Closed Fusion assembly](assets/fusion-assembly.png)

**v0.2: direct drive, enclosed, horizontally adjustable.** The servo lies sideways. Its metal horn directly rocks one paddle with a replaceable TPU leaf insert. There is no face cam, plunger stack or external controller tray. The controller fits above the servo, inside the cover.

This is a CAD revision awaiting a physical fit and actuation test. The photograph establishes the rocker shape; its exact projection, force and travel are not known. The model does not claim universal switch compatibility.

| Feature | Current design |
|---|---|
| Small-switch reference | Rounded 17 × 17 mm button, estimated from the supplied photograph |
| Horizontal positioning | 52 mm total (±26 mm), approximately the middle 60% of an 86 mm plate |
| Mounting | Six faceplate-only adhesive lands, 1,500 mm² nominal area |
| Fastening | M3 screws form threads in 2.7 mm printed pilots; no nuts or inserts |
| Drive | STS3215 → supplied metal horn → single rocking paddle → TPU leaf insert |
| Housing | 89 × 92 mm cover; 53 mm projection from faceplate front including tape |
| Overall footprint | 99 × 92 mm centered; up to 125 × 92 mm at the rightmost setting |
| Printing | Seven assembled printed pieces; pilot coupon and two alternative-depth inserts also supplied |

[Native Fusion file](cad/Mechanical_Switch_v02.f3d) · [STEP](cad/Mechanical_Switch_v02.step) · [Print files](stl) · [Assembly](docs/assembly.md) · [BOM](docs/bom.md) · [Mechanical details](docs/mechanics.md) · [Validation](docs/validation.md)

![Direct servo-to-rocker mechanism, surrounding structure hidden](assets/fusion-direct-drive.png)

The yellow part is the direct horn paddle. The black contact insert has two flexible ends on **one part**. Rotation presses one side of the short rocker; opposite rotation presses the other. Neutral clears both sides. Two directions of force are needed to operate this type of rocker; two separate moving fingers are not needed.

## Repository

- `cad/`: editable Fusion archive, dimensioned Python builder and geometric verifier.
- `stl/`: current individual print meshes in millimetres. `OPTION_` files replace the standard insert; do not fit all three.
- `docs/`: mechanics, hardware, assembly, control notes and verification limits.
- `assets/`: views captured from the actual Fusion model.
- `validation/`: machine-readable checks and a repeatable STL checker.
- `reference/`: provenance, dimensions and manufacturer links.

The previous v0.1 is available in Git history. Its cam, springs, plungers, sidecar and meshes are superseded. The repository name is retained to preserve its URL; instructional-session material has been removed.


