

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

## [DAY-186] If

Make snakes and ladders on your own with pygame zero.

![game-186-b.png](./screenshots/game-186-b.png "game 186-b screenshot")

> This is what she wrote. She just went and found 500x500 board so that its easy to compute the position of each square, and hardcoded the jumps.

```
import pgzrun
import random

HEIGHT = 500
WIDTH = 500

elf = Actor("c1")
elf.x = -25
elf.y = 475
game_over = False
board = Actor("snake-500")
def on_key_down(key):
    if key == keys.SPACE:
        elf.x += random.choice([50,100,150,200,250,300]) 
        if elf.x > 475 and elf.y == 25:
            elf.x = 25 
            elf.y = 25
        if elf.x > 475:
            elf.x -= 500 
            elf.y -= 50
        if elf.y == 375 and elf.x == 225:
            elf.y = 475 
            elf.x = 225
        if elf.y == 25 and elf.x == 25:
            elf.y = 175 
        if elf.y == 475 and elf.x == 125:
            elf.y = 225 
            elf.x = 25
        if elf.y == 325 and elf.x == 175:
            elf.y = 475 
            elf.x = 25
        if elf.y == 475 and elf.x == 275:
            elf.y = 375 
            elf.x = 325
        if elf.y == 175 and elf.x == 125:
            elf.y = 25 
            elf.x = 225
        if elf.y == 75 and elf.x == 325:
            elf.y = 225 
            elf.x = 325
        if elf.y == 25 and elf.x == 425:
            elf.y = 175 
            elf.x = 425
        if elf.y == 475 and elf.x == 425:
            elf.y = 175 
            elf.x = 425

def update():
    global game_over
    speed = 10

    if keyboard.UP:
        elf.y -= speed
    if keyboard.DOWN:
        elf.y += speed
    if keyboard.LEFT:  
        elf.x -= speed
    if keyboard.RIGHT:
        elf.x += speed
    
    if elf.x == 475 and elf.y == 25:
        game_over = True

def draw():
    board.draw()
    elf.draw()
    if game_over == True:
        screen.draw.text('YOU WIN CONGRATULATION',(100,100),color = (0,0,0))
pgzrun.go()
```
> she also made a grid to compute the positions of each square

![game-186-a.png](./screenshots/game-186-a.png "game 186-a screenshot")

## [DAY-187] If; While; Functions

Watch Programming for Advanced Beginners: Battleships - EP 1, from Robert Heaton (https://www.youtube.com/watch?v=Gi0Fdyhk1_0), and then watch it again and code with the author

## [DAY-188] OOP

Watch https://www.youtube.com/watch?v=JeznW_7DlB0 (Python Object Oriented Programming (OOP) - For Beginners
 from Tech With Tim)

## [DAY-189] Keyword Arguments; String Methods

Today you have to watch three videos:

* Python keyword arguments 🔑 by Bro Code - https://www.youtube.com/watch?v=Tu0lFBXQgPw
* Python string methods by Bro Code - https://www.youtube.com/watch?v=crw3rVFNwIM
* Python Object Oriented Programming (OOP) - For Beginners from Tech With Tim - https://www.youtube.com/watch?v=JeznW_7DlB0 (watch it again)



## [DAY-190] While

Make a web whatsapp bot that sends the same message in an infinite loop

* click on the chrome tab with whatsapp
* click on the search box
* searche for contact name (dad)
* clicks on the top result
* click on the message input field
* type 'hello world'
* click the send button

Using https://pyautogui.readthedocs.io/en/latest/ as a guide. There are many ways to read documentation, try to spend some time just brawsing through it. Another way is to go to the example section and see if you can find examples that can help you solve your problem.

This is a snippet with examples taken from pyautogui's page:

```
>>> import pyautogui

>>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
>>> screenWidth, screenHeight
(2560, 1440)

>>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
>>> currentMouseX, currentMouseY
(1314, 345)

>>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

>>> pyautogui.click()          # Click the mouse.
>>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
>>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

>>> pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
>>> pyautogui.doubleClick()     # Double click the mouse.
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

>>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

>>> with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
>>> # Shift key is released automatically.

>>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

>>> pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
```

> use `pyautogui.position()` to find the accurate positions for your screen.
```
import pyautogui
import time
while True:
    pyautogui.click(305,10)
    pyautogui.click(117,252)
    pyautogui.write('dad', interval=0.25)
    pyautogui.click(185, 395)
    pyautogui.write('hello world!', interval=0.20)
    pyautogui.click(935, 1132)
    time.sleep(1)
```

Have some fun with it pranking your parents :) _but not too much_.


## [DAY-191] While

Make another whatsapp bot, but this time send a very very long message.

