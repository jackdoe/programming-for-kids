from os import listdir
from itertools import cycle
CARD = 1
#color = '#ffb000' # amber
#color = '#33ff33' # green

font='BlockZone'
fontSize='25px'

color = '#ffcc00' # amber apple2
bgcolor = 'black'
theme='punko'

color = 'black'
bgcolor = 'white'
theme = 'vim'

#color = '#39FF14' 
#bgcolor = '#000000'
#theme='punk0'
#font='BlockZone'
#fontSize='25px'
#

def card_str(x):
  global CARD
  print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:::")
  CARD+=1
  print(x)
  print()

    
card_str(f"""{'BIN111'.center(40)}

Welcome to BIN111 game.

A game of using and abusing integers in
programming.

Each card has one of the following
functions:

  AND, OR, XOR, NOT
  INC, DEC 
  POPCOUNT 
  SHIFT
  ZERO

Starting from the number 1 the goal 
is to get to 7.

+ start with 5 cards each

+ each player decides to draw or play

+ if you play, you apply function to the
  previous card's output and compuite
  the new value with your card

+ whoever gets first to the number 7
  wins the game

""")

card_str(f"""{'BINARY'.center(40)}

In the binary system, each digit
represents a power of 2, starting from
the rightmost bit (also known as the
least significant bit) which represents
2^0, and going to the left each bit
represents the next power of 2.

Converting binary number to decimal:

The number: 01001011

  0   1   0   0  1  0  1  1
128  64  32  16  8  4  2  1 

you just sum the bits that are ON (with
value 1) and ignore the ones that are
OFF (with value 0):
64 + 8 + 2 + 1 = 75

To convert from decimal to binary use
the same approach, you have to represent
the number as a sum of 128, 64, 32, 16,
8, 4, 2 and 1. For example the number 72
is 64 + 8, or 01001000.

Leading zeroes are ignored, same as 099
in decimal is just 99, 00000111 is just
111.

""")

card_str(f"""{'BINARY'.center(40)}

All the cards in the game take and
return the type uint8_t, which means:
unsigned integer with 8 bits (1 byte).

So we have 8 bits to work with
binary   decimal number
00000000  0
00000001  1
00000010  2
00000011  3
00000100  4
00000101  5

The smallest number we can represent is
0, where all the bits are 0, and the
largest one is 255(all 8 bits set to 1).

If we were using uint64_t then we would
have 64 bits(8 bytes) to work with,
smallest number is 0 and the largest is
9223372036854775807 (all 64 bits set to
1).

If you need to work with negative
numbers then you need a signed integer,
int8_t is again 8 bits, but one bit is
used for the sign, if its - or not, so
the smallest number you can have is -128
and the largest is 127.
""")

listed = listdir('./code')
listed = [x for x in listed if x.endswith('.c') and '#' not in x]
starting = cycle(list(listed))

for i in range(CARD+len(listed), 56):
    listed.append(next(starting))
listed.sort()

for fn in listed:
    if '#' in fn:
        continue

    if not '.' in fn:
        continue

    lang = ''
    if fn.endswith('.c'):
        lang = 'c'
    if fn.endswith('.js'):
        lang = "javascript"
    if fn.endswith('.go'):
        lang = "go"
    if fn.endswith('.py'):
        lang = 'python'

    if lang ==  '':
      continue

    typL = 'INC'
    typR = 'INC'
    color = ''

    color = 'black'
    bgcolor = 'white'
    theme = ''

    themes = {
        "gpt1": {"Background": "#F7FAFF", "Keyword": "#123456", "Unknown": "#4F4F4F", "Number": "#467C98", "String": "#215973", "Comment": "#B20000"},
        "gpt2": {"Background": "#FFF5E6", "Keyword": "#854331", "Unknown": "#494949", "Number": "#714F4A", "String": "#5E4C40", "Comment": "#B20000"},
        "gpt3": {"Background": "#E8F5E6", "Keyword": "#2D6F38", "Unknown": "#545454", "Number": "#6B9C36", "String": "#4DA759", "Comment": "#B20000"},
        "gpt4": {"Background": "#FFFFFF", "Keyword": "#000000", "Unknown": "#5A5A5A", "Number": "#000000", "String": "#000000", "Comment": "#B20000"},
        "gpt5": {"Background": "#FEE6CE", "Keyword": "#933201", "Unknown": "#4C4C4C", "Number": "#CC5C00", "String": "#933201", "Comment": "#B20000"},
        "gpt6": {"Background": "#FAF9FC", "Keyword": "#A167A9", "Unknown": "#747474", "Number": "#C275A2", "String": "#C682C2", "Comment": "#B20000"},
        "gpt7": {"Background": "#E0F7FA", "Keyword": "#006770", "Unknown": "#3D646D", "Number": "#1FA4B8", "String": "#008FA3", "Comment": "#B20000"},
        "gpt8": {"Background": "#FFF9F0", "Keyword": "#5C2D0F", "Unknown": "#4A433A", "Number": "#684B47", "String": "#6F563F", "Comment": "#B20000"},
        "gpt9": {"Background": "#E8F5E9", "Keyword": "#195922", "Unknown": "#2E2E2E", "Number": "#2D8038", "String": "#4AA859", "Comment": "#B20000"},
        "gpt10": {"Background": "#F9F9F5", "Keyword": "#487256", "Unknown": "#565656", "Number": "#82988F", "String": "#677F6A", "Comment": "#B20000"}
    }
    if fn.startswith('and'):
      typL = 'AND'
      typR = 'AND'
      theme = 'gpt1'
    elif fn.startswith('or'):
      typL = ' OR'
      typR = 'OR '
      theme = 'gpt2'
    elif fn.startswith('not'):
      typL = 'NOT'
      typR = 'NOT'
      theme = 'gpt3'
    elif fn.startswith('xor'):
      typL = 'XOR'
      typR = 'XOR'
      theme = 'gpt4'
    elif fn.startswith('increment'):
      typL = 'INC'
      typR = 'INC'
      theme = 'gpt5'
    elif fn.startswith('decrement'):
      typL = 'DEC'
      typR = 'DEC'
      theme = 'gpt6'
    elif fn.startswith('popcount'):
      typL = 'CNT'
      typR = 'CNT'
      theme = 'gpt7'
    elif fn.startswith('shiftLeft'):
      typL = 'SHL'
      typR = 'SHL'
      theme = 'gpt8'
    elif fn.startswith('shiftRight'):
      typL = 'SHR'
      typR = 'SHR'
      theme = 'gpt9'
    elif fn.startswith('zero'):
      typL = 'ZER'
      typR = 'ZER'
      theme = 'gpt10'

    color = themes[theme]["Unknown"]
    bgcolor = themes[theme]["Background"]



    print(f"CARD:{CARD}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:{typL}:{typR}:fill=magenta")
    skip = True
    with open(f"./code/{fn}","r") as f:
        CARD+=1
        card = []
        for line in f.read().splitlines():
            line = line.rstrip()
            line = line.replace("\t","  ")
            card.append(line)

        n = int((32/2)) - int((len(card)) / 2)
        title = f"filename: {fn}"
        print(f"// {title}")          
        print('\n' * (n-1), end='')

        for line in card:
                print(line)
