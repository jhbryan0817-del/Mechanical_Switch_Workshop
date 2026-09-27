# Low-voltage control notes

Retain the existing STS3215 and Waveshare ESP32 servo driver. Connect a regulated supply compatible with the **actual servo variant** to the board's DC input; connect the servo to the compatible ST-series bus port. The controller's 6–12 V input specification does not override the servo's voltage limit. The referenced 7.4 V servo build must not be supplied with 12 V. Verify polarity and keyed pinout against the hardware markings and manufacturer documentation.

The mechanism has changed; **discard the v0.1 cam commands and ±40° examples**. No ready-to-run firmware is supplied in this mechanical repository.

1. Establish neutral with the paddle detached. Fit the horn in the documented neutral orientation, then disconnect power for assembly.
2. Confirm both soft contact ends clear the rocker in either latched state. Check the correct direction with small, low-speed movements.
3. Increase displacement only until latching occurs. Return to neutral after the press; do not hold the servo against the rocker.
4. Configure conservative torque/current protection using the actual servo/controller capabilities. Stop on abnormal current, missed movement or a stalled motor.
5. Keep the calibrated limit within the checked geometric range, and smaller wherever actual switch travel allows. The ±30° CAD sweep is a clearance study, not a safe default command.

The TPU leaves offer finite compliance, not a measured force limit. Characterize force versus displacement and check permanent set before powered cycling. Route and restrain cables inside the enclosure without touching the paddle or bending connectors against the lid. All wiring remains external to the faceplate/backbox.

Sources: [FEETECH STS3215 datasheet](https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf), [Waveshare controller documentation](https://docs.waveshare.com/Servo_Driver_with_ESP32).
