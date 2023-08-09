## [DAY-344] pointers

Add check_win function to the following tic tac toe game:

```
#include <stdio.h>
struct board {
    char a0;
    char a1;
    char a2;
    char b0;
    char b1;
    char b2;
    char c0;
    char c1;
    char c2;
};

struct user_input {
    char row;
    char col;
};

void board_print(struct board game) {
    printf("  a b c\n");
    printf("0 %c %c %c\n", game.a0, game.b0, game.c0);
    printf("1 %c %c %c\n", game.a1, game.b1, game.c1);
    printf("2 %c %c %c\n", game.a2, game.b2, game.c2);
    printf("\n");
}

int board_set(struct board *game, char symbol, struct user_input ui) {
    int valid_move = 1;
    if (ui.col == 'a' && ui.row == '0') {
        game->a0 = symbol;
    } else if (ui.col == 'a' && ui.row == '1') {
        game->a1 = symbol;
    } else if (ui.col == 'a' && ui.row == '2') {
        game->a2 = symbol;
    } else if (ui.col == 'b' && ui.row == '0') {
        game->b0 = symbol;
    } else if (ui.col == 'b' && ui.row == '1') {
        game->b1 = symbol;
    } else if (ui.col == 'b' && ui.row == '2') {
        game->b2 = symbol;
    } else if (ui.col == 'c' && ui.row == '0') {
        game->c0 = symbol;
    } else if (ui.col == 'c' && ui.row == '1') {
        game->c1 = symbol;
    } else if (ui.col == 'c' && ui.row == '2') {
        game->c2 = symbol;
    } else {
        valid_move = 0;
    }
    return valid_move;
}

struct user_input get_user_input(char symbol) {
    struct user_input ui = {0};
    printf("%c> ", symbol);
    ui.col = getchar();
    ui.row = getchar();
    getchar(); // ignore the new line
    return ui;
}

void toggle_symbol(char *symbol) {
    // if the symbol is X, set it to 0, if its 0, set it to X
    if (*symbol == 'X') {
        *symbol = '0';
    } else {
        *symbol = 'X';
    }
}

int main(void){
    char current_symbol = 'X';
    struct board game_board = {
        .a0 = '-',
        .a1 = '-',
        .a2 = '-',
        .b0 = '-',
        .b1 = '-',
        .b2 = '-',
        .c0 = '-',
        .c1 = '-',
        .c2 = '-',
    };

    while(1) {
        board_print(game_board);
        struct user_input input = get_user_input(current_symbol);
        if (board_set(&game_board, current_symbol, input)) {
            // only change the symbol if the move is valid
            toggle_symbol(&current_symbol);
        }
        // HOMEWORK:
        // write check_win(game_board) function that checks if there is a winner
        // if there is a winner print "X WIN!" if X wins or "0 WIN" if 0 wins, and break to exit the while loop
        // check the board_set function for inspiration
        /*
            example breaking out of a loop:
            while (1) {
                if (something) {
                    break;
                }
            }
        */
    }
}
```

> We spent 1 hour or so discussing pointers and disecting the code

![game-344.png](./screenshots/game-344.png "game 344 screenshot")


## [DAY-345] pointers

Write the hit() function in the following example:

```
#include <stdio.h>
#include <unistd.h>


struct alive {
    int life;
    int speed;
    int attack_power;
    int shield;
};

// FIXME: write the function body
void hit(struct alive *a, struct alive *b){
...
}

int main(void) {
    struct alive npc = {0};

    npc.life = 1000;
    npc.speed = 17;
    npc.attack_power = 10;
    npc.shield = 50;

    struct alive player = {0};
    player.life = 100;
    player.speed = 10;
    player.attack_power = 117;
    player.shield = 30;

    while(1) {
        hit(&npc, &player);
        hit(&player, &npc);

        printf("player: %d, npc: %d\n", player.life,npc.life);
        sleep(1);
    }

    return 0;
}
```

Example:

```
void hit(struct alive *a, struct alive *b){
    if (b->shield > 0) {
        b->shield -= a->attack_power;
    } else{
        b->life -= a->attack_power;
    }
}
```


## [DAY-346] machine code

> for few days we were playing the 4719 game https://punkx.org/4917/ every day we did a couple of cards, disassembling them and then assembling them and running them on paper


## [DAY-347] machine code; pointers


I made a lot of examples using the 27th card, and then also showed examples in C, and made some other cards on paper about dereferencing pointers

