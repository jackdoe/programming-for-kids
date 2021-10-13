## [DAY-95] Memory; Machine Code; Virtual Computer

It will be super nice if our multiply program can be used from multiple places from a bigger program:

```
...
r = multiply(5, 10)
print(r)
...
```

We can kind of do that, by just using jump, and carefully writing the multiply function in such a way, that when it is done, to jump back to where we called it. We also have to give it some values to work with, in our case 5 and 10.

We will use a simple list to append the values and the return address, and then pop them out in the right order to use them. Our multiply function has to know how many values to read and it must know which one of them is the return address. `[5, 10, ZZZ]` imagine ZZZ is the address where we should return after we have computed the result. And then the function will just do POP, POP, POP and know, first POP will be ZZZ, second pop will be one parameter, third pop will be another parameter. Do what it does with the parameters, and then append its result into the stack, then the caller must know to POP it.

It is called a stack because it is like a stack of things on top of each other (cards for example), you can append(push) one to the top, or remove one from the top (pop). When we pop() we will remove the last thing we push()ed.

If I push 1,2,3 then if i pop 3 times I will print 3 2 1

```
stack = [1,2,3]

print(stack.pop())
print(stack.pop())
print(stack.pop())
```

Here is our updated program, and computer:

```
memory = []
for i in range(1000000):
    memory.append(0)

HALT         = 0
ADD          = 1
PRINT        = 3
JUMP_IF_ZERO = 4
JUMP         = 5
PUSH         = 8
POP          = 9
SET          = 10

JUMPV        = 11 # same as jump, but jumps to the
                  # value of the address instead of the address itself
                  # so jumpv 9, will jump to the value of memory[9]

PUSHV        = 12 # same as jumpv but for push


# just used for debug
instruction_lookup = dict([
    (HALT         , 'HALT'),
    (ADD          , 'ADD'),
    (PRINT        , 'PRINT'),
    (JUMP_IF_ZERO , 'JUMP_IF_ZERO'),
    (JUMP         , 'JUMP'),
    (PUSH         , 'PUSH'),
    (POP          , 'POP'),
    (SET          , 'SET'),
    (PUSHV        , 'PUSHV'),
    (JUMPV        , 'JUMPV')
])

                  # pushv 9, will push memory[9] instead of 9
# constants addressess
# there is no such thing as constants though, we just think of them as such
MINUS_1 = 9999

# set "global" variable MINUS_1 to -1
memory[MINUS_1] = -1 # minus_1 = -1

# MAIN FUNCTION

# main function has only one variable, the MULTIPLY_RESULT
MULTIPLY_RESULT = 1000

# MULTIPLY_RESULT = multiply (5, 10)
memory[0] = PUSH            # |  |
memory[1] = 5               # ^  |
memory[2] = PUSH            #    |
memory[3] = 10              # >--+
memory[4] = PUSH            # >-------------+
memory[5] = 8               #               | after the function is called
memory[6] = JUMP            #               | jump to get the value
memory[7] = 198             #               | from the stack
memory[8] = POP             # <-------------+
memory[9] = MULTIPLY_RESULT #
memory[10] = PRINT
memory[11] = MULTIPLY_RESULT


####### MULTIPLY FUNCTION ######
# get the value of A
A = 9000
B = 9001
COUNTER = 9003
R = 9004
BACK_TO_ADDRESS = 9005

# get the value for where to return to
memory[198] = POP
memory[199] = BACK_TO_ADDRESS

# get the value for A
memory[200] = POP
memory[201] = A

# get the value for B
memory[202] = POP
memory[203] = B

# COUNTER = B (which is counter = 0 ; counter = counter + b)
# COUNTER = 0
memory[204] = SET
memory[205] = COUNTER
memory[206] = 0

# COUNTER = COUNTER + B
memory[207] = ADD
memory[208] = COUNTER
memory[209] = B
memory[210] = COUNTER

# the actual loop
memory[211] = JUMP_IF_ZERO
memory[212] = COUNTER
memory[213] = 224

# r = r + a
memory[214] = ADD
memory[215] = A
memory[216] = R
memory[217] = R

# since our add operation adds two things in memory, we
# need to store the value -1 somewhere to subtract it from the counter
#
# counter -= 1
memory[218] = ADD
memory[219] = COUNTER
memory[220] = MINUS_1
memory[221] = COUNTER

# go back to the if counter == 0 instruction
memory[222] = JUMP
memory[223] = 211

# return(r)
memory[224] = PUSHV
memory[225] = R

memory[226] = JUMPV
memory[227] = BACK_TO_ADDRESS

# start the computer from position 80, we will use positions up-to 80 for our function call stack
position = 0
stack = []
while True:
    instruction = memory[position]

    print(instruction_lookup[instruction], 'position',position, 'stack', stack)

    # quit if instruction is 0
    if instruction == HALT:
        break

    # add position+1 and position+2 and write result in position+3
    elif instruction == ADD:
        a_address = memory[position+1]
        b_address = memory[position+2]

        r_address = memory[position+3]

        memory[r_address] = memory[a_address] + memory[b_address]
        position += 4

    # print position + 1
    elif instruction == PRINT:
        address = memory[position+1]
        print(memory[address])
        position+=2

    # if memory[position+1] is 0 jump to positon+2, else continue to position+3
    elif instruction == JUMP_IF_ZERO:
        address = memory[position+1]
        if memory[address] == 0:
            position = memory[position+2]
        else:
            position += 3

    # jump to value of position+1
    elif instruction == JUMP:
        position = memory[position+1]

    elif instruction == JUMPV:
        position = memory[memory[position+1]]

    elif instruction == PUSH:
        stack.append(memory[position+1])
        position += 2

    elif instruction == PUSHV:
        stack.append(memory[memory[position+1]])
        position += 2

    elif instruction == POP:
        memory[memory[position+1]] = stack.pop()
        position += 2

    elif instruction == SET:
        memory[position+1] = memory[position+2]
        position += 3
```

