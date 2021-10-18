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

