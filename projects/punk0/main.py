from os import listdir
from itertools import cycle
CARD = 1

def card_meta(id, lang, symbol, symbol_style):
#  color = 'black'
#  bgcolor = 'white'
#  theme = 'friendly'
  color = '#39FF14' 
  bgcolor = '#000000'
  theme='punk0'
  font='BlockZone'
  fontSize='25px'

  if lang == "c":
    color = '#A9A2D7' # amber apple2
    bgcolor = '#0000AF'
    theme='gptamber'


  if lang == "go":
    color = '#202224' # green apple2
    bgcolor = '#ffd'
    theme='gptwhite'


  if lang == "javascript":
    color = '#c0c5ca' 
    bgcolor = '#1d2432'
    theme="gptblack" #next(possible["python"])


  if lang == "python":
    color = '#6e7781'
    bgcolor = '#ffffff'
    theme="gptredzz" #next(possible["javascript"])

  #bgcolor = '#ffffff'
  #color = '#ff5544'
  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}:{symbol}:{symbol_style}"
  
  
  
#color = '#ffb000' # amber
#color = '#33ff33' # green

#color = '#ffcc00' # amber apple2
#bgcolor = 'black'
#theme='doom-one2'
#

  
#color = '#ffcc00' # amber apple2
#bgcolor = 'black'
#theme='doom-one2'
  
def card_str(x):
  global CARD
  print(card_meta(CARD,"","",""))

  CARD+=1
  print(x)
  print()

card_str(f"""{'PUNK0'.center(40)}

{'PUNK ZERO or PUNK O'.center(40)}

PUNK0 is a game of function composition,
each card's output is another card's
input.

Each card has a function that takes a
list of integers and returns a list of
integers and each function is
implemented in c, go, python and
javascript.

The cards, especially the C cards, have
a lot of bugs in them, they dont check
for integer overflows and underflows,
break down in various ways like malloc
failing, but the idea of the card is
clear.

The code is made more explicit, like not
using slice operators, or using extra
variables, or calling slices lists, but
this way should be easier for beginners.

I hope you enjoy the game, and don't get
discouraged if you lose track of the
lists, just use a pen and paper to write
it down on every step, thats what I do.
""")


card_str(f"""{'RULES'.center(40)}

The starting list is:

{'[0, 0, 0, 0]'.center(40)}

* Each player starts with 8 cards, the
  youngest player goes first and they
  can play any card they choose.

* Players can either play the same
  function in a different language or
  any function in the same language as
  the previous card.

* Players must play a matching card if
  they have one, otherwise they must
  draw a card and play it if possible,
  otherwise they must skip their turn.

* If a player has to draw cards due to a
  punk() card they can play after
  drawing.

* The first player to finish their cards
  wins the game.

Don't make an angry face when you get to
draw many cards (๑•̀д•́๑).
Silently plan your revenge with the new
cards you just got ꉂ (´∀｀)ʱª.
""")


card_str(f"""{'PUNK CARDS'.center(40)}

* [color:cyan]punk0()[/color]
 
  The card will determine the next
  action based on the first element
  (index 0) of the list.
    
  + If the value of the first element is
  zero, the next player will skip their
  turn.

  + If the value is negative, the
  current player must play exactly N
  cards in the same turn, where N is the
  absolute value of the element. If they
  are unable to play N cards, they must
  draw from the deck and skip their
  turn.
  
  + If the value is positive, the next
  player must draw N cards from the
  deck, where N is the value of the
  element, unless they have a punk0
  card, in which case they can forward
  the penalty to the next player.

* [color:cyan]punk1() punk2() punk3()[/color]

  Same as punk0(), but using different
  element of the list.

""")


