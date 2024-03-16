

## [DAY-220] lists

![game-219.png](./screenshots/game-219.png "game 219 screenshot")

Improve the game to have an row of monsters that you have to avoid, also make the elf bounce left and right as well. It should be gameover if you collide with any of the monsters

> this is the game she made, she did some experimentation with random, and needed a bit of help with the list of monsters

```
import pgzrun

elf = Actor("c1")
elf.y = 50

WIDTH = 800
HEIGHT = 800
game_over = False
speed_y = 5
speed_x = 5
monsters = []
monster_speed_y = 1

for i in range(20):
    monster = Actor("c1")
    monster.x = 10 + (i * 70)
    monster.y = 10
    monsters.append(monster)


def update():
    global speed_y, speed_x, game_over

    elf.y += speed_y
    elf.x += speed_x

    if elf.y > 795:
        speed_y = -5
    if elf.y < 50:
        speed_y = 5
    if elf.x > 795:
        speed_x = -5
    if elf.x < 50:
        speed_x = 5

    if keyboard.A:
        elf.x += -5

    if keyboard.D:
        elf.x += 5

    for m in monsters:
        m.y += monster_speed_y
        if m.y > 795:
            m.y = 10
        if m.colliderect(elf):
            game_over = True


def draw():
    screen.fill("black")
    elf.draw()

    for m in monsters:
        m.draw()
    if game_over == True:
        screen.fill("pink")


pgzrun.go()
```


## [DAY-221] lists

Make the elf be able to attack the monsters with a bullet.

```
...
bull =  Actor("bullet")
bull.x = -10
bull.y = -19
bullet_speed=1
...

def update():
    ...
    if keyboard.SPACE:
        bull.x = elf.x + 10
    bull.x += 1
    ...
    for m in list(monsters):
        ...
        if m.colliderect(bull):
            monsters.remove(m)

def draw():
    ...
    bull.draw()
```

The key topic for discussion here is having bullet outside of the screen, and moving it in screen when the player hits SPACE.

And of course discussing removing from shallow clone of the list, which we have discussed many times so far, but it is still good to think about it.

```
a = [1,2,3]
b = list(a)
a.append(4)
print(a)
print(b)

c = a
c.append(5)
print(a)
print(b)
print(c)
```


## [DAY-222] lists

Make a boss that spawns after 20 mosters are defeated.

```
...
boss = Actor("c2")
boss.x = -200
boss.y = -200
counter = 0
...
def update():
    global counter
    ...
    for m in list(monsters):
        ...
        if m.colliderect(bull):
            monsters.remove(m)
            counter++
            if counter > 20:
                boss.x = 400
                boss.y = 400



def draw():
    ...
    boss.draw()
```

Using the same pattern as the player's bullet, we draw the boss off-screen, we keep a counter of how many monsters are killed and once we kill more than 20, we move the boss in the middle of the screen.


## [DAY-223] lists

![game-223.png](./screenshots/game-223.png "game 223 screenshot")

Make the boss shoot bullets in 4 directions

```
...
boss_bullets = []
bossIsAlive = False
...

def new_boss_bullet(x,y, where_to_go):
    #      KEY | VALUE
    #      ----+------
    #     image| "bullet"
    #        x | 47
    #        y | 27
    # direction| "right"

    b = Actor("bullet")
    b.x = x
    b.y = y
    b.direction = where_to_go

...
def update():
    global bossIsAlive
    ...
    if timer > 120:
        ...
        if bossIsAlive:
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"left"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"right"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"up"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"down"))

        timer = 0
    for m in list(monsters):
        ...
        if m.colliderect(bull):
            ...
            if counter > 20:
                bossIsAlive = True
                ...
    if bossIsAlive:
        for b in boss_bullets:
          if b.direction == "left":
              b.x -= speed
          if b.direction == "right":
              b.x += speed
          if b.direction == "up":
              b.y -= speed
          if b.direction == "down":
              b.y += speed

def draw():
    ...
    if bossIsAlive:
        boss.draw()
        for b in boss_bullets:
            b.draw()
```


Think about the objects in python like the tables in Lua, you can just add another row in the table, in our case we will add "direction" and we will put there the value we need.


## [DAY-224] lists

Make the boss die after being hit by 10 player bullets, and also make it so that the boss bullets kill the player if hit

```
...
bossHP = 100
...

def update():
    global bossHP
    ...
    if bossIsAlive:
        if boss.colliderect(elf):
            game_over = True
        for b in boss_bullets:
            if b.colliderect(elf):
                game_over = True
        if bull.colliderect(boss):
            bossHP -= 10
            bull.y = -100

            # move the boss a tiny amount
            boss.x += random.randint(-10,10)
            boss.y += random.randint(-10,10)

            if bossHP <= 0:
                bossIsAlive = False
        ...
```



## [DAY-225] functions

Make the elf bullet move in a random direction, reuse the code for moving the boss bullet

