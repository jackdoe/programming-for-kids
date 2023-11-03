# pip install pyautogui pywin32
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

while True:
  # sleep between 5 and 10 seconds
  time.sleep(random.randint(5,10))

  # only press Alt+Tab if Chrome is
  # the current active window
  if is_foreground("Chrome"):
    pyautogui.hotkey(
      "alt",
      "tab",
      interval=0.2)
