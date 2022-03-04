
## [DAY-192] Class; Methods


There are few ways to represent a rectangle, one is with one point plus width and height, e.g. top left point and width and height.


```
(the screen's y grows downwards, top left is 0,0)
    │       x=8                           x
────┼───────┬────────────────────────────────
    │       │
    │       │
 y=3├───────*──────────────────┐
    │       │##################│
    │       │##################│
    │       │##################│ height
    │       │##################│
    │       └──────────────────┘
    │              width
    │
    │
   y│
```

or you can store the position of two diagonal points, top left and bottom right (or top right and bottom left)

```
    │
    │       x=8              x=27         x
────┼───────┬──────────────────┬─────────────
    │       │                  │
    │       │                  │
 y=3├───────*──────────────────┤
    │       │##################│
    │       │##################│
    │       │##################│
    │       │##################│
 y=8├───────┴──────────────────*
    │
    │
   y│

```

In this example I chose the two points appriach as it I can just make a Point class and use it twice, but sometimes the first approach is more suitable. We want to make a Rect class that has a method to expand to include a point.

```
    │
    │       x=8              x=27   x=31    x
────┼───────┬──────────────────┬─────────────
    │       │                  │     .
    │       │                  │     .
 y=3├───────*──────────────────┤     .
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
 y=8├───────┴──────────────────*+++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
y=12│................................*
    │
    │
    │
   y│
```

> Pause here to think about how to approach this, use pen and paper to illustrate the approach.

The solutio is simply to move the topleft's x/y more left/up if they are bigger than the requested point, and move the bottomright's x/y if they are smaller than the requested point. This way the rectangle grows just enough to include the point.

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        if self.topLeft.y > point.y:
            self.topLeft.y = point.y
        if self.bottomRight.x < point.x:
            self.bottomRight.x = point.x
        if self.bottomRight.y < point.y:
            self.bottomRight.y = point.y

r = Rect(Point(10,10),Point(20,20))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(5,5))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,3))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

Sometimes its handy to be able to chain method calls, so if the method returns an instance you can just call a method on the returned value.

```
class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        ...
        return self

r = Rect(Point(10,10),Point(20,20))
r.expand(Point(5,5)).expand(Point(50,3)).expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

## [DAY-193] Richard Buckland's computer


Richard Buckland's Higher Computing course is absolutely brilliant, you can watch it on youtube: https://www.youtube.com/watch?v=JA_G8XbVYug&list=PL6B940F08B9773B9F

In the beginning of the course he makes up an virtual 4 bit computer that we can program into useful things.

It has two registers, R0 and R1, 16 4 bit slots in (8 bytes) memory and 16 instructions we could use. Some of the instructions take 1 byte, some take 2 bytes

```
                      │ IP: instruction pointer
┌──────┐ ┌──────┐     │ IS: instruction store (current instruction)
│IP: 0 │ │IS: 0 │     │ R0: register 0
└──────┘ └──────┘     │ R1: register 1
┌──────┐ ┌──────┐     ├──────────────────────────────────────────────
│R0: 0 │ │R1: 0 │     │    0 halt
└──────┘ └──────┘     │    1 add R0 = R0 + R1
  0   1   2   3       │    2 subtract R0 = R0 - R1
┌───┬───┬───┬───┐     │    3 increment R0 R0 = R0 + 1
│ 0 │ 0 │ 0 │ 0 │     │    4 increment R1 R1 = R1 + 1
├───┼───┼───┼───┤     │    5 decrement R0 R0 = R0 - 1
│ 0 │ 0 │ 0 │ 0 │     │    6 decrement R1 R1 = R1 - 1
├───┼───┼───┼───┤     │    7 ring bell
│ 0 │ 0 │ 0 │ 0 │     │  8 X print data X
├───┼───┼───┼───┤     │  9 X load value of address X into R0
│ 0 │ 0 │ 0 │ 0 │     │ 10 X load value of address X into R1
└───┴───┴───┴───┘     │ 11 X store R0 into address X
 12  13  14  15       │ 12 X store R1 into address X
                      │ 13 X jump to address X
                      │ 14 X jump to address X if R0 == 0
                      │ 15 X jump to address X if R0 != 0
