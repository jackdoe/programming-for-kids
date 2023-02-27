# EPILEPSY WARNING
# pip install tkinter pywin32
from tkinter import *
import win32api as a
from threading import Thread
import random

# create bazillion windows with
# different sizes

sw = a.GetSystemMetrics(0)
sh = a.GetSystemMetrics(1)

def win():
  b = Tk()
  b.title("HELLO")
  w = random.randint(100, sw)
  h = random.randint(100, sh)
  b.configure(width=w, height=h)
  b.configure(bg='lightgray')
  b.mainloop()

threads = []
while True:
  t = Thread(target=win)
  t.start()
  threads.append(t)
