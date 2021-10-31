from io import StringIO
import os
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time

cards = [
"""
# PROGRAMMING TIME
# 
#
# Start with 1 card per
# player, put the rest
# face down (numbers 
# up).
#
# Each player has to
# interpred the code on
# their card, and look
# for the output at
# the top most card of
# the deck.
#
# First person to see
# their output, takes
# the card from the deck
# and it becomes their
# active card.
# 
# Player with most cards
# wins.


print(3)

"""
,
"""
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

for i in range(3):
    if i % 2 == 1:
        print(i)
""",
"""
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

sum = 0

for i in range(10):
    if i % 2 == 1:
        sum += 1

print(sum)
""",
"""

a = {
    "x": 10,
    "y": 20,
    "z": 5
}

a["k"] = 8

print(a["x"] + a["k"])

""",
"""
a = {
    "x": 10,
    "y": 20,
    "z": 5
}

a["k"] = 8

print(a["x"] + a["k"])
""",
"""

# sometimes things 
# are not as they seem

def sum(a,b):
    return a * b

x = sum(1,2)
print(sum(x, sum(2,3)))
""",
"""
# 1 + 2 = 3
# 3 + 3 = 6
# ...

sum = 0

for i in range(5):
    sum += i

print(sum)
""",
"""
# ASCII:
#  a -> 97
#  b -> 98
#  ...
#  z -> 122

a = 'acd'
sum = 0

for c in a:
    sum += ord(c)

print(sum % 100)
""",
"""

# 
# len('abc') -> 3
#

b = 8

print(len('hi' * b))

""",
"""

a = '1'
b = '11'

print(a + b)

""",
"""

a = [1,2,0,1]
sum = 0

for n in a:
    sum += n

print(sum)
""",
"""

a = [6,-2,-1,1]
sum = 0

for n in a:
    sum += n

print(sum)
""",
"""

a = [1,2,3]
r = 0

for n in a:
    r *= n

print(r)
""",
"""
# ASCII
#  a -> 97
#  ...
#  o -> 111
#  ...

print(ord('q'))

""",


"""
# ASCII
#  a -> 97
#  ...
#  c -> 99
#  ...

print(ord(chr(111)))

""",
]

WIDTH = 1050 
HEIGHT = 600

fnt = ImageFont.truetype(os.path.join('..','fonts','437.ttf'),35)
bgcolor = (0,0,0)
fgcolor = (255, 176, 0)
#bgcolor = (255,255,255)
#fgcolor = (0,0,0)

def border(d):
    d.multiline_text((30,10), """
+-------------------------+
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
+-------------------------+
""", font=fnt, fill=fgcolor)

def back(id, numbers):
    img = Image.new('RGB', (HEIGHT, WIDTH), color = bgcolor)
    d = ImageDraw.Draw(img)
    border(d)
    x = random.randint(60, 500) 
    y = 60 + random.randint(0,80)
    for n in numbers:
        d.text((x,y), str(n), font=fnt, fill=fgcolor)
        y += 80
        x = random.randint(60, 500)
    img.save(os.path.join('images','card_'+str(id)+'_back.png'))

def front(id, code):
    img = Image.new('RGB', (HEIGHT, WIDTH), color = bgcolor)
    d = ImageDraw.Draw(img)
    border(d)
    d.multiline_text((60,60), code, font=fnt, fill=fgcolor)
    img.save(os.path.join('images','card_'+str(id)+'_front.png'))


def run(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(code)
    sys.stdout = old_stdout
    return redirected_output.getvalue()


possible = set()
for card in cards:
    for line in run(card).strip().split("\n"):
        possible.add(line)

random.seed(time.time())
shuffled = list(possible)

for (i,card) in enumerate(cards):
    random.shuffle(shuffled)
    rotate = cycle(shuffled)
    numbers = []
    for x in range(10):
        numbers.append(next(rotate))
    front(i, card)
    back(i, numbers)

