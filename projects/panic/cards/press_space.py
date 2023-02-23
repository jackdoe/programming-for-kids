# install the pyautogui package:
# pip install pyautogui
import pyautogui
import random
import time

def space_or_backspace():
  # pick a choice between
  # space or backspace
  # :evil:
  what = random.choice([
    'space',
    'backspace'
  ])

  pyautogui.press(what)


while True:
  # sleep between 10 and 30 seconds
  time.sleep(random.randint(10,30))

  space_or_backspace()