We cheated a bit by using python's lists instead of our own list to do the stack. We could reserve some memory (e.g. 100000 to 200000) and just push and pop the values there, memory[100000] will just say how many elements we have in the stack, and PUSH will do `memory[[memory[100000]] = value, memory[100000] += 1`, and pop will do `memory[100000] -= 1` and use `memory[memory[100000]]` as value.

You see how powerfull are continous pieces of memory? Arrays and Lists are how computers are built!

Look. In reallity more things happen, and actually normal machine code is easier than this, you can store values in temporary places called registers, and access them really fast and nobody actually writes code like that, we use languages such as Assembler to help us, and using assemblers we built other languages, such as C, and with C we built others, such as python, and then with python we build whole systems, like instagram or dropbox. You can of course build instagram with machine code if you want, it will just take incredible amount of time, and will be gazillion times more buggy. C is good at some things that python is not, and the other way around.

The one thing you have to remember, is whatever language you are using, whatever program you are looking at, it must have some memory, and some way of modifying that memory, and execute instructions over it.

There is no magic, it is all built on this. Built with few numbers in a block of memory.


Lets examine the output of the program, you see how the stack is empty, then we add 5, 10, and then 8 which will be used from the function to go back to us.

```
PUSH position 0 stack-before [] stack-after [5]
PUSH position 2 stack-before [5] stack-after [5, 10]
PUSH position 4 stack-before [5, 10] stack-after [5, 10, 8]
JUMP position 6 stack-before [5, 10, 8] stack-after [5, 10, 8]
POP position 198 stack-before [5, 10, 8] stack-after [5, 10]
POP position 200 stack-before [5, 10] stack-after [5]
POP position 202 stack-before [5] stack-after []
SET position 204 stack-before [] stack-after []
ADD position 207 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
PUSHV position 224 stack-before [] stack-after [50]
JUMPV position 226 stack-before [50] stack-after [50]
POP position 8 stack-before [50] stack-after []
PRINT position 10 stack-before [] stack-after []
50
HALT position 12 stack-before []
```


