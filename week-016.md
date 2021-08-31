# Chapter 14 - Week 14

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```

## [DAY-109] Basics of Basics

Touchtyping day!

## [DAY-110] Basics of Basics


![game-109.png](./screenshots/game-109.png "game 109 screenshot")

follow zippycode on tiktok https://www.tiktok.com/@zippycode
try some of their ideas, like:

```
from turtle import *
bgcolor('black')
n = 0
colormode(255)
while n < 200:
    right(n)
    forward(n*3)
    color(n,255-n,n%30*8)
    n+=1
```


```
from turtle import *
color('green')
speed(11)
i = 0
while True:
    circle(i*1.5)
    right(4)
    i+=1
```

## [DAY-111] Basics of Basics
![game-110.png](./screenshots/game-110.png "game 110 screenshot")

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
fox = Actor("c1")
fox.x= WIDTH/2
fox.y=HEIGHT/2

other = [
    Actor("c2", pos=(100,100)),
    Actor("c2", pos=(100,300)),
    Actor("c2",pos=(300,300)),
    Actor("c2",pos=(300,100))
]


def update():
    if keyboard.left:
        for o in other:
            o.x += 5
    if keyboard.right:
        for o in other:
            o.x -= 5
    if keyboard.up:
        for o in other:
            o.y += 5
    if keyboard.down:
        for o in other:
            o.y -= 5

    for o in list(other):
        if o.colliderect(fox):
            other.remove(o)
    if len(other) < 4:
        other.append(Actor("c2",pos=(random.randint(10,WIDTH-10), random.randint(10,HEIGHT-10))))

    for o in other:
        o.y -=1

def draw():
    screen.clear()
    screen.fill("deepskyblue")
    fox.draw()
    for o in other:
        o.draw()
pgzrun.go()
```

## [DAY-112] Basics of Basics
## [DAY-113] Basics of Basics
## [DAY-114] Basics of Basics
## [DAY-115] Basics of Basics