listed = [
 'punk0.c',
 'punk0.go',
 'punk0.py',
 'punk0.js',

 'punk1.c',
 'punk1.go',
 'punk1.py',
 'punk1.js',
 'punk2.c',
 'punk2.go',
 'punk2.py',
 'punk2.js',
 'punk3.c',
 'punk3.go',
 'punk3.py',
 'punk3.js',


 'increment.c',
 'increment.go',
 'increment.js',
 'increment.py',
 'increment.c',
 'increment.go',
 'increment.js',
 'increment.py',

 'decrement.c',
 'decrement.go',
 'decrement.js',
 'decrement.py',
 'decrement.c',
 'decrement.go',
 'decrement.js',
 'decrement.py',

 'rotate_left.c',
 'rotate_left.go',
 'rotate_left.js',
 'rotate_left.py',

 'rotate_right.c',
 'rotate_right.go',
 'rotate_right.js',
 'rotate_right.py',

 'reset.c',
 'reset.go',
 'reset.js',
 'reset.py',

# 'reverse.c',
# 'reverse.go',
# 'reverse.js',
# 'reverse.py',

 'increment.c',
 'increment.go',
 'increment.js',
 'increment.py',

 'decrement.c',
 'decrement.go',
 'decrement.js',
 'decrement.py',



# 'shift_left.js',
# 'shift_left.py',
# 'shift_left.c',
# 'shift_left.go',
#
# 'shift_right.js',
# 'shift_right.py',
# 'shift_right.c',
# 'shift_right.go',
]



for fn in listed:
    lang = ''
    if fn.endswith('.c'):
        color = 'black'
        bgcolor = 'white'
        theme = 'friendly'

        lang = 'c'
    if fn.endswith('.js'):
        lang = "javascript"

    if fn.endswith('.go'):
        lang = "go"
        
    if fn.endswith('.py'):
        lang = 'python'
    
    #p = next(possible)
    typ = 'INC'
    color = ''
    name, ext = fn.split('.')
    if fn.startswith('punk0'):
      typ = 'PK0'
    elif fn.startswith('punk1'):
      typ = 'PK1'
    elif fn.startswith('punk2'):
      typ = 'PK2'
    elif fn.startswith('punk3'):
      typ = 'PK3'
    elif fn.startswith('decrement'):
      typ = 'DEC'
    elif fn.startswith('rotate_left'):
      typ = 'RTL'
    elif fn.startswith('rotate_right'):
      typ = 'RTR'
    elif fn.startswith('reset'):
      typ = 'RST'

    color=''
    if ext == 'js':
      color='#ff636f'
    if ext == 'c':
      color='white'
    if ext == 'py':
      color='#cf222e'
    if ext == 'go':
      color='#1054af'
        
    print(card_meta(CARD,lang,typ, f'fill="{color}"'))
    skip = True
    with open(f"./code/{fn}","r") as f:
        CARD+=1
        card = []
        for line in f.read().splitlines():
            line = line.rstrip()
            if fn.endswith('go'):
              line = line.replace("\t", "  ")
            if fn.endswith('py'):
              line = line.replace("    ", "  ")

            if 'package' in line:
                continue

            if 'main' in line:
                break

            if line.strip() == '"fmt"' or line.strip() == '"sort"':
                continue
            if line.startswith('console') or line.startswith("\t\"") or line == ')' or line == 'import (':
                continue

            if 'function' in line or 'func' in line or 'def' in line or '(' in line and not 'import' in line:
                skip = False

            if line.startswith('import'):
                continue
            
            if 'print' in line and '[' in line:
                break

            if 'import' not in line and not line.startswith('#include') and (not skip or len(line) > 0):
                line = line.replace("\t","  ")
                card.append(line)

        n = int((32/2)) - int((len(card)) / 2)
        title = f"filename: {fn}"
        if fn.endswith('py'):
          title = f"# {title}"
        else:
          title = f"// {title}"

        print(title)
        print('\n' * (n-1), end='')

        for line in card:
                print(line)

if CARD != 56:
  raise Exception("AAAAAAAAAAAAAAAAA" + str(CARD))