We could do it the other way, first push the address to go back to, and then the values, which will be the same, we just have to decide, this is called a 'calling convention', convention is just the usuall way to do things. So each program on your computer obeys the calling convention, otherwise a chaos will arrive, imagine multiplying the return address by first paremeter and then returning to some random position in memory.

By now you can see how fragile this is, if one mistake is made, you can corrupt rest of the program, we can easilly write something into where the next instruciton is read, and make the computer halt, or go into infinite loop.

Sometimes we can find bugs in a program that we can exploit, if we can simply control the corruption, we can make it jump to somewhere where we have our own code, and then we can control what the program does.

## [DAY-96] Binary; ASCII; Memory

Lets spend a day on bits and bytes.

One bit is the minimum amount of information you can hold, it is either 1 or 0, on or off. If we have a variable that has to store the heads or tails value of a coin, we can store it in 1 bit, lets say 1 is heads, 0 is tails. To store the values of two coins we can use 2 bits.

```
0 # tails
1 # heads
```
2 possible

```
0 0 # both coins are tails
0 1 # second coin is heads
1 0 # first coin is heads
1 1 # both coins are heads
```

2 * 2 possible

We have 4 distinct values, in 2 bits, lets try 3 coins

```
000
001
010
011
100
101
110
111
```
2 * 2 * 2 possible

we have 8 distinct values in 3 bits, and in 4 bits we have 16 distinct values

```
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
```

2 * 2 * 2 * 2 possible

in 32 bits we can store 4294967295 distinct values! and in 64 bits we can store 18446744073709551615.

But what about if we want to store the value of a dice? Possible values are 1 2 3 4 5 6. We can do that in just 3 bits.

8 bits make a byte. Usually we need 1 bit of information for the sign of the number, is it - or +, so sometimes you will hear "signed integer" or "unsigned integer", and the difference is the unsigned integers get one more bit to work with, which is a big deal, if the integer is 4 bytes, that is 32 bits, the maximum possible numbmer for signed integer is 2147483647, and the minimum is -2147483647, but unsigned one is from 0 to 4294967295.

The reason is 2 * 2 * 2 * 2 * 2 * 2... 31 times is twice smaller than 2 * 2 * 2 * 2 ... 32 times.

We can also count in this system (called binary system) to make it represent numbers.

try this:

```
for i in range(255):
    print(i, ' -> ', format(i, '08b'))
```

in python format can take a number and print it as binary number:

```
0   ->  00000000
1   ->  00000001
2   ->  00000010
3   ->  00000011
4   ->  00000100
5   ->  00000101
6   ->  00000110
7   ->  00000111
8   ->  00001000
9   ->  00001001
10  ->  00001010
11  ->  00001011
12  ->  00001100
13  ->  00001101
14  ->  00001110
15  ->  00001111
16  ->  00010000
...
```

the rules to count in the binary system are the same in the decimal system, when you go from 9 to 10 you increase the number of digits, but here.. you havbe to do it many more because you habe only 0 and 1.

so you start with 0, then 1, then you are out of numbers, so you add one more and then ext one is 1 0, then 1 1 and then you are out of space again, and go 1 0 0, 1 0 1, 1 1 0, 1 1 1 and so on.

So if you need to store the number `x = 47917437`, which in binary is 10110110110010100101111101, you will need 27 bits of space. However there are more limitations, you can usually store only 4 or 8 bytes (so 32 or 64 bits) because of the way the computer is made, so we will just pad it with zeros, and what will get stored on the memory chip is 0000010110110110010100101111101, and python will know the address of that, so when you say 'a = x + 1' it will go to the specific address, read the value, add one to it, and store it back.


example if we want to store `5, h e l l o`, the computer memory might look like this:
```
       5               h                 e              l                    l               o
       5              104               101            108                  108             111

0,0,0,0,0,1,0,1, 0,1,1,0,1,0,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,1,1
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
...
```

