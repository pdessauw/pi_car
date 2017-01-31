"""

"""


class CarSystem(object):

    def __init__(self, sys_name):
        self._statuses = ["OFF", "ON"]
        self._sindex = 0
        self._name = sys_name

    def trigger(self, **params):
        raise NotImplementedError()

    def release(self, **params):
        raise NotImplementedError()

    def print_status(self):
        try:
            return self._statuses[self._sindex]
        except Exception as e:
            return "ERROR"

    def __str__(self):
        return "System: " + str(self._name).upper() + "; Status: " + self.print_status()
