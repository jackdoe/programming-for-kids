# EPILEPSY WARNING
import os,random,time
from ctypes import windll as w

# every second change the desktop with
# the images in c:\images
dir = "c:\\images"
images = []
for f in os.listdir(dir):
  if f.endswith('.png'):
    p = os.path.join(dir,f)
    images.append(p)

SPI_SETDESKWALLPAPER = 20
while True:
  w.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    random.choice(images),
    0
  )
  time.sleep(1)
