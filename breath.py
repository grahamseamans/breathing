# breath.py Graham Seamans
# Ujjayi breathing animation

import os
import sys
from utils import breath


def clear_per_100_breath(breath_count):
    breath_count += 1
    if breath_count >= 100:
        os.system("clear")
        return 0
    else:
        return breath_count


try:
    os.system("tput civis")
    breath_count = 0

    while True:
        breath(14)
        breath_count = clear_per_100_breath(breath_count)

except KeyboardInterrupt:
    print()
except Exception as e:
    print(e)
finally:
    os.system("tput cnorm")
    sys.exit(0)
