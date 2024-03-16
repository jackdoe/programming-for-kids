## [DAY-130] turtle; lists; classes

![game-130.png](./screenshots/game-130.png "game 130 screenshot")

many turtles

```
import turtle
import random
colors = ['violet', 'turquoise', 'black', 
          'deepskyblue','lawngreen', 'seagreen ', 
          'royalblue', 'purple', 'red','orange']

turtles = []
for i in range(10):
    t = turtle.Turtle()
    t.color(random.choice(colors))
    t.speed(9000)
    turtles.append(t)


while True:
    for i in range(len(turtles)):
        t = turtles[i]
        t.setheading(random.randint(0,360))
        t.forward(10)
```

Lets practice making a new class, you see when we say Turtle() or Actor() we make a new instance of the class Turtle and the class Actor

The Class itself is like a blueprint of how to make a new instance of itself, for example lets make a class Point that has two properties, `x` and `y`

```
class Point:
    x = 0
    y = 0

points = []
for i in range(10):
    p = Point()
    p.x = i * 20
    p.y = i * 20
    points.append(p)

for p in points:
    print(p, p.x, p.y)
```

When you define a function in a class, you have access to special parameter, `self` which is the instance on which this function is called:

```
class Dog:
    name = ''
    def bark(self):
        print(self.name+' woof woof woof')

max = Dog()
max.name = 'Maxie'
max.bark()

rocky = Dog()
rocky.name = "Rocky"
rocky.bark()

```

There is also a special `__init__` function, called constructor that lets you pass parameters directly when you create the instance.

```
class Point:
    x = 0
    y = 0

    def __init__(self, x,y):
        self.x = x
        self.y = y

points = []
for i in range(10):
    p = Point(i * 10, i * 20)
    points.append(p)

for p in points:
    print(p, p.x, p.y)

```



## [DAY-131] Lists; Files; Dictionaries

Example dictionary, List and String

```
words = {}

words["some long key"] = True
words["x"] = 10

for k in words:
    print(k)
    print(words[k])


list_of_characters = ['a','b','c']

for i in range(len(list_of_characters)):
    print(i)
    print(list_of_characters[i])



s = "hello"
for i in range(len(s)):
    print(i)
    print(s[i])

```

You see how in the list and string we can address individual element or character by its index? In the dictionary we address things by their key, for example if i want to see the value of `some long key` I do `print(words["some long key"])`.

Now unrelated, but lets practice printing the first 100 numbers from a list.

```
a = []

for i in range(100):
    a.append(i)

for i in range(100):
    print(a[i])
```

Append to file, whatever command line agurments 1 and 2 are

```
import sys
f = open("account.txt", "a")

f.write(sys.argv[1] + " " + sys.argv[2] + "\n")

f.close()
```



## [DAY-132] Lists; Classes

![game-132.png](./screenshots/game-132.png "game 132 screenshot")

a tower defense game


