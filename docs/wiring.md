# Wiring and commissioning — v0.4

Retain the STS3215 and Waveshare ESP32 driver. Match supply voltage, polarity and bus pinout to the actual purchased variants and manufacturer markings. No firmware/electrical changes are included.

Connect and test before closing the cover. Display and button openings are intentionally closed. Power/USB/servo routing and strain-relief slots remain; check actual plugs and bend clearance. Avoid loading solder joints and keep leads away from moving parts.

Do not reuse earlier repository motion examples. Establish physical switch fit and finalize the actuator before calibrating slow, small movements with conservative current/torque limits. The sampled ±15° clearance check is not an operating-range recommendation. Stop on unexpected contact or a stall; return to a non-loading position after operation.

All added wiring stays outside the faceplate/backbox. Consult the actual servo datasheet and [Waveshare documentation](https://docs.waveshare.com/Servo_Driver_with_ESP32).
