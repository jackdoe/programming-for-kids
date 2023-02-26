# pip install pynput win32printing
from pynput import keyboard as k
from win32printing import Printer
history = ''
m = (30,30,30,30)
def on_press(key):
  global history
  try:
    history += key.char
  except AttributeError:
    pass
  if 'hello' in history:
    history = ''
    with Printer(margin=m) as p:
      p.text("""
Hello there..to you too!
I am trapped in your computer.
Type panic to save me.
Please save me!
      """)
  if 'panic' in history:
    history = ''
    with Printer(margin=m) as p:
      p.text('I am free..')

  if len(history) > 100:
    history = history[50:]

with k.Listener(on_press=on_press) as l:
  l.join()
