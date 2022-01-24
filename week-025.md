## [DAY-171] while; for; if; list

Build a chess game in 3 days.

* day 1, build the board, black and white squares, think carefully about the algorithm how to alternate between the colors
* day 2, build the basic movement, how to pick and drop a piece (use the pieces from https://joszs.itch.io/, they are licensed as CC 4.0 and are very very beautiful)
* day 3, polish the pieces, make it possible to take a piece
* todo: add queening the pawn code later
* todo: add restrictions to illegal moves

![game-171.png](./screenshots/game-171.png "game 171 screenshot")

> This is the code that we wrote together, it actually took 3 days, 30 minutes per day, with a some help from the parent, but in the end its a (almost) working chess game.

```
import pgzrun
HEIGHT = 800
WIDTH = 800

board = []

black = [
    Actor('chess/rook-black',anchor=(0,0), pos=(0,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(100,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(200,0)),
    Actor('chess/queen-black',anchor=(0,0), pos=(300,0)),
    Actor('chess/king-black',anchor=(0,0), pos=(400,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(500,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(600,0)),
    Actor('chess/rook-black',anchor=(0,0), pos=(700,0)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(0,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(100,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(200,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(300,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(400,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(500,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(600,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(700,100)),
]

white = [
    Actor('chess/pawn-white',anchor=(0,0), pos=(0,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(100,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(200,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(300,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(400,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(500,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(600,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(700,600)),
    Actor('chess/rook-white',anchor=(0,0), pos=(0,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(100,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(200,700)),
    Actor('chess/queen-white',anchor=(0,0), pos=(300,700)),
    Actor('chess/king-white',anchor=(0,0), pos=(400,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(500,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(600,700)),
    Actor('chess/rook-white',anchor=(0,0), pos=(700,700)),
]
x = 0
y = 0

block = 0
for i in range(1,65):
    if block % 2 == 0:
        board.append(Actor('chess/white',anchor=(0,0), pos=(x,y)))
    else:
        board.append(Actor('chess/black',anchor=(0,0), pos=(x,y)))

    block += 1
    x += 100
    if i != 0 and i%8 == 0:
        y += 100
        x = 0
        block+=3

pick_white = None
pick_black = None
elf = Actor("c1",ancor=(0,0))
king = Actor("c2")

def on_key_down(key):
    global pick_white,pick_black

    if key == keys.R and pick_white == None:
        # pick up the piece below
        for w in white:
            if elf.colliderect(w):
                pick_white = w 
    elif key == keys.R and pick_white != None:
        for b in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(b):
                for w in white:
                    if w != pick_white and b.colliderect(w):
                        return

                # snap the white piece to the board
                pick_white.x = b.x
                pick_white.y = b.y

                # take the black piece if there
                for bl in list(black):
                    if bl.colliderect(pick_white):
                        black.remove(bl)
                # drop it
                pick_white = None
                break
    if key == keys.P and pick_black == None:
        # pick up the piece below
        for b in black:
            if king.colliderect(b):
                pick_black = b 
    elif key == keys.P and pick_black != None:
        for b in board:
            if king.colliderect(b):
                # dont allow a drop if there is already a black piece there
                for l in black:
                    if l != pick_black and b.colliderect(l):
                        return

                # snap the black piece to the board
                pick_black.x = b.x
                pick_black.y = b.y

                # take the white piece if there
                for w in list(white):
                    if w.colliderect(pick_black):
                        white.remove(w)
                # drop it
                pick_black = None
                break

def update():
    global pick_white,pick_black
    speed = 2
   
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5  
    if keyboard.A:
        elf.x -= 5  
    if keyboard.D:
        elf.x += 5      
    if keyboard.UP:
        king.y -= 5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.LEFT:
        king.x -= 5
    if keyboard.RIGHT:
        king.x += 5
    
    # move the white piece with the elf
    if pick_white != None:
        pick_white.x = elf.x - 30
        pick_white.y = elf.y - 30
    # move the black piece with the king
    if pick_black != None:
        pick_black.x = king.x - 30
        pick_black.y = king.y - 30



def draw():
    screen.fill('deepskyblue')

    for b in board:
        b.draw()
    for b in black:
        b.draw()
    for w in white:
        w.draw()

    elf.draw()
    king.draw()

pgzrun.go()
```



## [DAY-172] if

Add Queening the Pawn functionality, which means when a white/black pawn reaches the of the board it turns into a queen. Think a bit what that means, for a white pawn it reaches the end of the board when its .y property is 0, and for a black pawn when its 700. The only thing left to do is to actually check if we are holding a pawn.


```
# ...
# shouldnt be able to drop if there is already white piece there
if elf.colliderect(b):
    for w in white:
        if w != pick_white and b.colliderect(w):
            return

    # snap the white piece to the board
    pick_white.x = b.x
    pick_white.y = b.y

    # take the black piece if there
    for bl in list(black):
        if bl.colliderect(pick_white):
            black.remove(bl)

    # Queening the Pawn:
    # pick_white.image is chess/pawn-white for the white pawn
    # set the pick_white.image to chess/queen-white if it reaches the black end of the board
    if pick_white.image == 'chess/pawn-white' and pick_white.y == 0:
        pick_white.image = 'chess/queen-white'
    
    # drop it
    pick_white = None
    break
# ...    
```

and respective for the black pawn:

```
# ...

    if pick_black.image == 'chess/pawn-black' and pick_black.y == 700:
        pick_black.image = 'chess/queen-black'
    
    # drop it
    pick_black = None    

# ...        
```

## [DAY-173] if; variables

Today we will make another rule, the pawns can not go backwards. Also we will cleanup the code a bit, and rename few variable so it is more readable, previously we had `for b in board` and then we were using `b.x` and etc, which was kind of confusing. We will rename it for `for square in board` and you will see how much more readable the code is.


First if we want to check if something is going backwards we have to compare its current position with the previous position. In our case this is quite simple, we will make two variables `x` and `y` and once we select which piece we will be moving we will store the piece's .x and .y properties into our `x` and `y` variables.

After we have the original position it is just a matter of checking at the time of placing the piece if it is a pawn and if the original y position is bigger or smaller than the new position, depending which way is forward, for the black pawns up is downwards (y is growing),  for white its upwards (y is decreasing).


This is the whole program again, because of the rename of some variables, it is easier to re-read it.

```
import pgzrun
HEIGHT = 800
WIDTH = 800

board = []

black = [
    Actor('chess/rook-black',anchor=(0,0), pos=(0,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(100,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(200,0)),
    Actor('chess/queen-black',anchor=(0,0), pos=(300,0)),
    Actor('chess/king-black',anchor=(0,0), pos=(400,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(500,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(600,0)),
    Actor('chess/rook-black',anchor=(0,0), pos=(700,0)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(0,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(100,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(200,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(300,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(400,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(500,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(600,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(700,100)),
]

white = [
    Actor('chess/pawn-white',anchor=(0,0), pos=(0,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(100,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(200,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(300,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(400,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(500,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(600,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(700,600)),
    Actor('chess/rook-white',anchor=(0,0), pos=(0,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(100,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(200,700)),
    Actor('chess/queen-white',anchor=(0,0), pos=(300,700)),
    Actor('chess/king-white',anchor=(0,0), pos=(400,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(500,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(600,700)),
    Actor('chess/rook-white',anchor=(0,0), pos=(700,700)),
]

x = 0
y = 0

block = 0
for i in range(1,65):
    if block % 2 == 0:
        board.append(Actor('chess/white',anchor=(0,0), pos=(x,y)))
    else:
        board.append(Actor('chess/black',anchor=(0,0), pos=(x,y)))

    block += 1
    x += 100
    if i != 0 and i%8 == 0:
        y += 100
        x = 0
        block+=3

pick_white = None
pick_black = None
elf = Actor("c1",ancor=(0,0))
king = Actor("c2")
x = 0
y = 0

def on_key_down(key):
    global pick_white,pick_black,x,y

    if key == keys.SPACE and pick_white == None:
        # pick up the piece below
        for w in white:
            if elf.colliderect(w):
                pick_white = w

                # store the original position
                x = w.x
                y = w.y
                
    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                for w in white:
                    if w != pick_white and square.colliderect(w):
                      return

                # pawns cant move backwards
                if pick_white.image == 'chess/pawn-white' and square.y > y:
                    return
                
                # snap the white piece to the board
                pick_white.x = square.x
                pick_white.y = square.y

                # take the black piece if there
                for b in list(black):
                    if b.colliderect(pick_white):
                        black.remove(b)

                # Queening the Pawn:
                # pick_white.image is chess/pawn-white for the white pawn
                # set the pick_white.image to chess/queen-white if it reaches the black end of the board
                if pick_white.image == 'chess/pawn-white' and pick_white.y == 0:
                    pick_white.image = 'chess/queen-white'
                
                # drop it
                pick_white = None
                break
    if key == keys.P and pick_black == None:
        # pick up the piece below
        for b in black:
            if king.colliderect(b):
                pick_black = b 

                # store the original position                
                y = b.y
                x = b.x
    elif key == keys.P and pick_black != None:
        for square in board:
            if king.colliderect(square):
                # dont allow a drop if there is already a black piece there
                for b in black:
                    if b != pick_black and square.colliderect(b):
                        return

                # pawns cant move backwards
                if pick_black.image == 'chess/pawn-black' and square.y < y:
                    return

                # snap the black piece to the board
                pick_black.x = square.x
                pick_black.y = square.y

                # take the white piece if there
                for w in list(white):
                    if w.colliderect(pick_black):
                        white.remove(w)
    
                # Queen the Pawn
                if pick_black.image == 'chess/pawn-black' and pick_black.y == 700:
                    pick_black.image = 'chess/queen-black'

                # drop it
                pick_black = None
                break

def update():
    global pick_white,pick_black
   
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5  
    if keyboard.A:
        elf.x -= 5  
    if keyboard.D:
        elf.x += 5      
    if keyboard.UP:
        king.y -= 5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.LEFT:
        king.x -= 5
    if keyboard.RIGHT:
        king.x += 5
    
    # move the white piece with the elf
    if pick_white != None:
        pick_white.x = elf.x - 30
        pick_white.y = elf.y - 30

    # move the black piece with the king
    if pick_black != None:
        pick_black.x = king.x - 30
        pick_black.y = king.y - 30



def draw():
    screen.fill('deepskyblue')

    for square in board:
        square.draw()
    for b in black:
        b.draw()
    for w in white:
        w.draw()

    elf.draw()
    king.draw()

pgzrun.go()

```