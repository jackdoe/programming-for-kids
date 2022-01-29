## [DAY-178] if; absolute

Today we will do the rule for the bishop, since the bishop moves in diagonal. You see in the image that the diagonal means that both x and y change with the same absolute amount, lets say we want to move only one square, the possible values are: -1 -1, -1 1, 1 1, 1 -1, meaning move up and left (decrease y and decrease x), up and right (decrease y, increase x), down and right (increase y, indcrease x), down and left (increase y, decrease x). 

![game-178.png](./screenshots/game-178.png "game 178 screenshot")

Note that if you actually only care if the amount of steps away from the origin, the dirction does not matter. In math when we care about the absolute value of a number we just care about the amount of steps it would take to get from that number to zero, for example from -5 to zero it will take 5 steps, from 5 to zero it will also take 5 steps.

```
<--------------------|-------------------->
 -5  -4  -3  -2  -1  0   1   2   3   4   5
```

Imagine you walking from -5 to zero, or from 5 to zero both will take you 5 steps. So lets write a function that takes a number and if the number is negative we will just turn it into its positive value, as we only care about the amount of steps.


```
def abs(x):
    if x < 0:
        return x * -1
    return x
```

Now lets make the bishop rule. If the steps change in x is the same as the change in y then we must be moving in a diagonal, if not we refuse the move.


```
...

                if pick_white.image == 'chess/bishop-white':
                    # how much did the y change
                    d_y = pick_y - square.y

                    # how much did the x change
                    d_x = pick_x - square.x

                    # if they didnt change the same amount, then its illegal move
                    if abs(d_y) != abs(d_x):
                        return

...
```