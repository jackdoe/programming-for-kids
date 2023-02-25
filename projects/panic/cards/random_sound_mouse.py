# pip install pynput winsound
import random
import winsound
import pynput.mouse as m

def play_random_sound():
  freq = random.randint(100, 1000)
  # 100 milliseconds
  duration = 100
  winsound.Beep(freq, duration)

def on_move(x, y):
  # To make it more interesting, play a
  # sound only when the mouse is
  # positioned below a certain point on
  # the screen, for example the value of
  # 'y' is greater than 500.
  play_random_sound()

with m.Listener(on_move=on_move) as l:
  l.join()