```
#    0 halt
#    1 add R0 = R0 + R1, 2 subtract R0 = R0 - R1
#    3 inc R0, 4 inc R1
#    5 dec R0, 6 dec R1
#    7 ring bell
#  8 X print X
#  9 X R0 = mem[X]
# 10 X R1 = mem[X]
# 11 X mem[X] = R0
# 12 X mem[X] = R1
# 13 X jump to address X
# 14 X jump to address X if R0 == 0
# 15 X jump to address X if R0 != 0
#
# *p++
┌────────┐ ┌────────┐
│ IP:  0 │ │ IS:  0 │
└────────┘ └────────┘
┌────────┐ ┌────────┐
│ R0:  0 │ │ R1:  0 │
└────────┘ └────────┘

┌────┬────┬────┬────┐
│  9 │ 12 │ 11 │  7 │
├────┼────┼────┼────┤
│ 11 │ 10 │  9 │  0 │
├────┼────┼────┼────┤
│  3 │ 11 │  0 │  0 │
├────┼────┼────┼────┤
│ 15 │  0 │  0 │  6 │
└────┴────┴────┴────┘
```

examples:

```
#include <stdio.h>
int main(void) {
  int x = 7;
  int* p = &x;
  *p++;

  printf("%d\n",x)

  return 0;
}

#include <stdio.h>
int main(void) {
  int x = 7;
  int* p = &x;
  *p = 3;

  printf("%d\n",x)

  return 0;
}

#include <stdio.h>
int main(void) {
  int x = 7;

  scanf("%d",&x);

  printf("%d\n",x);

  return 0;
}
```


## [DAY-348] machine code; variables

Write the machine code for the following pseudo code:

Given this instruction set:
```
   0 halt
   1 add R0 = R0 + R1, 2 subtract R0 = R0 - R1
   3 inc R0, 4 inc R1
   5 dec R0, 6 dec R1
   7 ring bell
 8 X print X
 9 X R0 = mem[X]
10 X R1 = mem[X]
11 X mem[X] = R0
12 X mem[X] = R1
13 X jump to address X
14 X jump to address X if R0 == 0
15 X jump to address X if R0 != 0
```

```
x = 7
x += 1


assume x is on address 15:
┌────┬────┬────┬────┐
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  7 │
└────┴────┴────┴────┘

```

```
x = 7
y = 8
x = x + y

assume x is on address 15, and y is on addr 14:
┌────┬────┬────┬────┐
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  8 │  7 │
└────┴────┴────┴────┘

```

```
x = 7
print(x)

assume x is on address 15:
┌────┬────┬────┬────┐
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  7 │
└────┴────┴────┴────┘
```


## [DAY-349] machine code; variables

> we did more examples

![day-349-a.jpg](./screenshots/day-349-a.jpg "game 349 screenshot")
![day-349-b.jpg](./screenshots/day-349-b.jpg "game 349 screenshot")
![day-349-c.jpg](./screenshots/day-349-c.jpg "game 349 screenshot")
![day-349-d.jpg](./screenshots/day-349-d.jpg "game 349 screenshot")
![day-349-e.jpg](./screenshots/day-349-e.jpg "game 349 screenshot")
![day-349-f.jpg](./screenshots/day-349-f.jpg "game 349 screenshot")
![day-349-g.jpg](./screenshots/day-349-g.jpg "game 349 screenshot")
![day-349-h.jpg](./screenshots/day-349-h.jpg "game 349 screenshot")


## [DAY-350] machine code; functions

imagine we want to write something like:

```
def printme(x)
    print(x)
    print(x)

x = 4
printme(x)
beep
```

how would we call a function, for this we will pretend our computer has more memory and can work with addressess that are 1 whole byte (from 0 to 255).

first lets write our function, assuming the parameter will come from the R0 register: `11 X 8 _ 11 X 8 _`, we will write the value of R0 into the print instruction, lets write it at address 40:
and the rest of the program we will write at address 0, which is loading the value of X in the R0 register and then jumping to addr 40 to execute the function.

```
    ┌────┬────┬────┬────┐
0   │  9 │ 15 │ 13 │ 40 │
    ├────┼────┼────┼────┤
4   │  7 │  0 │  0 │  0 │ (attempt to beep after the jump)
    ├────┼────┼────┼────┤
8   │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
12  │  0 │  0 │  0 │  4 │ <- x is at addr 15
    ├────┼────┼────┼────┤
16  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
20  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
24  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
28  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
32  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
36  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
40  │ 11 │ 43 │  8 │  0 │
    ├────┼────┼────┼────┤
44  │ 11 │ 47 │  8 │  0 │
    ├────┼────┼────┼────┤
48  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
52  │  0 │  0 │  0 │  0 │

           ....

    ├────┼────┼────┼────┤
    │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
    │  0 │  0 │  0 │  0 │
    └────┴────┴────┴────┘
```


