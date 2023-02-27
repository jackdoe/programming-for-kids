# EPILEPSY WARNING
# fill the screen with random pixels
import random
from ctypes import windll

# get the width and height

w = windll.user32.GetSystemMetrics(0)
h = windll.user32.GetSystemMetrics(1)

dc = windll.user32.GetDC(None)

# red
color = 0x000000FF

# draw pixels forever
while True:
  x = random.randint(0,w)
  y = random.randint(0,h)
  windll.gdi32.SetPixel(dc, x, y, color)

windll.user32.ReleaseDC(None, dc)
