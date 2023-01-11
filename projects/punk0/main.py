from os import listdir
from itertools import cycle
CARD = 1

def card_meta(id, lang):
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
    color = '#000000' # green apple2
    bgcolor = '#FFFFE8'
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
  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}"
  
  
  
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
  print(card_meta(CARD,""))

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

{'[1, 2, 3, 4]'.center(40)}

You can either play the same fuction in
a different language or a different
function in the same language as the
previous card.

The first player who finishes their
cards wins.

When the draw() function is played, the
player has to do whatever the output
of the function is.

You can respond to a draw() card with
another draw() card in a different
language to make the next player draw
even more cards, and of course, they can
respond to your draw again (unless
draw() tells you to skip).

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
        
    print(card_meta(CARD,lang))
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
          print(f"# {title}")
        else:
          print(f"// {title}")          

        print('\n' * (n-1), end='')

        for line in card:
                print(line)
