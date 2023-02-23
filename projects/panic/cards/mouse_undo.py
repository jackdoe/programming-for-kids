import pyautogui, threading, time
import pynput.mouse as m

# slowly move the mouse back on tracing
# the movement
history = []
last_move = 0
moving = False
def on_move(x, y):
  if not moving:
    global last_move
    last_move = time.time()
    history.append([x,y])
def undo():
  global history, moving
  while True:
    if time.time() - last_move > 5:
      h = history
      history = []
      h.reverse()
      moving = True
      for x,y in h:
        pyautogui.moveTo(x,y)
      moving = False
    time.sleep(1)

t = threading.Thread(target=undo)
t.start()
with m.Listener(on_move=on_move) as l:
  l.join()

