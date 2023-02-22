# pip install pyautogui
import pyautogui
import random
import time

# as the mouse moves we keep bringing it
# back to where it was, and from time to
# time we allow it to move forward
x,y = pyautogui.position()
while True:
  # from time to time remember new
  # position
  if random.randint(0,3) == 0:
    x,y = pyautogui.position()

  # go back to where it was
  pyautogui.moveTo(x,y)

  # sleep 10 milliseconds
  time.sleep(0.01)


