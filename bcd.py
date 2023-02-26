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
    def __init__(self, pins=[], pin_bit_1=-1, pin_bit_2=-1, pin_bit_4=-1, pin_bit_8=-1) -> None:
        self.pin_bits = []
        if len(pins) > 0:
            for pin in pins:
                self.pin_bits.append(pin)
        else:
            if pin_bit_1 > 0:
                self.pin_bits[0] = pin_bit_1
            if pin_bit_2 > 0:
                self.pin_bits[1] = pin_bit_2
            if pin_bit_4 > 0:
                self.pin_bits[2] = pin_bit_4
            if pin_bit_8 > 0:
                self.pin_bits[3] = pin_bit_8

        GPIO.setmode(GPIO.BCM)
        for pin in self.pin_bits:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def value(self):
        """value reads the value from a BCD counter object

        Returns:
            int: Current integeter value displayed on the counter.

        """
        shift_bit = 0
        curr_value = 0
        for pin in self.pin_bits:
            curr_value = curr_value | read_pin(pin) << shift_bit
            shift_bit += 1

        return curr_value

    def __delattr__(self, __name: str) -> None:
        GPIO.cleanup(self.pin_bits)
