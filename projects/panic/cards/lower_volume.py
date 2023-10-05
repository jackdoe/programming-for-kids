# pip install pywin32
import win32api
import win32gui
import time
import random

WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_DOWN = 0x90000

def decrease_sound():
  win32api.SendMessage(
    win32gui.GetForegroundWindow(),
    WM_APPCOMMAND, 
    0, 
    APPCOMMAND_VOLUME_DOWN
  )


# slowly decrease the volume every 1 to 30
# seconds
while True:
  decrease_sound()
  time.sleep(random.randint(1,30))
