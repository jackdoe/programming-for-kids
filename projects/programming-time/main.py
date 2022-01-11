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
COLS = 39
ROWS = 31
fnt = ImageFont.truetype('dejavu-sans-mono.book.ttf', 28)

fgcolor = (20, 20, 20, 255)
dice_color = (20, 255, 160, 50)
#cmyk(0%, 99%, 67%, 22%)
border_color = (0, 0, 0, 100)
bgcolor = (0, 0, 0, 0)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

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

def ignore_the_comment(line, sym):
    in_comment = False
    out = ''
    for (i,s) in enumerate(line):
        if line[i:i+len(sym)] == sym:
            in_comment = True
        if in_comment:
            out += ' '
        else:
            out += s
    return out


def border(d, data, id):
    lines = []
    bottom = "'--------------------------------------'"
    top = '.-------------->  ' + str(id).zfill(3) + '  <---------------.'
    if id == -1:
        top = '.--------------------------------------.'
    around = []
    dice = []
    around.append(top)
    dice.append('')
    lines.append('')

    text = data.split('\n')
    if text[len(text)-1] == "":
        text.pop()
    if len(text) > ROWS:
        raise Exception(str(id) + "'s text has too many rows" + data)

    sym = '#'
    if '#include' in data:
      sym = '//'

    for i in range(ROWS):
        code = ''
        if i <= len(text) - 1:
            code = text[i]
        dice_line = re.sub('[^⚂]',' ',code)
        code = code.replace('⚂', ' ')

        lines.append('  '+ignore_the_comment(code,sym).ljust(COLS - 3, ' ')+' ')
        comment = ''
        if '#' in code or '//' in code:
            comment = ignore_until_comment(code,sym)

        around.append('| ' + comment.ljust(COLS - 3, ' ') + ' |')
        dice.append('  ' + dice_line.ljust(COLS - 3, ' ') + '  ')

    lines.append('')
    dice.append('')
    around.append(bottom)

#    help = (20, 20, 20, 20)
#    size = 2
#    d.rectangle([0, 0, size, size], fill=help)
#    d.rectangle([WIDTH-size, HEIGHT-size, WIDTH, HEIGHT], fill=help)
#    d.rectangle([0, HEIGHT-size, size, HEIGHT], fill=help)
#    d.rectangle([WIDTH-size, 0, WIDTH, size], fill=help)


    d.multiline_text((36, 20), "\n".join(lines), font=fnt, fill=fgcolor)
    d.multiline_text((36, 20), "\n".join(around), font=fnt, fill=border_color)
    d.multiline_text((36, 20), "\n".join(dice), font=fnt, fill=dice_color)

def back(deck, id, numbers, html):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, "\n".join(numbers), -1)

    img.save(os.path.join('images', deck, 'back_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")
    jpg = os.path.join('images', deck, 'back_card_' +
             str(id).zfill(3)+'.jpg')
    img.save(jpg)
    html.write('<img width="25%" src="' + jpg + '">')


def front(deck, id, code,html):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, code, id)
    img.save(os.path.join('images', deck, 'front_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")
    jpg = os.path.join('images', deck, 'front_card_' +
             str(id).zfill(3)+'.jpg')
    img.save(jpg)
    html.write('<img width="25%" src="' + jpg + '">')
    if int(id+1) % 4 == 0:
      html.write('<br>')

def cheat(deck, answers, numbers, html):
    i = 0
    for (n, a) in enumerate(list(chunks(answers, ROWS))):
        img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
        d = ImageDraw.Draw(img)
        border(d, "\n".join(a), -1)
        img.save(os.path.join(
            'images', deck, 'front_card_answers_'+str(n).zfill(3)+'.tiff'), compression="tiff_lzw")
        jpg = os.path.join(
            'images', deck, 'front_card_answers_'+str(n).zfill(3)+'.jpg')
        img.save(jpg)
        i += 1
        html.write('<img width="25%" src="' + jpg + '">')
    return i


def run(file):

  if file.endswith(".c"):
    tmpfile = "/tmp/card.c"
    fo = open(tmpfile, "w")
    fi = open(file)
    fo.write("""
    #include <stdlib.h>
    #include <time.h>
    int get_dice(void) {
      srand((int)time(NULL));
      return 1 + (rand() % 20);
    }
  """)
    for line in fi.readlines():
      fo.write(line.replace('⚂',"get_dice()"))
    fi.close()
    fo.close()
    process = Popen(["./compile.sh", tmpfile], stdout=PIPE)
  else:
    tmpfile = "/tmp/card.py"
    fo = open(tmpfile, "w")
    fi = open(file)
    fo.write("""
import random as __random
def get_dice():
  return __random.randint(1,20)

""")
    for line in fi.readlines():
      fo.write(line.replace('⚂',"get_dice()"))
    fi.close()
    fo.close()
    process = Popen(["/usr/local/bin/python3", tmpfile], stdout=PIPE)

  (output, err) = process.communicate()
  exit_code = process.wait()
  if exit_code != 0:
    raise Exception(file + " exitted with " + str(exit_code))
  return output

random.seed(time.time())
for deck in ['c','easy']:
    html = open(deck + '.html','w')
    try:
        images_path = os.path.join('images', deck)
        os.mkdir(images_path)
    except:
        pass
    files = [f for f in os.listdir(os.path.join('decks', deck)) if f.endswith(".py") or f.endswith('.c')]
    files.sort()
    print('printing', deck, 'deck, with', len(files), 'cards')
    seen = {}
    qa = []
    for (i, file) in enumerate(files):
        fp = os.path.join("decks", deck, file)
        f = open(fp, "r")
        text = f.read()
        f.close()
        if text in seen:
            raise Exception("ALREADY SEEN: " + text)
        seen[text] = True
        _out = run(fp).decode().strip().split("\n")
        print('-' * 40)
        print(file, '\n' + "\n".join(_out))
        print('-' * 40)
        if len(_out) == 0:
            raise "NO OUTPUT: " + file
        for line in _out:
            qa.append(str(i).zfill(3) + ": " + line)

        front(deck, i, text, html)

    hello = []
    message = '        print("Hello World!")'
    for i in range(ROWS):
      hello.append(message)
    back(deck, 0, hello, html)
    a1 = 55
    print(deck, 'total number of cards:', len(files), 'missing:', a1 - (len(files)))
    print('*' * 40)
    html.close()
