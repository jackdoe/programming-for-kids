
## [DAY-150] While; Classes

Circles And Squares.

![game-150.png](./screenshots/game-150.png "game 150 screenshot")

```
from turtle import *

bgcolor('black')

a = Turtle()
a.speed(0)
a.hideturtle()

b = Turtle()
b.speed(0)
b.hideturtle()

colorA = textinput('pencolor a',"what is your name?:")
colorB = textinput('pencolor b',"what is your name?:")

size = 0
while True:
    b.pencolor(colorB)
    b.forward(size*3)
    b.left(91)

    a.pencolor(colorA)
    a.forward(size*10)
    a.circle(size, 360)
    a.left(500)

    size += 1
```

More circles

![game-150-a.png](./screenshots/game-150-a.png "game 150-a screenshot")

```
import turtle as t
t.bgcolor('black')
t.hideturtle()
size = -300
t.speed(0)
while True:
    if size % 2 == 0:
        t.pencolor('cyan')
    else:
        t.pencolor('magenta')

    t.circle(size*3)
    size += 1
```


## [DAY-151] Classes; While

![game-151.png](./screenshots/game-151.png "game 151 screenshot")

First make a painting program where you can chose colors and draw rectangles

```
import pgzrun

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
x = 0
y = 0

color = None
drop = []
size = 40
def update():
    global color,size

    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.D:
        elf.x += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.C:
        screen.clear()

    if keyboard.SPACE and color != None:

        drop.append([color, Rect(elf.x, elf.y, size, size)])

    if keyboard.K_1:
        color = (255,0,0)
    if keyboard.K_2:
        color = (25,41, 88)

    if keyboard.K_8:
        size += 1
    if keyboard.K_9:
        size -= 1
def draw():
    screen.clear()
    elf.draw()

    for pixel in drop:
        screen.draw.rect(pixel[1],pixel[0])

    if color != None:
        screen.draw.rect(Rect(elf.x,elf.y,size,size), color)
pgzrun.go()
```

Same program but making a Pixel class instead of a list with color and rect.

```
import pgzrun

WIDTH = 800
HEIGHT = 800


class Pixel:
    def __init__(self, color, x, y, size):
        self.color = color
        self.rect = Rect(x,y,size,size)
    
    def draw(self):
        screen.draw.rect(self.rect, self.color)

elf = Actor('c1')
x = 0
y = 0

color = None
drop = []
size = 40
def update():
    global color,size

    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.D:
        elf.x += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.C:
        screen.clear()

    if keyboard.SPACE and color != None:
        pixel = Pixel(color, elf.x, elf.y, size)
        drop.append(pixel)

    if keyboard.K_1:
        color = (255,0,0)
    if keyboard.K_2:
        color = (25, 41, 88)

    if keyboard.K_8:
        size += 1
    if keyboard.K_9:
        size -= 1

def draw():
    screen.clear()
    elf.draw()

    for pixel in drop:
        pixel.draw()

    if color != None:
        screen.draw.rect(Rect(elf.x,elf.y,size,size), color)
pgzrun.go()
```

Go back in the book and re-read the class chapter.

Try out some ideas with a class, just to understand better what `self` is, for example play around with this Point class, try to add `move_right` or `move_up` methods.

```
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def move(self,x,y):
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 1

    def show(self):
        print(self.x, self.y)

    def equal(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True

        return False


p1 = Point(10,20)
p2 = Point(30,40)
p3 = Point(10,20)

p3.move(50,60)
p1.show()

p2.show()

p3.move_left()
p3.show()

print(p3.equal(p1))
```

---

Completely unrelated and just for fun, make a triangle like pattern:

```
while True:
    for i in range(0,10):
        print(':3'* i)
    for i in range(10,0,-1):
        print(':D' * i)
```

Prints infinite sequence of smilies

```
:3
:3:3
:3:3:3
:3:3:3:3
:3:3:3:3:3
:3:3:3:3:3:3
:3:3:3:3:3:3:3
:3:3:3:3:3:3:3:3
:3:3:3:3:3:3:3:3:3
:D:D:D:D:D:D:D:D:D:D
:D:D:D:D:D:D:D:D:D
:D:D:D:D:D:D:D:D
:D:D:D:D:D:D:D
:D:D:D:D:D:D
:D:D:D:D:D
:D:D:D:D
:D:D:D
:D:D
:D

:3
:3:3
:3:3:3
:3:3:3:3
:3:3:3:3:3
:3:3:3:3:3:3
...
```


## [DAY-152] Lists

![game-152.png](./screenshots/game-152.png "game 152 screenshot")

Make 3 actors you can pick up and drop them wherever you hit SPACE.

