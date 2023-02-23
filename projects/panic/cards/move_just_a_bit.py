# pip install pyautogui
import pyautogui
import random
import time

def move():
  x,y = pyautogui.position()

  # move the mouse just a bit
  # random 5 pixels off from its
  # current position
  
  x += random.randint(-10,10)
  y += random.randint(-10,10)
  
  pyautogui.moveTo(x,y,duration=0.4)

while True:
  move()

  # sleep between 5 and 10 seconds
  time.sleep(random.randint(5,10))


