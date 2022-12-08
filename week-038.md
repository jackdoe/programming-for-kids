

## [DAY-260] strings

Write (in notepad), run (from cmd) and explain(on paper) the following code:
```
def encrypt(s):
    r = ''

    for character in s:
        ascii = ord(character)
        r += 'z' * ascii
        r += ' '

    return r


def decrypt(s):
    r = ''
    ascii = 0

    for character in s:
        if character == 'z':
            ascii += 1
        else:
            r += chr(ascii)
            ascii = 0

    return r



encrypted = encrypt('hello world')
print(encrypted)
print(decrypt(encrypted))
```

![game-260.jpg](./screenshots/game-260.jpg "game 260 screenshot")


> walk through the code, explaining each line, and trying it with sample values


## [DAY-261] lists

Find and fix the bug in the following program:

```
# [2,2,2,2,2,2,2,2,3] should become [8, 2, 1, 3]
def rle(x):
  r = []
  for v in x:
    if len(r) == 0 or r[-1] != v:
      r.append(0)
      r.append(v)
    if v == r[-1]:
      r[-2] += 1
  return r

# [8, 2, 1, 3] should become [2,2,2,2,2,2,2,2,3]
def rld(x):
  r = []

  for i in range(0, len(x), 2):
    for k in range(x[i]):
      r.append(x[i+1])

  return r


a = rle([1,1,1,1,1,1,1])
print(a)
b = rld(a)
print(b)
```

> Spend some time stepping through or print debugging, I chose to use print debugging to emphasize on "what should this code do, and how do you make sure it does what it says", but I think proper debugging can be introduced at this point, in the same time I dont want to introduce new concepts yet. Learning programming takes time, you can not rush it.


## [DAY-262] lists

Find and fix the bug in the following program (using only notepad and cmd):

```
def avg(x):
    n = 0
    sum = 0
    for i in range(1, len(x)):
        sum += x[i]
        n += 1

    return sum / n


print(avg([7,3,5]))
```


## [DAY-263] lists

find the bug in the following code (using notepad and cmd):


```
def uniq(data):
    result = []
    for inputNumber in data:
        seen = False
        for resultNumber in result:
            if inputNumber != resultNumber:
                seen = True
        if not seen:
            result.append(inputNumber)

    return result

# should print [1,2,3]
print(uniq([1, 2, 1, 1, 1, 3, 1]))
```


## [DAY-264] design

Today we will do a basic design and 3d print it, first make an account on https://www.tinkercad.com/ and then build something there (use W to attach workarea to a surface so you can easilly put one thing on top or on the side of another).

Grab a masuring tool and get any object that you see and measure it and build it inside tinkercad.

> She did some great designs, but they are somewhat personal and I wont show them in the book. Also she was the one who found out about the W key doing temporary workarea, which makes the whole tinkercad propgram 10000 times better, and before this I was doing designs super slow and was very annoyed :)

## [DAY-265] c; if

Examine the following program, type it in notepad and compile it with gcc, then examine the output binary.

```
// comments in C
// save the file as hello.c
// use gcc -o hello hello.c to compile the program
#include <stdio.h>

int fizzbuzz(int n) {
	int fizbuzzes = 0;
	for (int i = 1; i < n; i++) {
		if (i % 3 == 0 && i % 5 == 0) {
			printf("fizzbuzz\n");
			fizbuzzes += 1;
		} else if (i % 3 == 0) {
			printf("fizz\n");
		} else if (i % 5 == 0) {
			printf("buzz\n");
		} else {
			printf("%d\n", i);
		}
	}
	return fizbuzzes;
}

int main(void) {
	while(1) {
		printf("hello, press q to stop\n");
		char c = getchar();
		getchar();
		if (c == 81 || c == 113) {
			break;
		} else if (c == 97) {
			int n = fizzbuzz(20);
			printf("amount of fizbuzzes: %d\n",n);
		} else if (c == 'A') {
			int n = fizzbuzz(50);
			printf("amount of fizbuzzes: %d\n",n);
		}
	}
	return 0;
}
```


## [DAY-266] lists

Maka e program to add a bunch of inputs to a list and pick a random item from it:

> thats what she wrote, I explained about the random.seed

```
import random
import time
random.seed(time.time())
a = ["Rumble","Fortnite","Call of Duty","Bedwars"]
print(a)
while True:
    b= input('add anything you want: ')
    if b == "quit":
        break
    a.append(b)

print("this is what you got in here: ",a)
print(random.choice(a))
```

## [DAY-267] lists

Make a program to sum a list of lists of numbers `x = [[1,2,3],[1,4],[6]]`

```
def sum(list_of_lists):
    s = 0
    for l in list_of_lists:
        for element in l:
            s += element
    return s
```

