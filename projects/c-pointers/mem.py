# creepy pasta code, just late afternoon hacking and smashing
# also mostly written at night after few glassess of wine
# dont judge

import re
import random
import itertools
import time
import subprocess
import os

CARD=1
random.seed(7)


intro = [
"""                 RULES:
1. Shuffle the cards. Split the code 
   cards amongst the players and put the 
   memory cards face down in the middle.

2. Pick the top memory card, and put it 
   face up in the middle of the table.

3. Find a code card matching the memory.
   All variables have to have the 
   correct value in the memory card.
   EXAMPLE:
     char *foo = "bar";
     char *pa = foo + 1;
     char v = foo[1]

   you need to look in the memory for
   + [color:red]98 97 114 0[/color] (e.g. address 172)
   + [color:royalblue]172[/color] (foo pointing to "bar")
   + [color:royalblue]173[/color] (pa = foo + 1)
   + [color:royalblue]97[/color] (v = foo[1])

4. First player that finds a match
   wins and puts the winning card aside.

5. [color:magenta]IF[/color] a player has zero cards [color:magenta]GOTO[/color] [color:teal]7[/color].

6. [color:magenta]GOTO[/color] [color:teal]2[/color].

7. Go and play outside, maybe get your
   rollerblades and skate a bit?
""",
"""                 ASCII

Computers understand only numbers, but
humans use sounds to communicate, so how
can computers and humans understand 
each other?

Humans have the alphabet, which is just
a way to have symbols representing a
sound, e.g. the symbol S represents the
sound you make that is similar to a 
snake. When you read the symbol S you 
know how it sounds. So now I can
write something and you can read it even
though we have never met each other.
Only because we agree what sound S
makes.

In 1963 some people gathered together
and put a number value to most useful
letters, digits, and symbols in the 
English alphabet, for example:

'0' is 48, '1' is 49, '2' is 50 ...
'A' is 65, 'B' is 66, 'C' is 67 ...
'a' is 95, 'b' is 96, 'c' is 97 ...
' ' is 32, '!' is 33, '"' is 34 ...
'>' is 62, '?' is 63, '@' is 64 ...

This is called the ASCII Table. Its a 
letter to number table.
""",
"""              ASCII TABLE
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
""",
"""            CHARACTERS IN C

The character type in C needs one byte 
of memory.

[color:royalblue]char[/color] x = [color:brown]'a'[/color];
x = [color:brown]'b'[/color];
x = [color:teal]99[/color];

You can use [color:brown]'a'[/color] to get the ASCII value
of the character a (which is [color:teal]97[/color]). So
x = [color:brown]'a'[/color] means put [color:teal]97[/color] somewhere in memory
where the variable x will live.

You can think of characters as one byte
numbers. By default they are signed,
so it can hold values from [color:teal]-128[/color] to [color:teal]127[/color].

For example:

x = [color:brown]'0'[/color] + [color:teal]17[/color];

Means, take the ASCII value of [color:brown]0[/color], which
is [color:teal]48[/color] and add [color:teal]17[/color] to it, so the variable x
will store the value [color:teal]65[/color], which is [color:brown]'A'[/color].
So if we do printf("%c",x) it will
print [color:brown]'A'[/color]. 

Use %c to print the character value of 
an ASCII code.
""",
"""             POINTERS IN C

[color:royalblue]char[/color] x = [color:brown]'a'[/color];

There is some place in memory holding
the value [color:teal]97[/color] (the ASCII code for [color:brown]'a'[/color]).
Lets imagine its on memory address [color:red]251[/color]

To modify the value of x you can do:

x = [color:brown]'b'[/color];

Now on address [color:red]251[/color] we have 98, ASCII
for [color:brown]'b'[/color]. You can get the address of x
you use & like so:

[color:royalblue]char[/color] *p;
p = &x;

that means, make a variable p that will 
be a pointer to char, and later we 
assign it the value of the address of x, 
so the actual value of p will be [color:red]251[/color].

Now we can use p to modify x:
[color:red]*p = 'c'[/color], will go to address [color:red]251[/color] and 
put [color:teil]99[/color] there, the [color:red]*p[/color] means: follow the 
pointer of p, or 'dereference' p.

printf("%c",x) will print 'c'
Remember p is just a number!
""",
"""              ARRAYS IN C
Array is a continuous piece of memory,
where each element has the same size.
For example array of 5 integers:

[color:royalblue]int[/color] arr[color:teal][5][/color];

Each integer is 4 bytes, so 20 bytes
will be needed (5 elements * 4 bytes).
Array of characters is easier to think
about, because each character is exactly
1 byte:

[color:royalblue]char[/color] arr[color:teal][5][/color];

So we will need 5 * 1 byte of continuous 
memory. The value of the [color:green]arr[/color] variable is 
a reference, it is a pointer to the  
location of first element of the 5 bytes
in memory. Imagine they are on address 
189. We can dereference the pointer 
using brackets [] or star *:
[color:magenta]Address[/color] = [color:green]Base Address[/color] + ([color:red]Offset[/color]*[color:royalblue]Size[/color])

[color:green]arr[/color][[color:red]3[/color]] = 49 store 49 at memory [color:green]189[/color]+[color:red]3[/color]*[color:royalblue]1[/color]
*([color:green]arr[/color]+[color:red]3[/color]) = 49 store 49 at memory [color:green]189[/color]+[color:red]3[/color]*[color:royalblue]1[/color]
[color:red]3[/color][[color:green]arr[/color]] = 49 store 49 memory [color:green]189[/color]+[color:red]3[/color]*[color:royalblue]1[/color]
[color:silver].. the last one actually works :D[/color]

We multiplty by 1 because each [color:royalblue]char[/color] is [color:royalblue]1[/color]
byte, for [color:royalblue]int[/color] we need to multiply by [color:royalblue]4[/color].
""",
"""             STRINGS IN C
String is a continuous sequence of 
characters. C does not have a string
type, so strings are just arrays of
characters that end with 0.

[color:royalblue]char[/color] a[color:teal][3][/color] = [color:teal]{[/color][color:brown]'h'[/color], [color:brown]'i'[/color], [color:teal]0}[/color];
[color:royalblue]char[/color] b[color:teal][3][/color] = [color:teal]{104, 105, 0}[/color];
[color:royalblue]char[/color] *c = [color:brown]"hi"[/color];

Those three represent the same thing.
Pointer to an array of 3 bytes.
You dereference (follow) the pointers
with [] or *:

[color:royalblue]char[/color] v = c[color:teal][1][/color]; // v now has value 105
[color:royalblue]char[/color] v = *[color:teal]([/color]c+[color:teal]1)[/color]; // v now has value 105

All string functions in C read from
the reference until first zero byte.

[color:royalblue]char[/color] f[color:teal][3][/color] = [color:teal]{[/color][color:brown]'h'[/color], [color:teal]0[/color], [color:brown]'i'[/color][color:teal]}[/color];
printf("%s",f) will print just 'h'
because it will stop at the first 0;

[color:royalblue]char[/color] e[color:teal][2][/color] = [color:teal]{[/color][color:brown]'h'[/color], [color:brown]'i'[/color][color:teal]}[/color];

printf("%s",e) will print some junk 
after 'hi', it will actually read memory
you did not intend to read, it will keep
going until it reads the value 0.
""",
"""                HISTORY
C was made in the '70s, so about 50 
years ago, by the titans Dennis Richie,
Ken Thompson, Brian Kernighan an others.
It is still one of the most used langu-
ages today. It has extremely simple
syntax with only 32 keywords.

Simple syntax does not mean simple lan-
guage. It takes extreme discipline to
write portable, robust and resilient C
code. And yet, most of the usable
programs are written in C or interact
with it somehow.

C is an invented language, it is not
discovered like LISP, and it is designed
in such a way to make it easy to 
program the computers we made, and it
does that very well.

              MEMORY CARDS

The red values are representing the 
character arrays, or character values
and the blue ones are pointers to data.

This however is just to help you scan
the cards faster. The computer does not
see any difference, its all just 
numbers.
""",
]
for c in intro:
    print(f"CARD:{CARD}")
    CARD+=1
    print(c)
    

