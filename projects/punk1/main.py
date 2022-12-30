from os import listdir
from itertools import cycle
CARD = 1

possible = {}

possible["javascript"] = cycle(["abap", "algol", "algol_nu", "arduino",
                               "autumn", "average", "base16-snazzy",
                               "borland", "catppuccin-frappe",
                               "catppuccin-latte", "catppuccin-mocha",
                               "colorful", "doom-one", "doom-one2",
                               "dracula", "emacs", "friendly",
                               "fruity", "github-dark", "github",
                               "gruvbox-light", "gruvbox",
                               "hr_high_contrast", "hrdark", "igor",
                               "lovelace", "manni", "modus-operandi",
                               "modus-vivendi", "monokai",
                               "monokailight", "murphy", "native",
                               "nord", "onedark", "onesenterprise",
                               "paraiso-dark", "paraiso-light",
                               "pastie", "perldoc", "pygments",
                               "rainbow_dash", "rose-pine-dawn",
                               "rose-pine-moon", "rose-pine", "rrt",
                               "solarized-dark", "solarized-dark256",
                               "solarized-light", "swapoff", "tango",
                               "trac", "vim", "witchhazel", "xcode-dark", "xcode"])

possible["go"] = cycle(["abap", "algol", "algol_nu", "arduino",
                               "autumn", "average", "base16-snazzy",
                               "borland", "catppuccin-frappe",
                               "catppuccin-latte", "catppuccin-mocha",
                               "colorful", "doom-one", "doom-one2",
                               "dracula", "emacs", "friendly",
                               "fruity", "github-dark", "github",
                               "gruvbox-light", "gruvbox",
                               "hr_high_contrast", "hrdark", "igor",
                               "lovelace", "manni", "modus-operandi",
                               "modus-vivendi", "monokai",
                               "monokailight", "murphy", "native",
                               "nord", "onedark", "onesenterprise",
                               "paraiso-dark", "paraiso-light",
                               "pastie", "perldoc", "pygments",
                               "rainbow_dash", "rose-pine-dawn",
                               "rose-pine-moon", "rose-pine", "rrt",
                               "solarized-dark", "solarized-dark256",
                               "solarized-light", "swapoff", "tango",
                               "trac", "vim", "witchhazel", "xcode-dark", "xcode"])

possible["python"] = cycle(["abap", "algol", "algol_nu", "arduino",
                               "autumn", "average", "base16-snazzy",
                               "borland", "catppuccin-frappe",
                               "catppuccin-latte", "catppuccin-mocha",
                               "colorful", "doom-one", "doom-one2",
                               "dracula", "emacs", "friendly",
                               "fruity", "github-dark", "github",
                               "gruvbox-light", "gruvbox",
                               "hr_high_contrast", "hrdark", "igor",
                               "lovelace", "manni", "modus-operandi",
                               "modus-vivendi", "monokai",
                               "monokailight", "murphy", "native",
                               "nord", "onedark", "onesenterprise",
                               "paraiso-dark", "paraiso-light",
                               "pastie", "perldoc", "pygments",
                               "rainbow_dash", "rose-pine-dawn",
                               "rose-pine-moon", "rose-pine", "rrt",
                               "solarized-dark", "solarized-dark256",
                               "solarized-light", "swapoff", "tango",
                               "trac", "vim", "witchhazel", "xcode-dark", "xcode"])


def card_meta(id, lang):
#  color = 'black'
#  bgcolor = 'white'
#  theme = 'friendly'
  color = '#ffcc00' # amber apple2
  bgcolor = 'black'
  theme='punk0'
  font='BlockZone'
  fontSize='25px'

  if lang == "c":
    color = '#ffcc00' # amber apple2
    bgcolor = '#000000'
    theme='gptamber'


  if lang == "go":
    color = '#0f0200' # green apple2
    bgcolor = '#ffffff'
    theme='gptwhite'


  if lang == "python":
    color = '#ffd808' 
    bgcolor = '#006ab3'
    theme="gptbluez" #next(possible["python"])


  if lang == "javascript":
    color = '#fffdff'
    bgcolor = '#c40f42'
    theme="gptredzz" #next(possible["javascript"])
    
  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}"
  
  
    
def card_str(x):
  global CARD
  print(card_meta(CARD,""))

  CARD+=1
  print(x)
  print()

card_str(f"""{'PUNK1'.center(40)}

{'PUNK ONE'.center(40)}

PUNK1 is a game of function composition,
each card's output is another card's
input.

There sare four types of functions:

LIST -> INTEGER
INTEGER -> INTEGER
INTEGER -> LIST
LIST -> LIST

Each function implemented in c, go,
python and javascript.

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
""")

card_str(f"""{'RULES'.center(40)}

The starting list is:

{'[1, 2, 3, 4, 5]'.center(40)}

The goal of the game is to get to the
number 7.

Start with 3 cards each.

You have to have your cards face up on
the table, so the oponents can see them.

You can can play many cards in a
specific language together as one
program, or draw one card from the deck.

After you play your cards you have to
say what the current output is.


""")


card_str(f"""{'EXAMPLE ROUND'.center(40)}

The starting list is:

{'[1, 2, 3, 4, 5]'.center(40)}

Alice's cards: 
    rest.c, min.go, first.c
Charlie's cards: 
    rotate.c, oneOrFive.c, inc.c

Alice plays the two C cards:
    first([1,2,3,4,5])
    which returns 1

Charlie draws from the deck and gets:
    max.c

Alice draws from the deck and gets:
    rest.js

Charlie plays the 3 C cards:
    inc(max(explode(1)))

    explode(1)
      -> [1,2,3,4,5,6]
    max([1,2,3,4,5,6])
      -> 6
    inc(6)
      -> 7

Charlie Wins!
""")


listed = [x for x in listdir('./code') if '#' not in x and (x.endswith('.c') or x.endswith('.go') or x.endswith('.js') or x.endswith('.py'))]
filtered = [f for f in listed if 'explode1' in f]
listed += filtered
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
