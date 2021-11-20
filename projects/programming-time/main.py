from subprocess import Popen, PIPE
from io import StringIO
import os
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time

HEIGHT = 1039
WIDTH = 744
COLS = 37
ROWS = 27
fnt = ImageFont.truetype('font.ttf', 35)

fgcolor = (20, 20, 20, 255)
bgcolor = (0, 0, 0, 0)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def border(d, data, id):
    lines = []
    bottom = "'-----------------------------------'"
    top = '.------------->  ' + str(id).zfill(3) + '  <-------------.'
    if id == 0:
        top = '.-----------------------------------.'
    lines.append(top)

    text = data.split('\n')
    if text[len(text)-1] == "":
        text.pop()
    if len(text) > ROWS:
        raise Exception(str(id) + "'s text has too many rows" + data)

    for i in range(ROWS):
        code = ''
        if i <= len(text) - 1:
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
    d.multiline_text((47, 24), "\n".join(lines), font=fnt, fill=fgcolor)


def back(deck, id, numbers):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    lines = []
    for n in numbers:
        lines.append(str(n).rjust(random.randint(0, COLS - 3), ' '))

    border(d, "\n".join(lines), 0)

    img.save(os.path.join('images', deck, 'back_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def front(deck, id, code):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, code, id)
    img.save(os.path.join('images', deck, 'front_card_' +
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


def run(file):
    process = Popen(["/usr/local/bin/python3", file], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    if exit_code != 0:
        raise Exception(file + " exitted with " + str(exit_code))
    return output


for deck in ['easy', 'medium', 'hardcore']:
    try:
        images_path = os.path.join('images', deck)
        os.mkdir(images_path)
    except:
        pass
    files = [f for f in os.listdir(os.path.join('decks', deck)) if f.endswith(".py")]
    files.sort()
    print('printing', deck, 'deck, with', len(files), 'cards')
    seen = {}
    qa = []
    possible = set()
    for (i, file) in enumerate(files):
        fp = os.path.join("decks", deck, file)
        f = open(fp, "r")
        text = f.read()
        f.close()
        if text in seen:
            raise Exception("ALREADY SEEN: " + text)
        seen[text] = True
        _out = run(fp).decode().strip().split("\n")
        if len(_out) == 0:
            raise "NO OUTPUT: " + file
        for line in _out:
            possible.add(line)
            qa.append(str(i).zfill(3) + ": " + line)
    
        front(deck, i, text)

    random.seed(time.time())
    shuffled = list(possible)
    print('possible results', len(possible), 'rows', ROWS)
    random.shuffle(shuffled)

    if len(shuffled) > ROWS:
        raise Exception(str(len(shuffled)) + ">" + str(ROWS))
    back(deck, 0, shuffled)

    cheatsheet = cheat(deck, qa, shuffled)

    a1 = 55
    print(deck, 'total number of cards:', cheatsheet + len(files),
          'cheatsheet:', cheatsheet, 'missing:', a1 - (cheatsheet + len(files)))
    print('*' * 40)
