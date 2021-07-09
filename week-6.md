# Chapter 5 - Week 5

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```

## [DAY-41] Basics of Basics

```
import random

words = ["pizza","pikachu","ball","pokemon"]

while True:
  word = random.choice(words)
  guessed = []
  life = 10
  while True:
    
    print('*' * 10, ' HANGMAN ', '*' * 10)

    matching = 0
    for c in word:
      if c in guessed:
        print(c,end='')
        matching = matching + 1
      else:
        print('-',end='')
    print('')
    print('*' * 31)
    

    if matching == len(word):
      print('congratz you won!')
      break

    character = input("guess a character: ")
    if character in word:
      guessed.append(character)
    else:
      print(character + " is not in the word, " + str(life) + ' lives left') 
      life = life - 1
      if life == 0:
        print('you lost!')
        break
```


## [DAY-42] Basics of Basics

World without a player

```
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

world = empty()

render(world)
while True:
  row = int(input("which row (count from 0): "))
  col = int(input("which column (count from 0): "))

  world[row][col] = 'x'
  render(world)

```

World with a player

```
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

world = empty()
player_row = 0
player_col = 0
world[player_col][player_row] = 'x'

render(world)
while True:
  direction = input("which direction: ")
  if direction == "up":
    player_col = player_col - 1
  elif direction == "down":
    player_col = player_col + 1
  elif direction == "left":
    player_row = player_row - 1
  elif direction == "right":
    player_row = player_row + 1

  world[player_col][player_row] = 'x'
  render(world)

```

## [DAY-43] Basics of Basics
## [DAY-44] Basics of Basics
## [DAY-45] Basics of Basics
## [DAY-46] Basics of Basics
## [DAY-47] Basics of Basics
