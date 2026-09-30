# References and assumptions — v0.5

The live **Mechanical Switch** Fusion document is authoritative for v0.5:
`urn:adsk.wipprod:dm.lineage:CupzHhEKR8SBy7rRZjCF3g`.

The repository's F3D, STEP, STLs, images and JSON reports are retained v0.4 references. No new CAD is uploaded for this revision.

## Battery

[Gens ace GEA8502S60E2, 850 mAh 2S 7.4 V 60C EC2](https://genstattu.com/gens-ace-850mah-2s-60c-7-4v-lipo-battery-ec2-plug-car-classic-non-g-tech/) supplies the mechanical envelope: 58 × 32 × 20 mm nominal, length ±5 mm and width/height ±2 mm. The manufacturer lists 100 mm discharge wires and a 45 mm JST-XHR-3P balance lead. Fusion contains a nominal envelope and a hidden maximum-size clearance body, not a detailed manufacturer STEP file.

The researched [1000 mAh 2S Gens ace alternative](https://genstattu.com/gens-ace-2s-1000mah-45c-lipo-battery-pack-with-deans-plug/) is 72 × 36 × 13 mm nominal, with the same listed ±5/±2/±2 mm tolerances. Its maximum length exceeds the original enclosure's internal span. The smaller 850 mAh pack was selected to stay near the requested capacity while providing dimensional allowance.

## Electronics and mechanics

- [Waveshare Servo Driver with ESP32](https://docs.waveshare.com/Servo_Driver_with_ESP32): 6–12 V input; existing detailed manufacturer PCB model retained and lowered.
- [Waveshare ST3215](https://www.waveshare.com/product/modules/st3215-servo.htm): distinguish voltage variants. The proposed 2S supply assumes the 6–12.6 V version.
- User-identified [Schneider S-Classic E31_1_2AR_WE](https://www.se.com/hk/en/product/E31_1_2AR_WE/sclassic-1way-switch-1-gang-white/): existing 86 mm faceplate reference retained. Rocker force/travel and plate curvature are unverified.

The approved cable pocket increases overall width to 90 mm; the battery-side wall adds 1 mm, making the other overall dimension 83 mm. The central mounting arrangement and actuator position are preserved.

The 6 mm servo-header plug allowance and battery lead-storage volume are design assumptions. Power-pigtail and protection-module fit remain unresolved. See [validation](../docs/validation.md).
