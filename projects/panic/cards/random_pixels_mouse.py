# draw random pixels around the mouse
import random
import time
from ctypes import windll
from ctypes import wintypes
from ctypes import byref

dc = windll.user32.GetDC(None)

def get_cursor_pos():
  cursor = wintypes.POINT()
  r = byref(cursor)
  windll.user32.GetCursorPos(r)
  return (cursor.x, cursor.y)
  
# red
color = 0x000000FF

while True:
  x,y = get_cursor_pos()
  x += random.randint(-20,20)
  y += random.randint(-20,20)

  windll.gdi32.SetPixel(dc, x, y, color)

  time.sleep(0.1)

windll.user32.ReleaseDC(None, dc)
