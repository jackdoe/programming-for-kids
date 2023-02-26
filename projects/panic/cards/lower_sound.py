# pip install pywin32
import win32api
import win32con
import time
import random

def decrease_sound():
  win32api.SendMessage(
      -1,
      win32con.WM_APPCOMMAND, 
      0, 
      win32con.APPCOMMAND_VOLUME_DOWN
    )


# slowly decrease the volume every 1 to 30
# seconds
while True:
  decrease_sound()
  time.sleep(random.randint(1,30))
