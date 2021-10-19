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



## [DAY-131] Lists; Files; Dictionares

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



## [DAY-131] Lists; Classes

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