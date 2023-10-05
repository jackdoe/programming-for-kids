# pip install pywin32
import win32api
import win32gui
import time
import random

WM_APPCOMMAND = 0x319
APPCOMMAND_VOLUME_MUTE = 0x80000

def mute_sound():
  win32api.SendMessage(
    win32gui.GetForegroundWindow(),
    WM_APPCOMMAND, 
    0, 
    APPCOMMAND_VOLUME_MUTE
  )

# mute every 5 minutes
while True:
  mute_sound()
  time.sleep(300)