```
import pgzrun
import random

WIDTH=1024
HEIGHT=576

towers = []
enemies = []
bullets = []
game_over = False
background = Actor("grass_template2", pos=(0,0), anchor=(0,0))

player = Actor("c1", pos=(WIDTH/2, HEIGHT/2), anchor=('center','bottom'))
lives = 100
cash = 100
current_wave = 1

class Tower:
    def __init__(self, image, x,y, size):
        self.actor = Actor(image, pos=(x,y), )
        self.rect = Rect((x-size/2,y-size/2), (size,size))
        self.color =  (random.randint(100,250),random.randint(100,250),random.randint(100,250))
    def shoot(self):
        for e in enemies:
            if e.colliderect(self.rect):
                b = Actor("bullet3")
                b.x = self.actor.x
                b.y = self.actor.y
                b.hit = False
                animate(b, pos=(e.x,e.y), tween='accelerate', on_finished=lambda: bullets.remove(b))
                bullets.append(b)
                break

    def colliderect(self,other):
        return self.actor.colliderect(other)
    def draw(self):
        self.actor.draw()
        #screen.draw.rect(self.rect,self.color)

def shoot():
    global cash
    for t in towers:
        t.shoot()
    for e in list(enemies):
        if e.image == 'exploded':
            enemies.remove(e)
            cash+=1

def new_wave():
    global current_wave
    for i in range(current_wave * 10):
        e = Actor("c3")
        e.y = HEIGHT
        e.x = random.randint(int(WIDTH/3), int(WIDTH-WIDTH/3))
        enemies.append(e)
    current_wave += 1

def on_key_down(key):
    global cash
    if key == keys.K_1:
        if cash >= 10:
            conflict = False
            for t in towers:
                if t.colliderect(player):
                    conflict = True

            if not conflict:
                t = Tower("tower_grass",player.x, player.y, 150)
                towers.append(t)
                cash -= 10

def update():
    global game_over
    if keyboard.UP:
        player.y -= 5
    if keyboard.DOWN:
        player.y += 5
    if keyboard.LEFT:
        player.x -= 5
    if keyboard.RIGHT:
        player.x += 5

    for e in enemies:
        if e.image != 'exploded':
            e.y -= random.randint(-1,2)
        for b in bullets:
            if b.colliderect(e):
                e.image = 'exploded'
                b.hit = True
                break
        if not background.colliderect(e):
            game_over = True
    pass


clock.schedule_interval(shoot, 1)
clock.schedule_interval(new_wave, 10)

new_wave()

def draw():
    screen.clear()
    if game_over:
        screen.fill('blue')
    else:
        background.draw()
        screen.draw.text("current_wave: " + str(current_wave) + ", cash: " + str(cash) + ", lives: " + str(lives), (5,0),fontname="437-win")   

        for b in bullets:
            if not b.hit:
                b.draw()

        for e in enemies:
            e.draw()

        for t in towers:
            t.draw()

        player.draw()

pgzrun.go()
```


## [DAY-133] Touch Typing; Lists

![game-133.png](./screenshots/game-133.png "game 133 screenshot")

Spend 15 minutes touch typing.

Add a path for the enemies to walk on.

The most important part is to think about, how would you follow a path, in this example we will follow a path by picking a next element to walk towards.

This is the most important part of the change, it is an what is called an algorithm, it is a sequence of steps to solve a problem. We can describe it in words: **find the current square you are colliding it, find which square is next in the list, start walking towards it**. Now lets write it down:

```

[...]

path = [
    Rect(0, HEIGHT/2, 50, 50),
    Rect(50, HEIGHT/2, 50, 50),

[...]

def update():

[...]

    for e in enemies:
        if e.image != 'exploded':
            destination = None
            for (i, p) in enumerate(path):
                if e.colliderect(p) and i < len(path) - 1:
                    destination = path[i+1]
                    break

            if destination != None:
                center_x = destination.x + 25
                center_y = destination.y + 25
                if e.x < center_x:
                    e.x += random.randint(0, 2)
                if e.x > center_x:
                    e.x -= random.randint(0, 2)
                if e.y > center_y:
                    e.y -= random.randint(0, 2)
                if e.y < center_y:
                    e.y += random.randint(0, 2)

[...]

```

