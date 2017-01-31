"""

"""
from pi_car_library.lights import CarLight
from pi_car_library.systems import CarSystem


class BrakingSystem(CarSystem):

    def __init__(self, light_pin):
        super(BrakingSystem, self).__init__("brakes")
        self.brake_light = CarLight(light_pin)  # Init brake light

    def trigger(self):
        self._sindex = 1  # ON
        self.brake_light.turn_on()
        # Activate brakes

    def release(self):
        self._sindex = 0  # OFF
        # Deactivate brakes
        self.brake_light.turn_off()
