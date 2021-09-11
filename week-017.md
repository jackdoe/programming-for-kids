# Chapter 14 - Week 14

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```

## [DAY-116] Basics of Basics

Many Turtles.

The ideas are borrowed from [Redisovering Logo with Bob the Turtle](https://notes.ayushsharma.in/2019/06/rediscovering-logo-with-bob-the-turtle), Ayush Sharma's amazing blog post!

![game-116-a.png](./screenshots/game-116-a.png "game 116-a screenshot")

```
import turtle

turtle.setup(width=800, height=800)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')
bob.speed(3000)

alice = turtle.Turtle(shape='turtle')
alice.color('lawngreen')
alice.speed(3000)

for i in range(500):

    bob.forward(i)
    bob.left(91)

    alice.backward(i)
    alice.right(91)

turtle.exitonclick()
```

even more turtles

![game-116-b.png](./screenshots/game-116-b.png "game 116-b screenshot")


```
import turtle

turtle.setup(width=800, height=800)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')
bob.speed(3000)

alice = turtle.Turtle(shape='turtle')
alice.color('lawngreen')
alice.speed(3000)


charlie = turtle.Turtle(shape='turtle')
charlie.color('deepskyblue')
charlie.speed(3000)

for i in range(500):

    bob.forward(i)
    bob.left(91)

    alice.backward(i)
    alice.right(91)

    charlie.forward(i)
    charlie.right(101)

turtle.exitonclick()
```

```
import turtle
turtle.setup(width=800, height=800)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')

alice = turtle.Turtle(shape='turtle')
alice.color('lawngreen')
angle = 10
while True:
    alice.backward(20)
    bob.forward(20)
    alice.right(angle)
    bob.left(angle)
    angle += 1
```

Again this is the same as in roblox's houses, you have the blueprint of the house, and you can create an instance of it, and then you can modify it. so `turtle.Turtle()` creates an instance, and then you see, bob, alice and charlie have their own changes. In the same time they have the same functionality, like `forward` `up` and etc coming from the blueprint and each of those methods work on the instance itself.

## [DAY-117] Basics of Basics

![game-117.png](./screenshots/game-117.png "game 117 screenshot")

And lets discuss another text editor.

(if you are on windows make sure you `pip3 install windows-curses`)

Start super simple, what do we need to make a text editor? first we need to show the text being edited, and second we need to capture user input and modify this text.

First show some text:

```
import curses
import time

screen = curses.initscr()
screen.addstr(0, 0, "hello world",curses.A_NORMAL)
screen.refresh()

time.sleep(2)
```

Capture input and modify the text:

```
import curses

screen = curses.initscr()
text = ''
while True:
    screen.addstr(0, 0, text,curses.A_NORMAL)
    screen.refresh()

    c = screen.getch()
    text += chr(c)
```

In order to Read and Write the file we are editing, we need to have some control keys, like Ctrl+S to save, and Ctrl+C to quit without saving. Also we need to add support for backspace to be able to delete from the text string.

Hint: use `text += str(c)` to actually see the codes you need.

```
import curses
import sys

screen = curses.initscr()
curses.curs_set(2)

if len(sys.argv) != 2:
    print("usage:")
    print(sys.argv[0] + " filename")
    sys.exit(1)


text = ''
try:
    file = open(sys.argv[1],"r")
    text = file.read()
    file.close()
except:
    pass

status = 'file: ' + sys.argv[1]
while True:
    screen.clear()
    screen.addstr(0, 0, status + ' (len: ' + str(len(text)) + ')',curses.A_NORMAL)
    screen.addstr(2, 0, text,curses.A_NORMAL)
    screen.refresh()

    c = screen.getch()
    if c == 3:
        # quit Ctrl+C
        break

    if c == 19:
        # save Ctrl+S
        file = open(sys.argv[1],"w")
        file.write(text)
        file.close()
        status = 'file: ' + sys.argv[1]
        screen.addstr(0, 0, text,curses.A_NORMAL)
        continue
    if c == 8:
        # backspace
        if len(text) > 0:
            text = text[:len(text)-1]
        continue
    if (c < 127 and c > 30) or c == 10:
        text += chr(c)
        status = 'file: ' + sys.argv[1] + " (modified)"

```

## [DAY-118] Basics of Basics

Search for your favorite lyrics, dont forget to `pip3 install lyricsgenius`

```
import lyricsgenius
genius = lyricsgenius.Genius('get api key from genius.com')
genius.verbose = False
while True:
    artist = input("🔥 Artist: ")
    song_name = input("🔥 Song: ")
    song = genius.search_song(song_name, artist)
    if song == None:
        print(song_name + " / " + artist + " not found")
    else:
        print('-'  * 40)
        print(song.lyrics)
        print('-'  * 40)
```


## [DAY-119] Basics of Basics

![game-119.png](./screenshots/game-119.png "game 119 screenshot")

Use https://github.com/ageitgey/face_recognition to see how easy it is to track people through a video stream only using 1 picture from them.

Recognize that if it is cheap and easy, it is done to you.

It will be done in the mall, to show you personalized ads, it will be done on the street to track where you go so they can sell you better things on tiktok.

They only need 1 picture.

If you are not paying, you are the product.

It is also not very easy to be tricked with mascara.


![game-119-a.png](./screenshots/game-119-a.png "game 119a screenshot")
![game-119-b.png](./screenshots/game-119-b.png "game 119b screenshot")
![game-119-c.png](./screenshots/game-119-c.png "game 119c screenshot")



even thought it was easy in 2014, https://www.theatlantic.com/technology/archive/2014/07/makeup/374929/


## [DAY-120] Basics of Basics

Today you are on your own. We start with: https://www.amazon.de/-/en/DK/dp/1465461884 chapter 2, read it for 1 hour and make the programs and exercieses.

Write down your experience and what you struggle with.

Simple ping pong game

```
import pgzrun
import random

HEIGHT = 600
WIDTH = 600

elf = Actor('c1')
king = Actor('c2')
ball = Actor('bullet')

king.y = HEIGHT/2
elf.y = HEIGHT/2
elf.x = WIDTH-10
ball.x = WIDTH/2
ball.y = HEIGHT/2
d = 1
game_over = False
speed = 1
def update():
    global d,game_over,speed
    if keyboard.up:
            elf.y -= 5
    if keyboard.down:
            elf.y += 5
    if keyboard.S:
            king.y += 5
    if keyboard.W:
            king.y -= 5

    if ball.x < 0 or ball.x > WIDTH:
        game_over = True

    if d == 1:
        ball.x += speed
    else:
        ball.x -= speed

    if elf.colliderect(ball):
        d = 0
        ball.y = random.randint(10,HEIGHT-10)
        speed += 1
    if king.colliderect(ball):
        d = 1
        ball.y = random.randint(10,HEIGHT-10)
        speed += 1

def draw():
    screen.clear()
    screen.fill("deepskyblue")

    elf.draw()
    king.draw()
    ball.draw()

    if game_over:
        screen.fill('red')

pgzrun.go()
```

## [DAY-121] Basics of Basics
## [DAY-122] Basics of Basics

