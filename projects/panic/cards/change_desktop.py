import os,random,time
from ctypes import windll as w

# every second change the desktop

images = []
# put some scary images in c:\images
for f in os.listdir("c:\\images"):
  if f.endswitdh('.jpg'):
    images.append(f)

SPI_SETDESKWALLPAPER = 20
while True:
  w.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER,
    0,
    random.choice(images),
    0
  )
  time.sleep(1)
