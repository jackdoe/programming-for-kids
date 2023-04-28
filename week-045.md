## [DAY-319] lists

Given that the update() function is called by pygame zero 60 times per second (so your game can have 60fps), make a "game" that adds a new actor every 1 second.


> this is what she wrote

```
import pgzrun
import random
HEIGHT = 500
WIDTH = 500

actors=[]
counter = 0

def update():
    global counter
    counter += 1
    if counter > 60:
        act = Actor("c1")
        act.y = random.randint(0,HEIGHT)
        act.x = random.randint(0,WIDTH)
        actors.append(act)
        counter = 0
    
def draw():
    screen.clear()
    for actor in actors:
        actor.draw()
    
pgzrun.go()

```


## [DAY-320] files

Write the fizzbuzz output to a file instead of the standard output


> this is what she wrote

```
f = open("zzz.txt","w")

for i in range(100):
    if i % 15 == 0:
        f.write("fizzbuzz\n")
    elif i % 3 == 0:
        f.write("fizz\n")
    elif i % 5 == 0:
        f.write("buzz\n")
    else:
        a = str(i)
        f.write(a + "\n")

f.close()
```

## [DAY-321] files

When you press P write the actor's position in a file, and when you press L, read the position from the file and move the actor to that position

```
import pgzrun
HEIGHT = 800
WIDTH = 800
elf = Actor("c1")
def update():

    if keyboard.W:
        elf.y-=5
    if keyboard.D:
        elf.x+=5
    if keyboard.S:
        elf.y+=5
    if keyboard.A:
        elf.x-=5
    if keyboard.L:
        f = open("zzz.txt","r")
        data = f.read()
        xy = data.split(" ")
        x = float(xy[0])
        elf.x = x
        y = float(xy[1])
        elf.y = y
        f.close()
    if keyboard.P:
        f = open("zzz.txt","w")
        f.write(str(elf.x) + " " + str(elf.y))
        f.close()

def draw():
    screen.clear()
    elf.draw()
pgzrun.go()
```






## [DAY-322] files; functions

Make a function writeFile which takes 2 parameters, the file name and a string to be written to the file, and a function readFile which takes one parameter, the name of the file, and returns the file's contents. Use those two functions in the program from day 321

```
def writeFile(name, s):
    # write the string s to a file with the given name
    pass

# example usage of the functin
# pos = str(elf.x) + " " + str(elf.y)
# writeFile("zzz.txt", pos)


# -------------------------

def readFile(name):
    # return the total contents of the file
    pass

# example usage of the functin
# s = readFile("zzz.txt")
```



## [DAY-323] functions

Make a calculator where every operation is in its own function, complete the following code to support division, multiplication and subtraction:


```
def add(a,b):
    return a + b

def calculate(n1, n2, op):
    v = None
    if op == "+":
        v = add(n1,n2)

    # make it work for multiplicaton, division and subtraction
    
    return v

while True:
    num1 = input("enter number num1: ")
    num2 = input("enter number num2: ")
    op = input("enter number op(+,-,/,mod): ")

    r = calculate(float(num1), float(num2), op)
    print("the result is:", r)
```

> this is the code she wrote, i asked her to sometimes use temporary variables sometimes not

```
def add(a,b):
    return a + b

def subs(a,b):
    return a - b

def divv(a,b):
    c = a / b
    return c

def mult(a,b):
    c = a * b
    return c

def calculate(n1, n2, op):
    v = None
    if op == "+":
        v = add(n1,n2)
    if op == "*":
        v = mult(n1,n2)
    if op == "/":
        v = divv(n1,n2)
    if op == "-":
        v = subs(n1,n2)

    return v

while True:
    num1 = input("enter number num1: ")
    num2 = input("enter number num2: ")
    op = input("enter number op(+,-,/,mod): ")

    r = calculate(float(num1), float(num2), op)
    print("the result is:", r)

```