```
import pyautogui
import time
import random
while True:
    pyautogui.click(305,10)
    pyautogui.click(117,252)
    pyautogui.write('dad', interval=0.25)
    time.sleep(1)
    pyautogui.click(185, 395)
    time.sleep(1)
    
    for i in range(3000):
        s = 'yo' * random.randint(1, 4)
        pyautogui.write(s + ' ')

    time.sleep(5)
    pyautogui.click(935, 1132)
```

this will send the message:

"yoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yo yo yoyo yoyo yo yoyo yoyo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yo yo yoyo yo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyo yoyo yoyo yo yo yoyo yoyoyoyo yo yoyo yo yoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yo yoyoyoyo yo yoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyo yo yo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyo yoyo yoyo yo yo yoyo yoyo yo yoyo yoyo yoyoyo yoyo yo yo yoyoyoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyo yo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yo yo yoyoyo yo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyo yo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yo yo yoyoyo yoyoyo yoyoyoyo yo yo yo yoyoyo yoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yo yo yoyo yoyoyoyo yo yo yoyoyo yo yoyoyo yoyoyoyo yo yoyo yoyoyo yoyo yoyoyo yo yo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yoyoyoyo yo yoyo yoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyoyo yo yoyo yo yoyo yoyoyoyo yo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yo yo yo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyoyo yo yo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyo yo yoyo yoyoyo yoyo yoyoyo yoyo yo yoyo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yo yoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyo yo yoyo yo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyo yoyoyo yoyo yoyo yoyo yoyo yo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yo yo yoyo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyo yo yoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yo yoyo yoyo yoyoyo yoyoyo yo yo yoyoyoyo yoyo yo yo yoyoyo yo yo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yo yo yo yoyoyo yo yoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yoyoyo yoyoyoyo yoyo yo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyo yo yoyoyo yoyoyo yo yoyoyoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yo yoyo yoyo yoyo yoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyo yoyoyoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yo yoyo yoyoyo yo yoyo yo yo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyo yoyo yo yoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyoyo yo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyo yoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yo yo yoyo yo yoyo yo yoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyo yoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yoyoyo yo yoyo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yo yoyoyo yo yoyo yoyoyo yoyo yoyo yo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyo yo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yo yoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yo yo yoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyo yo yo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyo yoyo yo yoyoyoyo yoyo yoyo yoyo yoyo yo yoyo yo yoyoyo yoyoyo yoyo yo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yo yo yo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyo yo yoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyo yoyoyo yo yoyoyo yo yoyo yoyoyoyo yoyoyo yo yoyoyo yo yoyoyoyo yo yoyo yoyoyo yoyo yoyoyo yo yo yo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yo yo yoyo yoyoyoyo yoyoyo yo yoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yo yoyo yoyoyo yoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyo yo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyo yo yoyoyoyo yoyoyo yoyoyo yo yo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yo yo yoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyoyoyo yo yo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyoyo yoyo yo yoyo yoyo yoyo yoyoyoyo yo yoyo yo yo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yoyoyo yo yo yo yoyo yo yoyoyoyo yoyo yoyo yoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyo yoyo yoyoyo yo yo yoyo yoyo yo yoyo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yo yo yoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyo yo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyo yoyo yoyoyoyo yo yoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yo yoyo yo yoyoyo yo yoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yo yo yo yo yoyoyoyo yoyoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yo yo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyo yoyo yoyo yo yoyo yoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyo yo yo yoyoyo yo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yo yoyoyo yoyo yoyoyo yo yoyoyoyo yo yo yo yoyoyo yo yo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyo yo yo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yo yo yo yo yo yoyo yo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yo yo yoyoyoyo yoyoyoyo yo yo yoyo yo yoyo yoyoyo yoyoyo yoyo yoyoyo yo yoyoyo yoyoyo yoyoyoyo yo yo yoyo yoyoyoyo yo yoyoyoyo yoyo yoyo yo yoyoyoyo yo yo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yoyo yo yo yoyoyoyo yoyoyo yoyo yoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyoyo yoyoyo yo yoyoyo yo yoyoyo yo yo yoyoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyo yo yo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yoyoyo yo yoyo yoyo yoyoyoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yo yoyo yoyoyoyo yoyoyo yo yoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yo yoyo yoyoyoyo yo yoyoyoyo yo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyo yo yoyo yoyoyoyo yo yoyo yoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyo yo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyoyo yo yoyo yoyoyo yo yoyo yoyoyo yo yo yoyoyoyo yo yoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yo yoyoyo yo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyo yoyo yo yo yoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyo yo yoyoyo yoyo yoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yo yo yoyoyo yoyoyo yo yoyo yoyo yoyoyoyo yo yoyo yoyo yoyoyo yoyoyoyo yo yo yoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yo yoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yo yo yoyoyo yo yoyoyoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yo yoyo yoyo yo yoyo yo yoyoyoyo yoyo yo yoyoyo yoyoyoyo ypoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yo yoyo yoyoyo yoyoyo yoyo yoyo yo yoyoyo yoyoyoyo yo yoyo yo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyoyo yoyo yoyoyo yoyo yoyo yo yoyoyoyo yoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yo yoyo yoyoyoyo yo yo yoyoyo yoyo yoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yoyo yo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yoyo yoyoyo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyo yo yoyoyo yo yoyoyo yoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yo yo yo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yo yoyo yoyoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yo yo yoyoyo yoyoyo yoyoyo yo yo yo yoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyo yo yoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyo yo yoyoyo yoyoyo yoyo yoyo yo yo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyo yo yoyoyoyo yo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyo yoyo yoyoyo yo yoyo yoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yo yoyo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yo yoyo yoyo yoyoyoyo yoyoyo yoyo yo yoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yo yo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyo yo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyo yoyoyoyo yo yoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyo yoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yo yo yoyoyoyo yo yoyoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyo yo yoyo yo yo yo yoyo yo yoyoyoyo yo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yo yo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yo yo yoyo yoyoyoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yo yoyoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yo yo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yoyo yo yo yoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yo yo yoyoyoyo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yo yoyo yoyo yo yoyo yoyoyoyo yo yoyo yo yoyo yoyoyoyo yoyoyoyo yo yo yoyoyo yo yoyoyo yoyo yoyoyoyo yoyo yoyo yo yoyo yo yoyo yoyoyoyo yo yoyoyo yo yoyoyoyo yo yoyoyoyo yo yo yoyo yoyoyoyo yo yo yo yoyoyo yo yo yoyo yoyo yoyoyo yoyo yo yoyoyo yo yoyo yoyoyoyo yoyo yo yoyoyo yoyoyo yoyo yoyo yoyoyo yo yoyo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yoyo yo yo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yo yo yoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yo yoyoyoyo yo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyo yo yo yoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yo yoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yoyo yo yoyo yoyo yo yo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yo yo yo yoyoyoyo yoyo yo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yo yo yoyoyo yoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyo yoyo yoyo yo yoyoyoyo yo yoyo yoyoyoyo yo yoyo yoyoyo yoyoyo yoyoyo"