If we use 1 byte per character, ASCII actuaklly fitst in 7 bits (its called 7 bit ascii) as the maximum value is 127, but we store things aligned to 1 byte, the way processors are made, they have certain restrictions,m they cant just go and read/write at a specific bit position in the memory, so many times when we want to store 7 bits of data we need to use 8 bits, Unless we come with something to store in the extra bit, it will be just waste.

## [DAY-97] Lists; 

![game-97.png](./screenshots/game-97.png "game 97 screenshot")

Catch all the falling snakes.

Take this skeleton, and fill in the blanks.

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 300

falling = []
game_area = Rect(0,0,WIDTH,HEIGHT)
elf = Actor("c1")

elf.y = HEIGHT - 10
elf.x = WIDTH/2
game_over = False

def drop():
    f = Actor("snake")
    f.x = random.randint(0,WIDTH)
    f.y = random.randint(0, 150)
    falling.append(f)

def update():
    global game_over

    # move the elf left or right
    ...


    # detect the collisions between snakes and elf
    # and remove them if they collide
    ...


    # advance the snakes downwards
    ...


    # check if the snakes are outside of the game area, and set game over
    ...


    # add new snakes if there are less than 5 on the screen
    ...


def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')
        for f in falling:
            f.draw()

        screen.draw.rect(game_area, (255,0,0))
        elf.draw()

pgzrun.go()

```

This is one example of implementing it, can you think of another?

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 300

falling = []
game_area = Rect(0,0,WIDTH,HEIGHT)
elf = Actor("c1")

elf.y = HEIGHT - 10
elf.x = WIDTH/2
game_over = False

def drop():
    f = Actor("snake")
    f.x = random.randint(0,WIDTH)
    f.y = random.randint(0, 150)
    falling.append(f)

def update():
    global game_over

    # move the elf left or right
    if keyboard.left:
        elf.x = elf.x-5
    if keyboard.right:
        elf.x = elf.x+5


    # detect the collisions between snakes and elf
    # and remove them if they collide
    remove = []
    for f in falling:
        if f.colliderect(elf):
            remove.append(f)

    for r in remove:
        falling.remove(r)

    # advance the snakes downwards
    for f in falling:
        f.y += 1

    # check if the snakes are outside of the game area, and set game over
    for f in falling:
        if not f.colliderect(game_area):
            game_over = True

    # add new snakes if there are less than 5 on the screen
    if len(falling) < 5:
        drop()

def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')
        for f in falling:
            f.draw()

        screen.draw.rect(game_area, (255,0,0))
        elf.draw()

pgzrun.go()
```

Another possible implementation, this one uses `list()` to make a copy of the falling list and also has score and lives.

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 300

falling = []
game_area = Rect(0,0,WIDTH,HEIGHT)
elf = Actor("c1")

elf.y = HEIGHT - 10
elf.x = WIDTH/2
game_over = False
score = 0
lives = 5

def drop():
    f = Actor("snake")
    f.x = random.randint(0,WIDTH)
    f.y = random.randint(0, 150)
    falling.append(f)

def update():
    global game_over, score, lives


    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5

    for i in falling:
        i.y += 1

    for i in list(falling):
        if not i.colliderect(game_area):
            falling.remove(i)
            lives -= 1

    game_over = lives <= 0

    if len(falling) < 5:
        drop()

    for i in list(falling):
        if i.colliderect(elf):
            falling.remove(i)
            score += 1

def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')
        screen.draw.text("score: " + str(score) + " lives: " + str(lives), topleft=(10,10))

        for f in falling:
            f.draw()

        screen.draw.rect(game_area, (255,0,0))
        elf.draw()

