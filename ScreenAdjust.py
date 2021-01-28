import monitorcontrol
from monitorcontrol import get_monitors
import time

# from 0 and up
primaryMonitor = get_monitors()[0]
secondaryMonitor = get_monitors()[1]

# percentage
maxbright = 50
bright = 40
midbright = 35
low = 30
dim = 25

# all settings required in the functions array argument
monitor1Settings = [primaryMonitor, 7, 0, 21, 8, 20, dim, bright, maxbright]
monitor2Settings = [secondaryMonitor, 7, 23, 21, 8, 20, midbright, bright, maxbright]

def SetBrightness(monitorSettings):
     # get time
     timestamp = int(time.strftime("%H"))
     print(timestamp)

     print(monitor1Settings[1],monitor1Settings[2],monitor1Settings[3],monitor1Settings[4],monitor1Settings[5])

     # lower than minval1 or minval2
     if timestamp <= monitorSettings[1] or timestamp == monitorSettings[2]:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(monitorSettings[6])
               print("\nTime: " + str(timestamp) + "\nMonitor was dimmed")

     elif timestamp == monitorSettings[3]:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(monitorSettings[7])
               print("\nTime: " + str(timestamp) + "\nMonitor was midbrightened")

     elif timestamp >= monitorSettings[4] and timestamp <= monitorSettings[5]:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(monitorSettings[8])
               print("\nTime: " + str(timestamp) + "\nMonitor was max brightened")
     elif timestamp >= 21 and timestamp <= 23:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(30)
               print("\nTime: " + str(timestamp) + "\nMonitor was dimmed")
     else:
          print("else")

try:
     SetBrightness(monitor1Settings)
except:
     print("Failed to apply the first monitors settings.")

try:
     SetBrightness(monitor2Settings)
except:
     print("Failed to apply the second monitors settings.")

# import monitorcontrol
# from monitorcontrol import get_monitors
# import time

# # from 0 and up
# primaryMonitor = get_monitors()[0]
# secondaryMonitor = get_monitors()[1]

# # percentage
# maxbright = 60
# bright = 50
# midbright = 45
# low = 30
# dim = 25


# def SetBrightness(monitor, minVal1 ,minVal2, medVal, maxval1, maxval2, minBrightness, medBrightness, maxBrightness):
#      # get time
#      timestamp = int(time.strftime("%H"))

#      # lower than minval1 or minval2
#      if timestamp <= minVal1 or timestamp == minVal2:
#           with monitor:
#                monitor.set_luminance(minBrightness)
#                print("\nTime: " + str(timestamp) + "\nMonitor was dimmed")

#      elif timestamp == medVal:
#           with monitor:
#                monitor.set_luminance(medBrightness)
#                print("\nTime: " + str(timestamp) + "\nMonitor was brightened")

#      elif timestamp >= maxval1 and timestamp <= maxval2:
#           with monitor:
#                monitor.set_luminance(maxBrightness)
#                print("\nTime: " + str(timestamp) + "\nMonitor was max brightened")

# try:
#      SetBrightness(primaryMonitor, 7, 0, 23, 8, 21, dim, bright, maxbright)
# except:
#      pass

# try:
#      SetBrightness(secondaryMonitor, 7, 23, 22, 8, 21, midbright, bright, maxbright)
# except:
#      pass