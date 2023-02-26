import RPi.GPIO as GPIO


class MotorController:
    """Motor Controller is a PWM output for motors."""

    def __init__(self, motor_pin) -> None:
        self.motor_pin = motor_pin  # PWM pin connected to LED
        GPIO.setwarnings(False)  # disable warnings
        GPIO.setmode(GPIO.BCM)  # set pin numbering system
        GPIO.setup(self.motor_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.motor_pin, 1000)  # create PWM instance with frequency
        self.percentage = 0
        self.pwm.start(self.percentage)  # start PWM of required Duty Cycle

    def set_pwm_percentage(self, percentage):
        """set the pwm dutycycle percentage as an offset from 50 = 0

        Args:
            percentage (_type_): _description_
        """
        if percentage > 100 or percentage < 0:
            raise ValueError
        self.percentage = percentage
        self.pwm.ChangeDutyCycle(self.percentage / 2 + 50)

    def get_pwm_percentage(self):
        return self.percentage
