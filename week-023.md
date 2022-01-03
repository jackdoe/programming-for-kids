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
