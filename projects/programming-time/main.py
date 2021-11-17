from io import StringIO
import os
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time
import easy,medium,hard

WIDTH = 1058
HEIGHT = 671
COLS = 33
ROWS = 28
fnt = ImageFont.truetype('font.ttf', 35)

fgcolor = (20, 20, 20, 255)
bgcolor = (0 , 0, 0, 0)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def border(d, difficulty, data, id):
    lines = []
    bottom = '+-------------------------------+'
    top = '+----------->' + str(id).zfill(2) + ' @ ' + \
        str(difficulty).zfill(2)+'<-----------+'
    if difficulty == 0:
        top = bottom
    lines.append(top)


    text = data.split('\n')
    for i in range(ROWS):
      code = ''
      if i <= len(text) -1:
        code = text[i]
      code = code.ljust(COLS - 3, ' ')
      lines.append('| '+code+'|')
    lines.append(bottom)

    help = (20, 20, 20, 20)
    size = 2
    d.rectangle([0, 0, size, size], fill=help)
    d.rectangle([HEIGHT-size, WIDTH-size, HEIGHT, WIDTH], fill=help)
    d.rectangle([0, WIDTH-size, size, WIDTH], fill=help)
    d.rectangle([HEIGHT-size, 0, HEIGHT, size], fill=help)
    d.multiline_text((45, 18),"\n".join(lines), font=fnt, fill=fgcolor)


def back(id, difficulty, numbers):
    img = Image.new('CMYK', (HEIGHT, WIDTH), color=bgcolor)
    d = ImageDraw.Draw(img)
    lines = []
    for n in numbers:
        lines.append(str(n).rjust(random.randint(0,COLS - 3), ' '))

    border(d, 0, "\n".join(lines), 0)
      
    img.save(os.path.join('images', 'back_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def front(id, difficulty, code):
    img = Image.new('CMYK', (HEIGHT, WIDTH), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, difficulty, code, id)
    img.save(os.path.join('images', 'front_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def cheat(answers, numbers):
    for (n, a) in enumerate(list(chunks(answers, ROWS))):
        img = Image.new('CMYK', (HEIGHT, WIDTH), color=bgcolor)
        d = ImageDraw.Draw(img)
        border(d, 0, "\n".join(a), 0)
        img.save(os.path.join(
            'images', 'front_card_answers_'+str(n).zfill(3)+'.tiff'), compression="tiff_lzw")

        back(800 + n, 0, numbers)


def run(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code, globals())
    except Exception as e:
        old_stdout.write("error " + str(e) + ", code:" + code)
        raise(e)

    sys.stdout = old_stdout
    return redirected_output.getvalue()



cards = [*easy.cards,*medium.cards, *hard.cards]


print('easy',len(easy.cards))
print('medium',len(medium.cards))
print('hard',len(hard.cards))
print('total',len(cards))

cards.sort(key=lambda x:x[0])
seen = {}
qa = []
possible = set()
for (_i, card) in enumerate(cards):
    if card[1] in seen:
      raise Exception("ALREADY SEEN: " + str(card[0]) + " -> " + card[1])
    seen[card[1]] = True
    _out = run(card[1]).strip().split("\n")
    if len(_out) == 0:
        raise "NO OUTPUT: " + card[1]
    for line in _out:
        possible.add(line)
        qa.append(str(_i).zfill(3) + ": " + line)


random.seed(time.time())
shuffled = list(possible)
print('possible results', len(possible), 'rows', ROWS)

for (i, card) in enumerate(cards):
    random.shuffle(shuffled)
    rotate = cycle(shuffled)
    numbers = []
    for x in range(ROWS):
        numbers.append(next(rotate))
    front(i, card[0], card[1])
    back(i, card[0], numbers)

cheat(qa, numbers)
