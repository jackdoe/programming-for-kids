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

The Class itself is like a blueprint of how to make a new instance of itself, for example Lets make a class Point that has two properties, `x` and `y`
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

When you define a function in a class, you have access to special parameter, `self` which is the instance on which this function is called/

```
class Dog:
    name = ''
    def bark(self):
        print(self.name+' woof woof woof')

max = Dog('Maxie')
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
