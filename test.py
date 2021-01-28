import monitorcontrol
from monitorcontrol import get_monitors
import time

# from 0 and up
primaryMonitor = get_monitors()[0]
secondaryMonitor = get_monitors()[1]

# percentage
maxbright = 60
bright = 50
midbright = 45
low = 30
dim = 25

# all settings required in the functions array argument
monitor1Settings = [primaryMonitor, 7, 0, 23, 8, 21, dim, bright, maxbright]
monitor2Settings = [secondaryMonitor, 7, 23, 22, 8, 21, midbright, bright, maxbright]

def SetBrightness(monitorSettings):
     # get time
     timestamp = int(time.strftime("%H"))

     # lower than minval1 or minval2
     if timestamp <= monitorSettings[1] or timestamp == monitorSettings[2]:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(monitorSettings[6])
               print("\nTime: " + str(timestamp) + "\nMonitor was dimmed")

     elif timestamp == monitorSettings[3]:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(monitorSettings[7])
               print("\nTime: " + str(timestamp) + "\nMonitor was brightened")

     elif timestamp >= monitorSettings[4] and timestamp <= monitorSettings[5]:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(monitorSettings[8])
               print("\nTime: " + str(timestamp) + "\nMonitor was max brightened")

try:
     SetBrightness(monitor1Settings)
except:
     print("Failed to apply the first monitors settings.")

try:
     SetBrightness(monitor2Settings)
except:
     print("Failed to apply the second monitors settings.")