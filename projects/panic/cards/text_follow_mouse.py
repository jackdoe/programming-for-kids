# pip install pywin32
import random,time
import win32gui as g
import win32api as a
from ctypes import windll
from ctypes import wintypes
from ctypes import byref

dc = windll.user32.GetDC(0)
font = g.LOGFONT()
font.lfFaceName = "Consolas"
fnt = g.CreateFontIndirect(font)
g.SelectObject(dc,fnt)
g.SetBkColor(dc, a.RGB(0,0,0))

def get_cursor_pos():
  cursor = wintypes.POINT()
  r = byref(cursor)
  windll.user32.GetCursorPos(r)
  return (cursor.x, cursor.y)
text = "Hello?"
while True:
  (x,y) = get_cursor_pos()
  g.DrawText(dc, 
             text, 
             len(text), 
             (x,y,x+40,y+40),
             0)
  time.sleep(1)
  
