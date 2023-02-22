# install the pyautogui package:
# pip install pyautogui
import pyautogui
import random
import time

def click():
  # locate the top right corner
  # of the current screen
  width,height = pyautogui.size()
  x = width - 20
  y = 20

  # remember where the mouse is
  oldX,oldY = pyautogui.position()
  # move and click top right corner
  pyautogui.click(x,y)
  # move back to where the mouse was
  pyautogui.moveTo(oldX,oldY)

random.seed(time.time())
while True:
  # sleep between 5 and 10 minutes
  time.sleep(random.randint(300,600))

  # close the current open window
  click()
