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


def card_middle(card):
    for line in card:
        print(line)

     
def binary(f,t):
    global CARD
    print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:::")
    CARD+=1

    for i in range(f, min(256,f+31)):
        a = i
        b = i + 31
        if b > t:
          print(f"{a:3} {a:08b}".center(40))
        else:
          print(f"{a:3} {a:08b}     |     {b:3} {b:8b}".center(40))



card_str(f"""{'BIN111'.center(40)}

[color:red]Game Setup:[/color] Each player begins the game
with 3 face-up cards, visible to
all. The game starts with a base number
of 1.

[color:red]Turn Mechanics:[/color] On their turn, each
player must play all 3 of their cards in
any order they wish. These cards modify
the base number through their
operations. The resulting number from
their operations is then passed on to
the next player as their new starting
number.

[color:red]Victory Condition:[/color] The goal is to reach
a certain binary number through the use
of cards. If a player's score equals the
target number (default is 7, binary
0111), they win the game! If they do not
reach the target, they draw 3 new cards
for their next turn.

[color:red]Adjusting Difficulty:[/color] To change the
difficulty, simply alter the target
number. For a harder game, aim for 1010
(decimal 10). For an easier game, aim
for 0011 (decimal 3).

[color:red]Strategy Tip:[/color] Can't win? Sabotage!
 """)

card_str(f"""{'BINARY'.center(40)}
In the binary system, each digit
represents a power of 2, starting from
the rightmost bit (also known as the
least significant bit) which represents
2^0, and going to the left each bit
represents the next power of 2.

Converting binary number to decimal:
The number: 1010

1      0       1       0
2^3    2^2     2^1     2^0
8      4       2       1 
you just sum the bits that are ON (with
value 1) and ignore the ones that are
OFF (with value 0): 8 + 0 + 2 + 0 = 10,
so the number 10 in binary is 1010

1111 is 8 + 4 + 2 + 1, which is 15
0000 is 0 + 0 + 0 + 0, which is 0

To convert from decimal to binary use
the same approach, you have to represent
the number as a sums of power of 2, 
... 1024 512 256 128 64 32 8 4 2 1
For example the number 362 is 101101010

Leading zeroes are ignored, same as 099
in decimal is just 99, 00000111 is just
111.
""")

card_str(f"""{'BINARY'.center(40)}
All the cards in the game take and
return the type uint4_t, which means:
unsigned integer with 4 bits (1 nibble).

So we have 4 bits to work with:
    00   0000             08   1000
    01   0001             09   1001
    02   0010             10   1010
    03   0011             11   1011
    04   0100             12   1100
    05   0101             13   1101
    06   0110             14   1110
    07   0111             15   1111

The smallest number we can represent is
0, where all the bits are 0, and the
largest one is 15 (all 4 bits set to 1).

If we were using uint64_t then we would
have 64 bits (8 bytes) to work with,
smallest number is 0 and the largest is
9223372036854775807 (all 64 bits set to
1).

In C there is no easy way to use 4 bit
numbers (you can struct x{{uint8_t
v:4;}} or mask with &11), the smallest
standard integer type you can use is 8
bits: uint8_t, but for the purpose of
the game, 4 bits are more fun.
""")

listed = [
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'decrement.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'increment.c',
  'not.c',
  'not.c',
  'not.c',
  'not.c',
  'not.c',
  'not.c',
  'not.c',
  'popcount.c',
  'popcount.c',
  'popcount.c',
  'popcount.c',
  'popcount.c',
  'popcount.c',
  'popcount.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftLeft.c',
  'shiftRight.c',
  'shiftRight.c',
  'shiftRight.c',
  'shiftRight.c',
  'shiftRight.c',
  'shiftRight.c',
  'shiftRight.c',
  'shiftRight.c',
  'zero.c',
  'zero.c',
  'zero.c',
  'zero.c'
]

    
themes = {
    "gpt1": {"Background": "#D7FAFF", "Keyword": "#003456", "Unknown": "#1F1F1F", "Number": "#005798", "String": "#004573", "Comment": "#B20000"},
    "gpt2": {"Background": "#FFD5B6", "Keyword": "#4C0000", "Unknown": "#1F1F1F", "Number": "#4C1A0A", "String": "#3B0A00", "Comment": "#B20000"},
    "gpt3": {"Background": "#C8E8C6", "Keyword": "#003806", "Unknown": "#1F1F1F", "Number": "#005E00", "String": "#004D0A", "Comment": "#B20000"},
    "gpt4": {"Background": "#FFFFFF", "Keyword": "#000000", "Unknown": "#1F1F1F", "Number": "#000000", "String": "#000000", "Comment": "#B20000"},
    "gpt5": {"Background": "#FEBB6E", "Keyword": "#5B0000", "Unknown": "#1F1F1F", "Number": "#7D3300", "String": "#5B0000", "Comment": "#B20000"},
    "gpt6": {"Background": "#E6D9FC", "Keyword": "#550086", "Unknown": "#1F1F1F", "Number": "#7D009E", "String": "#8000BF", "Comment": "#B20000"},
    "gpt7": {"Background": "#A2E8FA", "Keyword": "#004054", "Unknown": "#1F1F1F", "Number": "#007090", "String": "#006074", "Comment": "#B20000"},
}



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

    if fn.startswith('not'):
      typL = 'NOT'
      typR = 'NOT'
      theme = 'gpt1'
    elif fn.startswith('increment'):
      typL = 'INC'
      typR = 'INC'
      theme = 'gpt2'
    elif fn.startswith('decrement'):
      typL = 'DEC'
      typR = 'DEC'
      theme = 'gpt3'
    elif fn.startswith('popcount'):
      typL = 'CNT'
      typR = 'CNT'
      theme = 'gpt4'
    elif fn.startswith('shiftLeft'):
      typL = 'SHL'
      typR = 'SHL'
      theme = 'gpt5'
    elif fn.startswith('shiftRight'):
      typL = 'SHR'
      typR = 'SHR'
      theme = 'gpt6'
    elif fn.startswith('zero'):
      typL = 'ZER'
      typR = 'ZER'
      theme = 'gpt7'

    color = themes[theme]["Unknown"]
    bgcolor = themes[theme]["Background"]



    print(f"CARD:{CARD}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:{typL}:{typR}:fill=black")
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


if CARD != 56:
  raise Exception("AAAAAAAAAAAAAAAAA" + str(CARD))
                