```

Example programs (also some are from the video lecture):

* print 7 and beep

```
┌───┬───┬───┬───┐
│ 8 │ 7 │ 7 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```


* beep 3 times

```
┌───┬───┬───┬───┐
│ 7 │ 7 │ 7 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```


* print 3

```
┌───┬───┬───┬───┐
│ 8 │ 3 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```



* what would this program do?

```
┌───┬───┬───┬───┐
│ 7 │ 10│ 3 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```


* beep and put 3 in R1

```
┌───┬───┬───┬───┐
│ 7 │ 10│ 15│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 3 │
└───┴───┴───┴───┘ 
```

* beep forever

```
┌───┬───┬───┬───┐
│ 7 │ 13│  0│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 3 │
└───┴───┴───┴───┘ 
```

* put the value 4 in R0, increment it and put it back in memory and print it

```
┌──────┐ ┌──────┐ 
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘ 
┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 8 │ 4 │ 0 │
└───┴───┴───┴───┘
```

Lets walk through each step of the program, you can see the IP(instruction pointer) has a pointer to which memory address it is executing now, and IS(instruction store) is the current instruction:

```
START               load addr 14 in R0  increment R0
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │   │IP: 0 │ │IS: 10│   │IP: 2 │ │IS: 3 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘  
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │   │R0: 4 │ │R1: 0 │   │R0: 5 │ │R1: 0 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘

┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 8 │ 4 │ 0 │   │ 0 │ 8 │ 4 │ 0 │   │ 0 │ 8 │ 4 │ 0 │
└───┴───┴───┴───┘   └───┴───┴───┴───┘   └───┴───┴───┴───┘



put R0 in addr 14   jump to addr 13      print 5
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│IP: 3 │ │IS: 11│   │IP: 5 │ │IS: 13│   │IP: 13│ │IS: 8 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘ 
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│R0: 5 │ │R1: 0 │   │R0: 5 │ │R1: 0 │   │R0: 5 │ │R1: 0 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘

┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │ 
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 8 │ 5 │ 0 │   │ 0 │ 8 │ 5 │ 0 │   │ 0 │ 8 │ 5 │ 0 │
└───┴───┴───┴───┘   └───┴───┴───┴───┘   └───┴───┴───┴───┘


halt
┌──────┐ ┌──────┐ 
│IP: 15│ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 4 │ │R1: 0 │
└──────┘ └──────┘ 
┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 8 │ 5 │ 0 │
└───┴───┴───┴───┘
```

We can make a simpler to read language that we can easilly convert to machine code:
```
code  keyword   what it does
─────┼────────────────────────────────────
   0 │ halt      halt
   1 │ add       add R0 = R0 + R1
   2 │ sub       subtract R0 = R0 - R1
     │
   3 │ inc r0    increment R0 R0 = R0 + 1
   4 │ inc r1    increment R1 R1 = R1 + 1
   5 │ dec r0    decrement R0 R0 = R0 - 1
   6 │ dec r1    decrement R1 R1 = R1 - 1
     │ 
   7 │ ring      ring bell
     │
 8 X │ print     print X (whatever the next byte is)
     │
 9 X │ mov addr, r0  load value of address X into R0
10 X │ mov addr, r1  load value of address X into R1
     │
11 X │ mov r0, addr  store R0 into address X
12 X │ mov r1, addr  store R1 into address X
     │
13 X │ jmp addr   jump to address X
14 X │ je addr    jump to address X if R0 == 0
15 X │ jne addr   jump to address X if R0 != 0
```

now lets rewrite this program

```
┌──────┐ ┌──────┐ 
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘ 
┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 8 │ 4 │ 0 │
└───┴───┴───┴───┘
```

The same program looks like this:

```
0  mov 14, r0 # put value of addr 14 in r0
2  inc r0     # r0 += 1
3  mov r0, 14 # put r0's value in addr 14
5  jmp 13     # jump to addr 13
13 print      # print the next byte
15 halt       # halt
```

Which surely looks easier to read than `9 14 3 11 14 13 13 0 0 0 0 0 8 4 0`.

## [DAY-194] Self modifying programs

Make a program that prints the numbers from 12 to 1

![game-194.jpg](./screenshots/game-194.jpg "game 194 screenshot")


The instructions we will use are:

```
9X  - load value at address X to R0 (R0 = mem[x])
14X - jump to address if r0 == 0
11X - put value of R0 into memory address X (mem[x] = R0)
5   - decrement R0 (R0 -= 1)
13X - jump to address X
8X  - print X
```

And this is the program:

```
┌──────┐ ┌──────┐ 
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12|
└───┴───┴───┴───┘
```

Lets evaluate the program step by step:


```
9 15 - load the value of memory address 15 into R0
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 9 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

jump to address 12 if R0 == 0
┌──────┐ ┌──────┐
│IP: 2 │ │IS: 14│
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

