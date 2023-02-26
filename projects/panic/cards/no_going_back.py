# pip install pynput pywin32
from pynput import keyboard
import win32gui
# while minecraft is focused, disable
# the S key, so you cant go back

def is_foreground(name):
  w = win32gui.GetForegroundWindow()
  title = win32gui.GetWindowText(w)
  if name in title:
    return True
  return False

listener = None
def filter(msg,data):
  # 0x53 is S's virtual code on windows
  if is_foreground("Minecraft"):
    if data.vkCode == 0x53:
      listener.suppress_event()
def on_press(key):
  pass
def on_release(key):
  pass

listener = keyboard.Listener(
  win32_event_filter=filter,
  on_press=on_press,
  on_release=on_release)
listener.start()
listener.join()
