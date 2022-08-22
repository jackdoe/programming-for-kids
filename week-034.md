## [DAY-234] lists


Make a game where a bunch of enemies are moving in random direction.

> variable names are hers, and also the numbers for the movement
```
import pgzrun
import random
game_over=False
HEIGHT=800
king=Actor("c2")
king.y=300
WIDTH=800
HEIGHT=800
lon=[]
for i in range(10):
    elf=Actor("c1")
    elf.x=random.randint(10,790)
    elf.y=random.randint(10,790)
    lon.append(elf)

def update():
    global game_over
    if keyboard.W:
        king.y-=5
    if keyboard.S:
        king.y+=5
    if keyboard.A:
        king.x-=5
    if keyboard.D:
        king.x+=5


    for e in lon:
        if king.colliderect(e):
            game_over=True
        e.x+=random.choice([-1,+1,2,+3,-9,4,5,+3,7,12])
        e.y+=random.choice([+3,+3,+4,+4,+5,+7,+1,+2,+5,+13])

    if e.y>800:
        e.y=10
    if e.x>800:
        e.x=10

def draw():
    screen.fill('black')
    if game_over==True:
        screen.fill('pink')
        
    king.draw()

    for e in lon:
        e.draw()

pgzrun.go()
```

## [DAY-234] lists

Make the previous game into jumpscare game, when enemy hits you show scary image and play scary soubd.

```
...
corgi = Actor("narutoz")
maxx=Actor("gaaras")
...
def draw():
    ...
    if game_over==True:
        screen.fill('pink')
        scary = random.choice([corgi,maxx])
        scary.draw()
        sounds.retro.play()
...
```
