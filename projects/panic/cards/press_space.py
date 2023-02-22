# install the pyautogui package:
# pip install pyautogui
import pyautogui
import random
import time

def space_or_backspace():
  what = random.choice([
    'space',
    'backspace'
  ])

  pyautogui.press(what)

random.seed(time.time())

while True:
  # sleep between 10 and 30 seconds
  time.sleep(random.randint(10,30))

  space_or_backspace()
