from subprocess import Popen, PIPE
from io import StringIO
import os
import random
import sys
import re
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time

HEIGHT = 1039
WIDTH = 744
COLS = 20
ROWS = 31
fnt = ImageFont.truetype('3270.ttf', 54)
tiny = ImageFont.truetype('3270.ttf', 20)

fgcolor = (51, 0, 0, 255)
dice_color = (20, 255, 160, 50)
border_color = (0, 0, 0, 100)
bgcolor = (0, 0, 0, 0)
def ignore_until_comment(line, sym):
    ignore = True
    out = ''
    for (i,s) in enumerate(line):
        if line[i:i+len(sym)] == sym:
            ignore = False
        if not ignore:
            out += s
        else:
            out += ' '
    return out
def border(d, data, id):
    lines = []
    lines.append('')
    bottom = "'--------------------------------------'"
    top = '       ' + str(id).zfill(2) + '.prg    '

    if id == -1:
        top = ''
    around = []
    around.append(top)
    text = ['']
    for t in  data.split('\n'):
        if '#' not in t:
            text.append(t)

    if text[len(text)-1] == "":
        text.pop()

    for i in range(ROWS):
        code = ''
        if i <= len(text) - 1:
            code = text[i]

        if id == -1:
          lines.append(code)
        else:
          numbers = re.sub('(R0|R1)','  ',code)
          numbers = re.sub('[^\d]',' ',numbers)

          borders = re.sub('(\s\d\d)','   ',code)
          borders = re.sub('(\s\d)','  ',borders)

#        borders = re.sub('(┌|┬|┴|┐|┘|└)', '+', borders)

          borders = re.sub('(┌|┐)', ".", borders)
          borders = re.sub('(┘|└)', "'", borders)

          borders = re.sub('(─|┴|┬)', '-', borders)
          borders = re.sub('(┼)', '+', borders)
          borders = re.sub('(│|┤|├)', '|', borders)
          around.append(borders)
          lines.append(numbers)

    lines.append('')

    d.multiline_text((70, 55), "\n".join(lines), font=fnt, fill=fgcolor)
    d.multiline_text((70, 55), "\n".join(around), font=fnt, fill=border_color)

def back(deck, id, numbers, html):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, "\n".join(numbers), -1)

    img.save(os.path.join('images', deck, 'back_card_' +
                          str(id).zfill(3)+'.tiff'), compression="tiff_lzw",dpi=(300,300))
    jpg = os.path.join('images', deck, 'back_card_' +
             str(id).zfill(3)+'.jpg')
    img.save(jpg,dpi=(300,300))
    html.write('<img width="25%" src="' + jpg + '">')


def front(deck, id, code,html):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, code, id)
    img.save(os.path.join('images', deck, 'front_card_' +
                          str(id).zfill(3)+'.tiff'), compression="tiff_lzw", dpi=(300,300))
    jpg = os.path.join('images', deck, 'front_card_' +
             str(id).zfill(3)+'.jpg')
    img.save(jpg, dpi=(300,300))
    html.write('<img width="25%" src="' + jpg + '">')
    if int(id+1) % 4 == 0:
      html.write('<br>')


for deck in ['deck']:
    html = open(deck + '.html','w')
    try:
        images_path = os.path.join('images', deck)
        os.mkdir(images_path)
    except:
        pass
    files = [f for f in os.listdir(os.path.join(deck)) if f.endswith(".prg")]
    files.sort()
    print('printing', deck, 'deck, with', len(files), 'cards')
    seen = {}
    qa = []
    for (i, file) in enumerate(files):
        fp = os.path.join(deck, file)
        f = open(fp, "r")
        text = f.read()
        f.close()
        if text in seen:
            raise Exception("ALREADY SEEN: " + text)
        seen[text] = True

        front(deck, i, text, html)

    hello = """.........................
.........................
..0.halt.................
..1.R0.+=.R1.2.R0.-=.R1..
..3.R0.+=.1..4.R1.+=.1...
..5.R0.-=.1..6.R1.-=.1...
..7.beep.................
.8X.print.X..............
.9X.R0.=.mem[X]..........
10X.R1.=.mem[X]..........
11X.mem[X].=.R0..........
12X.mem[X].=.R1..........
13X.jump.to.address.X....
14X.jump.to.address.X....
...........if.R0.==.0....
15X.jump.to.address.X....
...........if.R0.!=.0....
.........................
.........................""".split('\n')

    back(deck, 0, hello, html)
    a1 = 55
    print(deck, 'total number of cards:', len(files), 'missing:', a1 - (len(files)))
    print('*' * 40)
    html.close()
