from os import listdir
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

There are four types of cards in this
version:

 * takes a LIST and returns a LIST
 * takes a LIST and returns an INT
 * takes an INT and returns a LIST
 * takes an INT and returns an INT

Cards are implemented in c, go, python
and js and some are also implemented
with different time complexity.

The cards, especially the C cards, have
a lot of bugs in them, they dont check
for integer overflows and underflows,
break down with negative integers, or
malloc failing if there is no memory and
etc, but the idea of the card is
clear. Some code is made more explicit,
like redefining python's sum and max or
not using slice operators, but this way
it is easier to onboard beginners.
""")

card_str(f"""{'SIMPLE RULES'.center(40)}
1. Shuffle the cards.

2. Each player gets 6 cards

3. Youngest player plays a card that
   takes a list.

   This is the starting list:
   [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

4. You can play a card in any language
   if it changes the type of the output,
   e.g. LIST -> INT or INT -> LIST, but
   if you do not change it, you have to
   play in the same language as in the
   previous card, or draw from the deck.

   If the player plays a card that
   returns an INT, and they can say the
   actual value, the next player, before
   playing, has to draw min(4, V) cards
   from the deck where V is the actual
   value returned, if they cant say the
   value, the game continues as normal.
   You can challlenge them, and if the
   value is wrong, they have to draw
   min(4,V).

5. The player who reaches zero cards
   wins.
""")

card_str(f"""{'ADVANCED RULES'.center(40)}

The goal of the game is to produce a
specific value, the number 7

1. Shuffle the cards

2. Each player gets 10 cards
   (you can decide to play open, so
   cards are face up on the table, so
   the other players can sabotage you)
3. The player who has traveled the most
   starts.

4. You can play multiple cards in the
   same language in the same time. Each
   turn you can decide to pull from the
   deck or play your hand.

5. The first one that produces the
   numner 7 wins

The starting list is:
  [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
""")

# double the explode and avg cards

#filtered = [f for f in listed if 'explode1' in f or f.startswith('max1')]
#listed += filtered

listed = listdir('./code')
listed.sort()

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
            
            if 'print' in line:
                break

            if 'import' not in line and not line.startswith('#include') and (not skip or len(line) > 0):
                line = line.replace("\t","  ")
                card.append(line)

        n = int((32/2)) - int((len(card)) / 2)
        print('\n' * n, end='')
        for line in card:
                print(line)
