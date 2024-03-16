## [DAY-164] pointers

Write a program to prepare for the test tomorrow. Its a test of abbreviations, from abbreviation to meaning. Make a program to help you study, it should ask you for a abbreviation and then you should write its meaning.

```
t.z.t -> ten zijner tijd
v.l.n.r -> van links naar rechts
e.d -> en dergelijk
nr. -> nummer
zg. -> zogenaamd
Gebr. -> gebroeders
dr. -> doctor
s.v.p -> s'il vous plait
t.o.v -> ten opzichte van
nl. -> namelijk
N.B. -> Nota Bene
sr. -> senior
jr. -> junior
C -> Celsius
etc -> etcetra
t.a.v -> ter attentie van
P.S. -> postscriptum
B. en W. -> Burgemeesteren Wethouders
NL -> Nederland
v.a -> vanaf
drs -> doctorandes
```

The program will have 2 lists with the same amount of elements, you should pick a random index, ask the user to type the meaning for `abbreviations[i]` and compare it with `meaning[i]`

```
import random
def test(taal,toets):
    i = random.randint(0,len(taal)-1)
    f = input(taal[i]+ ': ')
    if f == toets[i]:
        print('corect')
    else:
        print("WRONG, one more try!")
        f = input(taal[i]+ ': ')
        if f == toets[i]:
            print('corect')
        else:
            print('better luck next time the correct answer was: '+toets[i])

short = ['t.z.t','v.l.n.r','e.d','nr.','zg.','Gebr.','dr.',
         's.v.p','t.o.v','nl.','N.B.','sr.','jr.','C',
         'etc','t.a.v','P.S.','B. en W.','NL','v.a','drs']

long = ['ten zijner tijd','van links naar rechts','en dergelijk',
        'nummer','zogenaamd','gebroeders','doctor',
        "s'il vous plait",'ten opzichte van','namelijk',
        'Nota Bene','senior','junior','Celsius',
        'etcetra','ter attentie van','postscriptum',
        'Burgemeesteren Wethouders','Nederland','vanaf','doctorandes']

for i in range(len(short)):
    print(short[i] + ' -> ' + long[i])

while True:
    test(short,long)
    test(long, short)
```

## [DAY-165] if; while

Another tic tac toe on your own

> (this is the code she wrote)

```
def board(g):
    print(' ',1,2,3)
    print('a',g[0],g[1],g[2])
    print('b',g[3],g[4],g[5])
    print('c',g[6],g[7],g[8])

g = ['-']*9
idk = 'x'
while True:
    board(g)
    l = input(idk + 'choose a number 1,2,3 and a letter a,b,c: ')

    if l == 'a1':
        g[0] = idk
    if l == 'a2':
        g[1] = idk
    if l == 'a3':
        g[2] = idk
    if l == 'b1':
        g[3] = idk
    if l == 'b2':
        g[4] = idk
    if l == 'b3':
        g[5] = idk
    if l == 'c1':
        g[6] = idk
    if l == 'c2':
        g[7] = idk
    if l == 'c3':
        g[8] = idk
    if g[0] == idk and g[1] == idk and g[2] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[3] == idk and g[4] == idk and g[5] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[6] == idk and g[7] == idk and g[8] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[0] == idk and g[3] == idk and g[6] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[1] == idk and g[4] == idk and g[7] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[2] == idk and g[5] == idk and g[8] == idk:
        print(idk+ ' Won congratulations 🥳🥳🥳')
        break
    if g[2] == idk and g[4] == idk and g[6] == idk:
        print(idk+ 'Won congratulations 🥳🥳🥳')
        break
    if g[0] == idk and g[4] == idk and g[8] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break

    done = True
    for e in g:
        if e == '-':
            done = False
    if done:
        print('Its a tie')
        break

    if idk == 'x':
        idk = '0'
    else:
        idk = 'x'
    
board(g)
```

## [DAY-166] if; while

Write tic tac toe on your own but 4x4 instead of 3x3.

> (this is the code she wrote)

```
def board(g):
    print(' ',1,2,3,4)
    print('a',g[0],g[1],g[2],g[3])
    print('b',g[4],g[5],g[6],g[7])
    print('c',g[8],g[9],g[10],g[11])
    print('d',g[12],g[13],g[14],g[15])


g = ['-']*16
idk = 'x'
while True:
    board(g)
    l = input(idk + 'choose a number 1,2,3 and a letter a,b,c: ')

    if l == 'a1':
        g[0] = idk
    if l == 'a2':
        g[1] = idk
    if l == 'a3':
        g[2] = idk
    if l == 'a4':
        g[3] = idk

    if g[0] == idk and g[1] == idk and g[2] == idk and g[3] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    # ...

    if idk == 'x':
        idk = '0'
    else:
        idk = 'x'
    
board(g)
```

## [DAY-167] C; printf; scanf

We will use `printf` to display text and `scanf` to read text input from the user. First compile the following program, save it to a file `hello.c` and run `gcc -o hello hello.c` the C compiler we will use is called `gcc`, just as the C++ compiler we used was called `g++`, and the options are again `-o` for 'output file name' and then the source code file `hello.c`.

