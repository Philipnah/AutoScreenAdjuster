import monitorcontrol
from monitorcontrol import get_monitors
import time

# from 0 and up
primaryMonitor = get_monitors()[0]
secondaryMonitor = get_monitors()[1]

# percentage
maxbright = 46
bright = 38
midbright = 33
mid = 30
low = 25
dim = 20

# ---------------------------- not used -------------------------------
# all settings required in the functions array argument
# monitor1Settings = [primaryMonitor, 7, 0, 21, 8, 20, dim, bright, maxbright]
# monitor2Settings = [secondaryMonitor, 7, 23, 21, 8, 20, midbright, bright, maxbright]
# ---------------------------- not used -------------------------------


# function for printing time and luminance
def timeStamper(time, luminance):
     print("\nTime: " + str(time) + "\nMonitor was set to: " + str(luminance))

def SetBrightness(monitorSettings):

     # get time
     timestamp = int(time.strftime("%H"))
     print(timestamp)


     # from 00:00 to 7:00
     if timestamp <= 7 or timestamp == 0:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(dim)
               timeStamper(str(timestamp), dim)

     # 21:00
     elif timestamp == 21:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(dim)
               timeStamper(str(timestamp), dim)

     # from 8:00 to 19:00
     elif timestamp >= 8 and timestamp <= 19:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(maxbright)
               timeStamper(str(timestamp), maxbright)

     # from 20:00 to 23:00 
     elif timestamp >= 20 and timestamp <= 23:
          with monitorSettings[0]:
               monitorSettings[0].set_luminance(low)
               timeStamper(str(timestamp), low)


try:
     SetBrightness(primaryMonitor)
except:
     print("Failed to apply the first monitors settings.")

try:
     SetBrightness(secondaryMonitor)
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