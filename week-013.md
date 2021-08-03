# Chapter 13 - Week 13

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```

## [DAY-89] Basics of Basics

super simple text editor

![game-89.png](./screenshots/game-89.png "game 89 screenshot")

Reading exercise, make a text editor, save with `ctrl+s` and quit with `ctrl+q`

```
import pgzrun
import random

HEIGHT = 480
WIDTH = 640
filename = "example.py"
lines = [[]]
cursor_row = 0
cursor_col = 0

try:
    x = open(filename, "r")
    for c in x.read():
        if c== '\n' or c == '\r':
            lines.append([])
            cursor_row += 1
            cursor_col = 0
        else:
            lines[cursor_row].append(c)
            cursor_col += 1

    x.close()
except IOError:
    pass

def lines_to_string():
    s = ''
    for r in lines:
        for c in r:
            s += c
        s += '\n'
    return s

def on_key_down(key, mod, unicode):
    global cursor_row, cursor_col

    if key == keys.Q and mod == keymods.LCTRL:
        exit()
    if key == keys.S and mod == keymods.LCTRL:
        x = open(filename, "w")
        s = lines_to_string()
        x.write(s)
        x.close()

    elif key == keys.LEFT:
        if cursor_col > 0:
            cursor_col -= 1
    elif key == keys.RIGHT:
        if cursor_col < len(lines[cursor_row]):
            cursor_col += 1
    elif key == keys.UP:
        if cursor_row > 0:
            cursor_row -= 1
            if cursor_col > len(lines[cursor_row]):
                cursor_col = len(lines[cursor_row])
    elif key == keys.DOWN:
        if cursor_row < len(lines) - 1:
            cursor_row += 1
            if cursor_col > len(lines[cursor_row]):
                cursor_col = len(lines[cursor_row])


    elif key == keys.BACKSPACE:
        if cursor_col == 0:
            if cursor_row >= 1:
                row = lines.pop(cursor_row)
                cursor_col = len(lines[cursor_row-1])
                for c in row:
                    lines[cursor_row-1].append(c)
                cursor_row -= 1
        else:
            row = lines[cursor_row]
            if len(row) > 0:
                cursor_col -= 1
                row.pop(cursor_col)


    elif key == keys.RETURN:
        # get the rest of the lines
        left = []
        right = []
        if cursor_col < len(lines[cursor_row]):
            # split the line if we are pressing enter in the middle
            row = lines[cursor_row]

            left = row[:cursor_col]
            right = row[cursor_col:]

            if cursor_row < len(lines):
                lines[cursor_row] = left

        cursor_col = 0
        cursor_row += 1
        lines.insert(cursor_row, right)

    elif len(unicode) > 0 and ord(unicode) >= 20 and ord(unicode) <= 125:
        lines[cursor_row].insert(cursor_col, unicode)
        cursor_col += 1

def draw():
    screen.fill('black')
    screen.draw.text(filename + ", " + str(cursor_row) + ":" + str(cursor_col), (0,0), fontsize=20,fontname="437-win", color="green")

    x = 0
    y = 30
    stepX = 10
    stepY = 22

    for (index_row, row) in enumerate(lines):
        for (index_col, c) in enumerate(row):
            screen.draw.text(c, (x,y), fontsize=20,fontname="437-win")
            x += stepX
        y += stepY
        x = 0

    cursorX = cursor_col * stepX
    cursorY = 30 + (cursor_row * stepY)

    screen.draw.rect(Rect((cursorX,cursorY,stepX,stepY)), (255,0,0))

pgzrun.go()
```

write some python, and then run it with `python3 example.py`


## [DAY-90] Basics of Basics

![game-90.png](./screenshots/game-90.png "game 90 screenshot")

Write a super simple text editor. Start by thinking about the problem. How can you display a character on the screen? How can you get the input from the user? How are you going to deal with new lines?

```
import pgzrun

HEIGHT = 480
WIDTH = 640

text = ''

