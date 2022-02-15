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



## [DAY-179] if; for

Today we will do two more rules, one is the queen and one for the pawn. The queen can move like the rook and the bishop combined, so horizontally, vertically and diagonally. The pawn can move one step diagonally if she can take an enemy piece.

Lets start with the queen, as we already have the rook and bishop rules, it is quite easy, we just have to say 'if the move is not like the rook and not like the bishop then its illegal'.

```
                if pick_white.image == 'chess/rook-white':
                    if square.x != pick_x and square.y != pick_y:
                        return
                if pick_white.image == 'chess/bishop-white':
                    d_y = pick_y - square.y
                    d_x = pick_x - square.x
                    if abs(d_y) != abs(d_x):
                        return
                if pick_white.image == 'chess/queen-white':
                    d_y = pick_y - square.y
                    d_x = pick_x - square.x
                    if abs(d_y) != abs(d_x) and square.x != pick_x and square.y != pick_y:
                        return
...                        

```


The pawn is a bit more complicated, we need to check if the move is actually one step diagonally, and we also need to have a way to check if a piece is on specific position. We will make `is_on_square` function, that takes a position and a list and checks if any of the items of that list is on that position.

```
def is_on_square(x, y, pieces):
    for p in pieces:
        if p.x == x and p.y == y:
            return True

    return False

```


Now that we have the `is_on_square` function, we can simply check if the `y` of the square is exactly on top of the original position, and the `x` of the square is either one to the left or one to the right, which would mean either 1 square left diagonal or right diagonal, and then check if there is a black piece there, if it is allow the move.

![game-179.png](./screenshots/game-179.png "game 179 screenshot")


```
...
                if pick_white.image == 'chess/pawn-white':
                    # 1 or 2 squares
                    if pick_y == 600:
                        if pick_y - square.y > 200:
                            return
                    if pick_y != 600:
                        if pick_y - square.y > 100:
                            return

                    # pawn can only go left or right if theres someone
                    if pick_x != square.x:
                        ok = False
                        if pick_y - square.y == 100 and pick_x - square.x == 100 and is_on_square(square.x, square.y, black):
                            ok = True
                        if pick_y - square.y == 100 and pick_x - square.x == -100 and is_on_square(square.x, square.y, black):
                            ok = True

                        if not ok:
                            return
...
```

## [DAY-180] if

There is an important rule in chess, that many people dont know, En Passant (In Passing).

