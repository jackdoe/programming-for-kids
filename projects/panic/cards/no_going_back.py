# pip install pynput
from pynput import keyboard

# this card ignores the 'S' key
# so in video games you cant go
# backwards

listener = None

def filter(msg,data):
  # 0x53 is S's virtual code
  # on windows
  if data.vkCode == 0x53:
    listener.suppress_event()

def on_press(key):
  pass

def on_release(key):
  pass

listener = keyboard.Listener(
  win32_event_filter=filter,
  supress=False,
  on_press=on_press,
  on_release=on_release)
listener.start()
listener.join()
