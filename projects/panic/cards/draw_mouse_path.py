# pip install pynput
import pynput.mouse as m
from ctypes import windll
import random

# draw a red line following the mouse

dc = windll.user32.GetDC(None)
def draw(points):
  # red color
  c = 0x000000FF
  for [x,y] in points:
    windll.gdi32.SetPixel(dc, x, y, c)
    
history = []
def on_move(x, y):
  global history
  history.append([x,y])
  if len(history) > 500:
    # pick 100 random points
    s = random.choices(history, k=100)
    history = s
  draw(history)

with m.Listener(on_move=on_move) as l:
  l.join()
