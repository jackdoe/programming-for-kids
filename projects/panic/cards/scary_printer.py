# pip install win32printing
from win32printing import Printer

# print each word in huge letters on its
# own page

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

scary("I am alive Who Am I")
