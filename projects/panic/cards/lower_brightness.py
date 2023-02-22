# pip install screen_brightness_control
from screen_brightness_control import *

# start from 100% brightness and every
# 10 seconds lower it with 5%
brightness = 100

# lower it down to 5%, if you want to
# go completely dark, use 0%
while brightness > 5:
  # work only with the primary display
  # remove display=0 if you want to
  # change it on all displays
  set_brightness(brightness,display=0)

  # lower it with 5%
  brightness -= 5
  time.sleep(10)

