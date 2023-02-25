# pip install pynput winsound
import winsound
import pynput.keyboard as k


# play different on every character

def on_press(key):
  try:
    freq =  ord(key.char) * 100
    duration = 100
    winsound.Beep(freq, duration)
  except AttributeError:
    pass

with k.Listener(on_press=on_press) as l:
  l.join()
