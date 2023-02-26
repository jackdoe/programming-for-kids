# pip install pywin32
import win32gui, time, random
from PIL import Image, ImageWin

def wait_for_app_change():
  prev = None
  while True:
   cur = win32gui.GetForegroundWindow()
   if prev and cur != prev:
     return True
   prev = cur
   time.sleep(0.01)

def show_image(name):
  # put a scary image in c:\image.png
  img = Image.open(name)
  w,h = img.size
  dib = ImageWin.Dib(img)
  hdc = win32gui.GetDC(0)
  x = 200
  y = 200
  dib.draw(hdc,(x,y,x+w,y+h))

# wait 10 minutes after the program start
time.sleep(10 * 60)
# wait for the first app change
# so you know the user is active
wait_for_app_change()
time.sleep(random.randint(1000,100))
show_image("c:\\image.png")
