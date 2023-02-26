# pip install pynput winsound
import random
import winsound
import pynput.mouse as m
from threading import Thread

PLAYING = False
def play_random_sound():
  global PLAYING
  PLAYING = True
  freq = random.randint(100, 1000)
  # 100 milliseconds
  duration = 100
  winsound.Beep(freq, duration)
  PLAYING = False

def on_move(x, y):
  if PLAYING:
    return

  t = Thread(target=play_random_sound)
  t.start()

with m.Listener(on_move=on_move) as l:
  l.join()
