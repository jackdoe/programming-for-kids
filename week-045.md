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


## [DAY-324] functions

Make tic tac toe, but using more functions:

> this is what she made on the first day

```
import random

def empty_board():
    board =["-","-","-",
            "-","-","-",
            "-","-","-",]
    return board

def print_board(board):
    print(" ","1","2","3")
    print('a',board[0],board[1],board[2])
    print('b',board[3],board[4],board[5])
    print('c',board[6],board[7],board[8])

def person(board, personSymbol):
    pos = input("enter one of a1,a2,a3,b1,b2,b3,c1,c2,c3: ")
    # BUG: you can play over previously occpied place
    if pos == 'a1':
        board[0] = personSymbol
    if pos == 'a2':
        board[1] = personSymbol
    if pos == 'a3':
        board[2] = personSymbol
    if pos == 'b1':
        board[3] = personSymbol
    if pos == 'b2':
        board[4] = personSymbol
    if pos == 'b3':
        board[5] = personSymbol
    if pos == 'c1':
        board[6] = personSymbol
    if pos == 'c2':
        board[7] = personSymbol
    if pos == 'c3':
        board[8] = personSymbol


def computer(board,computerSymbol):
    # BUG: places computerSymbol on all empty spaces
    for i in range(0,9):
        if board[i] == '-':
            board[i] = computerSymbol
            
def check_win_or_lose(board):
    pass

b1 = empty_board()
while True:
    print_board(b1)
    person(b1,'X')
    print_board(b1)
    computer(b1,'O') 
```

## [DAY-325] functions

Continue the tictactoe game, fix the bugs

> this is what she wrote, she came up with the recursive solution, so we spent time discussing recursion, and I also showed her alternative solution without recursion

```
import random

def empty_board():
    board =["-","-","-",
            "-","-","-",
            "-","-","-",]
    return board

def print_board(board):
    print(" ","1","2","3")
    print('a',board[0],board[1],board[2])
    print('b',board[3],board[4],board[5])
    print('c',board[6],board[7],board[8])

def person(board, personSymbol):
    pos = input("enter one of a1,a2,a3,b1,b2,b3,c1,c2,c3: ")
    if pos == 'a1':
        if board[0] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[0] = personSymbol
    if pos == 'a2':
        if board[1] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[2] = personSymbol
    if pos == 'a3':
        if board[2] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[2] = personSymbol
    if pos == 'b1':
        if board[3] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[3] = personSymbol
    if pos == 'b2':
        if board[4] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[4] = personSymbol
    if pos == 'b3':
        if board[5] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[5] = personSymbol
    if pos == 'c1':
        if board[6] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[6] = personSymbol
    if pos == 'c2':
        if board[7] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[7] = personSymbol
    if pos == 'c3':
        if board[8] != '-':
            print("YOU CANNOT PLAY HERE")
            person(board,personSymbol)
        else:
            board[8] = personSymbol
def computer(board,computerSymbol):
    for i in range(0,9):
        if board[i] == '-':
            board[i] = computerSymbol
            break
            
def check_win_or_lose(board):
    if board[0] == board[1]  and board[1] == board[2]:
        print(board[0], "YOU WIN SIR PERFECT")
        return True
    #BUG add other conditions
    return False

b1 = empty_board()

while True:
    print_board(b1)
    person(b1,'X')
    if check_win_or_lose(b1) == True:
        break
    print_board(b1)
    computer(b1,'O')
    check_win_or_lose(b1)
```

alternative non recursive solution

```
import random

def empty_board():
    board =["-","-","-",
            "-","-","-",
            "-","-","-",]
    return board

def print_board(board):
    print(" ","1","2","3")
    print('a',board[0],board[1],board[2])
    print('b',board[3],board[4],board[5])
    print('c',board[6],board[7],board[8])

def person(board, personSymbol):
    pos = input("enter one of a1,a2,a3,b1,b2,b3,c1,c2,c3: ")
    if pos == 'a1':
        if board[0] != '-':
            return False
        board[0] = personSymbol
    if pos == 'a2':
        if board[1] != '-':
            return False
        board[1] = personSymbol
    if pos == 'a3':
        if board[2] != '-':
            return False
        board[2] = personSymbol        
    if pos == 'b1':
        if board[3] != '-':
            return False
        board[3] = personSymbol
    if pos == 'b2':
        if board[4] != '-':
            return False
        board[4] = personSymbol
    if pos == 'b3':
        if board[5] != '-':
            return False
        board[5] = personSymbol
    if pos == 'c1':
        if board[6] != '-':
            return False
        board[6] = personSymbol
    if pos == 'c2':
        if board[7] != '-':
            return False
        board[7] = personSymbol
    if pos == 'c3':
        if board[8] != '-':
            return False
        board[8] = personSymbol
    return True

def computer(board,computerSymbol):
    for i in range(0,9):
        if board[i] == '-':
            board[i] = computerSymbol
            break
            
def check_win_or_lose(board):
    pass
b1 = empty_board()

while True:
    print_board(b1)
    if not person(b1,'X'):
        continue
    print_board(b1)
    computer(b1,'O')
    check_win_or_lose(b1)
```

another example of recursion to print the numbers from 100 to 0:

```
def dec(x):
    print(x)
    if x == 0:
        return
    else:
        dec(x - 1)


dec(100)
```
