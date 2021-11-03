from io import StringIO
import os
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont
import time

cards = []
cards.append([1, """
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

"""])

cards.append([1, """
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

for i in range(3):
  if i % 2 == 1:
    print(i)
"""])

cards.append([1, """
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

sum = 0

for i in range(10):
  if i % 2 == 1:
    sum += 1

print(sum)
"""])

cards.append([1, """
a = {
  "x": 10,
  "y": 20,
  "z": 5
}

a["k"] = 8

print(a["x"] + a["k"])
"""])

cards.append([1, """
i = 0
while i < 3:
  i += 1

print(i)
"""])


cards.append([1, """
i = 0
while True:
  i += 1
  if i > 3:
    break
print(i)
"""])


cards.append([1, """
a = 'hello world'

print(len(a))
"""])


cards.append([1, """
a = 'hello world'
b = a[2:5]

print(len(b))
"""])


cards.append([1, """
a = 'hello world'
b = a[:2]

print(len(b))
"""])


cards.append([1, """
a = 'hello world'
b = a[0:2] + a[6:9]

print(len(b))
"""])


cards.append([1, """
def hello():
  return 'world'

a = hello()

print(len(a))
"""])


cards.append([1, """
def world():
  return 'world'

def hello():
  return 'hello'

a = hello() + world()

print(len(a))
"""])


cards.append([1, """
a = 'hello world'
b = a[2:]

print(len(b))
"""])


cards.append([2, """
def min(a):
  if len(a) == 0:
    return None

  s = a[0]
  for n in a:
    if n < s:
      s = n
  return s

print(min([3,2,4,3]))
"""])

cards.append([2, """
def max(a):
  if len(a) == 0:
    return None

  m = a[0]
  for n in a:
    if n > m:
      m = n
  return m

print(max([1,2,4,3]))
"""])


cards.append([2, """
def avg(a):
  sum = 0
  for n in a:
    sum += n
  return sum/len(a)

print(avg([2,2,4,4]))
"""])

cards.append([2, """
x = 0

for i in range(2):
  for j in range(3):
    x += 1

print(x)
"""])


cards.append([2, """
# sometimes things 
# are not as they seem

def sum(a,b):
  return a * b

x = sum(1,2)
print(sum(x, sum(2,3)))
"""])

cards.append([2, """
# 1 + 2 = 3
# 3 + 3 = 6
# ...

sum = 0

for i in range(5):
  sum += i

print(sum)
"""])

cards.append([3, """
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
"""])

cards.append([1, """
# 
# len('abc') -> 3
#

b = 8

print(len('hi' * b))
"""])

cards.append([1, """
a = '1'
b = '11'

print(a + b)
"""])

cards.append([2, """
a = [1,2,0,1]
sum = 0

for n in a:
  sum += n

print(sum)
"""])

cards.append([2, """
a = [6,-2,-1,1]
sum = 0

for n in a:
  sum += n

print(sum)
"""])

cards.append([2, """
a = [1,2,3]
r = 0

for n in a:
  r *= n

print(r)
"""])

cards.append([1, """
# ASCII
#  a -> 97
#  ...
#  o -> 111
#  ...

print(ord('q'))
"""])

cards.append([1, """
# ASCII
#  a -> 97
#  ...
#  c -> 99
#  ...

print(ord(chr(111)))
"""])

cards.append([3, """
a = [1,2,3]
b = [3,4,5]

i = 0
for x in a:
  b[i] = x
  i += 1

print(b[2])
"""])

cards.append([1, """
print(5)
"""])

cards.append([1, """
# ASCII
#  A -> '65'
#  B -> '66'
#  ..

b = ord('C') - 90

print(b)
"""])
cards.append([3, """
a = [ord('c'),
   -ord('b'),
   ord('a')]

r = ord('d')

for c in a:
  r -= c

print(r)
"""])

cards.append([1, """
sum = 0

for i in range(5):
  sum += i

print(sum)
"""])

cards.append([1, """
a = '7'
b = '8'
c = '9'

print(a + b + c)
"""])

cards.append([2, """
a = ['7','8','9']
x = ''

for c in a:
  x += c

print(x)
"""])

cards.append([2, """
a = ['8','9']
x = '7'

for c in a:
  x += c

print(x)
"""])


cards.append([2, """
a = ['2','1','1']
x = a.pop()

for c in a:
  x += c

print(len(x))
"""])

cards.append([2, """
# ' '.join([1,2,3])
#   -> "1 2 3"

a = ['7','8','9']

print(''.join(a))
"""])

cards.append([3, """
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
"""])

cards.append([3, """
# ASCII
#  0 -> 48
#  1 -> 49
#  ...

b = ['1','3']

r = ord(b[1])-ord(b[0])

print(r)
"""])


cards.append([3, """
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
"""])


cards.append([3, """
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
"""])


