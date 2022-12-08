from os import listdir
from itertools import cycle
CARD = 1
#color = '#ffb000' # amber
#color = '#33ff33' # green

font='BlockZone'
fontSize='25px'

color = '#ffcc00' # amber apple2
bgcolor = 'black'
theme='doom-one2'
#

#color = 'black'
#bgcolor = 'white'
#theme = 'friendly'

def card_str(x):
  global CARD
  print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
  CARD+=1
  print(x)
  print()

def card_middle(title, card):
    n = int((32/2)) - int((len(card)) / 2)
    global CARD
    print(f"CARD:{CARD}::{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
    print(title.center(40))
    CARD+=1
    print('\n' * (n-1), end='')
    for line in card:
        print(line)

    
def binary(f):
    s = []
    for i in range(f, f+16):
        a = i
        b = i + 16
        s.append((f"{a:03} {a:08b}     |     {b:03} {b:08b}").center(40))

    card_middle(f"from: {f} to: {f + 32 - 1}",s)


for j in range(8):
    binary(32 * j)


listed = listdir('./code')
starting = cycle(list(listed))

for i in range(CARD+len(listed), 56):
    listed.append(next(starting))
listed.sort()

for fn in listed:
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

    print(f"CARD:{CARD}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}")
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
