# pip install pynput winsound
import winsound
import pynput.keyboard as k
from threading import Thread

# play different on every character key

PLAYING = False
def snd(freq):
  global PLAYING
  PLAYING = True
  # 100 milliseconds
  winsound.Beep(freq, 100)
  PLAYING = False

def on_press(key):
  if PLAYING:
    return
  try:
    if key.char:
      freq = ord(key.char) * 97
      freq = 100 + (freq % 3000)
      t = Thread(target=snd,args=(freq,))
      t.start()
  except:
    pass

with k.Listener(on_press=on_press) as l:
  l.join()
