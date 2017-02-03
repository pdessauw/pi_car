"""

"""

BCM = "BCM"
OUT = "OUT"
HIGH = "HIGH"
LOW = "LOW"

LOGGING = True


def __mock_function(fname, fparams):
    global LOGGING
    if LOGGING:
        print "Function " + fname + " triggered with " + str(fparams)


def setup(pin, mode):
    __mock_function("setup", {"pin": pin, "mode": mode})


def output(pin, mode):
    __mock_function("output", {"pin": pin, "mode": mode})


def setwarnings(mode):
    global LOGGING
    LOGGING = mode
