# breath.py Graham Seamans

import time
import os
import numpy as np
import sys
import math

COARSE = 50
clear_count = 0

try:
    os.system("tput civis")

    while True:

        for i in np.arange(0, math.pi * 2, (math.pi * 2) / COARSE):
            print(int((((math.cos(i) + 1) * 15 + 1))) * "#")
            time.sleep(14 / COARSE)

        clear_count += 1
        if clear_count > 100:
            os.system("clear")
            clear_count = 0

    """
    while True:
        for i in range(1,8):
            print(i * '#')
            time.sleep(1)
        for i in range(7,0,-1):
            print(i * '#')
            time.sleep(1)

    """
except KeyboardInterrupt:
    print()
except Exception as e:
    print(e)
finally:
    os.system("tput cnorm")
    sys.exit(0)
