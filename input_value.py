import bcd


class InputValue:
    def __init__(self, digits) -> None:
        """InputValue is a number that is input through BCD Counters.
        The parameter is a list of lists that define the inputs of the
        counters for this value.

        Args:
            digits ([[int]]): List of lists of inputs. LSB is index0
        """
        self.bcd_counters = []
        for digit in digits:
            self.bcd_counters.append(bcd.BCD(pins=digit))

    def value(self):
        """Returns the current value of the counters.

        Returns:
            _type_: _description_
        """
        tens = 1
        result = 0
        for counter in self.bcd_counters:
            result += counter.value() * tens
            tens = tens * 10
        return result
