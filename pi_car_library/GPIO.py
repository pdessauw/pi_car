"""

"""

BCM = "BCM"
OUT = "OUT"
HIGH = "HIGH"
LOW = "LOW"


def __mock_function(fname, fparams):
    print "Function " + fname + " triggered with " + str(fparams)


def setup(pin, mode):
    __mock_function("setup", {"pin": pin, "mode": mode})


def output(pin, mode):
    __mock_function("output", {"pin": pin, "mode": mode})


def setmode(mode):
    __mock_function("setmode", {"mode": mode})


def setwarnings(mode):
    __mock_function("setwarnings", {"mode": mode})
