"""

"""
try:
    import RPi.GPIO as GPIO
except Exception as e:
    print e
    print "Loading mock library..."
    import pi_car_library.GPIO as GPIO


from pi_car_systems.brakes import BrakingSystem

USE_CONTROLLER = False


def init_car():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    return {
        "brakes": BrakingSystem(),
    }

if __name__ == "__main__":
    systems = init_car()

    for k, v in systems.items():
        print v

    # if USE_CONTROLLER:
    #     from pi_car_inputs import controller as input
    # else:
    #     from pi_car_inputs import keyboard as input