```
...
def move(speed,b):
    if b.direction == "left":
        b.x -= speed
    if b.direction == "right":
        b.x += speed
    if b.direction == "up":
        b.y -= speed
    if b.direction == "down":
        b.y += speed
    if b.direction == "diagonal_right":
        b.y += speed
        b.x += speed
...
def update():
    ...
    if keyboard.K_1:
        bull.direction= random.choice(['up','left','down','right', 'diagonal_right'])
    ...
    move(bullet_speed,bull)
    bullet_speed *= 1.06
    if bullet_speed > 20:
        bullet_speed = 1
    ...
    if bossIsAlive:
        for b in boss_bullets:
            move(1,b)
        ...
```

Our `move` function can work with **any** object that has the `direciton`, `x`  and `y` properties, it doesn't even care if its a bullet or a car.


## [DAY-226] lists

In the last few days we did few small refactors and improvements, e.g. improve the timer function to support multiple different seconds by using ever increasing number and checking if `timer % x_seconds == 0`. Split the code into `update_player`, `update_boss` etc, so that its easier to find the code.

Today's task is to make the player have 4 bullets instead of 1, and also increase the boss's bullet speed when he gets to low HP.

> This is how the code that we wrote together, she wrote most of it, but I helped as well. We spend a lot of time discussing patterns like having global timer that functions can check, or using a variable for a condition (e.g. if bossHP < 20 then speed = 4)


```
import random
import pgzrun
import math


def make_new_monster(x, y):
    monster = Actor("monster")
    monster.x = x
    monster.y = y
    return monster


def second(n):
    return (timer % math.floor((n * 60))) == 0


def new_boss_bullet(x, y, where_to_go):
    #      KEY | VALUE
    #      ----+------
    #     image| "bullet"
    #        x | 47
    #        y | 27
    # direction| "right"
    b = Actor("bullet")
    b.x = x
    b.y = y
    b.direction = where_to_go
    return b


elf = Actor("c1")
elf.y = 50
bullet_speed = 1
bull = []
bull.append(new_boss_bullet(-100, -10, "right"))
bull.append(new_boss_bullet(-100, -10, "left"))
bull.append(new_boss_bullet(-100, -10, "up"))
bull.append(new_boss_bullet(-100, -10, "down"))


WIDTH = 800
HEIGHT = 800
game_over = False
monsters_killed = 0

monsters = []
monster_speed_y = 1
for i in range(10):
    m = make_new_monster(i*100, 10)
    monsters.append(m)

boss = Actor("c2")
boss_bullets = []
bossIsAlive = False
bossHP = 100

timer = 1


def move(speed, b):
    if b.direction == "left":
        b.x -= speed
    if b.direction == "right":
        b.x += speed
    if b.direction == "up":
        b.y -= speed
    if b.direction == "down":
        b.y += speed
    if b.direction == "diagonal_right":
        b.y += speed
        b.x += speed


def update_player_bullet():
    global bullet_speed

    if keyboard.SPACE:
        for b in bull:
            b.x = elf.x+25
            b.y = elf.y + 5
        bullet_speed = 1
    if second(0.3):
        bullet_speed *= 1.20
        if bullet_speed > 20:
            bullet_speed = 1
    for b in bull:
        move(bullet_speed, b)


def update_player():
    global game_over
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x += -5
    if keyboard.D:
        elf.x += 5
    for b in bull:
        if elf.colliderect(b):
            game_over = True


def update_monsters():
    global game_over, monsters_killed, monsters

    for m in list(monsters):
        m.y += monster_speed_y
        if m.y > 795:
            m.y = 10

        if m.colliderect(elf):
            game_over = True
        for b in bull:
            if m.colliderect(b):
                if m in monsters:
                    monsters.remove(m)
                    monsters_killed += 1

    if second(5):
        m = make_new_monster(random.randint(10, 790), -10)
        monsters.append(m)


def reset_game():
    global game_over, timer, monsters
    game_over = False
    monsters = []
    for i in range(10):
        m = make_new_monster(i*100, 10)
        monsters.append(m)
    timer = 1
    elf.y = 500
    elf.x = 500


def update_boss():
    global game_over, bossIsAlive, monsters_killed, bossHP
    if bossIsAlive:
        for b in boss_bullets:
            if b.colliderect(elf):
                game_over = True
            for b in bull:
                if b.colliderect(boss):
                    bossHP -= 15
                    b.x = -100
                    b.y = -100
                    boss.x += random.randint(-10, 10)
                    boss.y += random.randint(-10, 10)
                    if bossHP <= 0:
                        bossIsAlive = False
                        boss.x = -1000
                        boss.y = -1000
                        monsters_killed = 0

        if second(3):
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "left"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "right"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "up"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "down"))

        boss_bullet_speed = 1
        if bossHP < 20:
            boss_bullet_speed = 5
        for b in boss_bullets:
            move(boss_bullet_speed, b)
    else:
        if monsters_killed > 1:
            boss.x = 400
            boss.y = 350
            bossIsAlive = True


def update():
    global timer
    update_player()
    update_player_bullet()
    update_monsters()
    update_boss()

    timer += 1

    if keyboard.R:
        reset_game()


def draw():
    screen.fill("white")
    elf.draw()
    for b in bull:
        b.draw()

    if bossIsAlive:
        boss.draw()
        for b in boss_bullets:
            b.draw()

    for m in monsters:
        m.draw()


pgzrun.go()
```
