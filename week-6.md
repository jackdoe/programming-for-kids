# Chapter 6 - Week 6

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
world[player_row][player_col] = 'x'

render(world)
while True:
  direction = input("which direction: ")
  
  world[player_row][player_col] = '*'
  if direction == "up":
    player_row = player_row - 1
  elif direction == "down":
    player_row = player_row + 1
  elif direction == "left":
    player_col = player_col - 1
  elif direction == "right":
    player_col = player_col + 1

  world[player_row][player_col] = 'x'
  render(world)

```

## [DAY-43] Basics of Basics


Even and Odd

```
number = int(input("give me a number: "))
if number % 2 == 0:
  print("this number is even")
else:
  print("this number is odd")
```


Fizz Buzz

Print integers 1 to N, but print "fizz" if an integer is divisible by 3, "buzz" if an integer is divisible by 5, and "fizzbuzz" if an integer is divisible by both 3 and 5.

```
n = 100

for i in range(1,n+1):
  if i % 5 == 0 and i % 3 == 0:
    print("fizz buzz")
  elif i % 3 == 0:
    print("fizz")
  elif i % 5 == 0:
    print("buzz")
  else:
    print(i)
```

or different version

```
n = 100
for i in range(1,n+1):
  fizzbuzzing = False
  if i % 3 == 0:
    fizzbuzzing = True
    print("fizz", end = '')

  if i % 5 == 0:
    fizzbuzzing = True
    print("buzz", end = '')

  if not fizzbuzzing:
    print(i, end = '')

  print('')
```

There are many ways to write this, lets just have fun.

```
n = 100
numbers = []

# first make empty list with 100 elements
for i in range(1, n+1):
  numbers.append('')

# then fill in the fizzes
for i in range(1, n+1):
  if i % 3 == 0:
    numbers[i-1] += 'fizz'

# then fill in the buzzess
for i in range(1, n+1):
  if i % 5 == 0:
    numbers[i-1] += 'buzz'

# then fill in the numbers
for i in range(1, n+1):
  if numbers[i-1] == '':
    numbers[i-1] = i

# then we print it
for x in numbers:
  print(x)
```

Haha this is a funny way to make fizzbuzz. See first it puts fizz if you can divide it by 3, and then buzz if you can divide it by 5, but if there was already fizz there it will just add if with `+=`, so it automatically works to put fizzbuzz for 15.

## [DAY-44] Basics of Basics

Reviews

```
reviews =[5,3,2,4,1,2,3,4,2,1,5,5,3,2]

sum = 0
for r in reviews:
  sum += r

rating = sum / len(reviews)
print(str(rating) + "⭐ out ot 5")
```

Icecream Maker

```
import random
flavors = ['vanilla','chocolate','blue','banana','bluberry']

flavorA = random.choice(flavors)
flavorB = random.choice(flavors)

print(flavorA + " + " + flavorB)
```

Spend the rest of the day touch typing.

## [DAY-45] Basics of Basics

Different touch typing

```
import random
vowels  = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def make_word(n_chars):
  word = ''

  for i in range(n_chars):
    if random.randint(1,100) < 40:
      word += random.choice(vowels)
    else:
      word += random.choice(consonants)
  return word

def make_sentence(n_words):
  sentence = ''
  for i in range(n_words):
    sentence += make_word(random.randint(3,6))
    sentence += ' '

  # this will remove the last element from the sentence string
  # so we dont have empty space in the end
  return sentence[:-1]

while True:
  sentence = make_sentence(random.randint(10,20))
  print(sentence)
  guess = input('write the sentence: ')
  if guess != sentence:
    print("SORRY")
  else:
    print("GOOD JOB")
```

spend the rest of the day trying it out

## [DAY-46] Basics of Basics

Some turtle!

```
import turtle
turtle.circle(30)
```

Many circles

```
import turtle
for i in range(30):
  turtle.circle(i)
```

Bigger circles

```
import turtle

turtle.color("blue")
for i in range(30):
  turtle.circle(50 + i)
```

Smile

```
import turtle

turtle.color("blue")
turtle.circle(100)
turtle.penup()
turtle.goto(60,120)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(20,120)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(-30,20)
turtle.pendown()
turtle.right(45)
turtle.circle(20, 120)
```


## [DAY-47] Basics of Basics

Try to make a program that prints a symbol N times, where N is coming from the user input.

Try by yourself.
