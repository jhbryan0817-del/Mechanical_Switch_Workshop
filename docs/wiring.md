# Low-voltage wiring and control notes

This repository supplies a mechanical prototype, not tested firmware. Do not command the full servo range with the cam installed.

```text
Regulated 7.4 V DC supply
        │  correct polarity + appropriate inline protection
        ▼
Waveshare DC barrel input (5.5 × 2.1 mm)
        │
        └── ST-series 3-wire bus connector ── STS3215
              GND / VCC / TTL signal

Computer ── USB-C ── Waveshare (programming)
```

Verify DC polarity from the actual board marking and manufacturer documentation before connecting power. Verify the bus cable pin order; wire colour alone is not evidence. The FEETECH datasheet lists pin 1 GND, pin 2 VCC and pin 3 signal. Use the compatible ST-series connector on the board.

The Waveshare input accepts 6–12 V, but **the input must also match the connected servo's voltage**. The referenced STS3215 variant is specified for 4–7.4 V and draws about 2.5 A at stall at 7.4 V. Use a regulated supply; do not treat the board's 12 V rating as a servo rating. Do not connect a raw fully charged 2S lithium battery (8.4 V) to this 7.4 V build. Do not assume USB-C powers the servo.

A 7.4 V supply rated at least 3 A is a starting design choice; 5 A gives supply headroom. Current limiting is still needed during first tests. Select fusing and cable size to the actual supply and conductor ratings. Never leave a stalled servo powered.

Proposed control sequence, to be implemented and tested separately:

1. Confirm calibrated neutral with both tips clear.
2. Ramp slowly toward the selected lobe.
3. Stop after the rocker latches; hold only briefly, approximately 100–250 ms.
4. Return to neutral.
5. Abort on abnormal current, travel, heat or loss of position feedback.

For a 4096-count revolution, 40° is approximately 455 counts. A nominal neutral of 2048 gives illustrative positions 1593 and 2503. These are **not ready-to-run limits**: horn phasing, direction and actual switch travel must be calibrated. Printed stops are backups, not targets. Force-limiting springs also have finite travel and cease providing protection if they go solid.

Sources checked for this iteration:

- [FEETECH STS3215 7.4 V datasheet](https://files.seeedstudio.com/products/Feetech/108090023_STS3215-C001_Datasheet.pdf)
- [Waveshare Servo Driver with ESP32 specifications](https://docs.waveshare.com/Servo_Driver_with_ESP32)

Use the manufacturer's current instructions for board setup and firmware; the mechanical repository does not replace them.

