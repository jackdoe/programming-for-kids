from io import StringIO
import random
import sys
from itertools import cycle
from PIL import Image, ImageDraw, ImageFont


cards = [
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
"""
]

WIDTH = 1050 
HEIGHT = 600


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
""", font=fnt, fill=(255, 176, 0))

fnt = ImageFont.truetype('Perfect DOS VGA 437.ttf', 35)

def back(id, numbers):
    img = Image.new('RGB', (HEIGHT, WIDTH), color = (0,0,0))
    d = ImageDraw.Draw(img)
    border(d)
    x = random.randint(60, 500) 
    y = 60 + random.randint(0,80)
    for n in numbers:
        d.text((x,y), str(n), font=fnt, fill=(255, 176, 0))
        y += 80
        x = random.randint(60, 500)
    img.save('images\\card_'+str(id)+'_back.png')

def front(id, code):
    img = Image.new('RGB', (HEIGHT, WIDTH), color = (0,0,0))
    d = ImageDraw.Draw(img)
    border(d)
    d.multiline_text((60,60), code, font=fnt, fill=(255, 176, 0))
    img.save('images\\card_'+str(id)+'_front.png')


def run(code):
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(code)
    sys.stdout = old_stdout
    return redirected_output.getvalue()

possible = []
for card in cards:
    for line in run(card).strip().split("\n"):
        possible.append(line)


random.shuffle(possible)
rotate = cycle(possible)
for (i,card) in enumerate(cards):
    numbers = []
    for x in range(10):
        numbers.append(next(rotate))
    front(i, card)
    back(i, numbers)

