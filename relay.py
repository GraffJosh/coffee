import RPi.GPIO as GPIO


class Relay:
    def __init__(self, pin_output) -> None:
        self.pin_output = pin_output
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_output, GPIO.OUT)
        GPIO.output(self.pin_output, 0)
        self.output = False

    def on(self):
        GPIO.output(self.pin_output, 1)
        self.output = True

    def off(self):
        GPIO.output(self.pin_output, 0)
        self.output = False

    def status(self):
        return self.output
