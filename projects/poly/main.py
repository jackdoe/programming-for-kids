from os import listdir
CARD = 1
listed = listdir('./code')
listed.sort()

#color = '#33ff33' # green
#color = '#ffcc00' # amber apple2
#color = '#ffb000' # amber
#theme='doom-one2'
color = 'black'
bgcolor = 'white'
theme = 'friendly'
def card_str(x):
  global CARD
  print(f"CARD:{CARD}::doom-one2:{bgcolor}:{color}:{color}")
  CARD+=1
  print(x)
  print()

card_str(f"""{'PUNKO'.center(40)}

The game PUNKO is a game of function
composition, each card's output is
another card's input.

There are three types of cards in this
version:

 * Takes a list and returns a list
 * Takes a list and returns an integer
 * Takes an integer and returns a list

Cards are implemented in multiple
languages and some are also implemented
with different space or time complexity.

The cards, especially the C cards, have
a lot of bugs in them, they dont check
for integer overflows and underflows,
break down with negative integers, or
for example the hash set can get into
infinite loop and also can't have keys
with value zero, or malloc failing if
there is no memory and etc, but the idea
of the card is clear.

Some code is made more explicit, like
redefining python's sum and max or not
using them, but this way it is easier to
onboard beginners.
""")

card_str(f"""{'RULES'.center(40)}

1. Shuffle the cards.

2. Each player gets 6 cards.

3. Youngest player plays a card that
   takes a list.

   This is the starting list:
   [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

4. The next player (clockwise) needs to
   play a card that takes the previous
   card's output as input. 

   For example if they played uniq(x),
   which takes a list and returns a
   list, you must play a card that takes
   a list. If they played avg(x) which
   takes a list and returns an integer,
   then you must play a card that takes
   an integer.

   If you dont have an appropriate card
   draw from the deck until you get one.

5. Whoever finishes their cards first
   is the winner.
""")

card_str(f"""{'ADVANCED RULES'.center(40)}

The advanced version of the game is much
more open, the only rule is: 

  the next card's input is the previous
  card's output

The starting list is:
  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

You will have to interpret the code in
your head, and keep evaluating the
result, maybe use pen and paper to write
the actual output of the last card.

There are tasks you can try to do:

* make last card return an empty list
* make the last card consume at least
  4GB of memory
* compete with another player who can
  make the biggest list
* come up with your own ridiculous
  task, e.g. avg should be 5
* start with [1] and get to [1,2,3,4,5]
* you can only use either different
  function or higher complexity of
  the same function
* you can only use function in different
  language
""")

# double the explode and avg cards

#filtered = [f for f in listed if 'explode1' in f or f.startswith('max1')]
#listed += filtered

from itertools import cycle
possible = cycle([
"abap", "algol", "algol_nu", "arduino",
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
 "trac", "vim", "witchhazel",
 "xcode-dark", "xcode"])

for fn in listed:
    if not '.' in fn:
        continue

    if 'rld' in fn or '#' in fn:
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

    #p = next(possible)

    print(f"CARD:{CARD}:{lang}:{theme}:{bgcolor}:{color}:{color}")
    skip = True
    with open(f"./code/{fn}","r") as f:
        CARD+=1
        card = []
#        card.append(p)
        for line in f.read().splitlines():
            line = line.rstrip()

            if 'package' in line:
                continue

            if 'main' in line:
                break

            if 'console' in line or line.startswith("\t\"") or line == ')' or line == 'import (':
                continue

            if 'function' in line or 'func' in line or 'def' in line or '(' in line and not 'import' in line:
                skip = False

            if line.startswith('import'):
                continue
            
            if 'print' in line:
                break

            if 'import' not in line and not line.startswith('#include') and (not skip or len(line) > 0):
                line = line.replace("\t","  ")
                card.append(line)

        n = int((32/2)) - int((len(card)) / 2)
        print('\n' * n, end='')
        for line in card:
                print(line)
