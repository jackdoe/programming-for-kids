## [DAY-302] classes

Watch Bro Code's Python Object Oriented Programming in 10 minutes video: https://www.youtube.com/watch?v=q2SGW2VgwAM , then make a class Line that has all the properties, and also has a method draw that draws the line to the screen, having a dynamic end point.

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
elf.x = 500
elf.y = 500

king = Actor('c2')
king.x = 200
king.y = 200

class Line:
    def __init__(self):
        self.x = random.randint(10,790)
        self.y = random.randint(10,790)
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        self.to = random.choice(["king","elf"])
        self.xd = random.randint(0,50)
        self.yd = random.randint(0,50)

    def draw(self,to_x,to_y):
        screen.draw.line([self.x,self.y],
                         [to_x - self.xd ,to_y - self.yd],
                         [self.r,self.g,self.b])

lines = []
for i in range(800):
    l = Line()
    lines.append(l)

def update():
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
    if keyboard.LEFT:
        king.x+=5
    if keyboard.RIGHT:
        king.x-=5


def draw():
    screen.fill('black')
    elf.draw()
    king.draw()

    for line in lines:
        if line.to == "king":
            line.draw(king.x,king.y)
        else:
            line.draw(elf.x,elf.y)

pgzrun.go()
```

## [DAY-303] lists

Record the wasd key pressess and show them on the screen:

![game-303.png](./screenshots/game-303.png "game 303 screenshot")

```
import pgzrun

WIDTH = 800
HEIGHT = 800

lines = []
def on_key_down(key,mod):
    if key == keys.W:
        lines.append("W")
    if key == keys.S:
        lines.append("S")
    if key == keys.A:
        lines.append("A")
    if key == keys.D:
        lines.append("D")

def update():
    pass

def draw():
    screen.clear()
    screen.draw.text(''.join(lines), (255,255),color=(23,233,123))


pgzrun.go()
```

This is the first step towards making an editor.


## [DAY-304] lists

Add more keys to your editor.

![game-304.png](./screenshots/game-304.png "game 303 screenshot")

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

lines = []
def on_key_down(key,mod):
    if key == keys.W:
       lines.append("W")
    if key == keys.S:
        lines.append("S")
    if key == keys.A:
        lines.append("A")
    if key == keys.D:
        lines.append("D")
    if key == keys.B:
        lines.append("B")
    if key == keys.C:
        lines.append("C")
    if key == keys.SPACE:
        lines.append(" ")
    if key == keys.RETURN:
        lines.append("\n")
    if key == keys.D:
        lines.append("D")
    if key == keys.E:
        lines.append("E")
    if key == keys.F:
        lines.append("F")
    if key == keys.G:
        lines.append("G")
    if key == keys.H:
        lines.append("H")
    if key == keys.I:
        lines.append("I")
    if key == keys.J:
        lines.append("J")
    if key == keys.K:
        lines.append("K")
    if key == keys.L:
        lines.append("L")
    if key == keys.M:
        lines.append("M")
    if key == keys.N:
        lines.append("N")
    if key == keys.O:
        lines.append("O")
    if key == keys.P:
        lines.append("P")
    if key == keys.Q:
        lines.append("Q")
    if key == keys.R:
        lines.append("R")
    if key == keys.T:
        lines.append("T")
    if key == keys.U:
        lines.append("U")
    if key == keys.V:
        lines.append("V")
    if key == keys.X:
        lines.append("X")
    if key == keys.Y:
        lines.append("Y")
    if key == keys.Z:
        lines.append("Z")

def update():
    pass

def draw():
    screen.clear()
    screen.draw.text(''.join(lines), (255,255),color=(23,233,123))

pgzrun.go()
```

Given the `is_shift` function, add support for lower and upper characters:

```
def is_shift(mod):
    return mod & keymods.LSHIFT > 0
```

example:


```
   if key == keys.W:
        if is_shift(mod):
            lines.append("W")
        else:
            lines.append("w")
```


## [DAY-305] lists

![game-305.png](./screenshots/game-305.png "game 305 screenshot")

Print and think about what each component of the following code does:

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
elf.x = 500
elf.y = 500

enemies = []
game_over = False
game_win = False

def add_row(y):
    has_gold = False
    for x in range(10):
        kind = 'c2'
        # we want at most one golden king on a random position
        if not has_gold and random.randint(0,10) < 3:
            kind = 'c3'
            has_gold = True
            
        e = Actor(kind)
        e.x = 100 + (x * 30)
        e.y = y
        enemies.append(e)

    enemies.append(e)
    

def increase_dificulty():
    max_y = 0
    for e in enemies:
        if e.y > max_y:
            max_y = e.y

    add_row(max_y + 40)

def on_mouse_down(pos):
    global game_over, game_win
    for e in list(enemies):
        if elf.colliderect(e):
            if e.image == 'c3':
                game_over = True
                break
            enemies.remove(e)
            break

    # check how many kings we have not counting the golden kings
    n_enemies = 0
    for e in enemies:
        if e.image == 'c2':
            n_enemies += 1
    # if there are no kings left, then we win the game
    if n_enemies == 0:
        game_win = True

def on_mouse_move(pos):
    elf.x = pos[0]
    elf.y = pos[1]


def update():
    for e in enemies:
        e.x += random.randint(-1,3)
        if e.x > 700:
            e.x = 100


increase_dificulty()
clock.schedule_interval(increase_dificulty, 10)

def draw():
    screen.fill('black')
    elf.draw()
    screen.draw.line([100,700], [elf.x,elf.y], [255,0,0])
    screen.draw.line([700,700], [elf.x,elf.y], [255,0,0])
    
    for e in enemies:
        e.draw()

    if game_over:
        screen.fill('red')
    elif game_win:
        screen.fill('blue')

pgzrun.go()
```


## [DAY-306] lists

![game-306.png](./screenshots/game-306.png "game 306 screenshot")

Make a program with 50 enemies, and make a line from each enemy to each other enemy

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

enemies = []
# make 50 enemies
for i in range(50):
    e = Actor("c2")
    e.x = random.randint(10, 790)
    e.y = random.randint(10, 790)
    enemies.append(e)

def update():
    # move them randomly left and right
    for e in enemies:
        e.x += random.randint(-5,5)
        e.y += random.randint(-5,5)

def draw():
    screen.fill('black')

    # make a line from each enemy to each other enemey
    for from_enemy in enemies:
        for to_enemy in enemies:
            if from_enemy != to_enemy:
                screen.draw.line([from_enemy.x,from_enemy.y], [to_enemy.x,to_enemy.y], [255,0,0])
    
    for e in enemies:
        e.draw()

pgzrun.go()
```

experiment with for in for, for example:

```
for i in range(10):
    for j in range(10):
        print(i,j)

```

```
l = ['a','b','c']
for a in l:
    for b in l:
        print(a,b)
```

![game-306-a.jpg](./screenshots/game-306-a.jpg "game 306 a screenshot")


## [DAY-307] for


make the following python program in c:

```
for i in range(10):
  for j in range(12):
    for k in range(14):
      print(i,j,k)
```

becomes:

```
#include <stdio.h>
int main(void){
    for(int i=0; i < 10; i++){
        for(int j=0; j < 12; j++){
            for(int k=0; k < 14; k++){
                printf("%d %d %d\n",i,j,k);
            }
        }
    }
    return 0;
}
```
