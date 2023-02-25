# pip install pynput win32printing
from win32printing import Printer
import time

def scary(message):
  m = (50,50,50,50)
  font = {
    "height": 80,
    "faceName":'Consolas',
  }
  words = message.split(" ")
  with Printer(margin=m) as p:
    for word in words:
      p.text(word,
             font_config=font,
             align='center')
      p.new_page()

while True:
  scary("I am alive Who Am I")
  time.sleep(300,600)
