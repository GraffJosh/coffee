import RPi.GPIO as GPIO


class MotorController:
    """Motor Controller is a PWM output for motors."""

    def __init__(self, forward_enable_pin, reverse_enable_pin, pwm_pin) -> None:
        """Initialize the motor controller object with pins for forward enable,
        reverse enable, and PWM control.

        Args:
            forward_enable_pin (int): Forward EN on motor controller
            reverse_enable_pin (int): Reverse EN on motor controller.
            pwm_pin (int): PWM Input on motor controller.
        """
        self.pwm_pin = pwm_pin  # PWM pin connected to PWM input on Motor Controller
        self.forward_enable_pin = forward_enable_pin  # Pin connected to EN Forward
        self.reverse_enable_pin = reverse_enable_pin  # PWM pin connected EN Reverse

        GPIO.setwarnings(False)  # disable warnings
        GPIO.setmode(GPIO.BCM)  # set pin numbering system
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        GPIO.setup(self.forward_enable_pin, GPIO.OUT)
        GPIO.setup(self.reverse_enable_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 1000)  # create PWM instance with frequency
        self.percentage = 0
        self.pwm.start(self.percentage)  # start PWM of required Duty Cycle

    def set_pwm_percentage(self, percentage):
        """set the pwm dutycycle percentage as an offset from 50 = 0

        Args:
            percentage (_type_): -100 for full reverse, 100 for full forward
        """
        # if reverse
        if percentage < 0 and percentage > -100:
            GPIO.output(self.forward_enable_pin, 0)
            GPIO.output(self.reverse_enable_pin, 1)
        # if forward
        elif percentage > 0 and percentage < 100:
            GPIO.output(self.reverse_enable_pin, 0)
            GPIO.output(self.forward_enable_pin, 1)
        # if error
        else:
            self.percentage = 0
            raise ValueError
        self.percentage = percentage
        self.pwm.ChangeDutyCycle(abs(self.percentage))

    def get_pwm_percentage(self):
        return self.percentage
