

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

