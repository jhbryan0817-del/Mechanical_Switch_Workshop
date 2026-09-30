# Battery power and commissioning — v0.7

Selected mechanical reference: **Gens ace GEA8502S60E2, 850 mAh, 2S, 7.4 V, 60C**, EC2 output and JST-XHR-3P balance lead. A standard 2S LiPo reaches 8.4 V fully charged. Its nominal energy is 6.29 Wh; runtime depends strongly on servo load and ESP32 standby current and has not been measured.

This selection is suitable in voltage for the **6–12.6 V ST3215 variant** and the Waveshare board's documented **6–12 V VIN**. The manufacturer also lists lower-voltage servo variants. Confirm the exact purchased servo: do not connect an 8.4 V charged pack to a servo whose maximum rating is 7.4 V. No regulator for that alternative is modeled.

The board passes input power to the servo; the servo is not powered from the ESP32's 3.3 V rail or USB. The advertised 60C rating gives ample nominal current headroom for one servo, but wiring, fuse, connector, board and protection limits still govern the assembly. Waveshare lists 2.7 A stall current for its 12 V ST3215; stall is not a normal duty condition.

Suggested topology:

Battery EC2 → fuse close to pack → suitable 2S low-voltage disconnect/protection → internal board DC input → servo bus connector.

Verify polarity at the actual jack and harness before connecting. Keep the balance lead insulated and available for charging; do not use it as the servo power output. The battery listing does not establish an integrated BMS, and the driver is not documented as a LiPo charger or a complete battery-protection system. Protection hardware and fuse sizing remain implementation tasks.

Route the servo lead into the closed side pocket opposite the horn, then through the unobstructed upper groove to the PCB top connector. The PCB drop increases nominal top-component headroom from 3.7 to 6.9 mm. The historical layout assumed 6 mm above one servo header and an above-battery lead-storage volume; those dedicated reference bodies are absent from the current live model. These assumed volumes do not validate actual plugs, cable bend radii, fuse or protection-module fit.

The existing DC jack has only about 4.6 mm to the left inner wall at its outermost modeled point. A stock straight barrel connector cannot be assumed to fit. Physically verify a compact right-angle pigtail or revise the power interface before building; do not force a connector or bend the board.

Remove and disconnect the battery for external balance charging with a compatible 2S LiPo charger. No charging port or onboard charger is included. Establish conservative discharge cutoff, strain relief, fuse protection and measured thermal behavior before unattended operation.

Retain the previous commissioning limitations: finalize the actuator, resolve actual switch fit, use slow small movements, stop on contact/stall, and return to a non-loading position. The historical sampled ±15° clearance check does not validate this revision; no actuator is present in the current live model.

Sources:
- [Waveshare board specifications](https://docs.waveshare.com/Servo_Driver_with_ESP32)
- [Waveshare ST3215 variants and current ratings](https://www.waveshare.com/product/modules/st3215-servo.htm)
- [Waveshare servo wiring guide](https://www.waveshare.com/wiki/ST3215_Servo)
- [Gens ace battery dimensions and leads](https://genstattu.com/gens-ace-850mah-2s-60c-7-4v-lipo-battery-ec2-plug-car-classic-non-g-tech/)
