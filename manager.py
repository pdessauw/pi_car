"""

"""
import time
from random import randint
from time import sleep
from pi_car_library import XboxController
from pi_car_systems.brakes import BrakingSystem
from pi_car_systems.blinkers import BlinkerSystem


BRAKE_PIN = 5
LEFT_BLINKER_PIN = 6
RIGHT_BLINKER_PIN = 13

_systems = []


def left_blinker_callback(value):
    global _systems

    if "lblinker" not in _systems:
        return

    if value == 0:
        return

    system = _systems["lblinker"]
    status = system.print_status()

    if status == "ON":
        system.release()
    elif status == "OFF":
        if "rblinker" in _systems and _systems["rblinker"].print_statsu() == "ON":
            _systems["rblinker"].release()

        system.trigger()


def right_blinker_callback(value):
    global _systems

    if "rblinker" not in _systems:
        return

    if value == 0:
        return

    system = _systems["rblinker"]
    status = system.print_status()

    if status == "ON":
        system.release()
    elif status == "OFF":
        if "lblinker" in _systems and _systems["lblinker"].print_statsu() == "ON":
            _systems["lblinker"].release()

        system.trigger()


def hazards_callback(value):
    global _systems

    if "hazards" not in _systems or "hazards" not in _systems:
        return

    if value == 0:
        return

    system = _systems["hazards"]
    status = system.print_status()

    if status == "ON":
        system.release()
    elif status == "OFF":
        system.trigger()


def brakes_callback(value):
    global _systems
    threshold = 0.2  # 20% of the push

    if "brakes" not in _systems:
        return

    system = _systems["brakes"]
    status = system.print_status()

    if value < threshold and status == "ON":
        system.release()
    elif value >= threshold and status in ["ON", "OFF"]:
        # Value is forwarded to the system to determine the force applied on the brakes
        system.trigger(value)


def init_car():
    # Configure car systems
    global _systems
    _systems = {
        "brakes": BrakingSystem(BRAKE_PIN),
        "lblinker": BlinkerSystem(LEFT_BLINKER_PIN),
        "rblinker": BlinkerSystem(RIGHT_BLINKER_PIN),
        "hazards": BlinkerSystem([LEFT_BLINKER_PIN, RIGHT_BLINKER_PIN])
    }

    _systems["lblinker"].set_name("left blinker")
    _systems["lblinker"].set_name("right blinker")
    _systems["hazards"].set_name("hazards")

    # Configure controller
    _controller = XboxController.XboxController()

    _controller.setupControlCallback(_controller.XboxControls.X, left_blinker_callback)
    _controller.setupControlCallback(_controller.XboxControls.B, right_blinker_callback)
    _controller.setupControlCallback(_controller.XboxControls.Y, hazards_callback)

    _controller.setupControlCallback(_controller.XboxControls.LTRIGGER, brakes_callback)

    return _controller


def test_system(system, min_range=1000, max_range=3000):
    wait_time = randint(min_range, max_range)/1000.
    print wait_time

    system.trigger()
    sleep(wait_time)
    system.release()


if __name__ == "__main__":
    controller = init_car()
    controller.start()

    _stop_request = 0
    _stop_timemillis = -1

    while _stop_request < 2:
        if controller.BACK == 1:
            _stop_diff = time.time() - _stop_timemillis
            if _stop_diff < 1.5 and _stop_request == 1:
                _stop_request = 2
            else:
                _stop_request = 1
                _stop_timemillis = time.time()

            print "SR " + str(_stop_request)

            while controller.BACK == 1:
                sleep(.01)

        sleep(.1)

    controller.stop()
