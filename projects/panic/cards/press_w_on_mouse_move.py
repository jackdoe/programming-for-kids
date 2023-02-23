import pynput.mouse as m
import pynput.keyboard as k

# press w while the mouse is moving
# its good to combine this with
# is_foreground() to run only while some
# game is active

kbd = k.Controller()

key = k.KeyCode.from_char('w')
def on_move(x, y):
  # while the mouse is moving
  # we keep pressing w
  kbd.press(key)
  kbd.release(key)

def on_click(x, y, button, pressed):
  pass

def on_scroll(x, y, dx, dy):
  pass

with m.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as l:
    l.join()

