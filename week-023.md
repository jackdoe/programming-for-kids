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