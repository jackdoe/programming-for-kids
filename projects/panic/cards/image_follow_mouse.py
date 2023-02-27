# EPILEPSY WARNING
# pip install pywin32
import win32gui
from PIL import Image, ImageWin
import pynput.mouse as m

# put any png image at c:\ and this card
# will draw it always following the
# mouse pointer

img = Image.open("c:\\image.png")
w,h = img.size
dib = ImageWin.Dib(img)

hdc = win32gui.GetDC(0)

def on_move(x, y):
  # you can use random.randint
  # here to make it move around
  # the cursor to be more funny
  dib.draw(hdc,(x,y,x+w,y+h))

with m.Listener(on_move=on_move) as l:
  l.join()
