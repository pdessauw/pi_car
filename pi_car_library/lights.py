"""

"""
try:
    import RPi.GPIO as GPIO

    if GPIO.getmode() is None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
except Exception as e:
    print e
    print "Loading mock library..."
    from pi_car_library import GPIO as GPIO
    GPIO.setwarnings(False)


class CarLight(object):

    def __init__(self, pin):
        self.light_pin = pin
        self.status = 0
        GPIO.setup(self.light_pin, GPIO.OUT)

    def turn_on(self):
        self.status = 1
        GPIO.output(self.light_pin, GPIO.HIGH)

    def turn_off(self):
        self.status = 0
        GPIO.output(self.light_pin, GPIO.LOW)
