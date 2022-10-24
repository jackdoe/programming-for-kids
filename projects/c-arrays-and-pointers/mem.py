# creepy pasta code, just late afternoon hacking and smashing
import re
import random
import itertools
import time
import subprocess
import os

CARD=1
random.seed(7)


intro = [
"""            CHARACTERS IN C

The character type in C needs one byte 
of memory.

char x = 'a';
x = 'b';
x = 99;

You can use 'a' to get the ASCII value
of the character 'a' (which is 97). So
x = 'a' means put 97 somewhere in memory
where we will store the value for the
variable x.

You can think of characters as one byte
numbers. By default they are signed,
so it can hold values from -128 to 127.

For example:

x = [color:blue]'0' + 17;[/color]

Means, take the ASCII value of 0, which
is 48,and add 17 to it, so the variable x
will store the value [color:blue]65[/color], which is 'A'.
So if we do printf("%c",x) it will
print 'A'. 

Use %c to print the character value of 
an ASCII code.
""",
"""            ARRAYS IN C
Array is a continuous piece of memory,
where each element has the same size.
For example array of 4 byte integers:

int a[5];

Will need 5 * 4 bytes of continuous
memory, so 20 bytes will be needed.

Array of characters is easier to think
about, because each character is exactly
1 byte:

char a[5];

So we will need 5 * 1 byte of continuous 
memory. [color:navy]The value of the array variable[/color]
[color:navy]is actually just the memory address of[/color]
[color:navy]the first element of the array.[/color]
Lets imagine it is on address 199932.

To access the elements we do:
[color:red]a[0] = 48;[/color]
[color:blue]a[1] = 49;[/color]
...
which means means 
MEMORY AT ADDR [color:red]199932+0*1 = 48[/color]
MEMORY AT ADDR [color:blue]199932+1*1 = 49[/color]
we use *1 because each char is 1 byte,
if it was integers we need 199932+1*4
""",
"""            POINTERS IN C

char x = 'a';

There is some place in memory holding
the value 97 (the ASCII code for 'a').
Lets imagine its on memory address [color:red]17262[/color]

To modify the value of x you can do:

x = 'b';

Now on address [color:red]17262[/color] we have 98, ASCII
for 'b'.

You can get the address of x you use &

char *p = &x;

that means, the variable p is a pointer
to char. The actual value of p will be 
[color:red]17262[/color], which is the address of x.

*p = 'd', will go to address [color:red]17262[/color] and 
put 99 there (ASCII for 'd'). Now the 
value of x is actually 99. Since p is 
just a number, you can do [color:blue]*(p + 1) = 65[/color], 
now this is power! And your program will
likely crash, because you dont actually 
know what is on address [color:blue]17262+1[/color] or [color:blue]17263[/color].
The variable x is only 1 byte.
""",
"""            STRINGS IN C
String is a continuous sequence of 
characters. C does not have a string
type, so strings are just arrays of
characters that end with 0.

char a[3] = {'h','i', 0};
char b[3] = {104, 105, 0};
char *c = "hi";

Those are the same thing.

The value of the variable is actually
a pointer to the first element of the
string.

char v = c[1]
char v = *(c+1)

both do the same, means go to wherever
address c holds, and add 1 to it.
This is called dereferencing, or 
following a pointer.

To print strings use the %s formatting:
printf("%s",a);
printf("%s",b);
printf("%s",c);
%s will just start from the address of
the variable, and go forward until it
reaches value of 0.

""",
"""


                 RULES:


1. Split the code cards amongst the 
   players.

2. Put the memory cards face down on
   the table.

3. Pick the top memory card, 
   and put it face up in the middle of 
   the table.

4. Players match their code from any
   of the code cards to the memory card.

   If the code has multiple variables
   you need to match them all.

5. First player that finds a match
   wins the round.

6. GOTO 3


""",
"""                 HISTORY

C was made in the '70s, so about 50 
years ago, by the titans Dennis Richie,
Ken Thompson, Brian Kernighan an others.

It is still one of the most used langu-
ages today.

It has extremely simple syntax:
auto,break,case,char,const,continue,
default,do,double,else,enum,extern,float
for,goto,if,int,long,register,return,
short,signed,sizeof,static,struct,switch,
typedef,union,unsigned,void,volatile,
while.

Those are [color:navy]all[/color] of its keywords.

Simple syntax does not mean simple lan-
guage. It takes extreme discipline to
write portable, robust and resilient C
code. And yet, most of the usable
programs are written in C or interact
with it somehow.

C is an invented language, it is not
discovered like LISP, and it is invented
in such a way, that makes it easy to 
program the computers we made, and it
does that very well.
""",
"""       ASCII TABLE (alphabet only)
CODE      CHAR            CODE   CHAR
000       NULL     |      033    !
010       \\n       |      ...
032       SPACE    |      ...
065       A        |      097    a
066       B        |      098    b
067       C        |      099    c
068       D        |      100    d
069       E        |      101    e
070       F        |      102    f
071       G        |      103    g
072       H        |      104    h
073       I        |      105    i
074       J        |      106    j
075       K        |      107    k
076       L        |      108    l
077       M        |      109    m
078       N        |      110    n
079       O        |      111    o
080       P        |      112    p
081       Q        |      113    q
082       R        |      114    r
083       S        |      115    s
084       T        |      116    t
085       U        |      117    u
086       V        |      118    v
087       W        |      119    w
088       X        |      120    x
089       Y        |      121    y
090       Z        |      122    z
"""
]
for c in intro:
    print(f"CARD:{CARD}")
    CARD+=1
    print(c)
    

