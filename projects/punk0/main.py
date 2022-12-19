from os import listdir
from itertools import cycle
CARD = 1
#color = '#ffb000' # amber
#color = '#33ff33' # green

#color = '#ffcc00' # amber apple2
#bgcolor = 'black'
#theme='doom-one2'
#
color = 'black'
bgcolor = 'white'
theme = 'friendly'
font='BlockZone'
fontSize='25px'

def card_str(x):
  global CARD
  print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
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
failing if there is no memory and etc,
but the idea of the card is clear.

Some code is made more explicit, like
not using slice operators, or using
extra variables, but this way it is
easier to onboard beginners.

We hope you enjoy the game, and don't
get discouraged if you lose track of the
lists, before the game simply remove the
cards you find difficult to follow.
""")

card_str(f"""{'RULES'.center(40)}

The starting list is:
{'[1, 2, 3, 4, 5]'.center(40)}

You can either play the same fuction in
a different language, or play a
different function. The first player who
finishes their cards wins.

When the draw() function is played, the
player has to draw whatever the first
element of the list is modulo 5, so
e.g. if the list is [7,2,1,0,5] the next
player has to draw 2 cards from the deck.

You can respond to a draw() card with
another draw () card in a different
language to make the next player draw
even more cards!

If you draw with the first element is
zero then the game will crash, because
of division by zero, and the player who
played the draw() card instantly loses
and all the other players win. 

Don't make an angry face when you get to
draw many cards (๑•̀д•́๑).
Silently plan your revenge with the new
cards you just got ꉂ (´∀｀)ʱª.
""")

# double the explode and avg cards

#filtered = [f for f in listed if 'explode1' in f or f.startswith('max1')]
#listed += filtered

listed = [x for x in listdir('./code') if '#' not in x and (x.endswith('.c') or x.endswith('.go') or x.endswith('.js') or x.endswith('.py'))]
listed.sort()
iter = cycle(listed)

while CARD <= 55:
    fn = next(iter)

    lang = ''
    if fn.endswith('.c'):
        lang = 'c'
    if fn.endswith('.js'):
        lang = "javascript"

    if fn.endswith('.go'):
        lang = "go"
        
    if fn.endswith('.py'):
        lang = 'python'
    
    #p = next(possible)

    print(f"CARD:{CARD}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
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
            if 'console' in line or line.startswith("\t\"") or line == ')' or line == 'import (':
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
          print(f"# {title}")
        else:
          print(f"// {title}")          

        print('\n' * (n-1), end='')

        for line in card:
                print(line)
