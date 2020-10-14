import monitorcontrol
from monitorcontrol import get_monitors
import time

# get time
timestamp = int(time.strftime("%H"))

# from 0 and up
primaryMonitor = get_monitors()[0]
secondaryMonitor = get_monitors()[1]

# percentage
bright = 60
dim = 25

# 15 mins
wait = 900

def SetBrightness(monitor):
     if timestamp <= 7 or timestamp == 23:
          with monitor:
               monitor.set_luminance(dim)
               print("\nTime: " + time + "\nMonitor was dimmed")

     elif timestamp >= 8 and timestamp <= 22:
          with monitor:
               monitor.set_luminance(bright)

while True:
     SetBrightness(secondaryMonitor)
     time.sleep(wait)