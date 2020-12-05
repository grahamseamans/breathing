import time
import os
import sys

try:
    os.system('tput civis')
    while True:
        for i in range(1,8):
            print(i * '#')
            time.sleep(1)
        for i in range(7,0,-1):
            print(i * '#')
            time.sleep(1)
except KeyboardInterrupt:
    print()
    os.system('tput cnorm')
    sys.exit(0)
