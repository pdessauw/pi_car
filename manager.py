"""

"""
from random import randint
from time import sleep

from pi_car_systems.brakes import BrakingSystem
from pi_car_systems.blinkers import BlinkerSystem


BRAKE_PIN = 5
LEFT_BLINKER_PIN = 6


def init_car():
    _systems = {
        "brakes": BrakingSystem(BRAKE_PIN),
        "lblinker": BlinkerSystem(LEFT_BLINKER_PIN)
    }

    _systems["lblinker"].set_name("left blinker")

    return _systems


def test_system(system, min_range=1000, max_range=3000):
    wait_time = randint(min_range, max_range)/1000.
    print wait_time

    system.trigger()
    sleep(wait_time)
    system.release()

if __name__ == "__main__":
    systems = init_car()

    # Test systems 1
    test_system(systems["brakes"])
    test_system(systems["lblinker"])

    # Test systems 2
    test_system(systems["brakes"])
    test_system(systems["lblinker"])

    for k, v in systems.items():
        print v
