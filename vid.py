import os
import time

os.system("raspivid -t 600000 -o dixmin.h264")

time.sleep(2)
