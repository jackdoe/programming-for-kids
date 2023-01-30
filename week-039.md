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



## [DAY-271] fizzbuzz; c

Write fizbuzz on your own starting with the following code:

```
#include <stdio.h>


int main(void) {
  int how_many;

  printf("how many do you want: ");
  scanf("%d", &how_many);

  ....
  ....
  ....
  ....


  return 0;
}
```


## [DAY-272] fizzbuzz; c

Print how many fuzzes, buzzes, fizbuzzes and numbers you are printing.

> thats what she wrote:

```
#include <stdio.h>

int main(void) {
  int how_many;
  int counternum = 0;
  int fizzbuzz = 0;
  int buzz = 0;
  int fizzz = 0;

  printf("how many do you want: ");
  scanf("%d", &how_many);

  for (int a = 0; a < how_many; a++) {
    if (a % 15 == 0) {
      printf("FIZZBUZZZZZZZZZZZZZ\n");
      fizzbuzz++;
    } else if (a % 5 == 0) {
      printf("FIZZzzz\n");
      fizzz++;
    } else if (a % 3 == 0) {
      printf("BUZZZZZZZZZZZZZ\n");
      buzz++;
    } else {
      printf("%d\n", a);
      counternum++;
    }
  }
  printf("%d %d %d %d\n", counternum, fizzbuzz, buzz, fizzz);
  return 0;
}
```

> change the ints to `unsigned char` and then to `unsigned short` and discuss integer overflow


## [DAY-273] fizzbuzz; c; struct

You can group a bunch of variables together in a custom type. In the fizzbuzz case, you might want to group all the counters together:

```
struct counter {
  int numbers;
  int fizzbuzz;
  int fizz;
  int buzz;
};

```

This is how we would use it, we would define the struct type `counter`, and then we will make a function that counts them and returns a counter value:

```
#include <stdio.h>

struct counter {
  int numbers;
  int fizzbuzz;
  int fizz;
  int buzz;
};

struct counter fizzy(int n) {
  struct counter ret = {0};

  for (int a = 0; a < n; a++) {
    if (a % 15 == 0) {
      ret.fizzbuzz++;
    } else if (a % 5 == 0) {
      ret.fizz++;
    } else if (a % 3 == 0) {
      ret.buzz++;
    } else {
      ret.numbers++;
    }
  }

  return ret;
}

int main(void) {
  int how_many;

  printf("how many do you want: ");
  scanf("%d", &how_many);

  struct counter f = fizzy(how_many);
  printf("%d %d %d %d\n", f.numbers, f.fizzbuzz, f.buzz, f.fizz);

  return 0;
}

```

You can see that you can access the inner methods of the struct using `.` (dot), by saying `ret.fizzbuzz = 6' it gets translated to put 6 where the member fizzbuzz is in the block of memory used by the `ret` structure.


Lets say you want to build a chess game, you might want to have a struct for the piece, for example:

```
struct chess_piece {
    uint8_t kind; // what kind of piece it is, 0: pawn, 1: bishop ...
    uint8_t x;    // board column
    uint8_t y;    // board row
    int used;     // how many time the piece was used
};

```

Or you are making a platformer game, you might want to have a struct for the player:

```
struct player {
    unsigned short health;
    int x;
    int y;
};
```

You can also embed structs in structs:

```
struct point {
    int x;
    int y;
};

struct player {
    unsigned short health; // health points left, 0 means game over
    struct point pos; // player's position
};
```


For now we will just do basics with structs to get used with them. How to pass them around in our program, giving them as parameters to functions, or returning them, or having poitners to them.