cards.append([3, """
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
"""])

cards.append([2, """
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
"""])

cards.append([1, """
x = {
  'a': 'hello',
  'b': 'world'
}

r = x['a'] +  x['b'] 
print(len(r))
"""])

cards.append([2, """
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
"""])


cards.append([1, """
# str(1) makes the
# integer 1 to the 
# string 1

a = '1'
b = 2

print(a + str(b))
"""])


cards.append([1, """
# int('2') makes the 
# string 2 to the 
# integer 2

a = '1'
b = 2

print(int(a) + b)
"""])


cards.append([2, """
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
"""])


cards.append([2, """
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
"""])


cards.append([3, """
memory = []
for i in range(10000):
  memory.append(0)

memory[800] = 3
memory[801] = 97
memory[802] = 98
memory[803] = 99
memory[804] = 48

def show(m, addr):
  l = m[addr]
  for i in range(l):
    c = m[addr+i+1]
    print(chr(c))

show(memory, 800)
"""])


cards.append([3, """
class Point:
  x = 0
  y = 0

a = Point()
a.x = 5
a.y = 10

b = Point()
b.x = 3
b.y = 1

print(a.x - b.x + b.y)
"""])


cards.append([1, """
# 5 / 2 is 2
# and 1 remainder
#
# 7 / 2 is 3
# and 1 remainder
# 
# 11 / 4 is 2
# and 3 remainder
# 11 % 4 is 3

print(99 % 10)
"""])

cards.append([2, """
a = "world"
b = ['h','e','llo']

print(len(a[0] + b[2]))
"""])


cards.append([1, """
while True:
  break

print(5)
"""])

cards.append([2, """
def mul(a,b):
  r = 0
  for i in range(b):
    r += a
  return r

print(mul(2,3))
"""])

cards.append([2, """
i = 0
while 1 == 1:
  i += 1
  if i > 5:
    break

print(i)
"""])


cards.append([2, """
i = 0
while 1 == 1:
  i += 1
  if i > 5:
    break
print(i)
"""])


cards.append([1, """
a = "world"
b = ['h','e','llo']

print(len(a[0] + b[2]))
"""])

cards.append([3, """
class Actor:
  x = 0
  y = 0

player = Actor()

def update():
  player.x += 1
  player.y += 1

def draw():
  print(player.x)
  print(player.y)

while True:
  update()
  draw()

  break
"""])

cards.append([3, """
def fib(n):
  if n <= 1:
    return n
  else:
    a = fib(n-1)
    b = fib(n-2)
    return(a + b)

print(fib(5))
"""])

cards.append([1, """
a = '7798'
b = 2

if b > 2:
  b -= 1

print(a[b])
"""])


cards.append([1, """
a = '7798'
b = 2

if b < 2 or b == 2:
  b -= 1

print(a[b])
"""])


cards.append([1, """
a = '7798'
b = 2
c = 3
if b < 2 and c >= 3:
  b -= 1

print(a[b])
"""])

cards.append([1, """
a = ['7',2,'5',9]
b = 2

b += 1

print(a[b])
"""])

cards.append([1, """
a = ['7',2,'5',9]
a.pop()
a.pop()

print(a[len(a)-1])
"""])

cards.append([2, """
a = [4,5,6]
b = [1,2,3]
c = [*a, *b]

print(len(c))
"""])


cards.append([2, """
a = [4,5,6]
b = [1,2,3]
c = [*a, *b]

print(len(c))
"""])


cards.append([2, """
a = []
a.append(1)
a.append(2)

b = a.pop()

print(b)
"""])


cards.append([2, """
a = []
a.append(1)
a.append(2)

b = a.pop()

print(b)
"""])

cards.append([2, """
b = '4321'
a = [b[0],b[1],b[2],b[3]]

print(a[3])
"""])


cards.append([1, """
b = '4321'

print(b[len(b) - 1])
"""])

cards.append([1, """
x = [1,2,3,4]

print(x[len(x)-2])
"""])


cards.append([1, """
x = [1,2,3,4]

print(x[3] - x[1])
"""])


cards.append([2, """
a = []
while True:
  a.append(1)
  if len(a) > 5:
    break

print(len(a))
"""])


cards.append([3, """
def compress(x):
  o = [x[0],0]

  for n in x:
    p = o[len(o)-2]

    if n == p:
      o[len(o)-1]+=1
    else:
      o.append(n)
      o.append(1)

  return o

a = [1,1,1,1,2,3,3,3,3]
print(compress(a)[1])
"""])


cards.append([3, """
def decompress(x):
  o = []
  l = len(x)
  for i in range(0,l,2):
    n = x[i+1]

    for k in range(n):
      o.append(x[i])

  return o

a = [1, 4, 2, 1, 3, 4]
print(decompress(a)[2])
"""])


