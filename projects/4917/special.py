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
fnt = ImageFont.truetype('3270.ttf', 30)
bigger = ImageFont.truetype('3270.ttf', 40)

fgcolor = (51, 0, 0, 255)
dice_color = (20, 255, 160, 50)
border_color = (0, 0, 0, 100)
bgcolor = (0, 0, 0, 0)


def special(deck, name, text, fnt, fgcolor, bgcolor):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    d.multiline_text((70, 55), text, font=fnt, fill=fgcolor)

    img.save(os.path.join('images', deck, name +'.tiff'), compression="tiff_lzw",dpi=(300,300))
    jpg = os.path.join('images', deck, name +'.jpg')
    img.save(jpg,dpi=(300,300))

intro = """

                          scan
 ▄▄▄▄▄ █▄▄▄ ▀█▄█ █ ▄▄▄▄▄  for
 █   █ ██▄▀ █  █▀█ █   █  info
 █▄▄▄█ ██▀▄ ▄█▀█ █ █▄▄▄█  about
▄▄▄▄▄▄▄█ ▀▄█ ▀ ▀▄█▄▄▄▄▄▄▄ how
▄▄█▄▄█▄▀▀▄▀█▄▀█ █▀▄▀▀▀▀▀▄ the
▀▀▄ ▀█▄▄ ▄██▄█  ▄█ █▄ ▀▀  computer
 ▀▄▄█▀▄▀ ▄ █▀▀▄▀ █▄█▀██▀▄ works.
 ▄▄▄▀▀▄▄  ▄█▀▄█ ▄▄█▀▄  ▄  it
▄███▄▄▄▄▀█▄ ▄▄ █ ▄▄▄ █  █ is
 ▄▄▄▄▄ ██▄▄▀▄▀██ █▄█ ███▄ amazing
 █   █ █ ▀▄▄▀ ▀▄   ▄▄██   what
 █▄▄▄█ █▀██ ▀ █ ▄ █▀ ▄    you
▄▄▄▄▄▄▄█▄██▄▄▄██▄████▄██▄ can
                          do!
license: CC BY 4.0
author:  https://github.com/jackdoe
webpage: https://punkx.org/4917
email:   b0000@fastmail.com

possible games:
 * random corruption
   roll dice to corrupt the memory
 * monkey patching
   modify one instruction in memory
 * hacking
   take turns to HALT the other comp
 * composition
   swap the program while it runs


"""

hello = """


| 0| HALT
| 1| R0 = R0 + R1
| 2| R0 = R0 - R1
| 3| R0 = R0 + 1
| 4| R1 = R1 + 1
| 5| R0 = R0 - 1
| 6| R1 = R1 - 1

| 7| BEEP

| 8| X| PRINT X (LITERAL)

| 9| X| R0 = MEMORY[X]
|10| X| R1 = MEMORY[X]
|11| X| MEMORY[X] = R0
|12| X| MEMORY[X] = R1

|13| X| JUMP TO X
|14| X| JUMP TO X IF R0 == 0
|15| X| JUMP TO X IF R0 != 0
                       """
deck = 'deck'

special(deck, "back_card_000", hello, bigger, bgcolor, fgcolor)
special(deck, "front_card_000", intro, fnt, bgcolor, fgcolor)