pgzrun.go()
```


## [DAY-98] Lists; Read/Write File


![game-98-a.png](./screenshots/game-98-a.png "game 98-a screenshot")

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
colors = [
    [(255,0,0), Rect(0,0,40,40)],
    [(0,255,0), Rect(60,0,40,40)],
    [(0,0,255), Rect(120,0,40,40)],
]
color = None
pixels = []

def update():
    global color, pixels

    if keyboard.LEFT:
        elf.x -= 2
    if keyboard.RIGHT:
        elf.x += 2
    if keyboard.UP:
        elf.y -= 2
    if keyboard.DOWN:
        elf.y += 2

    if keyboard.Q:
        sys.exit(0)

    if keyboard.SPACE and color != None:
        pixels.append([
            color,
            Rect(elf.x,elf.y,40,40)
        ])

    if keyboard.C:
        pixels = []
        color = None

    if keyboard.D:
        drop = Rect(elf.x,elf.y,40,40)
        for p in list(pixels):
            if drop.colliderect(p[1]):
                pixels.remove(p)

    for c in colors:
        if elf.colliderect(c[1]):
            color = c[0]

def draw():
    screen.fill('black')

    for c in colors:
        screen.draw.filled_rect(c[1], c[0])

    for p in pixels:
        screen.draw.filled_rect(p[1], p[0])

    if color != None:
        screen.draw.rect(Rect(elf.x,elf.y,40,40), color)

    elf.draw()
    screen.draw.text(str(len(pixels)), topleft=(10,10))

pgzrun.go()
```

Simple catch the flower game

![game-98-b.png](./screenshots/game-98-b.png "game 98-b screenshot")

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
flower = Actor("flower")

def update():
    if keyboard.LEFT:
        elf.x -= 5
    # add RIGHT/UP/DONW

    if keyboard.Q:
        sys.exit(0)

    # check if the elf collides the flower
    # and if it does, increment the score
    # and place the flower on some random place
    # ...

def draw():
    screen.fill('black')
    elf.draw()
    flower.draw()

    # show the score
    # ...
pgzrun.go()
```

Example implementation:

```
import pgzrun
import random
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
elf.x = WIDTH/2
elf.y = HEIGHT/2

flower = Actor("flower")
flower.x = 10
flower.y = 10
score = 0
def update():
    global score
    if keyboard.LEFT:
        elf.x -= 5
    if keyboard.RIGHT:
        elf.x += 5
    if keyboard.UP:
        elf.y -= 5
    if keyboard.DOWN:
        elf.y += 5

    if keyboard.Q:
        sys.exit(0)

    if elf.colliderect(flower):
        flower.x = random.randint(10,WIDTH-10)
        flower.y = random.randint(10,HEIGHT-10)
        score += 1

def draw():
    screen.fill('black')
    elf.draw()
    flower.draw()
    screen.draw.text(str(score), topleft=(10,10))

pgzrun.go()
```

Same program but with Load and Save

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
colors = [
    [(255,0,0), Rect(0,0,40,40)],
    [(0,255,0), Rect(60,0,40,40)],
    [(0,0,255), Rect(120,0,40,40)],
]
color = None
pixels = []

def make_rect_around_actor(a):
    return Rect(a.x,a.y,40,40)
def update():
    global color, pixels

    if keyboard.LEFT:
        elf.x -= 2
    if keyboard.RIGHT:
        elf.x += 2
    if keyboard.UP:
        elf.y -= 2
    if keyboard.DOWN:
        elf.y += 2

    if keyboard.Q:
        sys.exit(0)

    if keyboard.SPACE and color != None:
        pixels.append([
            color,
            make_rect_around_actor(elf),
        ])

    if keyboard.C:
        pixels = []
        color = None

    if keyboard.S:
        f = open("save.txt", "w")
        for p in pixels:
            (red,green,blue) = p[0]
            f.write(str(red))
            f.write(",")
            f.write(str(green))
            f.write(",")
            f.write(str(blue))
            f.write(",")
            f.write(str(p[1].x))
            f.write(",")
            f.write(str(p[1].y))
            f.write(",")
            f.write(str(p[1].width))
            f.write(",")
            f.write(str(p[1].height))
            f.write("\n")
        f.close()

    if keyboard.L:
        pixels = []

        f = open("save.txt", "r")

        lines = f.readlines()
        for l in lines:
            (red,green,blue,x,y,w,h) = l.split(",")
            pixels.append([
                (float(red),float(green),float(blue)),
                Rect(float(x),float(y), float(w), float(h))
            ])

        f.close()

    if keyboard.D:
        drop = make_rect_around_actor(elf)
        for p in list(pixels):
            if drop.colliderect(p[1]):
                pixels.remove(p)

    for c in colors:
        if elf.colliderect(c[1]):
            color = c[0]

def draw():
    screen.fill('black')

    for c in colors:
        screen.draw.filled_rect(c[1], c[0])

    for p in pixels:
        screen.draw.filled_rect(p[1], p[0])

    if color != None:
        screen.draw.rect(make_rect_around_actor(elf), color)

    elf.draw()
    screen.draw.text(str(len(pixels)), topleft=(10,10))

pgzrun.go()
```
## [DAY-99] Classes; Lists; Functions; Cartesian Coordinates

