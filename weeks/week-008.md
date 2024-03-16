## [DAY-55] Lists; Functions

Tic Tac Toe

```
def empty_game():
    game = [
      [' ','a','b','c','d'],
      ['1','-','-','-','-'],
      ['2','-','-','-','-'],
      ['3','-','-','-','-'],
      ['4','-','-','-','-']
    ]
    return game

def show_game(game):
    for row in game:
        #[' ','a','b','c','d']
        #...
        for col in row:
            #' '
            #'a'
            #'b'
            print (col, end=' ')
        print('')


g = empty_game()
x_or_zero='x'
while True:
    show_game(g)
    p = input('place ' + x_or_zero + ': ')

    if p == 'a1':
        g[1][1]=x_or_zero
    if p == 'a2':
        g[2][1]=x_or_zero
    if p == 'a3':
        g[3][1]=x_or_zero
    if p == 'a4':
        g[4][1]=x_or_zero

    if p == 'b1':
        g[1][2]=x_or_zero
    if p == 'b2':
        g[2][2]=x_or_zero
    if p == 'b3':
        g[3][2]=x_or_zero
    if p == 'b4':
        g[4][2]=x_or_zero

    if p == 'c1':
        g[1][3]=x_or_zero
    if p == 'c2':
        g[2][3]=x_or_zero
    if p == 'c3':
        g[3][3]=x_or_zero
    if p == 'c4':               
        g[4][3]=x_or_zero

    if p == 'd1':
        g[1][4]=x_or_zero    
    if p == 'd2':
        g[2][4]=x_or_zero
    if p == 'd3':
        g[3][4]=x_or_zero
    if p == 'd4':
        g[4][4]=x_or_zero


    if p == 'clear':
        g = empty_game()

        
    if x_or_zero =='x':
        x_or_zero = '0'
    else:
        x_or_zero='x'

```

Spend the rest of the day playing.

## [DAY-56] Functions; If; Random

Trivia game

```
def check(question, answer):
    x = input(question + ": ")
    if x == answer:
        return True
    else:
        return False


score = 0
if check("which animal lives on the north pole?", "polar bear"):
    score += 1
if check("which animal lives in the jungle?", "tiger"):
    score += 1

print("your score is: " + str(score))
```

Math test:

```
import random

while True:
    a = random.randint(1,10)
    b = random.randint(1,10)

    r = int(input("what is " + str(a) + " * " + str(b) + "? " ))

    if r == a * b:
        print("Correct!")
    else:
        print("Incorrect, the answer was: " + str(a * b))
```

Random characters

```
import random

while True:
    x = random.randint(ord('a'), ord('z'))
    print(chr(x))
```


## [DAY-57] Lists; Functions; Grid

Snake

```
import random
APPLE_SYMBOL = '@'

def render(world):
  for row in world:
    for col in row:
      print(col,end=' ')
    print('')

def empty():
  return  [
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
]

def snake_eats_itself(positions, current_col, current_row):
    for (col,row) in positions:
        if col == current_col and row == current_row:
            return True

def place_apple(world):
    # just place it on a random square from all possible squares
    possible = []
    for index_row in range(len(world)):
        for index_col in range(len(world[index_row])):
            if world[index_row][index_col] == '-':
                possible.append((index_col,index_row))

    if len(possible) == 0:
        # we cant place an apple
        return False
    else:
        (col,row) = random.choice(possible)
        world[row][col] = APPLE_SYMBOL
        return True
    
world = empty()
player_row = 0
player_col = 0
player_history = []

world[player_row][player_col] = '%'
player_history.append((player_col,player_row))


place_apple(world)
render(world)


while True:
  direction = input("which direction: ")
  
  world[player_row][player_col] = '='
  if direction == "u":
    player_row = player_row - 1
  elif direction == "d":
    player_row = player_row + 1
  elif direction == "l":
    player_col = player_col - 1
  elif direction == "r":
    player_col = player_col + 1
  else:
      print("try again, u for up/d for down/l for left/r for right")
      continue
  if snake_eats_itself(player_history, player_col, player_row):
      print("GAME OVER")
      break

  if world[player_row][player_col] == APPLE_SYMBOL:

      world[player_row][player_col] = '$'
      if not place_apple(world):
          print("YOU WON!")
          break
  else:
      world[player_row][player_col] = '%'

  player_history.append((player_col,player_row))

  render(world)

```

## [DAY-58] Continue Previous Day

Keep working on the snake game if you are not done. if you are do touch typing

## [DAY-59] Tuples; Lists

Tuples are kind of like lists that you cant grow or shrink, but also you usually assign meaning to each of the positions, for example

```
position = (1,2)

(x,y) = position
print(x)
print(y)
```

it can have more elements

```
posittion = (1,2,3)
(width,depth,height) = position

print(width)
print(depth)
print(height)
```

You see how we used it in the snake game, to make a list of tuples, where we had the player history.

```
positions = [(1,2),(3,4),(5,6)]
print(positions)
for p in positions:
    print(p)
    (x,y) = p
    print(x)
    print(y)
```

It is quite handy when you know you have pairs of data, like X and Y position or Season number and Episode number.

```
favorite_miraculous = [(3,1),(3,2),(2,1)]

for m in favorite_miraculous:
    (season,episode) = m
    print(str(season) + " season episode: " + str(episode))
```

Or more than 2 pieces, you can hold however many you want, but it usually is you that assign meaning to each position, like in the above case, the first element we decide is season, and the second one we decide is episode

## [DAY-60] Go Back In Time

Back to the beginning.

* Write a program to make a spy name
* Write a program to ask for favorite food
* Write a program to ask what is your name forever

