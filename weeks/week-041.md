## [DAY-280] ast


![game-280.jpg](./screenshots/game-280.jpg "game 280 screenshot")

> again we spent the day with AST examples, this time we did FROM ast TO python program, and particularly discussing AST that makes a program that looks valid, but errors at runtime


## [DAY-281] ast

![game-281-a.jpg](./screenshots/game-281-a.jpg "game 281 a screenshot")

![game-281-b.jpg](./screenshots/game-281-b.jpg "game 281 b screenshot")


Using `()` you can force python to build certain kind of AST, for example:

```
a = 1
b = 2
c = 3

if a > b or c > a and b > c:
    print('zz')
```

python reads it right to left as: 'if (a is bigger than b) **OR** (c is bigger than a and b is bigger than c)', but if we write:

```
if (a > b or c > a) and b > c:
    print('zz')
```

python will read 'if (a is bigger than b or c is bigger than a) **AND** (b is bigger than c)',

## [DAY-282] ast

![game-282.jpg](./screenshots/game-282.jpg "game 282 screenshot")

> just 5 minutes while waiting for dinner do a quick ast parse

## [DAY-283] ast

![game-283.jpg](./screenshots/game-283.jpg "game 283 screenshot")

> 5 minutes after dinner (as visible by the pizza oil stains on the paper..), focused a bit on the implicit 'self' argument when calling a method


## [DAY-284] ast

![game-284.jpg](./screenshots/game-284.jpg "game 284 screenshot")

> before going to bed we did a quick ast discussion, what happens if you dont know the precedence and how to overpower the ast using brackets


## [DAY-285] for

![game-285.jpg](./screenshots/game-285.jpg "game 285 screenshot")

Make a game where you have a wall of foxes you cant pass through, and make it so that the elf cant pass through them, but the king can, and the king can pass through the foxes but but not through the elf.

![game-285-b.jpg](./screenshots/game-285-b.jpg "game 285 b screenshot")

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

foxes=[]
elf = Actor('c1')
king = Actor("c2")
elf.x = 500
elf.y = 500
king.x = 400
king.y = 400

for i in range(38,250,62):
    foxes.append(Actor("fox",[i,38]))
for i in range(0,250,62):
    foxes.append(Actor("fox",[i,250]))
for i in range(250,700,83):
    foxes.append(Actor("fox",[250,i]))


def update():
    old_elf_x = elf.x
    old_elf_y = elf.y
    old_king_x = king.x
    old_king_y = king.y
    if keyboard.W:
        elf.y-=5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x-=5
    if keyboard.D:
        elf.x+=5
    if keyboard.UP:
        king.y-=5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.RIGHT:
        king.x+=5
    if keyboard.LEFT:
        king.x-=5

    elf.y += 1
    for i in foxes:
        if elf.colliderect(i):
            elf.y=old_elf_y
            elf.x=old_elf_x
    if king.colliderect(elf):
        king.y=old_king_y
        king.x=old_king_x



def draw():
    screen.fill('black')
    elf.draw()
    king.draw()
    for i in foxes:
        i.draw()

pgzrun.go()
```

## [DAY-286] ast

![game-286.jpg](./screenshots/game-286.jpg "game 286 screenshot")

> just 5 minutes before going to bed