cards.append([3, """
def delta(x):
  o = [x[0]]
  l = len(x)

  for i in range(1,l):
    p=x[i]
    c=x[i-1]

    o.append(p-c)

  return o

a = [1, 2, 3, 4, 5 ,6]
print(delta(a)[3])
"""])


cards.append([1, """
x = 0
for i in range(len('a')):
  x += 11

print(x)
"""])

cards.append([1, """
x = 0
while x < 10 or x < 5:
  x += 1

print(x)
"""])

cards.append([3, """
def is_prime(n):
  if n == 0 or n == 1:
    return False
  for x in range(2,n):
    if n%x == 0:
      return False

  return True

if is_prime(9):
    print(1)
elif is_prime(7):
    print(2)
else:
    print(3)
"""])


cards.append([3, """
# series converge to pi
# pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 ...
k = 1
s = 0
for i in range(1000):
  if i % 2 == 0:
    s += 4/k
  else:
    s -= 4/k
  k += 2
   
print(int(s))
"""])

cards.append([1, """
text = "hello 1 2 3"
s = text.split(" ")

print(s[1])
"""])

cards.append([1, """
a = \"""hello
this
is
a
multiline
string
\"""

lines = a.split('\\n')
print(len(lines))
"""])

cards.append([2, """
a = "h2llo"
b = 3

a += str(b)

print(a[len(a)-1])
"""])

cards.append([2, """
phones = {
    "Jack": 5551212,
    "John": 5556622,
    "Jill": 555621
}

s = phones["Jack"]
print(str(s)[0])
"""])

cards.append([1, """
a,b,c = [1,2,3]

print(c)
"""])


SCALE = 2
WIDTH = 1058 * SCALE
HEIGHT = 671 * SCALE
COLS = 33
ROWS = 28
fnt = ImageFont.truetype('font.ttf', 75)

bgcolor = (20, 20, 20, 255)
fgcolor = (178, 0, 255, 0)
#bgcolor = (255, 255, 255)
#fgcolor = (0, 0, 0)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def border(d, difficulty, data, id):
    lines = []
    bottom = '+-------------------------------+'
    top = '+----------->' + str(id).zfill(2) + ' @ ' + \
        str(difficulty).zfill(2)+'<-----------+'
    if difficulty == 0:
        top = bottom
    lines.append(top)


    text = data.split('\n')
    for i in range(ROWS):
      code = ''
      if i <= len(text) -1:
        code = text[i]
      code = code.ljust(COLS - 3, ' ')
      lines.append('| '+code+'|')
    lines.append(bottom)

    d.rectangle([0, 0, HEIGHT-1, WIDTH-1], outline=(0, 0, 0, 0))
    d.multiline_text((50, 50),"\n".join(lines), font=fnt, fill=fgcolor)


def back(id, difficulty, numbers):
    img = Image.new('CMYK', (HEIGHT, WIDTH), color=bgcolor)
    d = ImageDraw.Draw(img)
    lines = []
    for n in numbers:
        lines.append(str(n).rjust(random.randint(0,COLS - 3), ' '))

    border(d, 0, "\n".join(lines), 0)
      
    img.save(os.path.join('images', 'back_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def front(id, difficulty, code):
    img = Image.new('CMYK', (HEIGHT, WIDTH), color=bgcolor)
    d = ImageDraw.Draw(img)
    border(d, difficulty, code, id)
    img.save(os.path.join('images', 'front_card_' +
             str(id).zfill(3)+'.tiff'), compression="tiff_lzw")


def cheat(answers, numbers):
    for (n, a) in enumerate(list(chunks(answers, ROWS))):
        img = Image.new('CMYK', (HEIGHT, WIDTH), color=bgcolor)
        d = ImageDraw.Draw(img)
        border(d, 0, "\n".join(a), 0)
        img.save(os.path.join(
            'images', 'front_card_answers_'+str(n).zfill(3)+'.tiff'), compression="tiff_lzw")

        back(800 + n, 0, numbers)


def run(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    try:
        exec(code, globals())
    except Exception as e:
        old_stdout.write("error " + str(e) + ", code:" + code)
        raise(e)

    sys.stdout = old_stdout
    return redirected_output.getvalue()


qa = []
possible = set()
for (_i, card) in enumerate(cards):
    _out = run(card[1]).strip().split("\n")
    if len(_out) == 0:
        raise "NO OUTPUT: " + card[1]
    for line in _out:
        possible.add(line)
        qa.append(str(_i).zfill(3) + ": " + line)


random.seed(time.time())
shuffled = list(possible)

for (i, card) in enumerate(cards):
    random.shuffle(shuffled)
    rotate = cycle(shuffled)
    numbers = []
    for x in range(ROWS):
        numbers.append(next(rotate))
    front(i, card[0], card[1])
    back(i, card[0], numbers)


cheat(qa, numbers)
