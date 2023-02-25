import RPi.GPIO as GPIO


class BCD:
    def __init__(self, pin_control, pin_bit_1, pin_bit_2, pin_bit_4, pin_bit_8) -> None:
        self.pin_control = pin_control
        self.pin_bit_1 = pin_bit_1
        self.pin_bit_2 = pin_bit_2
        self.pin_bit_4 = pin_bit_4
        self.pin_bit_8 = pin_bit_8
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(pin_control, GPIO.OUT)
        GPIO.setup(pin_bit_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin_bit_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin_bit_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(pin_bit_8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def value(self):
        """value reads the value from a BCD counter object

        Returns:
            int: Current integeter value displayed on the counter.
        """
        GPIO.setup(self.pin_control, GPIO.OUT)
        GPIO.output(self.pin_control, 1)
        bit_1 = GPIO.input(self.pin_bit_1)
        bit_2 = GPIO.input(self.pin_bit_2)
        bit_4 = GPIO.input(self.pin_bit_4)
        bit_8 = GPIO.input(self.pin_bit_8)
        GPIO.cleanup(self.pin_control)

        return bit_1 + (bit_2 * 2) + (bit_4 * 4) + (bit_8 * 8)

    def __delattr__(self, __name: str) -> None:
        GPIO.cleanup(
            [self.pin_control, self.pin_bit_1, self.pin_bit_2, self.pin_bit_4, self.pin_bit_8]
        )
