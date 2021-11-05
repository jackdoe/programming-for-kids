## [DAY-136] For; Arrays; Memory

Lets make a super simple C program

Just to get familiar witht he syntax, it does not use indentation to group code, but {}, and also each variable has to have known type (size), e.g we have to tell the C compiler (compiler is a program that takes the text code and transforms it into machine code) that  `i` is of type `int` which on our computer is exactly 4 bytes long.

```
#include <stdio.h>
int main() {
    int sum = 0;
    for (int i = 0; i < 100; i++) {
        sum += 10;
    }

    printf("%d\n", sum);
}
```

When you execute `gcc -o foo foo.c` (if you save the program in foo.c), it will make the binary `foo`, do `cat foo` to see the actual binary made from the compiler. If you run `objdump -D foo` you will see the assembly code and the machine code corresponding to it.

`cat foo`:
```
????X? H__PAGEZERO?__TEXT@@__text__TEXT0?X0??__stubs__TEXT????__stub_helper__TEXT?????__cstring__TEXT????__unwind_info__TEXT??H???__DATA_CONST@@@@__got__DATA_CONST@?__DATA?@?@__la_symbol_ptr__DATA?__data__DA?H__LINKEDIT?@?"?? ?0?0h???H
                               P?? 
                                   /usr/lib/dyld9??
                                                   f:^?[c?υ02 

                                                              ?*(?0?
                                                                    8d
                                                                      /usr/lib/libSystem.B.dylib&`)h?UH??H???E??E??E??}?d??E???
?E??E???E???????u?H?=2??	?E?H??]??%r@L?q@AS?%a?h?????%d
0?44??4
       ??#Q@dyld_stub_binderQr?s@_printf?__mh_execute_header!main%?~??0?$ __mh_execute_header_main_printfdyld_stub_binder__dyld_privat
```

Because its a binary file, most of the bytes are not actually printable ASCII characters, you can use `hexdump` to see the byte's values:

`hexdump -C foo`

```
00000000  cf fa ed fe 07 00 00 01  03 00 00 00 02 00 00 00  |................|
00000010  10 00 00 00 58 05 00 00  85 00 20 00 00 00 00 00  |....X..... .....|
00000020  19 00 00 00 48 00 00 00  5f 5f 50 41 47 45 5a 45  |....H...__PAGEZE|
00000030  52 4f 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |RO..............|
00000040  00 00 00 00 01 00 00 00  00 00 00 00 00 00 00 00  |................|
00000050  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000060  00 00 00 00 00 00 00 00  19 00 00 00 d8 01 00 00  |................|
00000070  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
00000080  00 00 00 00 01 00 00 00  00 40 00 00 00 00 00 00  |.........@......|
00000090  00 00 00 00 00 00 00 00  00 40 00 00 00 00 00 00  |.........@......|
000000a0  05 00 00 00 05 00 00 00  05 00 00 00 00 00 00 00  |................|
000000b0  5f 5f 74 65 78 74 00 00  00 00 00 00 00 00 00 00  |__text..........|
000000c0  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
000000d0  30 3f 00 00 01 00 00 00  58 00 00 00 00 00 00 00  |0?......X.......|
000000e0  30 3f 00 00 04 00 00 00  00 00 00 00 00 00 00 00  |0?..............|
000000f0  00 04 00 80 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000100  5f 5f 73 74 75 62 73 00  00 00 00 00 00 00 00 00  |__stubs.........|
00000110  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
00000120  88 3f 00 00 01 00 00 00  06 00 00 00 00 00 00 00  |.?..............|
00000130  88 3f 00 00 01 00 00 00  00 00 00 00 00 00 00 00  |.?..............|
00000140  08 04 00 80 00 00 00 00  06 00 00 00 00 00 00 00  |................|

[...]