```
import pgzrun
import random

WIDTH = 1024
HEIGHT = 576

towers = []
enemies = []
bullets = []
game_over = False
background = Actor("grass_template2", pos=(0, 0), anchor=(0, 0))


path_size = 50
path = [
    Rect(0, HEIGHT/2, 50, 50),
    Rect(50, HEIGHT/2, 50, 50),
    Rect(50, HEIGHT/2 + 50, 50, 50),
    Rect(100, HEIGHT/2 + 50, 50, 50),
    Rect(150, HEIGHT/2 + 50, 50, 50),
    Rect(200, HEIGHT/2 + 50, 50, 50),
    Rect(250, HEIGHT/2 + 50, 50, 50),
    Rect(250, HEIGHT/2 + 100, 50, 50),
    Rect(300, HEIGHT/2 + 100, 50, 50),
    Rect(350, HEIGHT/2 + 100, 50, 50),
    Rect(400, HEIGHT/2 + 100, 50, 50),
    Rect(450, HEIGHT/2 + 100, 50, 50),
    Rect(500, HEIGHT/2 + 100, 50, 50),
    Rect(500, HEIGHT/2 + 150, 50, 50),
    Rect(550, HEIGHT/2 + 150, 50, 50),
    Rect(600, HEIGHT/2 + 150, 50, 50),
    Rect(650, HEIGHT/2 + 150, 50, 50),
    Rect(650, HEIGHT/2 + 200, 50, 50),
    Rect(700, HEIGHT/2 + 200, 50, 50),
    Rect(750, HEIGHT/2 + 200, 50, 50),
    Rect(800, HEIGHT/2 + 200, 50, 50),
    Rect(850, HEIGHT/2 + 200, 50, 50),
    Rect(850, HEIGHT/2 + 150, 50, 50),
    Rect(850, HEIGHT/2 + 100, 50, 50),
    Rect(850, HEIGHT/2 + 50, 50, 50),
    Rect(850, HEIGHT/2 + 0, 50, 50),
    Rect(850, HEIGHT/2 - 50, 50, 50),
    Rect(850, HEIGHT/2 - 100, 50, 50),
    Rect(900, HEIGHT/2 - 100, 50, 50),
    Rect(950, HEIGHT/2 - 100, 50, 50),
    Rect(1000, HEIGHT/2 - 100, 50, 50),
    Rect(1050, HEIGHT/2 - 100, 50, 50),
    Rect(1100, HEIGHT/2 - 100, 50, 50),
]


player = Actor("c1", pos=(WIDTH/2, HEIGHT/2), anchor=('center', 'bottom'))
lives = 100
cash = 100
current_wave = 1


class Tower:
    def __init__(self, image, x, y, size):
        self.actor = Actor(image, pos=(x, y), )
        self.rect = Rect((x-size/2, y-size/2), (size, size))
        self.color = (random.randint(100, 250), random.randint(
            100, 250), random.randint(100, 250))

    def shoot(self):
        for e in enemies:
            if e.colliderect(self.rect):
                b = Actor("bullet3")
                b.x = self.actor.x
                b.y = self.actor.y
                b.hit = False
                animate(b, pos=(e.x, e.y), tween='accelerate',
                        on_finished=lambda: bullets.remove(b))
                bullets.append(b)
                break

    def colliderect(self, other):
        return self.actor.colliderect(other)

    def draw(self):
        self.actor.draw()
        screen.draw.rect(self.rect,self.color)


def shoot():
    global cash
    for t in towers:
        t.shoot()
    for e in list(enemies):
        if e.image == 'exploded':
            enemies.remove(e)
            cash += 1


def new_wave():
    global current_wave
    for i in range(10 + (current_wave * 2)):
        e = Actor("c3")
        e.y = HEIGHT/2+10
        e.x = 0
        enemies.append(e)
    current_wave += 1


def on_key_down(key):
    global cash
    if key == keys.K_1:
        if cash >= 10:
            conflict = False
            for t in towers:
                if t.colliderect(player):
                    conflict = True

            for p in path:
                if player.colliderect(p):
                    conflict = True

            if not conflict:
                t = Tower("tower_grass", player.x, player.y, 150)
                towers.append(t)
                cash -= 10


def update():
    global game_over
    if keyboard.UP:
        player.y -= 5
    if keyboard.DOWN:
        player.y += 5
    if keyboard.LEFT:
        player.x -= 5
    if keyboard.RIGHT:
        player.x += 5

    for e in enemies:
        if e.image != 'exploded':
            destination = None
            for (i, p) in enumerate(path):
                if e.colliderect(p) and i < len(path) - 1:
                    destination = path[i+1]
                    break

            if destination != None:
                center_x = destination.x + 25
                center_y = destination.y + 25
                if e.x < center_x:
                    e.x += random.randint(0, 2)
                if e.x > center_x:
                    e.x -= random.randint(0, 2)
                if e.y > center_y:
                    e.y -= random.randint(0, 2)
                if e.y < center_y:
                    e.y += random.randint(0, 2)

        for b in bullets:
            if b.colliderect(e):
                e.image = 'exploded'
                b.hit = True
                break
        if not background.colliderect(e):
            game_over = True
    pass


clock.schedule_interval(shoot, 1)
clock.schedule_interval(new_wave, 10)

new_wave()


def draw():
    screen.clear()
    if game_over:
        screen.fill('blue')
    else:
        background.draw()

        screen.draw.text("current_wave: " + str(current_wave) + ", cash: " +
                         str(cash) + ", lives: " + str(lives), (5, 0), fontname="437-win")

        for i in range(len(path)):
            p = path[i]
            screen.draw.filled_rect(p,(255,0,0))
            screen.draw.text(str(p.x), (p.x,p.y))
        for b in bullets:
            if not b.hit:
                b.draw()

        for e in enemies:
            e.draw()

        for t in towers:
            t.draw()

        player.draw()


pgzrun.go()
```



