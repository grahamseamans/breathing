# breath.py Graham Seamans
# Ujjayi breathing animation

import os
import sys
from utils import breath


def clear(clear_count):
    clear_count += 1
    if clear_count > 100:
        os.system("clear")
        return 0
    else:
        return clear_count


try:
    os.system("tput civis")
    clear_count = 0

    while True:
        breath(14)
        clear_count = clear(clear_count)

except KeyboardInterrupt:
    print()
except Exception as e:
    print(e)
finally:
    os.system("tput cnorm")
    sys.exit(0)
