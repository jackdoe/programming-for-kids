## [DAY-355] riscv assembler

Tle last month or so we spent learning RISCV assembler while making a board game: [PROJEKT:OVERFLOW](https://punkx.org/overflow/)

Each day I made an exercise and then we wrote (either together or her own) the execution of the program, you can see most of the examples at https://punkx.org/overflow/#assembly

I am attaching the photos of some of the work just for the record:

![game-355.jpg](./screenshots/game-355.jpg "game 355 screenshot")


## [DAY-356] pointers

![game-356.jpg](./screenshots/game-356.jpg "game 356 screenshot")

## [DAY-357] buffer overflow

Play a round of easy mode projekt:overflow https://punkx.org/overflow

![game-357.jpg](./screenshots/game-357.jpg "game 357 screenshot")

## [DAY-358] buffer overflow

Play a round of easy mode projekt:overflow https://punkx.org/overflow

![game-358.png](./screenshots/game-358.png "game 358 screenshot")

## [DAY-359] scanf; printf

Get 4 numbers from the user and print them.

```
#include <stdio.h>
int main(void){
    int number1, number2, number3, number4;
    printf("Choose 4 numbers: ");
    scanf("%d %d %d %d",&number1,&number2,&number3,&number4);
    printf("You chose: %d %d %d %d\n",number1,number2,number3,number4);
    return 0;
}

```

## [DAY-360] fscanf

Read all lines from a file, each containing 4 numbers, and print the numbers

file numbers.txt:
```
1 2 3 54
1.2 3 4 6
0 1 2 3
```


```
#include <stdio.h>
int main(void){
    int number1, number2, number3, number4;
    FILE *fp;
    fp = open("numbers.txt","r");
    while(1)
        int r = fscanf(fp,"%d %d %d %d",&number1,&number2,&number3,&number4);
        if (r == EOF) {
            break;
        }
        printf("numbers: %d %d %d %d\n",number1,number2,number3,number4);
    }
    return 0;
}

```


## [DAY-361] files


write multipe lines in a file using python

```
fout = open('output.txt', 'w')
line1 = "This here\'s the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)
fout.close()
```