```
import pgzrun

WIDTH = 500
HEIGHT = 500

king = Actor('c2')
elf = Actor('c1')
flower =  Actor('flower')
rock = Actor('rock')

king.x = 480
king.y = 125
flower.y = 380
flower.x = 480
rock.x = 480
rock.y = 250

drop = []

speed = 5
def update():
    global speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.D:
        elf.x += speed
    if keyboard.A:
        elf.x -= speed
    if keyboard.C:
        screen.clear()

    if elf.colliderect(king):
        elf.image=king.image
        speed = 2
    if elf.colliderect(rock):
        elf.image=rock.image
        speed = 1
    if elf.colliderect(flower):
        elf.image=flower.image
        speed = 10
    if keyboard.SPACE and elf.image != 'c1':
        a = Actor(elf.image)
        a.x = elf.x
        a.y = elf.y
        drop.append(a)

        elf.image='c1'
        speed = 5

def draw():
    screen.clear()
    elf.draw()
    king.draw()
    flower.draw()
    rock.draw()
    for d in drop:
        d.draw()

pgzrun.go()
```


## [DAY-153] Lists; Dictionaries

![game-153.png](./screenshots/game-153.png "game 153 screenshot")

Find Waldo, here are two different implementations of the game, one uses dictionaries and one doesnt.

In this game, one of the actors has his back turned, and the purpose of the game is to find them.

We are using this example to practice lists, using `for element in list` and `for i in range(len(list))`, and overusing iterating over the list to find a matching element.

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
elf.x = 400
elf.y = 400
drop = []

def on_key_down(key):
    if key == keys.SPACE:
        found = False
        for i in drop:
            if i.image == 'c2-back':
                found = True
        if not found:
            a = Actor('c2-back')
            a.x = random.randint(0,1500)
            a.y = random.randint(0,1500)
            drop.append(a)
        for i in range(100):
            a = Actor('c2')
            a.x = random.randint(0,2000)
            a.y = random.randint(0,2000)
            drop.append(a)
    if key == keys.P:
        for i in drop:
            if i.image == 'c2-back':
                i.x = random.randint(elf.x - 200,elf.x + 200)
                i.y = random.randint(elf.y - 200,elf.y + 200)

waldo_found = False
def update():
    global waldo_found
    if keyboard.W:
        for x in range(len(drop)):
            i = drop[x]
            i.y += 5
    if keyboard.S:
        for a in range(len(drop)):
            drop[a].y -= 5
    if keyboard.A:
        for i in drop:
            i.x += 5
    if keyboard.D:
        for i in drop:
            i.x -= 5
    for i in drop:
        if i.image == 'c2-back' and elf.colliderect(i):
            waldo_found = True

def draw():
    screen.fill('black')
    elf.draw()
    for i in drop:
        i.draw()
    if waldo_found == True:
        screen.draw.text(" YOU HAVE FOUND WALDO ", (10,10))

pgzrun.go()
```


A second implementation where we use a `waldo` variable so we dont have to scan the list of actors so many times, and also we move the elf instead of moving all the actors. And we use a dictionary with positions to try to avoid adding an actor close to already existing one.

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
elf.x = 400
elf.y = 400
drop = []
waldo = Actor('c2-back')
seen = {}
def on_key_down(key):
    if key == keys.SPACE:
        waldo.x = random.randint(0,WIDTH)
        waldo.y = random.randint(0,HEIGHT)
        place = str(int(waldo.x/50)) + "_" + str(int(waldo.y/100))
        seen[place] = True
        for i in range(100):
            x = random.randint(0,WIDTH)
            y = random.randint(0,HEIGHT)
            place = str(int(x/50)) + "_" + str(int(y/100))
            if place not in seen:
                a = Actor('c2')
                a.x = x
                a.y = y
                drop.append(a)
                seen[place] = True

waldo_found = False
def update():
    global waldo_found

    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5

    if waldo.colliderect(elf):
        waldo_found = True

def draw():
    screen.fill('black')
    elf.draw()
    for i in drop:
        i.draw()
    waldo.draw()

    if waldo_found == True:
        screen.draw.text(" YOU HAVE FOUND WALDO ", (10,10))

pgzrun.go()
```
## [DAY-154] Classes


Pacman, make things move around, stop when they hit something

![game-154.png](./screenshots/game-154.png "game 154 screenshot")


