from monitorcontrol import get_monitors
import time

# from 0 and up
primaryMonitor = get_monitors()[0]
secondaryMonitor = get_monitors()[1]

# percentage
maxbright = 60
bright = 50
dim = 25


def SetBrightness(monitor):
     # get time
     timestamp = int(time.strftime("%H"))

     if timestamp <= 7 or timestamp == 23:
          with monitor:
               monitor.set_luminance(dim)
               print("\nTime: " + str(timestamp) + "\nMonitor was dimmed")

     elif timestamp == 22:
          with monitor:
               monitor.set_luminance(bright)
               print("\nTime: " + str(timestamp) + "\nMonitor was brightened")

     elif timestamp >= 8 and timestamp <= 21:
          with monitor:
               monitor.set_luminance(maxbright)
               print("\nTime: " + str(timestamp) + "\nMonitor was brightened")


SetBrightness(secondaryMonitor)