def on_key_down(key, mod, unicode):
    global text

    if key == keys.Q and mod == keymods.LCTRL:
        exit()


    elif key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:len(text)-1]

    elif key == keys.RETURN:
        text += '\n'

    elif len(unicode) > 0 and ord(unicode) >= 20 and ord(unicode) <= 125:
        text += unicode

def draw():
    screen.fill('black')
    x = 0
    y = 0
    stepX = 10
    stepY = 22

    for c in text:
        if c == '\n':
            y += stepY
            x = 0
        else:
            screen.draw.text(c, (x,y), fontsize=20,fontname="437-win")
            x += stepX

    screen.draw.rect(Rect((x,y,stepX,stepY)), (255,0,0))

pgzrun.go()
```

This is kind of what `screen.draw.text` does, you can of course just do `screen.draw.text(text, (0,0), fontsize=20,fontname="437-win")` and it will work fine, instead of displaying character by character and computing our own char spacing, but what is the fun in that? Also this way we are one step closer to be able to move the cursor left and right so we can edit in the middle of the text.

## [DAY-91] Basics of Basics

list your favorite games, and rank them

```
games = [
    ["mario smash bros", 3],
    ["mario party", 4],
    ["super mario", 2]
]

while True:
    for game in games:
        print(game[0])
    what = input("which game are you interested in: ")
    for game in games:
        if what in game[0]:
            print("i like " + game[0] + ", score: " + str(game[1]))
```

print the lyrics of songs:

```
songs = [
    ["wellerman", """There once was a ship that put to sea
The name of the ship was the Billy of Tea
The winds blew up, her bow dipped down
Oh blow, my bully boys, blow (huh)

Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go"""],
]

while True:
    what = input("which song are you interested in: ")
    for song in songs:
        if what in song[0]:
            print('-' * 40)
            print(song[1])
            print('-' * 40)
```
## [DAY-92] Basics of Basics

Today is command line day.

> First quickly go back to the start and read about files and folders (directories).

The same way functions can get parameters, your program can get parameters as well, try this:

```
import sys 
print(sys.argv)
```

save it as `a.py` and then run `python3 a.py hello those are paremeters` frmo the Terminal app, you will see `['a.py', 'hello', 'those', 'are', 'paremeters']`, sys.argv[0] is the name of the program, and then the parameters you gave it.

Now lets make few handy programs to help us with our command line:

---

xcat.py

```
import sys

x = open(sys.argv[1], "r")
data = x.read()
print(data)
```

---

xls.py
```
import os
import sys

files = os.listdir(sys.argv[1])
files.sort()

for f in files:
    if os.path.isdir(f):
        print(f + "/")
    else:
        print(f)
```

---

xed.py

```
import sys
import os

text = ''

filename = sys.argv[1]

try:
    f = open(filename, "r")
    text = f.read()
    f.close()
except IOError:
    pass
    
while True:
    what = input("> ")
    if what == '?':
        print("""
        * ? - help
        * p - print
        * s - save
        * d [n] - delete last N lines
        * a text - append text to the end
        """)
    elif what == 'q':
        sys.exit(0)
    elif what == 'p':
        print(text, end = '')
    elif what == 's':
        f = open(filename, "w")
        f.write(text)
        f.close()
    elif what[0] == 'a' and what[1] == ' ':
        text += what[2:] + '\n'
    elif what[0] == 'd':
        lines = text.split('\n')

        n = 1
        if len(what) > 2:
            n = int(what[2:])

        for i in range(0, n):
            lines.pop()

        text = "\n".join(lines)
        

    else:
        print("* use ? for help")
```

---

OK now we have a text editor, a program to list files, and a program to print the file's content, now we can use our programs to write more programs :)

try this:

```
$ python3 xed,py example.py
> a for i in range(100)
> a   print(i)
> p
> s

$ python3 xls.py .
$ python3 xcat.py example.py
$ python3 example.py
```

## [DAY-93] Basics of Basics
## [DAY-94] Basics of Basics
## [DAY-95] Basics of Basics
