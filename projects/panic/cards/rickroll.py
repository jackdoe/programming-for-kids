# pip install pyautogui win32gui
import pyautogui as p
import random
import time

# no prank is complete without a
# rickroll.

# open chrome with rickroll every 30 to
# 60 seconds

while True:
  # sleep between 30 and 60 seconds
  time.sleep(random.randint(30,60))

  p.hotkey('win','r')
  time.sleep(0.5)

  p.typewrite('chrome ')
  p.typewrite('https://www.youtube.com/')
  p.typewrite('watch?v=dQw4w9WgXcQ')
  p.hotkey('enter')

    