place the value of R0 in address 7 (mem[7] = 12)
┌──────┐ ┌──────┐
│IP: 4 │ │IS: 11│
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

print 12

> this is the most important step of the program
> you see in the previous instruction (11 7), we modified the value 
> of the print instruction which is about to print the content of 
> the next byte, which was zero when our program started,
> but now it is filled with the current value of R0

┌──────┐ ┌──────┐
│IP: 6 │ │IS: 8 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

decrement R0 (R0 -= 1)
┌──────┐ ┌──────┐
│IP: 8 │ │IS: 5 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 11│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

jump to address 2
┌──────┐ ┌──────┐
│IP: 9 │ │IS: 13│
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 11│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

> back from scratch, check if R0 is zero, if not it will put its value 
> as the second byte of the print instruction and then decrement it 
> until it reaches zero, at which point it will jump to address 12 and halt, 
> 

┌──────┐ ┌──────┐
│IP: 12│ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 1 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

```


## [DAY-195] loops


![game-195.jpg](./screenshots/game-195.jpg "game 195 screenshot")

![game-195-b.jpg](./screenshots/game-195-b.jpg "game 194-b screenshot")


* beep forever

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 7 │ 13│ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```

* print 6 forever

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 8 │ 6 │ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```

* print 0 1 2 3 4 5 6 7 8 ... forever

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 8 │ 0 │ 3 │ 11│
├───┼───┼───┼───┤
│ 1 │ 13│ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```


* if R0 == 0 print 6 else print 7

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 14│ 6 │ 8 │ 7 │
├───┼───┼───┼───┤
│ 13│ 8 │ 8 │ 6 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```


## [DAY-196] loops

![game-196.jpg](./screenshots/game-196.jpg "game 196 screenshot")

* make a program that prints 0 15 1 14 2 13 3 12 4 11 5 10 ... 15 0

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 15│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 11│ 5 │ 12│ 7 │
├───┼───┼───┼───┤
│ 8 │ 0 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 4 │ 14│ 15│
├───┼───┼───┼───┤
│ 13│ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```

we will start with initial state of R0 and R1 to 15 and 0, then we will put R0's value in memory address 5 and R1 in address 7, where they will become arguments to two print instructions, then we will decrement R0 and increment R1, after that we check if R0 is zero if it is we go to halt at address 15, if not we loop back to the beginning but now with updated values of R0 and R1

* jump to a jump

follow the jumps in this program

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 13│ 2 │ 13│ 12│
├───┼───┼───┼───┤
│ 13│ 14│ 13│ 10│
├───┼───┼───┼───┤
│ 13│ 4 │ 13│ 8 │
├───┼───┼───┼───┤
│ 13│ 6 │ 13│ 0 │
└───┴───┴───┴───┘
```


## [DAY-196] interpreter

> I wrote a simple interpreter for the 4 bit cpu so we can discuss step by step, feel free to try to see what it does, print it on piece a paper and try to read it line by line


```
import sys
import time


def ascii(state, highlight):
    center = []
    for (i,s) in enumerate(state):
        if i-4 in highlight:
            s = "_"+str(s)+"_"
        center.append(str(s).center(4))

    print("""
    ┌────────┐ ┌────────┐
    │IP: {0}│ │IS: {1}│
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0: {2}│ │R1: {3}│
    └────────┘ └────────┘
      0    1    2    3
    ┌────┬────┬────┬────┐
  0 │{4}│{5}│{6}│{7}│ 3
    ├────┼────┼────┼────┤
  4 │{8}│{9}│{10}│{11}│ 7
    ├────┼────┼────┼────┤
  8 │{12}│{13}│{14}│{15}│ 11
    ├────┼────┼────┼────┤
 12 │{16}│{17}│{18}│{19}│ 15
    └────┴────┴────┴────┘  
      12   13   14   15   
""".format(*center))