```

`objdump -D foo`
```
[...]
100003f30: 55                           pushq   %rbp
100003f31: 48 89 e5                     movq    %rsp, %rbp
100003f34: 48 83 ec 10                  subq    $16, %rsp
100003f38: c7 45 fc 00 00 00 00         movl    $0, -4(%rbp)
100003f3f: c7 45 f8 00 00 00 00         movl    $0, -8(%rbp)
100003f46: c7 45 f4 00 00 00 00         movl    $0, -12(%rbp)
100003f4d: 83 7d f4 64                  cmpl    $100, -12(%rbp)
100003f51: 0f 8d 17 00 00 00            jge     0x100003f6e <_main+0x3e>
100003f57: 8b 45 f8                     movl    -8(%rbp), %eax
100003f5a: 83 c0 0a                     addl    $10, %eax
100003f5d: 89 45 f8                     movl    %eax, -8(%rbp)
100003f60: 8b 45 f4                     movl    -12(%rbp), %eax
100003f63: 83 c0 01                     addl    $1, %eax
100003f66: 89 45 f4                     movl    %eax, -12(%rbp)
100003f69: e9 df ff ff ff               jmp     0x100003f4d <_main+0x1d>
[...]
```

`addl` meand `add`, `jmp` means jump and so forth. This is not important for now, the point is that `gcc` which is a popular C compiler, will take your code and make it into machine code.

Lets have another example:


FizzBuzz

```
#include <stdio.h>
int main() {
    for (int i = 0; i < 100; i++) {
        if (i % 15 == 0) {
            printf("fizzbuzz\n");
        } else if (i % 5 == 0) {
            printf("buzz\n");
        } else if (i % 3 == 0) {
            printf("fizz\n");
        } else {
            printf("%d\n",i);
        }
    }
}
```

What is your name?

```
#include <stdio.h>
int main() {
    char input[20] = {0};
    while(1) {
        printf("What is your name: ");
        scanf("%s",input);
        printf("\nHello %s\n",input);
    }
}
```

You see how we say `char input[20]` which means we habe 20 elements of type `char` pointed by the input variable, it is literally just a pointer to some memory, and we can use `input[1]` to go to the address `input` plus 1 byte. Same with `int x[10]`, if we do x[3], it will go to the address pointed by `x` and add 3 * 4 to it.

We can make interesting bugs like that, because nobody will check if we go and read somewhere outside of the defined array:


```
#include <stdio.h>
int main() {
    char input[20] = {0};
    int b = 5;
    while(1) {
        printf("What is your name: ");
        scanf("%s",input);
        printf("\nHello %s\n",input);

        for (int i = 0; i < 40; i++) {
            printf("  %d -> %d -> %c\n", i, input[i],input[i]);
        }
    }
}

```

You will see some garbage from element 20 to 39, because it will actually go and read beyond the input bounderioes.


## [DAY-137] For; File; If

Play with [words.txt](words.txt)

Open the file and print all the lines:

```
f = open("words.txt")
for line in f:
    print(line)
```

Remove the newline:

```
f = open("words.txt")
for line in f:
    word = line.strip()
    print(word)
```

Print only words with more than 10 characters:

```
f = open("words.txt")
for line in f:
    word = line.strip()
    if len(word) > 10:
        print(word)
```

Print only words starting with 'ab':

```
f = open("words.txt")
for line in f:
    word = line.strip()
    if word[0] == 'a' and word[1] == 'b':
        print(word)
```

Print words not containing a character

```
f = open("words.txt")
for line in f:
    word = line.strip()
    if 'e' not in word:
        print(word)
```

Avoid words containing multiple characters

```
f = open("words.txt")
def avoid(word, characters):
    for c in characters:
        for w in word:
            if w == c:
                return False
    return True

for line in f:
    word = line.strip()
    if avoid(word, ['a','b','c']):
        print(word)
```

Another implementation using 'char' in 'string':

```
f = open("words.txt")

def avoid(word, characters):
    for c in characters:
        for c in word:
            return False
    return True

for line in f:
    word = line.strip()
    if avoid(word, ['a','b','c']):
        print(word)
```

Spinning turtle

![game-137.png](./screenshots/game-137.png "game 137 screenshot")


```
import turtle as t
size = 10
t.speed(10000)
while True:
    t.right(150)
    t.forward(size)
    size += 1
```

![game-137-3.png](./screenshots/game-137-3.png "game 137-3 screenshot")

```
import turtle as t
size = 10
t.speed(10000)
while True:
    t.right(150)
    t.forward(size)
    if size % 2 == 0:
        t.color('cyan')
    else:
        t.color('magenta')
    size += 1

```

![game-137-4.png](./screenshots/game-137-4.png "game 137-4 screenshot")

```
import turtle as t
size = 1
t.speed(100000)
t.bgcolor('black')
t.hideturtle()
i = 0
while True:
    if i % 2 == 0:
        t.color('cyan')
    else:
        t.color('magenta')
    t.forward(i*3)
    t.left(91)
    i+=1
```
![game-137-2.png](./screenshots/game-137-2.png "game 137-2 screenshot")

```
from turtle import *
begin_fill()
color('red')
pensize(3)
left(48)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
done()
```

![game-137-1.png](./screenshots/game-137-1.png "game 137-1 screenshot")


```
from turtle import *
size = 1
speed(10000)
while True:
    if size % 2 == 0:
        color('blue')
    else:
        color('red')

    circle(size, size * 5)
    size += 1
```


## [DAY-138] For; File; If

Take it easy.

Count how many lines have exactly 5 characters

```
fi = open('words.txt')
n = 0
for line in fi:
    w = line.strip()
    if len(w) == 5:
        n += 1
print(n)
```

How many words have 7 and how many 5 characters?

```
fi = open('words.txt')
n = 0
x = 0
for line in fi:
    w = line.strip()
    if len(w) == 5:
        n += 1
    if len(w) == 7:
        x += 1 