## [DAY-191] Class; Methods


There are few ways to represent a rectangle, one is with one point plus width and height, e.g. top left point and width and height.


```
(the screen's y grows downwards, top left is 0,0)
    │       x=8                           x
────┼───────┬────────────────────────────────
    │       │
    │       │
 y=3├───────*──────────────────┐
    │       │##################│
    │       │##################│
    │      h│##################│ height
    │       │##################│
    │       └──────────────────┘
    │              width
    │
    │
   y│
```

or you can store the position of two diagonal points, top left and bottom right (or top right and bottom left)

```
    │
    │       x=8              x=27         x
────┼───────┬──────────────────┬─────────────
    │       │                  │
    │       │                  │
 y=3├───────*──────────────────┤
    │       │##################│
    │       │##################│
    │       │##################│
    │       │##################│
 y=8├───────┴──────────────────*
    │
    │
   y│

```

In this example I chose the two points appriach as it I can just make a Point class and use it twice, but sometimes the first approach is more suitable. We want to make a Rect class that has a method to expand to include a point.

```
    │
    │       x=8              x=27   x=31    x
────┼───────┬──────────────────┬─────────────
    │       │                  │     .
    │       │                  │     .
 y=3├───────*──────────────────┤     .
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
 y=8├───────┴──────────────────*+++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
y=12│................................*
    │
    │
    │
   y│
```

> Pause here to think about how to approach this, use pen and paper to illustrate the approach.

The solutio is simply to move the topleft's x/y more left/up if they are bigger than the requested point, and move the bottomright's x/y if they are smaller than the requested point. This way the rectangle grows just enough to include the point.

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        if self.topLeft.y > point.y:
            self.topLeft.y = point.y
        if self.bottomRight.x < point.x:
            self.bottomRight.x = point.x
        if self.bottomRight.y < point.y:
            self.bottomRight.y = point.y

r = Rect(Point(10,10),Point(20,20))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(5,5))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,3))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

Sometimes its handy to be able to chain method calls, so if the method returns an instance you can just call a method on the returned value.

```
class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        ...
        return self

r = Rect(Point(10,10),Point(20,20))
r.expand(Point(5,5)).expand(Point(50,3)).expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```
