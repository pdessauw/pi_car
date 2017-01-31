from threading import Thread
from time import sleep

from pi_car_library.lights import CarLight
from pi_car_library.systems import CarSystem


class BlinkerSystem(CarSystem):

    def __init__(self, light_pin):
        super(BlinkerSystem, self).__init__("blinkers")
        self.blinker = CarLight(light_pin)  # Init light
        self.blink_thread = Thread(target=self.blink)
        self.blink_thread.daemon = True

    def trigger(self):
        self._sindex = 1  # ON
        self.blink_thread.start()

    def release(self):
        self._sindex = 0  # OFF

    def blink(self):
        while self._sindex == 1:
            self.blinker.turn_on()
            sleep(.5)
            self.blinker.turn_off()
            sleep(.5)
