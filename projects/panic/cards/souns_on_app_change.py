# pip install pywin32 winsound
import winsound, win32gui, time
import random

# beep every time the window changes

def wait_for_app_change():
  prev = None
  while True:
   cur = win32gui.GetForegroundWindow()
   if prev and cur != prev:
     return True
   prev = cur
   time.sleep(0.01)

while True:
  wait_for_app_change()
  freq = random.randint(1000,3000)
  winsound.Beep(freq, 100)
