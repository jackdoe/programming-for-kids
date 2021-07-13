# Chapter 10 - Week 10

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```


## [DAY-68] Basics of Basics

Shoot bullets and remove them from the list, play sound, and also level up after killing 3 snakes!


![game-68.png](./screenshots/game-68.png "game 68 screenshot")


```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
elf = Actor("c1")
snake = Actor("snake")
beep = tone.create('A3', 0.5)

elf.x = WIDTH/2
elf.y = HEIGHT/2
bullets = []

def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def bullet_out_of_screen():
    # just delete the first bullet
    bullets.pop(0)

def on_key_down(key):
    if key == keys.SPACE:
        b = Actor("bullet2")
        b.x = elf.x + 5
        b.y = elf.y
        animate(b, pos=(WIDTH + 100, elf.y), tween='accelerate', on_finished=bullet_out_of_screen)
        bullets.append(b)
        
def update():
    global game_over, speed, score, bullets
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
        elf.image = "c1"
        bullets = []

    for b in bullets:
        if b.colliderect(snake):
            score += 1
            speed += 1
            if score == 3:
                elf.image = "c2"
            beep.play()
            place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()
    for b in bullets:
        b.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))

pgzrun.go()
```

## [DAY-69] Basics of Basics
## [DAY-70] Basics of Basics
## [DAY-71] Basics of Basics
## [DAY-72] Basics of Basics
## [DAY-73] Basics of Basics
## [DAY-74] Basics of Basics
