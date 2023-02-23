# pip install pyautogui win32gui
import pyautogui, random, time
import win32gui, sys

def is_foreground(name):
  w = win32gui.GetForegroundWindow()
  title = win32gui.GetWindowText(w)
  if name in title:
    return True
  return False
# use the start_at_login() card
# def start_at_login():
#  ...
# if not start_after_login():
#   sys.exit(0) # exit the first time

# this card is small, but particularly
# evil, especially if someone is playing
# a game where you can fall, or jump in
# lava.. like Minecraft
while True:
  # sleep between 5 and 10 minutes
  # change those numbers to make the
  # sleep shorter
  time.sleep(random.randint(300,600))

  # only press W if Minecraft is
  # the current active window
  if is_foreground("Minecraft"):
    # press W for 1 second
    with pyautogui.hold('w'):
      pyautogui.sleep(1)

