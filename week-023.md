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

If you ommit the condition from the for loop, it becomes an infinite loop.

```
#include <iostream>
using namespace std;
int main()
{
    for(;;) {
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