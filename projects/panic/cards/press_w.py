# pip install pyautogui win32gui
import pyautogui
import random
import time
import win32gui

def is_foreground(name):
  w = win32gui.GetForegroundWindow()
  title = win32gui.GetWindowText(w)
  if name in title:
    return True
  return False
  
# this card is small, but particularly
# evil, especially if someone is playing
# a game where you can fall, or jump in
# lava.. like Minecraft
while True:
  # sleep between 5 and 10 minutes
  time.sleep(random.randint(300,600))

  # only press W if Minecraft is
  # the current active window
  if is_foreground("Minecraft"):
    # press W for 1 second
    with pyautogui.hold('w'):
      pyautogui.sleep(1)