print(n)
print(x)
```
## [DAY-139] While; List; Counter

First touchtype for 20 minutes.

Then do some chill turtle shapes.

![game-139-2.png](./screenshots/game-139-2.png "game 139-2 screenshot")

```
from turtle import *

speed(100000)
pencolor('cyan')
size = 66
while True:
    forward(size)
    left(size)
    size += 1
```

![game-139-1.png](./screenshots/game-139-1.png "game 139-1 screenshot")

```
from turtle import *

c = ['cyan','magenta']
dist = 20

hideturtle()
speed(11)

while True:
    color(c[dist%2])
    forward(dist)
    left(90)
    dist = dist-3
```




## [DAY-140] While; Turtle; Strings

Read the strings chapter in the Thinking Python book.

Then do some chill turtle shapes.

![game-140-1.png](./screenshots/game-140-1.png "game 140-1 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)

while True:
    for x in turtles:
        size = random.randint(10,300)
        extent = random.randint(0, 360)
        x.circle(size, extent=extent)

```


![game-140-2.png](./screenshots/game-140-2.png "game 140-2 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)



while True:
    for x in turtles:
        size = random.randint(10,300)
        for i in range(4):
            x.forward(size)
            x.right(90)

        x.circle(size)
```




![game-140-3.png](./screenshots/game-140-3.png "game 140-3 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)



while True:
    for x in turtles:
        size = random.randint(10,300)
        for i in range(4):
            x.forward(size)
            x.right(90)
```


![game-140-4.png](./screenshots/game-140-4.png "game 140-4 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)



while True:
    for x in turtles:
        size = random.randint(10,300)
        x.circle(size)
```


## [DAY-141] Wiki; API

Today we are going to make a small app that uses wikipedia. First install the wikipedia package:
```
pip3 install wikipedia
```

```
import wikipedia as wiki

while True:
    what = input("search> ")
    summary = wiki.summary(what)
    print(summary)
    print('*' * 40)
```

Will search wikipeadia the string you input, like this:

```
search> leonadro da vinci
Leonardo da Vinci (15 April 1452 – 2 May 1519) was an Italian polymath of...
[...]
search>
```

Lets do the same but with pygame:

![game-141.png](./screenshots/game-141.png "game 141 screenshot")

```
import wikipedia as wiki
import pgzrun

HEIGHT = 800
WIDTH = 800
text = ''
info = ''
def on_key_down(key, mod, unicode):
    global text, info
    if key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:-1]
    elif key == keys.RETURN:
        info = wiki.summary(text)
        text = ''

    elif len(unicode) > 0 and ord(unicode) >= 32 and ord(unicode) <= 126:
        text += unicode


def draw():
    screen.clear()
    screen.draw.text(info, (10,10), fontsize=18,fontname="437-win", width=WIDTH-20)
    screen.draw.text(text, (WIDTH/2,HEIGHT - 40), color=(255,0,0), fontsize=30,fontname="437-win")

pgzrun.go()
```

What does this do actually? How does the wikipedia module work? First thing you want to check is the documentation page, https://pypi.org/project/wikipedia/ and then you can also check the source code: https://github.com/goldsmith/Wikipedia

Next you would like to think, how would this python module download the data from wikipedia.

What it actually does, is it opens a web page, just a page that is specifically made to be easier to be read with programs, try to open: https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&explaintext=&titles=Dog which will be the page for `Dog`, you will see:

```
{"batchcomplete":"","query":{"pages":{"4269567":{"pageid":4269567,"ns":0,"title":"Dog","extract":"The dog or domestic dog
[...]
an end to the dinosaurs and the appearance of the first carnivoran...
[...]
Their personality traits include hypersocial behavior, boldnes
[...]
```

You can see the equivalent HTML page at https://en.wikipedia.org/wiki/Dog, The other page, which had structured data easier to read by python and any other programming language, is called API, Application Proggramming Interface. It just means that someone thought explicitly that their output will be read by programs and not people, and so they designed the interface that way. In the wikipedia example they return JSON.

JSON is data serialization format, its goal is to make it easy for programs to exchange data, for example I can have an array, or dictionary, and I want to make it easy for some other program to read it, so I use JSON to make it into text with special rules, and they can use their JSON decoder to make it into data.

```
>>> import json
>>> a = {"a":"b","c":3}
>>>
>>> print(json.dumps([1,2,a]))
[1, 2, {"a": "b", "c": 3}]
>>>
>>> d = json.loads('[1, 2, {"a": "b", "c": 3}]')
>>> d
[1, 2, {'a': 'b', 'c': 3}]
```


You see how it looks similar to the wikipedia API output, we will go in depth in the JSON format some times later, the point now is to just recognize that there is a whole world of APIs that are gluing the programs on your computer, and even the internet together so they can communicate. JSON is one of the most common serialization protocol, but there are many many more.

