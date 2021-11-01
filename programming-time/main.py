from io import StringIO
import os
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time

cards = []
cards.append("""
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

""")

cards.append("""
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

for i in range(3):
    if i % 2 == 1:
        print(i)
""")

cards.append("""
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

sum = 0

for i in range(10):
    if i % 2 == 1:
        sum += 1

print(sum)
""")

cards.append("""
a = {
    "x": 10,
    "y": 20,
    "z": 5
}

a["k"] = 8

print(a["x"] + a["k"])

""")

cards.append("""
a = {
    "x": 10,
    "y": 20,
    "z": 5
}

a["k"] = 8

print(a["x"] + a["k"])
""")

cards.append("""

# sometimes things 
# are not as they seem

def sum(a,b):
    return a * b

x = sum(1,2)
print(sum(x, sum(2,3)))
""")

cards.append("""
# 1 + 2 = 3
# 3 + 3 = 6
# ...

sum = 0

for i in range(5):
    sum += i

print(sum)
""")

cards.append("""
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
""")

cards.append("""
# 
# len('abc') -> 3
#

b = 8

print(len('hi' * b))
""")

cards.append("""
a = '1'
b = '11'

print(a + b)
""")

cards.append("""
a = [1,2,0,1]
sum = 0

for n in a:
    sum += n

print(sum)
""")

cards.append("""
a = [6,-2,-1,1]
sum = 0

for n in a:
    sum += n

print(sum)
""")

cards.append("""
a = [1,2,3]
r = 0

for n in a:
    r *= n

print(r)
""")

cards.append("""
# ASCII
#  a -> 97
#  ...
#  o -> 111
#  ...

print(ord('q'))
""")

cards.append("""
# ASCII
#  a -> 97
#  ...
#  c -> 99
#  ...

print(ord(chr(111)))
""")

cards.append("""
a = [1,2,3]
b = [3,4,5]

i = 0
for x in a:
    b[i] = x
    i += 1

print(b[2])
""")

cards.append("""
print(5)
""")

cards.append("""
# ASCII
#  A -> '65'
#  ..

b = ord('C') - 90

print(b)
""")
cards.append("""
a = [ord('c'),
     -ord('b'),
     ord('a')]

r = ord('d')

for c in a:
    r -= c

print(r)
""")

cards.append("""
sum = 0

for i in range(5):
    sum += i

print(sum)
""")

cards.append("""
a = '7'
b = '8'
c = '9'

print(a + b + c)
""")

cards.append("""
a = ['7','8','9']
x = ''

for c in a:
    x += c

print(x)
""")

cards.append("""
a = ['8','9']
x = '7'

for c in a:
    x += c

print(x)
""")



cards.append("""
a = ['7','8','9']
x = '7'

for c in a:
    x += c

print(len(x))
""")

cards.append("""
# ' '.join([1,2,3])
#   -> "1 2 3"

a = ['7','8','9']

print(''.join(a))
""")

cards.append("""
# ASCII
#  0 -> 48
#  1 -> 49
#  ...
#  9 -> 57
#  ...

b = ['9','3']
f = ['3','4']
l = ''

for i in b:
    l += i
for i in f:
    l += i

print(ord(l[3]) -
      ord(l[1]))
""")

cards.append("""
# ASCII
#  0 -> 48
#  1 -> 49
#  ...

b = ['1','3']

r = ord(b[1])-ord(b[0])

print(r)
""")



cards.append("""
# You can override
# keys in dictionaries

a = ['1','1','1','2']
b = {}
for x in a:
    b[x] = True

r = ''
for k in b:
    r += k

print(r)
""")


cards.append("""
# Dictionary keys
# can be integers as 
# well

b = {}
b[1] = 5
b[2] = 6
x = 0
for k in b:
    x += k

print(x)
""")


cards.append("""
# you can index into
# a string, just as 
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

# Split a string into
# a list of strings:
# "a b".split(" ")
# makes ["a","b"]

a = "hello world"
b = a.split(" ")

print(ord(b[1][1]))
""")

cards.append("""
# you can index into
# a string, just as
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

a = "hello world"

print(ord(a[7]))
""")

cards.append("""
x = {
    'a': 'hello',
    'b': 'world'
}

r = x['a'] +  x['b'] 
print(len(r))
""")

cards.append("""
# time.time() gives
# the amount of seconds
# since midnight 1st of
# Jan 1970 in Greenwich.
# 
# e.g. at the time this
# card is made:
# 1635787548.417151

import time

now = time.time()
print(str(now)[0])
""")


cards.append("""
# str(1) makes the
# integer 1 to the 
# string 1

a = '1'
b = 2

print(a + str(b))
""")


cards.append("""
# int('2') makes the 
# string 2 to the 
# integer 2

a = '1'
b = 2

print(int(a) + b)
""")


cards.append("""
# int('2') makes the 
# string 2 to the 
# integer 2

a = '1'
b = 2
c = 3

r = 0
for i in range(c):
    r += int(a) + b

print(r)
""")


cards.append("""
# you can index into
# a string, just as 
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

a = 'hello world'

m = 0

for i in range(len(a)):
    if a[i] == 'o':
        m += 1

print(m)
""")



cards.append("""
memory = []
for i in range(10000):
    memory.append(0)

memory[800] = 3
memory[801] = 97
memory[802] = 98
memory[803] = 99

def show(m, addr):
    l = m[addr]
    for i in range(l):
        c = m[addr+i+1]
        print(chr(c))

show(memory, 800)
""")



WIDTH = 1050 
HEIGHT = 600

fnt = ImageFont.truetype(os.path.join('..','fonts','437.ttf'),35)
bgcolor = (0,0,0)
fgcolor = (255, 176, 0)
#bgcolor = (255,255,255)
#fgcolor = (0,0,0)

def border(d):
    d.multiline_text((50,10), """
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
+-------------------------+
""", font=fnt, fill=fgcolor)

def back(id, numbers):
    img = Image.new('RGB', (HEIGHT, WIDTH), color = bgcolor)
    d = ImageDraw.Draw(img)
    border(d)
    x = random.randint(80, 500) 
    y = 60 + random.randint(0,80)
    for n in numbers:
        d.text((x,y), str(n), font=fnt, fill=fgcolor)
        y += 80
        x = random.randint(80, 500)
    img.save(os.path.join('images','back_card_'+str(id)+'.png'))

def front(id, code):
    img = Image.new('RGB', (HEIGHT, WIDTH), color = bgcolor)
    d = ImageDraw.Draw(img)
    border(d)
    d.multiline_text((80,80), code, font=fnt, fill=fgcolor)
    img.save(os.path.join('images','front_card_'+str(id)+'.png'))


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