code = [
"""
char *word = "wizard"; // PY: x

printf("%s\\n",word);
""",
"""
char *bottle = "of water"; // PY: x

printf("%s\\n",bottle);
""",
"""
char *hi = "world"; // PY: x

printf("%s\\n",hi);
""",
"""
char *hi = "hello"; // PY: x
char *ph = hi + 3; // PY: x + 3
printf("%s\\n",ph);
printf("%s\\n",hi);
""",
"""
char *foo = "baz"; // PY: x
char letter = 'z'; // PY: (122,'value')

printf("%c\\n",letter);
printf("%s\\n",foo);
""",
"""
char foo[4] = {'b', 'a', 'z', 0}; // PY: x
char *pf = foo + 2; // PY: x + 2
char letter; // PY: (122,'value')
letter = *pf;

printf("%c\\n",letter);
printf("%s\\n",foo);
""",
"""
char *foo = "baz"; // PY: x
char letter; // PY: (122,'value')
letter = foo[2];

printf("%c\\n",letter);
printf("%s\\n",foo);
""",

"""
char *foo = "baz"; // PY: x

printf("%s\\n",foo);
""",

"""
char *foo = "baz"; // PY: x
char *pb = foo + 2; // PY: x+2
char letter; // PY: (122,'value')
letter = *pb;

printf("%c\\n",letter);
printf("%s\\n",pb);
printf("%s\\n",foo);
""",

"""
char foo[4];  // PY: x
foo[0] = 'b';
foo[1] = 'a';
foo[2] = 'z';
foo[3] = 0;

printf("%s\\n",foo);
""",

"""
char name[6] = {'j', 'a', 0, 0, 's', 0}; // PY: x
name[2] = 'c';
name[3] = 'k';

printf("%s\\n",name);
""",
"""
char *world = "hello world"; // PY: x

printf("%s\\n",world);
""",
"""
char word[4] = {'h', 'i', '!', 0}; // PY: x

printf("%s\\n",word);
""",

"""
char cow[5]; // PY: x

cow[0] = 'm';
*(cow+1) = 'o';
cow[2] = 'o';
cow[3] = 'z';
cow[4] = 0;

char letter = cow[3]; // PY: (122,'value')

printf("%c\\n",letter);
printf("%s\\n",cow);
""",
"""
char foo[4]; // PY: x

0[foo] = 0;
(0[foo] + foo[0])[foo] = 'b';
foo[1] = 'a';
(1+1)[foo] = 'r';
foo[1+1+1] = 0;

printf("%s\\n",foo);
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
char *hello = "world"; // PY: x
char *p = hello + 2; // PY: x + 2

printf("%s\\n",p);
printf("%s\\n",hello);
""",


"""
char hello[5] = {'h', 'e', 'y', 'o', 0}; // PY: x
char *p = hello + 2; // PY: x + 2

printf("%s\\n",p);
printf("%s\\n",hello);
""",


"""
char *hello = "hello world"; // PY: x
char *pa = hello + 1; // PY: x + 1
char *pb = pa + 2; // PY: x + 3

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",
    
"""
char *hello = "hello world"; // PY: x
char *pa = hello + 1; // PY: x + 1
char *pb = pa - 1; // PY: x

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",


"""
char *hello = "hello world"; // PY: x
char *pa = hello+3; // PY: x + 3

printf("%s\\n",pa);
printf("%s\\n",hello);
""",

"""
char *hello = "hello world"; // PY: x
char *pa = hello; // PY: x
char *pb = pa; // PY: x

printf("%s\\n",pa);
printf("%s\\n",pb);
printf("%s\\n",hello);
""",

"""
char *foo = "foobarbaz"; // PY: x
char *pa = &foo[8]; // PY: x+8
char va = *pa; // PY: (122,'value')

printf("%c\\n",va);
printf("%s\\n",pa);
printf("%s\\n",foo);
""",
"""
char *cow = "moo"; // PY: x
char *pa = (cow + 2); // PY: x+2

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
char *cow = "mooz"; // PY: x
char v = *(cow + 3); // PY: (122,'value')

printf("%c\\n",v);
printf("%s\\n",cow);
""",
"""
char cow[4]; // PY: x
cow[0] = 'm';
cow[1] = 'o';
cow[2] = 'o';
cow[3] = 0;

char *pa = cow + 1; // PY: x+1

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
"""
char cow[4] = {'m', 'o', 'o', 0}; // PY: x
char *pa = cow + 2; // PY: x+2

printf("%s\\n",pa);
printf("%s\\n",cow);
""",
]
def magic_first(x, y):
    if "magic" in x:
        return 1
    return 0

random.shuffle(code)
codeCycle = itertools.cycle(code)

runCode = {}

for i in range(55 - len(intro) - len(code)):
#for i in range(len(code)):
    mem = [(0,'zero')]*256
    seen={}
    for c in [next(codeCycle),next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle), next(codeCycle)]:
#    for c in [next(codeCycle)]:
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
            print(program)
            print(output);
            os.exit(1)
    
        # append it to memory
        w = subprocess.getoutput("./current").rstrip()
        runCode[c] = w

        splitted = w.split("\n")
        if len(splitted) != 1:
            w = splitted[-1] # use only the whole string, which should always be last

        pointers = []
        for line in c.split("\n"):
            if "PY:" in line:
                a,b = line.split("PY:")
                pointers.append(b)

        if False:
            with open(f"testing/{i:03}.txt","w") as f:
                f.write(program)
                f.write('\n\n')
                f.write(w)
                f.write('\n\n')
        
        while True:
            offset = random.randint(0, len(mem) - len(w) - 1 - len(pointers) - 2)
            if w in seen:
                offset = seen[w]
            else:
                busy = False
                for j in range(len(w)+2):
                    if mem[j + offset][1] != 'zero':
                        busy = True
        
                if busy:
                    continue
    
    
                for j in range(len(w)):
                    v = ord(w[j])
                    mem[j + offset] = (v,'value')

                if w != 'z':
                    mem[len(w) + offset] = (0,'value')
            # used by the eval
            x = offset
            for p in pointers:
                v = eval(p)

                kind = 'pointer'
                if type(v) is tuple:
                    kind = v[1]
                    v = v[0]
                    
                while True:
                    r = random.randint(1, len(mem)-4)
                    if mem[r-2][1] == 'zero' and mem[r-1][1] == 'zero'  and mem[r][1] == 'zero' and mem[r+1][1] == 'zero' and mem[r+2][1] == 'zero':
                        mem[r] = (v,kind)
                        break

            seen[w] = offset
            break

    if False:
        with open(f"testing/{i:03}.txt","a") as f:
            for i in range(32):
                f.write(f"{(i*8):3} | ")
                for j in range(8):
                    v,kind = mem[(i * 8) + j]
                    f.write(f"{v:03} ")
                f.write("\n")

      
    print(f'CARD:{CARD}')
    CARD+=1
    c = ''
    for i in range(32):
        print(f" {(i*8):3} | ", end='')
        
        if c != '':
            print(f"[color:{c}]",end='')
        for j in range(8):
            v,kind = mem[(i * 8) + j]
            if kind != 'zero':
                if c == '':
                    c = 'red'
                    if kind == 'pointer':
                         c = 'royalblue'
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

    c = re.sub('(char|int\s+)','[color:royalblue]\\1[/color]',c)
    c = re.sub('(for)','[color:magenta]\\1[/color]',c)
    c = re.sub(r"(?<!')(\d+)",'[color:teal]\\1[/color]',c)
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

    
