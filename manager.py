"""

"""
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

if __name__ == "__main__":
    systems = init_car()

    # Brake test
    systems["brakes"].trigger()
    sleep(1)
    systems["brakes"].release()

    # Blinker test
    systems["lblinker"].trigger()
    sleep(1)
    print systems["lblinker"]
    sleep(1)
    systems["lblinker"].release()

    for k, v in systems.items():
        print v
