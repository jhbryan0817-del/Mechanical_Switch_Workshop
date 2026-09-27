# References and dimensional provenance

The current user request controls this revision: direct servo actuation of the short rocker in the supplied photograph, a compact enclosure, horizontal positioning over approximately the middle 60% of the faceplate, adhesive contact on faceplate plastic, and undersized printed M3 pilots. Attached material and old repository text were treated as reference context, not additional instructions.

The photograph is not redistributed. It shows a rounded-square button rather than an elongated rocker. Its approximate button/plate width ratio is 66/334 = 0.198; an 86 mm plate gives about 17 mm. This is the basis of the reference button, not an exact SKU identification. Projection (6 mm), switch travel and force remain unmeasured. The design therefore provides three insert depths and a replaceable contact interface.

Related manufacturer information:

- [Schneider S-Classic E31/1/2A](https://eshop.se.com/ae/switch-s-classic-250v-10ax-1-way-switch-1-gangs-white-e31-1-2a.html): a related small-button product family, **not a confirmed match** to the photograph. No exact rocker travel was obtained from this page.
- [FEETECH STS3215 datasheet](https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf): retained servo model. The CAD uses the prior 45.2 × 24.7 × 35 mm body envelope. Shaft offset, supplied horn and mounting ears must be checked against the physical unit.
- [Waveshare Servo Driver with ESP32](https://docs.waveshare.com/Servo_Driver_with_ESP32): 65 × 30 mm PCB, 58 × 23 mm mounting pattern and 2.75 mm holes. Component/plug geometry is represented by a provisional keepout, not an imported board model.
- [Autodesk temporary BRep API](https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/files/fusion_TemporaryBRepManager.htm): repeatable direct-solid construction, copying, transformation and Boolean intersection checks.

The previous green rectangle was the Waveshare PCB reference. In v0.2 the same controller is mounted internally above the servo and hidden by the cover during normal viewing.
