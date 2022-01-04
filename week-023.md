## [DAY-157] strings; cin

Make love tester in python:

```
while True:
    sum = 0
    name1 = input('name 1: ')
    name2 = input('name 2: ')

    for i in range(len(name1)):
        sum += ord(name1[i])
    for i in range(len(name2)):
        sum += ord(name2[i])

    match = 1 + (sum % 100)
    print("love test result:")
    print(match)
```

Write the same program in c++:

```
#include <iostream>
using namespace std;
int main()
{
    while(1) {
        string name1;
        string name2;

        cout << "name1: ";
        cin >> name1;

        cout << "name2: ";
        cin >> name2;

        int sum = 0;
        for (int i = 0; i < name1.size(); i++) {
            sum += name1[i];
        }
        for (int i = 0; i < name2.size(); i++) {
            sum += name2[i];
        }

        int match = 1 + (sum % 100);
        cout << "love test result:" << endl;
        cout << match << endl;
    }
}
```

`cin` is `character input`, you can perform a read operation by geting data out of cin with `>>`. Both `cin` and `cout` are streams. We will talk more about it later. For now just remember `cin >> variable` will read from the input and put the value in `variable`, and `cout << variable` will print the value of the variable.



## [DAY-158] if; while

rock paper scissors again

```
import random
options = ['rock','paper','scissors']

while True:
    player = input(' '.join(options) + ': ')
    if player not in options:
        print("i dont know what to do with " + player)
        continue
    computer = random.choice(options)
    print(computer)
    if player == computer:
        print("its a tie!")
    if player == 'rock':
        if computer == 'paper':
            print('U lose the round')
        elif computer == 'scissors':
            print('U win this round')
    if player == 'paper':
        if computer == 'rock':
            print('U win this round')
        elif computer == 'scissors':
            print('U lose the round')
    if player == 'scissors':
        if computer == 'rock':
            print('U lose the round')
        elif computer == 'paper':
            print('U win this round')
```

sum things

```
data = ['hello','world','earth']
r = ''
for d in data:
  r += d
print(r)

data = [1,2,3]
r = 0
for d in data:
  r += d
print(r)

data = [[1,2],[3,4],[5,6]]
r = []
for d in data:
  r += d
print(r)
```

The pattern, start with an empty result, iterate over the list and append append to the result is very very common. Examine the above code and notice how the part where it adds to the result is the same regardless if the list is list of strings, integers or list of lists

## [DAY-159] strings; sizeof

Back to basics, how are strings layed out in memory, and how many bytes the primitive types occupy in memory:

```
#include <iostream>
using namespace std;
int main(void) {
    char c = 'a';
    int x = 'a';
    bool b = true;
    int sum = 0;
    long l = 1;
    short s = 1;
    float f = 0.555;
    double d = 0.4123123;
    long double ld = 0.123123;

    cout << "char" << sizeof(c) << endl;
    cout << "bool" << sizeof(b) << endl;
    cout << "int" << sizeof(sum) << endl;
    cout << "short" << sizeof(s) << endl;
    cout << "long" << sizeof(l) << endl;
    cout << "float" << sizeof(f) << endl;
    cout << "double" << sizeof(d) << endl;
    cout << "long double" << sizeof(ld) << endl;

    int ages[10]= {10,12,10,9,10,12,12,2,3,2};
    cout << sizeof(ages) << endl;;

    long double z[5] = {0,0,0,0,0};
    cout << sizeof(z) << endl;;

    char s1[10] = {'h','e','l','l','o','w','o','r','d','\0'};
    char s2[] = "helloword";
    
    cout << s1 << endl;
    cout << s2 << endl;
}
```
<hr>
argc and argv

```
#include <iostream>
using namespace std;
int main(int argc, char* argv[]) {
    cout << "Have " << argc << " arguments:" << endl;
    cout << "my name is: " << argv[0] << endl;
    for (int i = 0; i < argc; ++i) {
        cout << i << ": " << argv[i] << endl;
    }
    return 0;
}
```
Compile the the program above as `g++ -o xyz file.cpp`, and run it with `./xyz hello world "aaa bbbb cccc" ddd`. You see `g++` has a `main` function as well, and it has `argc` and `argv` as well.

<hr>
Formatting example:

```
#include <iostream>
#include <iomanip>
using namespace std;
int main(void) {
    for (int fahr=0; fahr<=100; fahr+=10){
        cout<< endl
        << setw(6)
        << setprecision(0)
        << fahr
        << setw(10)
        << setprecision(3)
        << 5.0/9.0 * (fahr-32.0);

    }
    cout << endl;
    return(0);
}
```

## [DAY-160] pointers

c/c++ pointes and arrays are sometimes confusing, we will come back to them multiple times, especially because strings are pointers to arrays of characters, it is important for the concept to "click". Do not worry if you dont get it at first (or at second, or at third) attempt.

