# wim_hof.py Graham Seamans
# Wim Hof breathing helper

import os
import sys
from utils import breath


def fast():
    print("Fast breaths")
    for _ in range(20):
        breath(3)


def hold():
    print("Hold")
    input("Press enter when done with breath hold")


def recovery():
    print("Deep breath")
    breath(20)


def cycle():
    fast()
    hold()
    recovery()


try:
    os.system("tput civis")

    while True:
        cycle()

except KeyboardInterrupt:
    print()
except Exception as e:
    print(e)
finally:
    os.system("tput cnorm")
    sys.exit(0)