def cpu(IP, IS, R0, R1, memory):
    """
                          │ IP: instruction pointer
    ┌──────┐ ┌──────┐     │ IS: instruction store (current instruction)
    │IP: 0 │ │IS: 0 │     │ R0: register 0
    └──────┘ └──────┘     │ R1: register 1
    ┌──────┐ ┌──────┐     ├──────────────────────────────────────────────
    │R0: 0 │ │R1: 0 │     │    0 halt
    └──────┘ └──────┘     │    1 add R0 = R0 + R1
      0   1   2   3       │    2 subtract R0 = R0 - R1
    ┌───┬───┬───┬───┐     │    3 increment R0 R0 = R0 + 1
    │ 0 │ 0 │ 0 │ 0 │     │    4 increment R1 R1 = R1 + 1
    ├───┼───┼───┼───┤     │    5 decrement R0 R0 = R0 - 1
    │ 0 │ 0 │ 0 │ 0 │     │    6 decrement R1 R1 = R1 - 1
    ├───┼───┼───┼───┤     │    7 ring bell
    │ 0 │ 0 │ 0 │ 0 │     │  8 X print data X
    ├───┼───┼───┼───┤     │  9 X load value of address X into R0
    │ 0 │ 0 │ 0 │ 0 │     │ 10 X load value of address X into R1
    └───┴───┴───┴───┘     │ 11 X store R0 into address X
     12  13  14  15       │ 12 X store R1 into address X
                          │ 13 X jump to address X
                          │ 14 X jump to address X if R0 == 0
                          │ 15 X jump to address X if R0 != 0
    """

    while True:
        IS = memory[IP]
        highlight = [IP]
        if (IS >= 8):
            highlight = [IP, IP+1]

        ascii([IP, IS, R0, R1, *memory], highlight)

        if IS == 0:
            break
        elif IS == 1:
            R0 = R0 + R1
            IP += 1
        elif IS == 2:
            R0 = R0 - R1
            IP += 1
        elif IS == 3:
            R0 += 1
            IP += 1
        elif IS == 4:
            R1 += 1
            IP += 1
        elif IS == 5:
            R0 -= 1
            IP += 1
        elif IS == 6:
            R1 -= 1
            IP += 1
        elif IS == 7:
            print("*** BEEP ***")
            IP += 1
        elif IS == 8:
            print("*** ", memory[IP+1], "***")
            IP += 2
        elif IS == 9:
            R0 = memory[memory[IP+1]]
            IP += 2
        elif IS == 10:
            R1 = memory[memory[IP+1]]
            IP += 2
        elif IS == 11:
            memory[memory[IP+1]] = R0
            IP += 2
        elif IS == 12:
            memory[memory[IP+1]] = R1
            IP += 2
        elif IS == 13:
            IP = memory[IP + 1]
        elif IS == 14:
            if R0 == 0:
                IP = memory[IP + 1]
            else:
                IP += 2
        elif IS == 15:
            if R0 != 0:
                IP = memory[IP + 1]
            else:
                IP += 2

        input()


if len(sys.argv) == 1 or ".prog" not in sys.argv[1]:
    print("usage: python3 ", sys.argv[0] + " file.prog")
    sys.exit(1)

f = open(sys.argv[1])
state = []
for line in f.readlines():
    if '#' in line:
        continue
    for s in line.replace("│", " ").split():
        if s.isdigit():
            state.append(int(s))
f.close()

instruction_pointer, instruction_store, r0, r1, *memory = state
cpu(instruction_pointer, instruction_store, r0, r1, memory)

```

Save a program as 'name.prog' and run it a `python3 interpreter.py name.prog`, then press enter for each step of the execution.

For example:

```
# print 1,2,3,1,2,3,1,2,3... forever
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 3 │ │R1: 1 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 12│ 3 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 4 │ 5 │ 15│ 12│
├───┼───┼───┼───┤
│ 9 │ 15│ 10│ 14│
├───┼───┼───┼───┤
│ 13│ 0 │ 1 │ 3 │
└───┴───┴───┴───┘
```

Will output of `python3 interpreter.py example.prog`:

```

    ┌────────┐ ┌────────┐
    │IP:  0  │ │IS:  12 │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘
      0    1    2    3
    ┌────┬────┬────┬────┐
  0 │_12_│_3_ │ 8  │ 0  │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  
      12   13   14   15   



    ┌────────┐ ┌────────┐
    │IP:  2  │ │IS:  8  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘
      0    1    2    3
    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │_8_ │_1_ │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  
      12   13   14   15   

***  1 ***


    ┌────────┐ ┌────────┐
    │IP:  4  │ │IS:  4  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘
      0    1    2    3
    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │ 8  │ 1  │ 3
    ├────┼────┼────┼────┤
  4 │_4_ │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  
      12   13   14   15   



    ┌────────┐ ┌────────┐
    │IP:  5  │ │IS:  5  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  2  │
    └────────┘ └────────┘
      0    1    2    3
    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │ 8  │ 1  │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │_5_ │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  
      12   13   14   15   



    ┌────────┐ ┌────────┐
    │IP:  6  │ │IS:  15 │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  2  │ │R1:  2  │
    └────────┘ └────────┘
      0    1    2    3
    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │ 8  │ 1  │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │ 5  │_15_│_12_│ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  
      12   13   14   15   

```