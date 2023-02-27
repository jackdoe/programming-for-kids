# pip install pywin32
import win32gui as g,win32api as a
import random
sym = "ｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕ"
sym += "日ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂ"
sym += "0123456789"

dc = g.GetDC(0)
font = g.LOGFONT()
font.lfFaceName = "Consolas"
fnt = g.CreateFontIndirect(font)
g.SelectObject(dc,fnt)
g.SetBkColor(dc, a.RGB(0,0,0))
colors=[
  a.RGB(0, 255, 65),
  a.RGB(0, 59, 0),
  a.RGB(0, 143, 17)
]
w = a.GetSystemMetrics(0)
h = a.GetSystemMetrics(1)
while True:
  x = random.randint(0,w)//10 * 10
  to = random.randint(0,h)
  for y in range(0,to,15):
    color = random.choice(colors)
    g.SetTextColor(dc, color)
    g.DrawText(dc, 
               random.choice(sym), 
               1,
               (x,y,x+20,y+30),0)
