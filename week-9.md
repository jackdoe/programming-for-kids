# Chapter 9 - Week 9

```
day0: pygame and pgzero
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```


## [DAY-61] pygame and pgzero

open `cmd` and run:

```
pip install pygame
pip install pgzrun
```

then make a circle

```
import pgzrun
WIDTH = 400
HEIGHT = 400
 
def draw():
    screen.clear()
    x = WIDTH/2
    y = WIDTH/2
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

Now lets move it:

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400

x = WIDTH/2
y = WIDTH/2

def on_mouse_down(pos):
    global x,y
    (mouse_x, mouse_y) = pos

    x = mouse_x
    y = mouse_y


def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

Move it with keyboard

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
STEP = 10
x = WIDTH/2
y = WIDTH/2


def on_key_down(key):
    global x,y
    if key == keys.LEFT:
        x -= STEP
    elif key == keys.RIGHT:
        x += STEP
    elif key == keys.UP:
        # coordinates start 0,0 on the upper left corner
        y -= STEP
    elif key == keys.DOWN:
        y += STEP

def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

Lets say we have 400 width and 300 height window

```
(0,0)
  +---------------------------+
  |                           |
  |                           |
  |                           |
  |                           |
  |                           |
  |                           |
  +---------------------------+
                          (400, 300)
```

top left corner is y = 0 and x = 0, bottom right is `x = 400` and `y = 300`. So when we move 'UP' with the keyboard we actually have to decrease `y` instead of increasing it like in `turtle`, where 0,0 is in the center of the screen, so top left is `(-half_x, -half_y)` and bottom right is `(half_x, half_y)`

## [DAY-62] Basics of Basics


Smooth movement.

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
STEP = 10
x = WIDTH/2
y = WIDTH/2


def update():
    global x,y
    if keyboard.LEFT:
        x -= STEP
    elif keyboard.RIGHT:
        x += STEP
    elif keyboard.UP:
        y -= STEP
    elif keyboard.DOWN:
        y += STEP

def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

`pgzero` will call your `update` function 60 times per second, and now it will just check at the time of the call, is `keyboard.UP`, and if it is it will just move. Which is completely different, where each time you press the `up` key the `on_key_down` function is called. So previously you had ot press the key every time to move, now you can just hold it.

Where do those `keyboard` and `screen` magic variables come from? In python there is such thing as `__builtin__` which literally adds new keywords, kind of like `input` or `print`, when you `import pgzrun` it will import also those builtins. `Actor`, `Rect`, `keyboard` etc.. you can check them at https://pygame-zero.readthedocs.io/en/stable/builtins.html

COLLIDE!

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
STEP = 10
x = WIDTH/2
y = WIDTH/2

box = Rect((20,20),(100,100))

game_over = False


def update():
    global x, y, game_over
    if keyboard.LEFT:
        x -= STEP
    elif keyboard.RIGHT:
        x += STEP
    elif keyboard.UP:
        y -= STEP
    elif keyboard.DOWN:
        y += STEP

    if box.collidepoint((x,y)):
        game_over = True

def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.rect(box, color="red")
    screen.draw.circle(pos, radius, 'white')

    if game_over:
        screen.draw.text("GAME OVER", (50, 30), color="blue")
 
pgzrun.go()

```


## [DAY-63] Basics of Basics
## [DAY-64] Basics of Basics
## [DAY-65] Basics of Basics
## [DAY-66] Basics of Basics
## [DAY-67] Basics of Basics