make a program to return a copy of the list without the first and last element (using `pop()`)

```
def middle(x):
    copy = []
    for e in x:
        copy.append(e)

    copy.pop(len(x)-1)
    if len(copy) > 0:
        copy.pop(0)

    return e
```


## [DAY-268] lists

make fizbuzz

```
for i in range(50):
	if i%5==0 and i%3 ==0:
		print("fizzzz buzz")
	elif i%3==0:
		print("buxx")
	elif i %5==0:
		print("fizzzz")
	else:
		print(i)
```

add all the non fizz,buzz,fizbuzz numbers to a list and print it

```
a=[]
for i in range(50):
	if i%5==0 and i%3 ==0:
		print("fizzzz buzz")
	elif i%3==0:
		print("buxx")
	elif i %5==0:
		print("fizzzz")
	else:
		print(i)
		a.append(i)
print(a)
```


## [DAY-269] fizzbuzz; c; goto

write fizzbuzz in C

```
#include <stdio.h>
int main(void) {
  int i;

  // init; condition; increment
  for (i = 0; i < 99; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      printf("fizzbuzz\n");
    } else if (i % 3 == 0) {
      printf("fizz\n");

    } else if (i%5==0){
      printf("buzz\n");
    } else {
      printf("the number is: %d\n", i);
    }
  }


  // init
  i = 0;
  // condition
  while(i < 99) {
    if (i % 5 == 0 && i % 3 == 0) {
      printf("fizzbuzz\n");
    } else if (i % 3 == 0) {
      printf("fizz\n");

    } else if (i%5==0){
      printf("buzz\n");
    } else {
      printf("the number is: %d\n", i);
    }

    // increment
    i++;
  }



  // init
  i = 0;
  while(1) {
    // condition
    if (i >= 99) {
      break;
    }

    if (i % 5 == 0 && i % 3 == 0) {
      printf("fizzbuzz\n");
    } else if (i % 3 == 0) {
      printf("fizz\n");

    } else if (i%5==0){
      printf("buzz\n");
    } else {
      printf("the number is: %d\n", i);
    }

    // increment
    i++;
  }

  // init
  i = 0;
 START:
  // condition
  if (i >= 99) {
    goto END;
  }

  if (i % 5 == 0 && i % 3 == 0) {
    printf("fizzbuzz\n");
  } else if (i % 3 == 0) {
    printf("fizz\n");

  } else if (i%5==0){
    printf("buzz\n");
  } else {
    printf("the number is: %d\n", i);
  }

  // increment
  i++;
  goto START;
 END:

  printf("fizzbuzz done\n");

  return 0;
}
```


![game-269.jpg](./screenshots/game-269.jpg "game 269 screenshot")

> using a for loop, a while loop and goto, explain how each of them actually works




## [DAY-270] fizzbuzz; c

Count the amount of fizzes, buzzes, numbers and fizzbuzzes, and also ask the user to enter the number for how many numbers to check.

```
#include <stdio.h>

int main(void) {
  int i;

  int fizzbuzzes;
  int fizzes;
  int buzzes;
  int numbers;
  int how_many;

  fizzbuzzes = 0;
  fizzes = 0;
  buzzes = 0;
  numbers = 0;

  printf("how many do you want: ");
  scanf("%d", &how_many);

  for (i = 0; i < how_many; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      fizzbuzzes++;
    } else if (i % 3 == 0) {
      fizzes++;
    } else if (i % 5==0){
      buzzes++;
    } else {
      numbers++;
    }
  }

  printf("total: %d, fizzes: %d, buzzes: %d, fizzbuzzes: %d, numbers: %d\n", how_many, fizzes, buzzes,fizzbuzzes, numbers);

  return 0;
}

int main(void) {
  int fizzbuzzes = 0;
  int fizzes = 0;
  int buzzes = 0;
  int numbers = 0;
  int how_many = 0;

  printf("how many do you want: ");
  scanf("%d", &how_many);

  for (int i = 0; i < 99; i++) {
    if (i % 5 == 0 && i % 3 == 0) {
      fizzbuzzes++;
    } else if (i % 3 == 0) {
      fizzes++;
    } else if (i % 5==0){
      buzzes++;
    } else {
      numbers++;
    }
  }

  printf("total: %d, fizzes: %d, buzzes: %d, fizzbuzzes: %d, numbers: %d\n", how_many, fizzes, buzzes,fizzbuzzes, numbers);

  return 0;
}

```

![game-270.jpg](./screenshots/game-270.jpg "game 270 screenshot")

> explain initialization of variables, and printf parameters, also focus on how scanf gets a pointer to the how_many variable