## [DAY-134] Lists; Methods

Upgrade our tower game, make it possible to:

* delete towers and get some money back
* be able to upgrade the tower's range

First we will store original `x`,`y` and `size` in the tower's instance, and then use it to increase its range.

Again pay attention when deleting from a list we are walking on (iterating on), we actually make a clone of the list and iterate over the clone, but remove items from the original list by value.

```
[...]

class Tower:
[...]
    def __init__(self, image, x, y, size):
        self.size = size
        self.x = x
        self.y = y
        self.actor = Actor(image, pos=(x, y))
        self.rect = Rect((x-size/2, y-size/2), (size, size))
        self.color = (random.randint(100, 250), random.randint(100, 250), random.randint(100, 250))

    def resize(self, bump):
        new_size = self.size + bump
        self.size = new_size
        self.rect = Rect((self.x-new_size/2, self.y-new_size/2), (new_size, new_size))
[...]

def on_key_down(key):
    global cash
    if key == keys.K_2:
        for t in towers:
            if t.colliderect(player):
                t.resize(5)
                cash -= 10
        
    if key == keys.D:
        for t in list(towers):
            if t.colliderect(player):
                cash += 15
                towers.remove(t)
[...]

```


## [DAY-134] If

![game-134.png](./screenshots/game-134.png "game 134 screenshot")

Relax day.

Make super simple game to draw with two players, because we dont clear the screen.

```
import pgzrun

HEIGHT = 800
WIDTH = 800

elf = Actor('c1')
king = Actor('c2')

def update():
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5
    if keyboard.UP:
        king.y -= 5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.LEFT:
        king.x -= 5
    if keyboard.RIGHT:
        king.x += 5


def draw():
    elf.draw()
    king.draw()

pgzrun.go()
```

## [DAY-135] Dictionary; For

[game-135](screenshots/game-135.mp3)


Make a morse code machine!

```
import pgzrun
import time

short = tone.create('A3', 0.3)
long = tone.create('D3', 0.7)

morse = {
    'a': [short, long],
    'b': [long, short, short, short],
    'c': [long, short, long, short],
    'd': [long, short, short],
    'e': [short],
    'f': [short, short, long, short],
    'g': [long, long, short],
    'h': [short, short, short, short],
    'i': [short, short],
    'j': [short, long, long, long],
    'k': [long, short, long],
    'l': [short, long, short, short],
    'm': [long, long],
    'n': [long, short],
    'o': [long, long, long],
    'p': [short, long, long, short],
    'q': [long, long, short, long],
    'r': [short, long, short],
    's': [short, short, short],
    't': [long],
    'u': [short, short, long],
    'v': [short, short, short, long],
    'w': [short, long, long],
    'x': [long, short, short, long],
    'y': [long, short, long, long],
    'z': [long, long, short, short]
}


def play(key):
    for t in morse[key]:
        t.play()
        time.sleep(1)
    time.sleep(1)


def on_key_down(key):
    if key == keys.A:
        play('a')
    if key == keys.B:
        play('b')
    if key == keys.C:
        play('c')
    if key == keys.D:
        play('d')
    if key == keys.E:
        play('e')
    if key == keys.F:
        play('f')
    if key == keys.G:
        play('g')
    if key == keys.H:
        play('h')
    if key == keys.I:
        play('i')
    if key == keys.J:
        play('j')
    if key == keys.K:
        play('k')
    if key == keys.L:
        play('l')
    if key == keys.M:
        play('m')
    if key == keys.N:
        play('n')
    if key == keys.O:
        play('o')
    if key == keys.P:
        play('p')
    if key == keys.Q:
        play('q')
    if key == keys.R:
        play('r')
    if key == keys.S:
        play('s')
    if key == keys.T:
        play('t')
    if key == keys.U:
        play('u')
    if key == keys.V:
        play('v')
    if key == keys.W:
        play('w')
    if key == keys.X:
        play('x')
    if key == keys.Y:
        play('y')
    if key == keys.Z:
        play('z')


def update():
    pass


def draw():
    pass


pgzrun.go()
```