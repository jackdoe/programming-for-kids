# EPILEPSY WARNING
# pip install pywin32
import random
import win32gui as g

# flood the screen with the text
# 'Hello?'

dc = g.GetDC(0)
text = "Hello?"

while True:
  x = random.randint(0, 6000)
  y = random.randint(0, 6000)
  g.DrawText(dc, 
             text, 
             len(text), 
             (x,y,x+100,y+100),
             0)
  
