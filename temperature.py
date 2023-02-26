import board
import digitalio
import adafruit_max31865


class Temperature:
    def __init__(self) -> None:
        spi = board.SPI()
        cs = digitalio.DigitalInOut(board.D5)
        self.sensor = adafruit_max31865.MAX31865(spi, cs, wires=2)

    def value(self):
        return self.sensor.temperature
