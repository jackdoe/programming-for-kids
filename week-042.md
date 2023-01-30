## [DAY-287] follow the line

Make a follow the line robot.

> we had microbit and kitronik kit, and this is the code she wrote (i wrote the helper functions)

![game-287.png](./screenshots/game-287.png "game 287 screenshot")

```
def forward(n):
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.FORWARD,n)
def back(n):
    Kitronik_Move_Motor.move(Kitronik_Move_Motor.DriveDirections.REVERSE,n)

def turn_left(n):
    Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MotorLeft)
    Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorRight,Kitronik_Move_Motor.MotorDirection.Forward, n)
    
def turn_right(n):
    Kitronik_Move_Motor.motor_off(Kitronik_Move_Motor.Motors.MotorRight)
    Kitronik_Move_Motor.motorOn(Kitronik_Move_Motor.Motors.MotorLeft,Kitronik_Move_Motor.MotorDirection.Forward, n)

def distance():
    return Kitronik_Move_Motor.measure()

def rand(n):
    return int(Math.random() * n)

def sensor_left():
    return Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.LEFT)

def sensor_right():
    return Kitronik_Move_Motor.read_sensor(Kitronik_Move_Motor.LfSensor.RIGHT)

def on_forever():
    left = sensor_left()
    right = sensor_right()
    if left>221:
        turn_right(30)
    elif right>221:
        turn_left(30)
    else:
        forward(2)

basic.forever(on_forever)
```


## [DAY-288] lines

Make two lines going through the center of the screen, and two lines from the elf to the y axis and the x axis

```
WIDTH = 800
HEIGHT = 800
...
def draw():
    screen.fill('black')
    elf.draw()
    screen.draw.line([elf.x,elf.y],[400,400],[255,255,255])
    screen.draw.line([elf.x,elf.y],[elf.x,400],[223,25,123])
    screen.draw.line([elf.x,elf.y],[400,elf.y],[132,123,231])
    screen.draw.line([0,400],[800,400],[255,255,255])
    screen.draw.line([400,800],[400,0],[255,255,255])
    ...
```

![game-288-a.jpg](./screenshots/game-288-a.jpg "game 288 a screenshot")
![game-288-b.jpg](./screenshots/game-288-b.jpg "game 288 b screenshot")


## [DAY-289] lines

Make a line between the elf and the king that moves with them.

![game-289.png](./screenshots/game-289.png "game 289 screenshot")

```
import pgzrun
HEIGHT=800
WIDTH=800
elf=Actor("c1")
king=Actor("c2")

def update():
    if keyboard.W:
        elf.y-=5
    if keyboard.S:
        elf.y+=5
    if keyboard.A:
        elf.x-=5
    if keyboard.D:
        elf.x+=5

    if keyboard.D:
        elf.x+=5
    if keyboard.UP:
        king.y-=5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.RIGHT:
        king.x+=5
    if keyboard.LEFT:
        king.x-=5

def draw():
    screen.clear()
    elf.draw()
    king.draw()
    screen.draw.line([elf.x,elf.y],[king.x,king.y],[123,132,19])


pgzrun.go()
```

## [DAY-290] lines

Make lines between many actors and the elf

![game-290.png](./screenshots/game-290.png "game 290 screenshot")

```
import pgzrun
import random

HEIGHT=800
WIDTH=800
elf=Actor("c1")

kings=[]
for i in range(10):
    b=Actor("c2")
    b.x=random.randint(10,790)
    b.y=random.randint(10,790)
    kings.append(b)

def update():
    if keyboard.W:
        elf.y-=5
    if keyboard.S:
        elf.y+=5
    if keyboard.A:
        elf.x-=5
    if keyboard.D:
        elf.x+=5

def draw():
    screen.clear()
    elf.draw()
    for i in kings:
        screen.draw.line([elf.x,elf.y],[i.x,i.y],[123,132,19])

pgzrun.go()
```