From Wikipedia (https://en.wikipedia.org/wiki/En_passant):

> En passant (French: [ɑ̃ paˈsɑ̃], lit. in passing) is a move in chess. It is a special pawn capture that can only occur immediately after a pawn makes a move of two squares from its starting square and provided that it could have been captured by an enemy pawn had it advanced only one square. The opponent captures the just-moved pawn "in passing" through the first square. The result is the same as if the pawn had advanced only one square and the enemy pawn had captured it normally.

> The en passant capture must be made on the very next turn or the right to do so is lost. En passant capture is a common theme in chess compositions.

> The en passant capture rule was added in the 15th century when the rule that gave pawns an initial double-step move was introduced. It prevents a pawn from using the two-square advance to pass an adjacent enemy pawn without the risk of being captured.


![game-180-a.png](./screenshots/game-180-a.png "game 180-a screenshot")
![game-180-b.png](./screenshots/game-180-b.png "game 180-b screenshot")
![game-180-c.png](./screenshots/game-180-c.png "game 180-b screenshot")

So its pretty nice rule, what we have to do is to remember each pawn that moves two squares and consider it possible en_passant, and then if the oponnent's pawn wants to move diagonally we will check if there is en_passant above(black)/below(white) and if there is we will capture it. If any move is made we will clear the en-passant

the code looks like this:

```
enpassant = None


def on_key_down(key):
    global pick_white, pick_black, pick_x, pick_y, enpassant

    ...
    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                ...
                if pick_white.image == 'chess/pawn-white':
                    # 1 or 2 squares
                    if pick_y == 600:
                        if pick_y - square.y == 200:
                            enpassant = pick_white

                        if pick_y - square.y > 200:
                            return
                    if pick_y != 600:
                        if pick_y - square.y > 100:
                            return
                    # if y > 200 first move:

                    # pawn can only go left or right if theres someone
                    if pick_x != square.x:
                        ok = False
                        if pick_y - square.y == 100 and pick_x - square.x == 100 and is_on_square(square.x, square.y, black):
                            ok = True
                        if pick_y - square.y == 100 and pick_x - square.x == -100 and is_on_square(square.x, square.y, black):
                            ok = True

                        if (pick_y - square.y == 100 and pick_x - square.x == 100) or (pick_y - square.y == 100 and pick_x - square.x == -100):
                            if enpassant != None and enpassant.image == 'chess/pawn-black':
                                if enpassant.x == square.x and enpassant.y == square.y + 100:
                                    black.remove(enpassant)
                                    ok = True

                        if not ok:
                            return

                    # pawns cant move backwards
                    if square.y > pick_y:
                        return
                    # Queening the Pawn:
                    # pick_white.image is chess/pawn-white for the white pawn
                    # set the pick_white.image to chess/queen-white if it reaches the black end of the board
                    if square.y == 0:
                        pick_white.image = 'chess/queen-white'
                ...
                # snap the white piece to the board
                pick_white.x = square.x
                pick_white.y = square.y
                if enpassant != pick_white:
                    enpassant = None
...
```

Notice how we set enpassant = pick_white if the pawn moves 2 squares (this will be used if the black pawn tries to capture), and later when we see that the pawn is moving diagonally we do:

```
if (pick_y - square.y == 100 and pick_x - square.x == 100) or (pick_y - square.y == 100 and pick_x - square.x == -100):
    if enpassant != None and enpassant.image == 'chess/pawn-black':
        if enpassant.x == square.x and enpassant.y == square.y + 100:
            black.remove(enpassant)
            ok = True
```

This basically checks if it is one square diagonal to the left or one square diagonal to the right, and if it is it checks if there is active enpassant and it is a black pawn, then it checks if it sits directly above the square we want to go to, and if it is we capture it and mark the move valid.


## [DAY-181] if

Add undo support. We need to store the piece's position when its picked up, the piece itself and its image (in case of Queening The Pawn) and we need to store those for every move, then if the key 'b' is pressed we need to take the last move and revert it, and so on.

A good strategy for that is to simply use a list, and each time we pick a piece we will append the position_x, position_y, image, actor and then when 'b' is pressed we will pop them out and set them to the actor in question.

```
...
back = []

def on_key_down(key):
    global pick_white, pick_black, pick_x, pick_y, pick_image, enpassant,back

    if key == keys.SPACE and pick_white == None:
        # pick up the piece below
        for w in white:
            if elf.colliderect(w):
                pick_white = w

                # store the original position
                pick_x = w.x
                pick_y = w.y
                pick_image = w.image

    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                # make sure the move is valid
                ...
                back.append(pick_image)
                back.append(pick_y)
                back.append(pick_x)
                back.append(pick_white)

                pick_white.x = square.x
                pick_white.y = square.y

                ...

    if key == keys.B:
        if len(back) != 0:
            actor = back.pop()
            x = back.pop()
            y = back.pop()
            image = back.pop()
            actor.x = x
            actor.y = y
            actor.image = image
...            
```

We are using the list like a stack, we add stuff to it and when we need we pop the top most items. You can see that we append image, y, x, actor but when we pop we get them in reverse order, because pop() removes the top most item from the ist, so we get back actor, x, y, image.


There is a fundamental limitation to this aproach, which is that we lose pieces that were taken, so if you undo they will just be gone.

## [DAY-182] look back

Today we will look back on some of the first programs you wrote.

Open our old files and read as many of them as you can.

## [DAY-183] Generalization

From today we will start to think before we code. You can see the game of chess we made, it kind of works but it is quite hard to add things to it, and to add new rules and etc. It is already around 500 lines of hard to read if statements.

We will do one week of exercises without writing code, just with pen and paper, where we will generalize, or try to extract the common attributes of things. We will think about how to think about things.

Lets start with an example. You know that `1 + 2` is the same as `2 + 1`, or `1 + 2 = 2 + 1`, same with `3 + 5 = 5 + 3`, this is quite intuitive, if you have two apples in one hand and one in the other, you have 3 apples irrelevant of which hand has 2 apples and which has 1. We can generalize that rule to `a + b = b + a`, meaning that any number `a` plus any number `b` is the same as wiriting `b+a`. It might seem like we did nothing here, just stated the obvious, but I will show you how powerful this generalization is.

At first we were thinkging of numbers, but with this generalization we can actually use expressions, for example `a = ((4838 + 8272) * 3)` and `b = ((7467 / 2) + 27838)` and still `a + b = b + a`, we can substitute `a` and `b`, so `((4838 + 8272) * 3) + ((7467 / 2) + 27838) = ((7467 / 2) + 27838) + ((4838 + 8272) * 3)`. We have higher level of reason, we are not confined to numbers anymore, but to whole expressions and expressions of expressions.

Lets talk now about what is needed to represent a chess piece. First we need its color, is it black or white, we need its kind (rook, bishop etc..), and its position x and y. Those are the properties of a piece. Each piece however can move in a different way, this is its behavior. Those are the two main things we have to think about, we can generalize thenm into 'what does the thing do' and 'how does the thing look'.

This week we will spend more time on examples about generalization and abstraction, and after that we will rewrite the chess game. It is very common to write something quick, and then rewrite it when you know how to actually think about it. The first time you code something is almost never good, purely because you still dont know how to represent the things in your program yet, even if you think a lot about it. In the real world you need to combine the both aproaches, of code and explore, and think carefully about how the pieces in your program talk to each other.

## [DAY-184] Generalization

> We (me and my daughter) have spent 30 minutes per day for the last week just talking about how to think about behavior and state. With all kinds of discussions, from tic tac toe, to stratego, to classess and lists and many more concepts. The talks were very open and unstructured, so it is hard to put them directly 1:1 in the book. I recommend you do the same. Spend time talking about how to think about your program, how the parts in it communicate, how you group the state, and how do you abstract behaviour. It is also important to think about how to think about problems in general, move one layer above practicality. Discuss patterns.


## [DAY-185] Generalization

Today we will build three different versions of snakes and ladders to illustrate different approaches.

We will use super small Snakes and Ladders game with the following rules:

* there are 9 squares, from 0 to 8
* 0 -> 0
* 1 -> 2
* 2 -> 2
* 3 -> 3
* 4 -> 2
* 5 -> 7
* 6 -> 0
* 7 -> 7
* 8 -> 8

1. While and If, most basic implementation. In this implementation if we do 99 squares or we want to render a board, or we want to make the game more interesting to roll the dice twice or something like that, everything will just explode in complexity.

```
player1 = 0
while True:
    print("player board position: ", player1)
    dice = int(input("dice roll> "))

    player1 += dice
    if player1 == 1:
        player1 = 3
    elif player1 == 4:
        player1 = 2
    elif player1 == 5:
        player1 = 7
    elif player1 == 6:
        player1 = 0

```

2. Think about the rules of the game and what is a bit more abstract way to think about the them. The only rule actually is: if you land on the square you move wherever the square says, could be 0 (stay there), +steps or -steps. This is an example implementation where we just keep the state of each square in a list, square index 1 moves you to index 3 and so on.

```
board = [
    0,
    2,   # 1 -> 3
    0,
    0,
    -2,  # 4 -> 2
    2,   # 5 -> 7
    -6,  # 6 -> 0
    0,
    0
]

player1 = 8
while True:
    print("player board index: ", player1)
    dice = int(input("dice roll> "))
    player1 += dice

    if player1 >= len(board) - 1:
        print("finished")
        break

    snake_or_ladder = board[player1]
    player1 += snake_or_ladder
```

The whole game is actually encoded in those two lines:

```
    snake_or_ladder = board[player1]
    player1 += snake_or_ladder
```

See how different this is? The size of the code is very similar in lines, but this version is so much easier to change and to extend. For example if we want to display the board, now we can just pass the board list to some `render` function and be done. This is actually not possible in the first version with the if conditions unless we almost duplicate the whole program.


3. There is one more thing we could do to simplify it a bit, and that is to split the board from the input. So that we could move it maybe in a separate file (board.py) if we want. Separating the user input from the board action is quite nice because now it will be super easy to add mouse click functionality, and board rendering.


```
class Board:
    def __init__(self):
        self.player = 0
        self.squares = [
            0,
            2,   # 1 -> 3
            0,
            0,
            -2,  # 4 -> 2
            2,   # 5 -> 7
            -6,  # 6 -> 0
            0,
            0
        ]

    def move(self, dice):
        position = self.player + dice
        if position >= len(self.squares) - 1:
            return True

        self.player += self.squares[position]
        return False

#################################################

b = Board()
while True:
    print("player board position: ", b.player)
    roll = int(input("dice roll> "))
    if b.move(roll):
        print('finished')
        break
```