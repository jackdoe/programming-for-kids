## [DAY-330] html

Make 5 webpages with image, link to a website some title, description and a list of items

> this is an example page she made, this exercise actually took 5-6 days, she made one page every few days

![game-330.png](./screenshots/game-330.png "game 330 screenshot")

Upload them to the server your parents bought with scp then ssh into it and move the files to the right directory so they are visible from http://x.x.x.x/page.html




## [DAY-331] for; input

Rewrite this card from our [https://punkjazz.org/programming-time](programming-time) game from python to c:

```
# Welcome to the haunted house!
# ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
# 
#     ___
#   _/ @@\   +--0--+ +--1--+ +--2--+
#  ( \  O/__ |     | |     | |     |
#   \    \__)|*    | |*    | |*    |
#   /     \  |     | |     | |     |
#  /      _\ |     | |     | |     |
# `"""""``   +-----+ +-----+ +-----+
# (ghost art
#  by jgs)
#
#
# There are 3 doors.
# Behind one of the doors there is a
# ghost.
#
# Roll the dice until your door is
# different from the ghost's door.
while True:
  ghost_door = ⚂ % 3
  your_door = ⚂ % 3

  if your_door == ghost_door:
    print("RUUUNNN!!")
  else:
    print("phew! no ghost!")
    break
```


those are two example C programs that you can read to draw inspiration from:

```
// printf, scanf come from here:
#include <stdio.h>

// random() comes from here:
#include <stdlib.h>

int main(void) {
    int a = random();

    printf("the random number is: %d\n",a);

    return 0;
}

```

and

```
// printf, scanf come from here:
#include <stdio.h>

int main(void) {
  int b = 0;

  printf("enter number: ");
  scanf("%d",&b);

  printf("the number you entered is is: %d\n",b);

  return 0;
}

```


## [DAY-332] unix


Play the [bandit war game](https://overthewire.org/wargames/bandit/) level 0 to 7:

* https://overthewire.org/wargames/bandit/bandit0.html
* https://overthewire.org/wargames/bandit/bandit1.html
* https://overthewire.org/wargames/bandit/bandit2.html
* https://overthewire.org/wargames/bandit/bandit3.html
* https://overthewire.org/wargames/bandit/bandit4.html
* https://overthewire.org/wargames/bandit/bandit5.html
* https://overthewire.org/wargames/bandit/bandit6.html
* https://overthewire.org/wargames/bandit/bandit7.html

Read the instructions carefully, try to not use chatgpt, but if you get stuck its better to use it to unblock yourself.

## [DAY-333] unix

In order to understand how arguments are passed to your program, read chapter [18.1 from Beej's C guide](https://beej.us/guide/bgc/html/split/the-outside-environment.html#command-line-arguments) and implement the program to print the sum of the command line arguments.
