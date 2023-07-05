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

![game-344.png](./screenshots/game-344.jpg "game 344 screenshot")
