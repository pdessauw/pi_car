"""

"""
try:
    import RPi.GPIO as GPIO
except Exception as e:
    print e
    print "Loading mock library..."
    import pi_car_library.GPIO as GPIO


class Light(object):

    def __init__(self, pin):
        self.light_pin = pin
        GPIO.setup(self.light_pin, GPIO.OUT)

    def turn_on(self):
        GPIO.output(self.light_pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.light_pin, GPIO.LOW)
