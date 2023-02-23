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

# If World of Warcraft is active, write
# 'hello there..' in the chat every 30
# to 60 seconds
while True:
  if is_foreground("World of Warcraft"):
    pyautogui.press('enter')
    pyautogui.write('hello there..')
    pyautogui.press('enter')

  # sleep between 30 and 60 seconds
  time.sleep(random.randint(30,60))
    
