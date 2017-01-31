"""

"""
from pi_car_library.systems import CarSystem


class BrakingSystem(CarSystem):

    def __init__(self):
        super(BrakingSystem, self).__init__("brakes")
        # Initialize light

    def trigger(self, **params):
        self._sindex = 1  # ON
        # turn light on
        # activate brakes

    def release(self):
        self._sindex = 0  # OFF
        # turn light off
        # deactivate brakes