There are two important operators '*' and '&', `int *pa = &a` means we have a pointer (`*`) to a variable of type `int` equal to the address (`&`) of variable `a`. The value of `pa` is just a number, it is literally the address of the memory where the value of `a` will be.

The most important concept is that `pa` is actually just a number, this is the actual value of `pa`, and with `*pa = 5` means, go to this place in memory and put 5 there, we can literally go anywhere in memory and put some value there.

Arrays are a continuous chunks of memory, `char b[10]` means `b` is a pointer to somewhere in memory where you hold `10` slots of type `char` which is 10 bytes. so `b` actually just holds the location of those 10 bytes. Thats right, `b` is a pointer, we can do `b[2] = 'a'` or `*(b + 2) = 'a'` they are the same thing, as `b[2]` means go to wherever `b` points to, and add 2 slots of `b`'s type, same as `*(b + 2)`.

Examine the following program:

```
#include <iostream>
using namespace std;
int main(int argc, char* argv[]) {
    int a = 7;
    int *pa = &a;

    *pa = 8;
    cout << a << endl;

    int b[8] = {10,11,12,13,14,15,16,17};
    cout << b << endl;
    cout << (b + 3) << endl;
    cout << *(b + 3) << endl;
    cout << b[3] << endl;

    return 0;
}
```


## [DAY-161] pointers

Tic tac toe with 9 variables, one for each position of the grid.

This is how the gameplay should look:

```
  a b c
0 - - -
1 - - -
2 - - -
[x] enter position (row col): 0 a

  a b c
0 x - -
1 - - -
2 - - -
[0] enter position (row col): 0 b

  a b c
0 x 0 -
1 - - -
2 - - -
[x] enter position (row col): 1 a

  a b c
0 x 0 -
1 x - -
2 - - -
[0] enter position (row col): 1 b

  a b c
0 x 0 -
1 x 0 -
2 - - -
[x] enter position (row col): 2 a

  a b c
0 x 0 -
1 x 0 -
2 x - -
x wins!
```

And this is the code:

```
#include <iostream>
using namespace std;
void render(char g0, char g1, char g2, char g3, char g4, char g5, char g6, char g7, char g8) {
    cout << "  a b c" << endl;
    cout << "0 " << g0 << " " << g1 << " " << g2 << endl;
    cout << "1 " << g3 << " " << g4 << " " << g5 << endl;
    cout << "2 " << g6 << " " << g7 << " " << g8 << endl;
}

bool wins(char symbol, char g0, char g1, char g2, char g3, char g4, char g5, char g6, char g7, char g8) {
    if (g0 == symbol && g1 == symbol && g2 == symbol) {
        return true;
    }
    if (g0 == symbol && g3 == symbol && g6 == symbol) {
        return true;
    }
    if (g0 == symbol && g4 == symbol && g8 == symbol) {
        return true;
    }
    if (g1 == symbol && g4 == symbol && g7 == symbol) {
        return true;
    }    
    if (g2 == symbol && g5 == symbol && g8 == symbol) {
        return true;
    }
    if (g3 == symbol && g4 == symbol && g5 == symbol) {
        return true;
    }    
    if (g6 == symbol && g7 == symbol && g8 == symbol) {
        return true;
    }     
    if (g6 == symbol && g4 == symbol && g2 == symbol) {
        return true;
    }
    return false;
}


int main(void) {
    char g0,g1,g2,g3,g4,g5,g6,g7,g8;
    g0 = g1 = g2 = g3 = g4 = g5 = g6 = g7 = g8 = '-';
    char symbol = 'x';
    while(1) {
        render(g0,g1,g2,g3,g4,g5,g6,g7,g8);
        char row,col;
        cout << "[" << symbol <<  "] enter position (row col): ";
        cin >> row >> col;
        cout << endl;

        if (row == '0') {
            if (col == 'a') {
                g0 = symbol;
            }
            if (col == 'b') {
                g1 = symbol;
            } 
            if (col == 'c') {
                g2 = symbol;
            }                            
        }


        if (row == '1') {
            if (col == 'a') {
                g3 = symbol;
            }
            if (col == 'b') {
                g4 = symbol;
            } 
            if (col == 'c') {
                g5 = symbol;
            }                            
        }

        if (row == '2') {
            if (col == 'a') {
                g6 = symbol;
            }
            if (col == 'b') {
                g7 = symbol;
            } 
            if (col == 'c') {
                g8 = symbol;
            }                            
        }        
        if (wins(symbol,g0,g1,g2,g3,g4,g5,g6,g7,g8)) {
            render(g0,g1,g2,g3,g4,g5,g6,g7,g8);
            cout << symbol << " wins!" << endl;
            break;
        }

        if (symbol == 'x') {
            symbol = '0';
        } else {
            symbol = 'x';
        }        
    }
    return 0;
}
```

## [DAY-162] pointers

Watch "What Are Pointers? (C++)", by javidx9 on youtube. https://www.youtube.com/watch?v=iChalAKXffs



