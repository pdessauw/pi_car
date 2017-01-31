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

    def set_name(self, name):
        self._name = name

    def print_status(self):
        try:
            return self._statuses[self._sindex]
        except Exception as e:
            return "ERROR: " + str(e.message)

    def __str__(self):
        return "System: " + str(self._name).upper() + "; Status: " + self.print_status()
