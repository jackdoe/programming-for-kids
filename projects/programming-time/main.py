from io import StringIO
import os
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time
import intro,easy,medium,hard

HEIGHT = 1039
WIDTH = 744
COLS = 37
ROWS = 27
fnt = ImageFont.truetype('font.ttf', 35)

fgcolor = (20, 20, 20, 255)
bgcolor = (0 , 0, 0, 0)

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def border(d, data, id):
    lines = []
    bottom = '+-----------------------------------+'
    top = '+--------------->' + str(id).zfill(3) + '<---------------+'
    if id == 0:
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
    d.rectangle([WIDTH-size, HEIGHT-size, WIDTH, HEIGHT], fill=help)
    d.rectangle([0, HEIGHT-size, size, HEIGHT], fill=help)
    d.rectangle([WIDTH-size, 0, WIDTH, size], fill=help)
    d.multiline_text((47, 24),"\n".join(lines), font=fnt, fill=fgcolor)


def back(deck, id, numbers):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    lines = []
    for n in numbers:
        lines.append(str(n).rjust(random.randint(0,COLS - 3), ' '))

    border(d, "\n".join(lines), 0)
      
    img.save(os.path.join('images', deck, 'back_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def front(deck, id, code):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, code, id)
    img.save(os.path.join('images', deck,'front_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def cheat(deck, answers, numbers):
    i = 0
    for (n, a) in enumerate(list(chunks(answers, ROWS))):
        img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
        d = ImageDraw.Draw(img)
        border(d, "\n".join(a), 0)
        img.save(os.path.join(
            'images', deck, 'front_card_answers_'+str(n).zfill(3)+'.tiff'), compression="tiff_lzw")
        i += 1
        back(deck, 0, numbers)
    return i


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





for (deck, cards) in [['easy', [*intro.cards, *easy.cards]],['medium',[*intro.cards,*medium.cards]], ['hard',[*intro.cards,*hard.cards]]]:
    path = os.path.join('images', deck)
    try:
        os.mkdir(path)
    except:
        pass
    print('printing', deck, 'deck, with',len(cards),'cards')
    seen = {}
    qa = []
    possible = set()
    for (_i, card) in enumerate(cards):
        if card in seen:
            raise Exception("ALREADY SEEN: " + card)
        seen[card] = True
        _out = run(card).strip().split("\n")
        if len(_out) == 0:
            raise "NO OUTPUT: " + card
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
        front(deck, i, card)
        back(deck, i, numbers)

    cheatsheet = cheat(deck, qa, numbers)

    a1 = 55
    print(deck, 'total number of cards:', cheatsheet + len(cards), 'cheatsheet:', cheatsheet, 'missing:', a1 -  (cheatsheet + len(cards)))
    print('*' * 40)