Today we talk about classes and instances.

Classes are a bit like the houses you buy in roblox, its just a recepie for a house, and when you buy it you can customize it.

If two people have houses made from the same blueprint, we call them instances, they are seperate entities, you can lock one and that does not mean the other is locked. One can have a couch the other one doesn't.

The blueprint or recipe we call 'class' and the real thing that comes out of it we call 'instance'.

The class can define functions, and those functions will take a magic `self` parameter, where `self` will be the instance. For example in roblox, the house probably has a function 'lock()' that does something like `self.is_locked = True`.

Those functions are called 'methods' and the instance is also called an object. A method is supposed to be a bit like a message to the object, `p.colliderect(r)` for example you can look at sending the message `colliderect` to the object `p` with parameter `r`. Or you can look at it just as a function with hidden `self` parameter. In the following example you can see a method `def colliderect(self,r)` in the Point class, and also a standalone function `def collidepoint(rect, point)` that just expects a rect and a point objects.


```
class Point:
    x = 0
    y = 0
    def __init__(self, name):
        self.name = name

    def print(self):
        print('point',self.x,self.y,self.name)

    def colliderect(self,r):
        return self.x > r.x and self.x < r.x + r.w and self.y > r.y and self.y < r.y + r.h

class Rect:
    x = 0
    y = 0
    w = 0
    h = 0
    def print(self):
        print('rect',self.x,self.y,self.w,self.h)


#
# |-----------------------+
# |                       |
# 6  +-------+            |
# |  |       |            |
# 4--|---x   |            |
# |  |   |   |            |
# 2--+-------+            |
# |  |   |   |            |
# +--2---6---9------------+
# 0,0
def collidepoint(rect, point):
    if point.x > rect.x and point.x < rect.x + rect.w and point.y > rect.y and point.y < rect.y + rect.h:
        return True
    else:
        return False

p = Point("blue") # instance
p.x = 6
p.y = 4

r = Rect() # instance
r.x = 2
r.y = 2
r.w = 7
r.h = 4

if collidepoint(r,p):
    print("COLLIDES")
    r.print()
    p.print()

p2 = Point("red")
p2.x = 10
p2.y = 10
if not collidepoint(r,p2):
    print("NO COLLISION")
    r.print()
    p.print()


if p.colliderect(r):
    print("p collides")
```

```
import pgzrun
import sys # for sys.exit()
import random

HEIGHT = 600
WIDTH = 600

elf = Actor("c1")
speed = 3
back = []
def update():
    global score
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.J:
        f = Actor('flower')
        f.x = elf.x
        f.y = elf.y
        back.append(f)

    if keyboard.M:
        f = open("save.txt", "w")
        for x in back:
            f.write(str(x.x))
            f.write(",")
            f.write(str(x.y))
            f.write("\n")
        f.close()
    if keyboard.L:
        f = open("save.txt", "r")
        for line in f.readlines():
            (x,y) = line.split(",") # 30,20
            a = Actor('flower')
            a.x = float(x)
            a.y = float(y)
            back.append(a)
        f.close()
    if keyboard.Q:
        sys.exit(0)

def draw():
    screen.fill('black')

    for i in back:
        i.draw()

    elf.draw()

pgzrun.go()
```

![game-99.png](./screenshots/game-99.png "game 99 screenshot")

simpler painting game:

```
import pgzrun
import sys # for sys.exit()
import random

HEIGHT = 600
WIDTH = 600

elf = Actor("c1")
speed = 3
back = []
def update():
    global score
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.J:
        f = Actor('flower')
        f.x = elf.x
        f.y = elf.y
        back.append(f)

    if keyboard.M:
        f = open("save.txt", "w")
        for x in back:
            f.write(str(x.x))
            f.write(",")
            f.write(str(x.y))
            f.write("\n")
        f.close()
    if keyboard.L:
        f = open("save.txt", "r")
        for line in f.readlines():
            (x,y) = line.split(",") # 30,20
            a = Actor('flower')
            a.x = float(x)
            a.y = float(y)
            back.append(a)
        f.close()
    if keyboard.Q:
        sys.exit(0)

def draw():
    screen.fill('black')

    for i in back:
        i.draw()

    elf.draw()

pgzrun.go()
```

## [DAY-100] Touch Typing; Lists

Day 100 party!

We will make another touch typing game

![game-100.png](./screenshots/game-100.png "game 100 screenshot")

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 600

words = []
text = ''
game_over = False
beep = tone.create('A3', 0.5)

def move():
    global game_over
    for w in words:
        w[1]+= random.randint(10,15)
        if w[1] > HEIGHT:
            game_over = True

def add_word():
    common = ['a','about','all','also','and','as','at','be','because','but','by','can','come','could','day',
              'do','even','find','first','for','from','get','give','go','have','he','her','here','him','his',
              'how','i','if','in','into','it','its','just','know','like','look','make','man','many','me',
              'more','my','new','no','not','now','of','on','one','only','or','other','our','out','people',
              'say','see','she','so','some','take','tell','than','that','the','their','them','then','there',
              'these','they','thing','think','this','those','time','to','two','up','use','very','want','way',
              'we','well','what','when','which','who','will','with','would','year','you','your',
    ]
    words.append([random.randint(10,WIDTH-50), random.randint(10,HEIGHT/2), random.choice(common)])

def on_key_down(key, mod, unicode):
    global text
    if key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:-1]
    elif len(unicode) > 0 and ord(unicode) >= 65 and ord(unicode) <= 125:
        text += unicode
        for w in list(words):
            if w[2] == text:
                words.remove(w)
                text = ''
                beep.play()


def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')

        for w in words:
            screen.draw.text(w[2], (w[0],w[1]), fontsize=20,fontname="437-win")

        screen.draw.text(text, (WIDTH/2,HEIGHT - 40), color=(255,0,0), fontsize=40,fontname="437-win")

for i in range(5):
    add_word()

clock.schedule_interval(add_word, 2)
clock.schedule_interval(move, 1)
pgzrun.go()
```


ghost!

```
import random
score = 0
while True:
    ghost = random.randint(1,3)
    choice = input('Pick a door from 1,2, or 3: ')
    if choice == str(ghost):
        print ('there is a ghost :O GAME OVER !!!')
        break
    else:
        score += 1
        print('lucky no gosht')
print('your score is ' + str(score))

```


## [DAY-101] Functions; Strings

invert a list

```
def invert(l):
    #...

print(invert([1,2,3]))
```

invert a string

```
def invert(s):
    #...

print(invert("hello"))
```

invert a number

```
def invert(n):
    #...

print(invert(123456))
```

Check if a string is a palindrome, a palindrome is a string that you can read backwards and it sounds the same.

```
Anna
civic
kayak
level
madam
mom
noon
racecar
radar
redder
refer
repaper
rotator
rotor
sagas
solos
stats
tenet
wow
Never odd or even.
We panic in a pew.
Won’t lovers revolt now?
Don’t nod.
Sir, I demand, I am a maid named Iris.
Don't nod.
I did, did I?
Step on no pets.
Eva, can I see bees in a cave?
Was it a cat I saw?
```

example:

```
while True:
    n = input("which string you want to check: )
    if is_palindrome(n):
        print(n + " is a palindrome")
    else:
        print(n + " is not a palindrome")
```
