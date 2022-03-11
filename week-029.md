
## [DAY-199] coordinates

Add a blur around the cutescare game's actor so the game is more spooky

![game-199.png](./screenshots/game-199.png "game 199 screenshot")

Use images/fog.png which is a 2000x2000 black png with a transparent circle in the middle, we will use it to create "fog" around the player.

Read on https://pygame-zero.readthedocs.io/en/stable/builtins.html about how to anchor an actor so that the fog's x and y are actually at the center and not in the topleft.

Add a game level sound to make the game more fun, read in the pygame-zero docs how to loop a sound forever.

```
...
elf = Actor("c1")
elf.x = 520
elf.y = 420
...
fog = Actor("fog", anchor=("center","center"))

def update():
    ...
    if not isInside:
        elf.x = 520 
        elf.y = 420
    # move the fog's center to where the elf is 
    # so the elf is always in the center of the fog
    fog.x = elf.x
    fog.y = elf.y

...

sounds.level.play(-1)

def draw():
    screen.clear()
    for r in data:
        screen.draw.rect(r, (255,255,255))
    elf.draw()
    fog.draw()
    ...

pgzrun.go()
```



## [DAY-200] coordinates


Make a better maze

```
...

data = [
    Rect(0,0,100,200),
    Rect(20,200, 300, 30),
    Rect(267,226, 30, 500),
    Rect(408,678, 20, 200),
    Rect(23,659, 800, 20),
    Rect(429,101, 30, 500),
    Rect(299,356, 800, 20)
]

...
```

![game-200-a.png](./screenshots/game-200-a.png "game 200-a screenshot")


![game-200-b.png](./screenshots/game-200-b.png "game 200-b screenshot")
