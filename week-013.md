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

Reading docs. type this in the terminal: `pydoc3 open` `pydoc3 input` `pydoc3 print` and `pydoc3 pgzero.actor`.

Lets take `open` as an example.

```
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.

    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.

    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.

    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.

    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:

    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.

    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.

    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.

    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.

    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:

    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.

    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.

    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.

    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).

    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.

    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
```

It's a lot! But I guarantee you its the best way to learn about something, the people who wrote the `open` function, wrote text to help anyone who is going to use it, describging what it does and how it behaves. It is always worth reading the docs of functions you are going to use. Sometimes they are not very good, but it is worth checking it out.

The other way find things is to google `python3 open` and you will usually see stackoverflow answers and maybe some examples, in many cases they will be incomplete or wrong, or pure scam 'pay 10$ to buy our video to learn how to use python3 open'


You can also do pydoc3 on modules, e.g. `pydoc3 sys` or `pydoc3 sys.argv`. Sometimes it might look a bit intimidating, but its usually much better than using google.

Try also `pydoc3 pgzero`, `pydoc3 pygame` and `pydoc3 pygame.Rect`. There is also a way to find documentation for the command line programs, try `man python3`, `man` from `manual`, if you want to search for something use `man -k something` for example `man -k python`.

## [DAY-94] Basics of Basics

Command line editors:

* nano, pico

super easy to use, press ctrl+x to exit, ctrl+k to cut text, and ctrl+u to uncut (paste)

* vi

Type `vimtutor` to see how it works, to quit use `ESC` then type `:` and then `q!`

* emacs

emacs is my favorite editor, in in fact I am writing this book using it. type `ctrl+x ctrl+c` to quit, and `ctrl+x ctrl+s` to save.

* ed

ed is super old editor, it is somewhat similar to xed.py that you wrote, its called 'line editor'. To quit use `q` or `Q` if you want to quit without saving, to print the contents of the file use `1,$n` which prints the lines from 1 to $, or you can print specific line with `1n` or `2n` where 1 or 2 is the linue number.

try this:

```
$ ed zzz
a
for i in range(10);
  print(i)
.
w
31
1,$n
1	for i in range(10);
2	  print(i)
q
```

`a` will append to the file, `w` will save the file, `1,$n` will print the contents, and `q` will quit. Commands like `a,i,d` (append,insert,delete) take line numbers as parameters as well. Use `man ed` to see the docs.

I don't think anyone uses `ed` anymore, at least not as a text editor, but sometimes its handy to know how to use it.

---

There are many many text editors, and some are better for you than others, but to me I dont really care, I want to type in my program and save it.. its not the end of the world if I use one or another editor.

So use the one you like most, but sometimes you will go on another computer and they wont have your editor there, so be be sure to be 'ok' with vim, nano or emacs, because they are on virtually any system.

## [DAY-95] Basics of Basics


Memory.


Lets make a huuuuuge list.

```
memory = []
for i in range(1000000):
    memory.append(0)

```

Our memory looks like this:

```
[0,0,0,..............0,0,0,0....0,0,0,0,0]
```

Now we can make variables in this list of numbers, by addressing each variable with its index in the list, for exampke `x` can be at index 1000 and `y` can be at position 1001.


```
def add(a_address,b_address):
    return memory[a_address] + memory[b_address]

x_address = 1000
y_address = 1001
memory[x_address] = 5
memory[y_address] = 10

r = add(x_address,y_address)

print(r)
```

This is cheating though, because python uses its own memory to store the result from x and y, lets fix that:

```
def add(a_address,b_address,r_address):
    memory[r_address] = memory[a_address] + memory[b_address]

x_address = 1000
memory[x_address] = 5

y_address = 1001
memory[y_address] = 10

r_address = 1002
add(x_address,y_address,r_address)

print(memory[r_address])
```

This is how our memory looks like
```
[....0,0,0,5,10,15,0,...]
           ^ ^  ^
           | |  |
           x |  |
             y  |
                r

x at index 1000
y at index 1001
r at index 1002
```

The code above translates roughly to:

```
x = 5
y = 10
r = x + y
print(r)
```

How about strings? We can store strings by just defining how big the string is, and then follow with the characters of the string. You see how it is continous piece of memory.
```

h_address = 2000
memory[h_address] = 5
memory[h_address+1] = ord('h')
memory[h_address+2] = ord('e')
memory[h_address+3] = ord('l')
memory[h_address+4] = ord('l')
memory[h_address+5] = ord('o')

def xprint(address):
    l = memory[address]
    for i in range(l):
        # +1 is because of the length
        c = memory[address + 1 + i]
        print(chr(c), end = '')
    print('')
```


Strings with without length. We can also just say 'the string ends with 0' so start reading and stop when you see 0.

```

n_address = 3000
memory[n_address+0] = ord('h')
memory[n_address+1] = ord('e')
memory[n_address+2] = ord('l')
memory[n_address+3] = ord('l')
memory[n_address+4] = ord('o')

def nprint(address):
    for addr in range(address, len(memory)):
        c = memory[addr]
        if c == 0:
            break
        print(chr(c), end = '')
    print('')

nprint(n_address)

```

Now lets add a funciton to add two strings:

```


a_address = 4000
memory[a_address] = 5
memory[a_address+1] = ord('h')
memory[a_address+2] = ord('e')
memory[a_address+3] = ord('l')
memory[a_address+4] = ord('l')
memory[a_address+5] = ord('o')

b_address = 4006
memory[b_address] = 5
memory[b_address+1] = ord('w')
memory[b_address+2] = ord('o')
memory[b_address+3] = ord('r')
memory[b_address+4] = ord('l')
memory[b_address+5] = ord('d')

c_address = 7000

def xadd(a,b,dst):
    len_a = memory[a]
    len_b = memory[b]
    memory[dst] = len_a + len_b
    for i in range(len_a):
        c = memory[a + 1 + i]
        memory[dst + 1 + i] = c

    for i in range(len_b):
        c = memory[b + 1 +i]
        memory[dst + 1 + len_a + i] = c

xadd(a_address, b_address, c_address)
xprint(c_address)
```