```
#include <stdio.h>

int main(void) {
    int age = 0;

    printf("How old are you: ");
    scanf("%d",&age);
    
    if (age > 10) {
        printf("you are a grownup\n");
    } else {
        printf("are you a little kid, %d %d %c\n", age, 102, 103);
    }
    return 0;
}
```

Now lets read it line by line, first we make a variable `age` of type `integer` with initial value of `0`, then we print "How old are you" using `printf`, and immidiately after tat we do `scanf("%d",&age)`, first we say to scanf that we are looking for a integer `%d` and then once it reads an integer to put it on memory where the variable `age` is located at. With the `&` symbol we take the memory address of the variable.

Then we compare if the age that the user entered is > 10, we print one thing, and if not we print `printf("are you a little kid, %d %d %c\n", age, 102, 103);` this will print the age itself (the first %d) will use the second parameter which is `age`, then the second %d will print 102, and then %c will print the ascii value of 103 (g).

Both printf and scanf's first argument is the formatting string, while it is printing or scanning the input, whenever it sees %d %c %f (digit, character, floating point number), it will read from the arguments you passed to it and do what you want, read or write depending if printf or scanf.

This is just the first steps towards C, dont worry if you dont get the `&` thing and the memory address, with some practice things will click and it will all make sense.

Lets say your coputer has only 30 bytes of memory:

```
00-09|..........|
10-19|0000......| int age at memory address 10, occupying 4 bytes
20-29|..........|
30-39|PPPPPPPPPP| the program itself
```

`&age` is the address of age, which is 10, its as simple as that, `scanf` gets the value 10 as the location in memory in which it should write down the number that it processed from the user input.

## [DAY-168] c; while; if

Rock paper scissors in C.


```
#include <stdio.h>
#include <stdlib.h>

#define ROCK 0
#define PAPER 1
#define SCISSORS 2

int main(void) {
    while (1) {
        int player;
        printf("rock(0) paper(1) scissors(2): ");
        scanf("%d", &player);

        int computer = rand() % 3;
        printf("player: %d, computer: %d\n", player, computer);

        if (computer == player) {
            printf("its a tie\n");
        } else {
            if (computer == ROCK && player == PAPER) {
                printf("player wins\n");
            }
            if (computer == ROCK && player == SCISSORS) {
                printf("computer wins\n");
            }
            if (computer == PAPER && player == ROCK) {
                printf("computer wins\n");
            }
            if (computer == PAPER && player == SCISSORS) {
                printf("player wins\n");
            }
            if (computer == SCISSORS && player == ROCK) {
                printf("player wins\n");
            }
            if (computer == SCISSORS && player == PAPER) {
                printf("computer wins\n");
            }
        }
    }
    return 0;
}
```

`#define ROCK 0` just makes the c compiler to replace ROCK with 0 wherever it sees it in the source code. 


`#include <stdlib.h>` is needed for the `rand` function, it returns an integer, but since we need a number from 0, 1, 2 we just do `rand() % 3`, which will take the reminder from the random number and 3.

Try this in python:

```
for i in range(100000):
    print(i, i % 3)
```

You will see:

```
0 0
1 1
2 2
3 0
4 1
5 2
6 0
7 1
8 2
9 0
10 1
11 2
12 0
13 1
14 2
15 0
16 1
17 2
18 0
19 1
20 2
21 0
22 1
23 2
24 0
25 1
26 2
27 0
28 1
29 2
30 0
31 1
32 2
33 0
34 1
35 2
36 0
37 1
38 2
39 0
40 1
41 2
42 0
43 1
44 2
45 0
46 1
47 2
48 0
49 1
50 2
51 0
52 1
53 2
54 0
...
```


## [DAY-169] c; while; if

Battle ship in C.

Arrays are continous block of memory, for example `int x[10]` creates 10 integers (4 bytes each, so 40 bytes block), you can access each element by its index from `x[0]` to `x[9]`, e.g. `x[2] = 5` will set the 3rd element to be equal to 5.

In C it is very easy to have multi dimensional arrays, simply say `int x[10][10]` and that creates 10x10 integers you can access by their row and column, we will use two dimensional array to store our boards for the battleship game. As usual, we use one hidden board with the ships and one display board with the guesses.

```
#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
int main(void) {
    int hidden[SIZE][SIZE];
    int display[SIZE][SIZE];
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            hidden[i][j] = 0;
            display[i][j] = 0;
        }
    }

    // make 20 random ships
    for (int i = 0; i < 20; i++) {
        hidden[rand() % SIZE][rand() % SIZE] = 1;
    }

    while (1) {
        // print the display board
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                printf("%d ", display[i][j]);
            }
            printf("\n");
        }

        // get the row and column from the user
        int row, column;
        printf("row column> ");
        scanf("%d %d", &row, &column);

        // modify the display board depending if ship is 
        // found in the hidden board or not.
        if (hidden[row][column] == 1) {
            display[row][column] = 1;
        } else {
            display[row][column] = 2;
        }
    }
    return 0;
}
```
## [DAY-170] pointers

Watch "What Are Pointers? (C++)", by javidx9 on youtube. https://www.youtube.com/watch?v=iChalAKXffs

