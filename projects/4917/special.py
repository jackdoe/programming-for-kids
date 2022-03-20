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


def special(deck, name, text, fnt):
    img = Image.new('CMYK', (WIDTH, HEIGHT), color=bgcolor)
    d = ImageDraw.Draw(img)
    d.multiline_text((70, 55), text, font=fnt, fill=fgcolor)

    img.save(os.path.join('images', deck, name +'.tiff'), compression="tiff_lzw",dpi=(300,300))
    jpg = os.path.join('images', deck, name +'.jpg')
    img.save(jpg,dpi=(300,300))

intro = """

█████████████████████████████ scan
██ ▄▄▄▄▄ █▄▄▄ ▀█▄█ █ ▄▄▄▄▄ ██ for
██ █   █ ██▄▀ █  █▀█ █   █ ██ info
██ █▄▄▄█ ██▀▄ ▄█▀█ █ █▄▄▄█ ██ about
██▄▄▄▄▄▄▄█ ▀▄█ ▀ ▀▄█▄▄▄▄▄▄▄██ how
██▄▄█▄▄█▄▀▀▄▀█▄▀█ █▀▄▀▀▀▀▀▄██ the
██▀▀▄ ▀█▄▄ ▄██▄█  ▄█ █▄ ▀▀ ██ computer
██ ▀▄▄█▀▄▀ ▄ █▀▀▄▀ █▄█▀██▀▄██ works.
██ ▄▄▄▀▀▄▄  ▄█▀▄█ ▄▄█▀▄  ▄ ██ It
██▄███▄▄▄▄▀█▄ ▄▄ █ ▄▄▄ █  ███ is
██ ▄▄▄▄▄ ██▄▄▀▄▀██ █▄█ ███▄██ amazing
██ █   █ █ ▀▄▄▀ ▀▄   ▄▄██  ██ what
██ █▄▄▄█ █▀██ ▀ █ ▄ █▀ ▄   ██ you
██▄▄▄▄▄▄▄█▄██▄▄▄██▄████▄██▄██ can
█████████████████████████████ do!

license: CC BY 4.0
author:  https://github.com/jackdoe
webpage: https://punkx.org/4719
email:   b0000@fastmail.com

possible games:
  * random corruption
    roll dice to corrupt the memory
  * monkey patching
    modify one instruction in memory
  * hacking
    players take turns to HALt each
    other's computers
  * composition
    load new program mid-way as 
    registers keep their old value    

"""

hello = """                         
   

 0 HALT                (HLT)
 1 R0 = R0 + R1        (ADD)
 2 R0 = R0 - R1        (SUB)
 3 R0 = R0 + 1         (INC)
 4 R1 = R1 + 1         (INC)
 5 R0 = R0 - 1         (DEC)
 6 R1 = R1 - 1         (DEC)

 7 BEEP

 8 X PRINT X
  
 9 X R0 = RAM[X]       (LDR)
10 X R1 = RAM[X]       (LDR)
11 X RAM[X] = R0       (STR)
12 X RAM[X] = R1       (STR)
  
13 X JUMP X            (B)
14 X JUMP X IF R0 == 0 (BZ)
15 X JUMP X IF R0 != 0 (BNZ)
                       """
deck = 'deck'

special(deck, "back_card_000", hello, bigger)
special(deck, "front_card_000", intro, fnt)
    
