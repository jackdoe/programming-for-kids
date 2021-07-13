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

![game-62.png](./screenshots/game-62.png "game 62 screenshot")


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

Catch the snake

![game-63.png](./screenshots/game-63.png "game 63 screenshot")

Make images/ folder and download the images from https://github.com/jackdoe/programming-for-kids. When you say `Actor("c1")` it will look for `c1.png` in images/ folder in the current directory.

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
elf = Actor("c1")
snake = Actor("snake")
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def update():
    global game_over, speed, score
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0

    if elf.colliderect(snake):
        score += 1
        speed += 1
        place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))                         
pgzrun.go()

```


## [DAY-64] Basics of Basics

Many Snakes

![game-64.png](./screenshots/game-64.png "game 64 screenshot")

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 1
speed = 1
elf = Actor("c1")
snakes = []
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snakes():
    global snakes
    snakes = []
    for i in range(score):
        snake = Actor("snake")
        snake.x = random.randint(10,WIDTH-10)
        snake.y = random.randint(10,HEIGHT-10)
        snakes.append(snake)

place_snakes()

def update():
    global game_over, speed, score, snakes
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0
        snakes = []
        place_snakes()
    for s in snakes:
        if elf.colliderect(s):
            score += 1
            speed += 1
            place_snakes()

def draw():
    screen.fill('black')
    elf.draw()
    for s in snakes:
        s.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))                         
pgzrun.go()
```
## [DAY-65] Basics of Basics

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
game_over = False
elf = Actor("c1")
snake = Actor("snake")
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def update():
    global game_over, speed, score
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0

    if elf.colliderect(snake):
        score += 1
        speed += 1
        place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))                         
pgzrun.go()

```


## [DAY-66] Basics of Basics

Catch as many snakes as you can in 5 seconds.

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

game_over = False
score = 0
speed = 1
elf = Actor("c1")
snake = Actor("snake")
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def time_is_up():
    global game_over
    game_over = True

def update():
    global game_over, speed, score
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0

    if elf.colliderect(snake):
        score += 1
        speed += 1
        place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))

    if game_over:
        screen.fill('blue')
        screen.draw.text("GAME OVER, Score: "+ str(score), color="white", topleft=(10,10))

clock.schedule(time_is_up, 5)
pgzrun.go()
```


You see we just overwrite the screen with 'blue' and write another text, but you can still move in the back and the score will update if you catch a sneak.

If you want to stop the hero to move outside of the window, simply restrict elf.x and elf.y to be smaller than 0 or bigger than WIDTH and HEIGHT

Example:


```
def update():
    ...
    if keyboard.left:
        elf.x = elf.x-speed
        if elf.x > WIDTH:
            elf.x = WIDTH

```

## [DAY-67] Basics of Basics

Cross the road. Work with your parent to find images for the game, you need few cars, fox and a door. If not just use the existing assets from your images/ folder

```
import pgzrun
import random

HEIGHT = 1000
WIDTH = 1200

score = 0
step = 5
coin_speed = 1
fox = Actor("fox")
gate = Actor("door")
gate.y = HEIGHT - 50
gate.x = WIDTH/2 - 20
cars=[
    [Actor("car-2"),Actor("car-5"),Actor("car-3")],
    [Actor("car-1"),Actor("car-5")],
    [Actor("car-3"),Actor("car-4"),Actor("car-2")],
]

for a in cars:
    for (coin_index,f) in enumerate(a):
        f.x += coin_index * int(WIDTH/len(a)) + 30
def move_coins():
    for (index,a) in enumerate(cars):
        for (coin_index, f) in enumerate(a):
           
            f.y = (index * int(HEIGHT/len(cars))) + int(HEIGHT/len(cars))/2
            f.x += coin_speed
            if f.x > WIDTH:
                f.x = 0

game_over = False
move_coins()

def update():
    global score
    global step
    global game_over
    global coin_speed
    if keyboard.left:
        fox.x = fox.x-step
        if fox.x <0:
            fox.x=0
    if keyboard.right:
        fox.x = fox.x+step
        if fox.x >WIDTH:
            fox.x=WIDTH
    if keyboard.up:
        fox.y =fox.y-step
        if fox.y <0:
            fox.y=0
    if keyboard.down:
        fox.y= fox.y+step
        if fox.y >HEIGHT:
            fox.y=HEIGHT
    if keyboard.R:
        game_over = False
        score = 0
        fox.x = 0
        fox.y = 0
        coin_speed = 1
    for i in cars:
        for s in i:
            if fox.colliderect(s):
                game_over = 1 == 1

    if fox.colliderect(gate):
        fox.x = 0
        fox.y = 0
        score += 1
        coin_speed += 2
    move_coins()

def draw():
    screen.fill('black')
    fox.draw()
    gate.draw()

    for i in cars:
        for k in i:
            k.draw()
    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))
    if game_over:
        screen.fill("blue")
        screen.draw.text("Final Score: "+ str(score), color="white", topleft=(10,10),fontsize=60)    
                         
pgzrun.go()
```