```
import random
import pgzrun

WIDTH = 600
HEIGHT = 600
game_over = False
lives = 3
obsticles = [
    Rect(100,100,20,20),
    Rect(200,200,100,200),
]

class Mover:
    def __init__(self, image, x, y, direction):
        self.actor = Actor(image)
        self.direction = direction
        self.actor.x = x
        self.actor.y = y
        self.counter = 0

    def draw(self):
        self.actor.draw()

    def update(self):
        orig_x = self.actor.x
        orig_y = self.actor.y
        self.counter += 1
        if self.counter > 120 and self.actor.image == "c2":
            self.direction = random.choice(['up','down','left','right'])
            self.counter = 0

        if self.direction == 'up':
            self.actor.y -= 1
        if self.direction == 'down':
            self.actor.y += 1
        if self.direction == 'left':
            self.actor.x -= 1
        if self.direction == 'right':
            self.actor.x += 1
        
        if self.actor.x > WIDTH:
            self.actor.x = 0
        if self.actor.x < 0:
            self.actor.x = WIDTH
        if self.actor.y > HEIGHT:
            self.actor.y = 0
        if self.actor.y < 0:
            self.actor.y = HEIGHT 
        hit_wall = False
        for o in obsticles:
            if self.actor.colliderect(o):
                self.actor.x = orig_x
                self.actor.y = orig_y
                hit_wall = True
                break
        if hit_wall and self.actor.image == "c2":
            self.direction = random.choice(['up','down','left','right'])


pacman = Mover("c1", 10, 10, 'up')
movers = [pacman, 
  Mover("c2", 100, 40, 'up'),
  Mover("c2", 100, 50, 'up'),
  Mover("c2", 100, 60, 'up'),
  Mover("c2", 100, 70, 'up')
]

def update():
    global lives,game_over
    if keyboard.W:
        pacman.direction = 'up'
    if keyboard.S:
        pacman.direction = 'down'
    if keyboard.A:
        pacman.direction = 'left'
    if keyboard.D:
        pacman.direction = 'right'

    for m in movers:
        m.update()
    for o in movers:
        if pacman.actor.colliderect(o.actor) and o != pacman:
            lives -= 1
            pacman.actor.x = 0
            pacman.actor.y = 0
            
            if lives < 0:
                game_over = True

def draw():
    screen.fill('black')
    for o in obsticles:
        screen.draw.filled_rect(o,(255,0,0))
    screen.draw.text('lives: ' + str(lives), (10,10))
    if game_over == True:
        screen.fill('royalblue')
        screen.draw.text('GAME OVER YOU LOST',(10,10))
    for m in movers:
        m.draw()

pgzrun.go()
```

## [DAY-155] c++

First lets discuss a bit about the difference between `c++` and `python`. For example, lets examine what happens with the following program:

```
while True:
    print("hello world")
```
If you save it in the file `hello.py`, and you have to start it with `python hello.py`. Python is a program on its own, which will load the `hello.py` file and execute it line by line. The `python` program is called `interpreter` because it interprets the code, kind of like when you read a program, trying to find out what it does, you interpret the code in your head and evaluate it.

`c` and `c++` on the other hand are compiled languages, you need a program `gcc` for c and `g++` for c++ to transform your source code to machine code, that your computer will directly run, instruction by instruction.

Lets start where everything starts, print "Hello World". Save the following program in a file `hello.cpp` (cpp for c plus plus).


```
#include <iostream>
using namespace std;

int main(void) {
	cout << "Hello World " << endl;
}
```

Now lets compile it, `g++ -o hello hello.cpp` will make a program `hello` that you will be able to execute by running `./hello` you see it is very different, you run directly `hello` which will make your computer execute its instructions one by one, which is very different than running python to load your `hello.py`, in the python case your computer is running the python executable which loads your `hello.py` and interprets it line by line.

`int main()` declares the `main` function, each c/c++ program must have a main() function, thats where your program starts, unlike python, where it starts from the top of the file. You can think of your processor jumping to the address of the main function in memory, as we spoke in the previous lessons, in the computer's memoruy code is data, and data is code.

`cout` means `character output` and `<<` means `pour into the cout` whatever follows, e.g. `cout << 5` will just print 5, `cout "hello"` will print hello, `cout << 5 << "hello"` will print 5hello, and `endl` inserts the newline character `\n`.

`using namespace std;` is similar to from `turtle import *`, we will get into it later

And very importantly you `c++` does not care about your spaces, the following program compiles just fine

```
#include <iostream>
using namespace std;int main(void) {cout << "Hello World " << endl;}
```

Each code block is surrounded by `{}` and each statement ends with `;` and thats it

Try out the following programs, and just experiment with them using your python knowledge. (hint: `int` means integer)

```
#include <iostream>

using namespace std;

int main(void) {
	int i = 1000;

	while(i) {
		if (i < 500) {
			cout << "HIII" << endl;
		} else {
			cout << "Hello World " << i << endl;
		}
		i--;
	}
}
```

```
#include <iostream>

using namespace std;

int main(void) {
	for (int i = 1000; i >= 0 ; i--) {
		if (i < 500) {
			cout << "HIII " << i << endl;
		} else {
			cout << "Hello World " << i << endl;
		}
	}
	return 0;
}
```