now you can see we can call the function, but we cant go back in order to beep, so what we will do is in R1 we will store which address we want to go back after the function is done.

```
    ┌────┬────┬────┬────┐
0   │  9 │ 15 │ 10 │  6 │ <- load the value of addr 8 into R1,
    ├────┼────┼────┼────┤    so we can go back to wherever it points
4   │ 13 │  40│  8 │  7 │ <- we want to go back to addr 8
    ├────┼────┼────┼────┤    where we have the beep instruction
8   │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
12  │  0 │  0 │  0 │  4 │ <- x is at addr 15
    ├────┼────┼────┼────┤
16  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
20  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
24  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
28  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
32  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
36  │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
40  │ 11 │ 43 │  8 │  0 │
    ├────┼────┼────┼────┤
44  │ 11 │ 47 │  8 │  0 │
    ├────┼────┼────┼────┤
48  │ 12 │ 51 │ 13 │  0 │ <- use R1 to jump back
    ├────┼────┼────┼────┤
52  │  0 │  0 │  0 │  0 │

           ....

    ├────┼────┼────┼────┤
    │  0 │  0 │  0 │  0 │
    ├────┼────┼────┼────┤
    │  0 │  0 │  0 │  0 │
    └────┴────┴────┴────┘
```

so you can see we store the return address in r1 and then go back to where it points to



## [DAY-351] tic tac toe

another day, another tic tac toe

```
#include <stdio.h>

void print_board(char *b) {
    printf("%c %c %c\n",b[0], *(b + 1), b[2]);
    printf("%c %c %c\n",b[3], b[4], b[5]);
    printf("%c %c %c\n",b[6], b[7], b[8]);
}
int check_win(char *b){
    if (b[0] != '-' && b[0] == b[1] && b[1] == b[2]) {
        return 1;
    }
    if (b[3] != '-'  && b[3] == b[4] && b[4] == b[5]) {
        return 1;
    }
    if (b[0] != '-'  && b[0] == b[3] && b[3] == b[6]) {
        return 1;
    }
    if (b[1] != '-'  && b[1] == b[4] && b[4] == b[7]) {
        return 1;
    }
    if (b[2] != '-'  && b[2] == b[5] && b[5] == b[8]) {
        return 1;
    }
    if (b[6] != '-'  && b[6] == b[7] && b[7] == b[8]) {
        return 1;
    }
    if (b[0] != '-'  && b[0] == b[4] && b[4] == b[8]) {
        return 1;
    }
    if (b[2] != '-'  && b[2] == b[4] && b[4] == b[6]) {
        return 1;
    }
    return 0;
}

int main(void) {
    char board[9] = {'-','-','-','-','-','-','-','-','-'};
    char symbol = '0';


    while(1) {
        print_board(board);
        char str[3];
        printf("%c>",symbol);
        scanf("%2s",str);
        if (str[0] == 'a' && str[1] == '1') {
            board[0] = symbol;
        }
        if (str[0] == 'b' && str[1] == '1') {
            board[3] = symbol;
        }
        if (str[0] == 'c' && str[1] == '1') {
            board[6] = symbol;
        }
        if (str[0] == 'a' && str[1] == '2') {
            board[1] = symbol;
        }
        if (str[0] == 'a' && str[1] == '3') {
            board[2] = symbol;
        }
        if (str[0] == 'b' && str[1] == '2') {
            board[4] = symbol;
        }
        if (str[0] == 'b' && str[1] == '3') {
            board[5] = symbol;
        }
        if (str[0] == 'c' && str[1] == '2') {
            board[7] = symbol;
        }
        if (str[0] == 'c' && str[1] == '3') {
            board[8] = symbol;
        }

        if (check_win(board)) {
            print_board(board);
            printf("%c WINS\n", symbol);
            break;
        }

        if (symbol == '0') {
            symbol = 'X';
        } else {
            symbol = '0';
        }
    }
}
```


## [DAY-352] files

Watch Bro Code's reading and writing files: https://www.youtube.com/watch?v=UqB4EgUxapM and https://www.youtube.com/watch?v=Hzg3kCHJcxI

> the code she wrote

```

#include <stdio.h>

int main() {
    FILE *pF = fopen("test.txt","w");

    fprintf(pF, "spongebob sqquerpants KIRA AND RYUK");
    fclose(pF);
    return 0;
}


#include <stdio.h>
int main() {
    FILE *pF = fopen("/Users/jack/book/poem.txt","r");
    char buffer[255];
    while(fgets(buffer,255,pF) != NULL) {
        printf("%s", buffer);
    }
    fclose(pF);
}
```
