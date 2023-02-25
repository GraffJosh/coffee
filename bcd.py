import RPi.GPIO as GPIO


def read_pin(pin_data):
    """returns the value of a pin, given a differential

    Args:
        pin_data (int): pin that sets the data

    Returns:
        int: value high or low given input pin
    """
    # GPIO.setup(pin_control, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    value = not GPIO.input(pin_data)
    return value


class BCD:
    def __init__(self, pin_bit_1, pin_bit_2, pin_bit_4, pin_bit_8) -> None:
        self.pin_bit_1 = pin_bit_1
        self.pin_bit_2 = pin_bit_2
        self.pin_bit_4 = pin_bit_4
        self.pin_bit_8 = pin_bit_8
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pin_bit_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pin_bit_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pin_bit_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pin_bit_8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def value(self):
        """value reads the value from a BCD counter object

        Returns:
            int: Current integeter value displayed on the counter.
        """

        bit_1 = read_pin(self.pin_bit_1)
        bit_2 = read_pin(self.pin_bit_2)
        bit_4 = read_pin(self.pin_bit_4)
        bit_8 = read_pin(self.pin_bit_8)
        curr_value = bit_8 << 3 | bit_4 << 2 | bit_2 << 1 | bit_1

        return curr_value

    def __delattr__(self, __name: str) -> None:
        GPIO.cleanup([self.pin_bit_1, self.pin_bit_2, self.pin_bit_4, self.pin_bit_8])
