# utils.py Graham Seamans
# shared codebin

import math
import time
import numpy as np


def breath(seconds):
    COARSE = 30
    HEIGHT = 15
    SYMBOL = "#"
    two_pi = math.pi * 2
    for i in np.arange(0, two_pi, two_pi / COARSE):
        print(round(((((math.cos(i) * -1) + 1) * HEIGHT + 0.5))) * SYMBOL)
        time.sleep(seconds / COARSE)
