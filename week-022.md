
## [DAY-150] While; Classes

Circles And Squares.

![game-150.png](./screenshots/game-150.png "game 150 screenshot")

```
from turtle import *

bgcolor('black')

a = Turtle()
a.speed(0)
a.hideturtle()

b = Turtle()
b.speed(0)
b.hideturtle()

colorA = textinput('pencolor a',"what is your name?:")
colorB = textinput('pencolor b',"what is your name?:")

size = 0
while True:
    b.pencolor(colorB)
    b.forward(size*3)
    b.left(91)

    a.pencolor(colorA)
    a.forward(size*10)
    a.circle(size, 360)
    a.left(500)

    size += 1
```

More circles

![game-150-a.png](./screenshots/game-150-a.png "game 150-a screenshot")

```
import turtle as t
t.bgcolor('black')
t.hideturtle()
size = -300
t.speed(0)
while True:
    if size % 2 == 0:
        t.pencolor('cyan')
    else:
        t.pencolor('magenta')

    t.circle(size*3)
    size += 1
```





## [DAY-152] Lists

![game-152.png](./screenshots/game-152.png "game 152 screenshot")

Make 3 actors you can pick up and drop them wherever you hit SPACE.

```
import pgzrun

WIDTH = 500
HEIGHT = 500

king = Actor('c2')
elf = Actor('c1')
flower =  Actor('flower')
rock = Actor('rock')

king.x = 480
king.y = 125
flower.y = 380
flower.x = 480
rock.x = 480
rock.y = 250

drop = []

speed = 5
def update():
    global speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.D:
        elf.x += speed
    if keyboard.A:
        elf.x -= speed
    if keyboard.C:
        screen.clear()

    if elf.colliderect(king):
        elf.image=king.image
        speed = 2
    if elf.colliderect(rock):
        elf.image=rock.image
        speed = 1
    if elf.colliderect(flower):
        elf.image=flower.image
        speed = 10
    if keyboard.SPACE and elf.image != 'c1':
        a = Actor(elf.image)
        a.x = elf.x
        a.y = elf.y
        drop.append(a)

        elf.image='c1'
        speed = 5

def draw():
    screen.clear()
    elf.draw()
    king.draw()
    flower.draw()
    rock.draw()
    for d in drop:
        d.draw()

pgzrun.go()
```