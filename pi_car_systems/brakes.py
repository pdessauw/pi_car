"""

"""
from threading import Thread
from time import sleep
from pi_car_library.lights import CarLight
from pi_car_library.systems import CarSystem


class BrakingSystem(CarSystem):

    def __init__(self, light_pin):
        super(BrakingSystem, self).__init__("brakes")
        self.brake_light = CarLight(light_pin)  # Init brake light
        self.blink_thread = Thread(target=self.display_brake_light)
        self.blink_thread.daemon = True
        self.blink_thread.start()

    def trigger(self, brake_force):
        self._sindex = 1  # ON
        # Activate brakes
        # TODO add code for brakes

    def release(self):
        self._sindex = 0  # OFF
        # Deactivate brakes
        # TODO add code for brakes

    def display_brake_light(self):
        while True:
            if self._sindex == 1 and self.brake_light.status == 0:
                self.brake_light.turn_on()
            elif self._sindex == 0 and self.brake_light.status == 1:
                self.brake_light.turn_off()

            sleep(.1)