code = [
"""
char name[6] = {'j','a', 0, 0, 's', 0}; // PY: x
name[2] = 'c';
name[3] = 'k';

printf("%s\\n",name);
""",
"""
char *world = "hello world"; // PY: x

printf("%s\\n",world);
""",
"""
char word[] = {'h','i','!',0}; // PY: x

printf("%s\\n",word);
""",

"""
char *alphabet = malloc(10); // PY: x

for (int i = 0; i < 9; i++) {
    *(alphabet + i) = 65 + i;
}
alphabet[9] = 0;

printf("%s\\n",alphabet);
""",
"""
char cow[4]; // PY: x

cow[0] = 'm';
*(cow+1) = 'o';
cow[2] = 'o';
cow[3] = 0;

printf("%s\\n",cow);
""",
"""
char foo[4]; // PY: x

0[foo] = 'b';
foo[1] = 'a';
(1+1)[foo] = 'r';
foo[3] = 0;

printf("%s\\n",foo);
""",

"""
char year[] = {'1','9','7','2',0}; // PY: x

printf("%s\\n",year);
""",

"""
char year[5]; // PY: x

year[0] = '1';
year[1] = '9';
year[2] = '7';
year[3] = '2';
year[4] = 0;

printf("%s\\n",year);
""",
"""
char year[5]; // PY: x

year[0] = 49;
year[1] = 57;
year[2] = 55;
year[3] = 50;
year[4] = 0;

printf("%s\\n",year);
""",

"""
char zeroToNine[11]; // PY: x

zeroToNine[0] = 48;
for (int i = 1; i < 10; i++) {
    zeroToNine[i] = zeroToNine[0] + i;
}
zeroToNine[10] = 0;

printf("%s\\n",zeroToNine);
""",

"""
char *hello = "world"; // PY: x
char *p = hello + 2; // PY: x + 2

printf("%s\\n",p);
printf("%s\\n",hello);
""",


"""
char hello[5] = {'h','e','y','o',0}; // PY: x
char *p = hello + 1; // PY: x + 1

printf("%s\\n",p);
printf("%s\\n",hello);
""",


"""
char *hello = "hello world"; // PY: x
char *pa = hello + 4; // PY: x + 4
char *pb = pa + 2; // PY: x + 6

printf("%s\\n",pb);
printf("%s\\n",hello);
""",
    
"""
char *hello = "hello world"; // PY: x
char *pa = hello + 4; // PY: x + 4
char *pb = pa - 3; // PY: x + 1

printf("%s\\n",pb);
printf("%s\\n",hello);
""",


"""
char *hello = "hello world"; // PY: x
char *pa = &hello[5]; // PY: x + 5
char *pb = pa - 5; 

pb = pb + 6; // PY: x + 6

printf("%s\\n",pb); // PY: x
printf("%s\\n",hello);
""",

"""
char *hello = "hello world"; // PY: x
char *pa = &hello[0]; // PY: x
char *pb = pa + 6; // PY: x + 6

printf("%s\\n",pb);
printf("%s\\n",hello);
""",

"""
char *hello = "hello world"; // PY: x
char *pa = &hello[0]; // PY: x
char *pb = &pa[6]; // PY: x+6

printf("%s\\n",pa);
printf("%s\\n",hello);
""",


"""
char *cow = "moo"; // PY: x
char *pa = &cow[0]; // PY: x

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = &cow[2]; // PY: x + 2

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = &cow[1]; // PY: x + 1

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = cow; // PY: x

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char *cow = "moo"; // PY: x
char *pa = cow + 1 - 1; // PY: x

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char cow[4] = {'m','o','o',0}; // PY: x
char *pa = cow + 1; // PY: x+1

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char cow[4] = {'m','o','o',0}; // PY: x
char *pa = cow + 2; // PY: x+2

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
]


random.shuffle(code)
codeCycle = itertools.cycle(code)
shuffled = ['red','green','blue','orange','navy']
random.shuffle(shuffled)
colors = itertools.cycle(shuffled)
runCode = {}
for i in range(len(code)):
    mem = [0]*256
    seen={}
    for c in [next(codeCycle),next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle)]:

        program = """
    #include <stdio.h>
    #include <stdlib.h>
    
    int main(void) {
        """ + c + """
        return 0;
    }
    """
        with open("current.c","w") as f:
            f.write(program)
    
        output = subprocess.getoutput("gcc -o current current.c")
        if output.strip() != '':
            print(output);
            os.exit(1)
    
        # append it to memory
        w = subprocess.getoutput("./current").rstrip()
        runCode[c] = w

        splitted = w.split("\n")
        if len(splitted) != 1:
            w = splitted[1] # use only the whole string

        pointers = []
        for line in c.split("\n"):
            if "PY:" in line:
                a,b = line.split("PY:")
                pointers.append(b)

        while True:
            offset = random.randint(0, len(mem) - len(w) - 1 - len(pointers) - 2)
            if w in seen:
                offset = seen[w]
            else:
                busy = False
                for j in range(len(w)+2):
                    if mem[j + offset] !=0:
                        busy = True
        
                if busy:
                    continue
    
    
                for j in range(len(w)):
                    v = ord(w[j])
                    mem[j + offset] = v
    
            # used by the eval
            x = offset
            for p in pointers:
                v = eval(p)

                while True:
                    r = random.randint(1, len(mem)-4)
                    if mem[r-2] == 0 and mem[r-1] == 0  and mem[r] == 0 and mem[r+1] == 0 and mem[r+2] == 0:
                        mem[r] = v
                        break

            seen[w] = offset                
            break

      
    print(f'CARD:{CARD}')
    CARD+=1
    c = ''
    for i in range(32):
        print(f"{(i*8):3} | ", end='')
        
        if c != '':
            print(f"[color:{c}]",end='')
        for j in range(8):
            v = mem[(i * 8) + j]
            if v != 0:
                if c == '':
                    c = next(colors)
                    print(f"[color:{c}]",end='')
            else:
                if c != '':
                    c = ''
                    print(f"[/color]", end='')                
            print(f"{v:03} ",end='')
        if c != '':
            print(f"[/color]")
        else:
            print()
        

def colorme(s, color):
    out = []
    for l in s.splitlines():
        out.append(f"[color:{color}]{l}[/color]")
    return "\n".join(out)

for c in runCode:
    print(f'CARD:{CARD}')
    CARD+=1

    prints = runCode[c]
    comment = colorme(f"/*\nprints:\n{prints}\n*/", 'green')
    c = re.sub(r'(\[|\])','[color:teal]\\1[/color]',c)
    c = re.sub(r'(\(|\))','[color:teal]\\1[/color]',c)
    c = re.sub(r'(\{|\})','[color:teal]\\1[/color]',c)

    c = re.sub('(char|int\s+)','[color:blue]\\1[/color]',c)
    c = re.sub('(for)','[color:magenta]\\1[/color]',c)
    c = re.sub(r'(\d+)','[color:teal]\\1[/color]',c)
    c = re.sub('printf','[color:olive]printf[/color]',c)


    c = re.sub(r'(".*?")','[color:brown]\\1[/color]',c)
    c = re.sub(r'(\'.*?\')','[color:brown]\\1[/color]',c)


    c = f"{c}\n{comment}"
    n = int((32/2)) - int((len(c.split('\n'))) / 2) - 1
    print('\n' * n)
    

    for l in c.split('\n'):
        l = re.sub(r"//.*PY: .*","", l)
        print(l)
    print("")

    