You see, the list is just a list with 1 million numbers, but we decide what those numbers mean, if we are reading a string, we *know* that the first number represents the length of the string, so its just an integer, but we know that the other numbers are actually characters.

```
i_address = 3996
memory[i_address] = 9999

[....9999,0,0,0,5,104,101,108,108,111,5,119,111,114,108,100....]
     ^          ^                     ^
     i          this is a             this is b
  idx: 3996     idx: 4000             idx: 4006

```

The memory doesnt care, string integers, characters,, its all the same. It doesn't know where one array ends or begins. You just read and write to specific address and thats all it cares about. *WHERE* to read and write.

Think about what it means to remove a character from our string, if its the last character we can sinply reduce the lengthm but lets say we want to remove 'o' from 'world', that would mean something like:

```
world

* reduce the length to 4
* move r to the left
* move l to the left
* move d to the left

```

You see we had to do 4 things to remove 1 character, and imagine if the string is 10000 chars long and we want to remove the first one, we wikl have to do 999 things, moving each character to the left.


In the same time, it is super easy to go to specific character, if I want to print the 3rd char, I can just do memory[address + 1 + 3] and thats it, add 1 because of the length and then add however many characters i want to skip.

There are different way to store collections of things, Linked Lists are one example

```

[0, value]            # w
 |
[next_address, value] # o
 |
[next_address, value] # r
 |
[next_address, value] # l
 |
[0, value ]           # d
```

Arrays and Lists are very differentm arrays are *always* continous, like strings, actually string is just an array of characters. Lists however can be on scattered amongst the memory, and each element can point to the next one.

So with a linked list it is hard to get to position 3 for example, because we have to start from the top, and go down until we see 3 elements, so we have to do 3 things to get to position 3, or 1000 things to get to position 1000. In the same time if we want to remove something, we can simply make it disappear, by making the previous element point to the next one, e.g. make `o` point to `l`, and then `r` will disappear.


Our format will be (next element from the list, value)

```
memory[20000] = 30000
memory[20001] = 1

memory[30000] = 30500
memory[30001] = 2

memory[30500] = 30605
memory[30501] = 3

memory[30605] = 0
memory[30606] = 4
```   

the memory now looks like this:

```
[ ....30000, 1, .... 30500, 2, .... 30605, 3, .... 0, 4, ...]
      ^              ^              ^              ^
      first          second         third          forth element
```


This is an example function that will print all the values in a linked list, following the links.

```
def lprint(start_address):
    done = False
    while not done:
        # check if this is the last element of the list
        done = memory[start_address] == 0

        # print the value at address + 1
        print(memory[start_address+1])

        # go to the next element from the list
        start_address = memory[start_address]

lprint(20000)
```

You see, having a flat area of memory is so powerfull! it doesnt know anything about what we store in it, so of course we can store pointers to other parts of the memory, we can have lists of lists of lists of lists that just point around, and of course we can have infinite loops, imagine a linked list where one of the elements points to a previous elemnent.

Check this out:
```
memory[20000] = 30000
memory[20001] = 1

memory[30000] = 20000
memory[30001] = 2

lprint(20000)
```

Inifinite loop! How cool is that!

```
1
2
1
2
1
2
1
2
1
2
1
2
1
2
1
2
```



Lets make a computer, it needs Memory and CPU, the CPU will read instructions from memory and produce results back in memory.

```
memory = []
for i in range(1000000):
    memory.append(0)


memory[1000] = 5  # a
memory[1001] = 10 # b
memory[1002] = 0  # result

# lets multiply a * b
# the code looks like this
# counter = b
# while counter > 0:
#     r = r + a
#     counter -= 1
# print(r)

# counter = b
memory[1003] = memory[1001]

# jump to position 10 if counter is 0
memory[0] = 4
memory[1] = 1003
memory[2] = 13

# r = r + a
memory[3] = 1
memory[4] = 1002
memory[5] = 1000
memory[6] = 1002


# since our add operation adds two things in memory, we
# need to store the value -1 somewhere to subtract it from the counter
#
# counter -= 1
memory[9999] = -1
memory[7] = 1
memory[8] = 1003
memory[9] = 9999
memory[10] = 1003

# go back to the if counter == 0 instruction
memory[11] = 5
memory[12] = 0 

# print(r)
memory[13] = 3
memory[14] = 1002

# stop the program
memory[15] = 0

position = 0
while True:
    instruction = memory[position]
    print('instruction',instruction, 'position',position)
    # quit if instruction is 0
    if instruction == 0:
        break

    # add position+1 and position+2 and write result in position+3
    elif instruction == 1:
        a_address = memory[position+1]
        b_address = memory[position+2]

        r_address = memory[position+3]

        memory[r_address] = memory[a_address] + memory[b_address]
        position += 4

    # print position + 1
    elif instruction == 3:
        address = memory[position+1]
        print(memory[address])
        position+=2

    # if memory[position+1] is 0 jump to positon+2, else continue to position+3
    elif instruction == 4:
        address = memory[position+1]
        if memory[address] == 0:
            position = memory[position+2]
        else:
            position += 3

    # jump to value of position+1
    elif instruction == 5:
        position = memory[position+1]
```


start the computer and see the result!

```
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 3, 'position', 13)
50
('instruction', 0, 'position', 15)
```
