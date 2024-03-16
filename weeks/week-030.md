## [DAY-206] client server

In order for computers to talk to each other we use the Internet Protocol, there are other ways to do it, but at the moment using the internet protocol is the most common one. The two computers talking to each other will need unique IP addresses. An IP address is just a 4 byte (32 bit) number, the minimum one is 0 and the maximum one is 4294967295. This is quite hard to remember, so we split the 32 bit number into 4x8 bit numbers, so for example the IP address of google.com is 2899945710, but this is super hard to read, if we split it into 4x8 bit numbers it looks like this: 172.217.168.238.

In another lesson we will discuss how the packet goes from computer to computer to get from your PC to google.com, it probably goes through 20 computers on its way.

Going back to the 32 bit number, lets start with something simple, 1 bit is as simple as an on/off switch, like the one controlling your lights.

One switch can either be on or off, so the possible configurations is 2 (0 or 1)

```
     .----------.
     |   ~ON~   |
     |   ____   |
     |  |.--.|  |
     |  ||  ||  |
     |  ||__||  |
     |  ||\ \|  |
     |  |\ \_\  |
     |  |_\[_]  |
     |          |
     |  ~OFF~   |
     '----------'
     (art by jgs)
```


Once we add a switch, the possible configurations double, however the previous ones were, we can have them either with the new switch on or off. So with 2 switches we have `00 01 10 11`


```
     .----------.      .----------.
     |   ~ON~   |      |   ~ON~   |
     |   ____   |      |   ____   |
     |  |.--.|  |      |  |.--.|  |
     |  ||  ||  |      |  ||  ||  |
     |  ||__||  |      |  ||__||  |
     |  ||\ \|  |      |  ||\ \|  |
     |  |\ \_\  |      |  |\ \_\  |
     |  |_\[_]  |      |  |_\[_]  |
     |          |      |          |
     |  ~OFF~   |      |  ~OFF~   |
     '----------'      '----------'
```


Adding third switch, the possible configurations doubles again `000 001 010 011 100 101 110 111`:

```
     .----------.      .----------.       .----------.
     |   ~ON~   |      |   ~ON~   |       |   ~ON~   |
     |   ____   |      |   ____   |       |   ____   |
     |  |.--.|  |      |  |.--.|  |       |  |.--.|  |
     |  ||  ||  |      |  ||  ||  |       |  ||  ||  |
     |  ||__||  |      |  ||__||  |       |  ||__||  |
     |  ||\ \|  |      |  ||\ \|  |       |  ||\ \|  |
     |  |\ \_\  |      |  |\ \_\  |       |  |\ \_\  |
     |  |_\[_]  |      |  |_\[_]  |       |  |_\[_]  |
     |          |      |          |       |          |
     |  ~OFF~   |      |  ~OFF~   |       |  ~OFF~   |
     '----------'      '----------'       '----------'
```

Going back to the IP address, one byte is just 8 switches, 4 bytes is 32 switches.

Now imagine 32 switches.. the possible amount of configurations is `2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2` or 4294967295.

So over the internet for any two computers to communicate they need their own 32 bit number, this btw is version 4 of the Internet Protocol, now we are in the process of adopting the new version 6 which has 128 bits for the IP address. Imagine 128 switches, the possible configurations are: 340282366920938463463374607431768211456, which is very very big number.


There are other few things needed in order to send messages between computers, and this is to be able to communicate with a specific program on the computer, for that we need a PORT, you can tell the operating system that when it recives a packet on specific port to send it to your program. We will use this in order to make a super simple chat program. The port is only 2 bytes (16 bits), so from 0 to 65535.

We will make a simple helper module, just copy paste the code for now, we will investigate it later.

Make a file 'multiplayer.py' and type the following code in it:

```
from socket import *
from threading import Thread

def server(ip, port,fn):
    t = Thread(target=listen, args=(ip,int(port),fn))
    t.start()
    t.join()

def listen(ip, port, fn):
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind((ip, port))
    while True:
        data, addr = sock.recvfrom(1024)
        r = fn(data.decode("utf-8"), addr)
        sock.sendto(r.encode("utf-8"), addr)


def send(ip, port, message):
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.sendto(message.encode("utf-8"), (ip, int(port)))
    data, addr = sock.recvfrom(1024)
    return data.decode("utf-8")
```


Now make a server:

```
import multiplayer
import sys

messages = []
def incoming(text, sender):
    ip, port = sender
    if '>' in text:
        name, message = text.split("> ")
        if len(message) > 0:
            messages.append(text)
    return "\n".join(messages)

ip = sys.argv[1]
port = sys.argv[2]
print('listening on', 'ip:', ip, 'port:', port)

multiplayer.server(ip, port, incoming)
```

To see your ipaddress go to CMD and type `ipconfig`, on macos go to the terminal and type `ifconfig`, a computer can have multiple ip addresses, so use your parent to help you out. You will see `127.0.0.1`, you can use this ip address when you want to communicate with another program on the same computer, it is called the local host address.

Start the server with `python3 server.py 192.168.x.x 6500` we will use port 6500

Make a client:

```
import multiplayer
import sys

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

while True:
    my_message = input("message> ")
    all_messages = multiplayer.send(ip, port, name + "> " + my_message)
    print(all_messages)
```

Start the client on two computers with `python3 client.py server_ip 6500`, then when you type something and send a message, the server will reply to you with all messages it recived so far.

There is a lot of code you dont understand here, and this is totally ok, we will get back to it in the future. The important part to remember is that IP version 4 addresses are 32 bits, and the port is 16 bits, and IP address allows you to talk to a computer and a port allows you to talk to a program.


## [DAY-207] 0; 1; infinity; how to break things down

When you think about any solution to any problem, it is very important to think in context of zero, one and infinity (or one million if infinity is impractical).

Lets look at this code for rot13:

```
def rot13(c):
    n = ord(c) - ord('a')
    return chr(97 + ((n + 13) % 26))
```

This `97 + ((n + 13) % 26)` seems a bit intimidating, but if we set `n = 0` then `(n + 13) % 26` becomes `13 % 26` which is just 13, so the whole thing becomes 97+13, which is 110. To get `n=0` we need to pass 'a' as a parameter, so this function takes `a` and returns `chr(110)` which is `n`. See 0 is incredibly powerful, now lets try with 1, 97+14 is 111, so if we pass `b` as parameter, the function will return `o`. And for infinity, the biggest `n` we can have here is 25 or `ord('z') - ord('a')`, `(25+13)%26` is 12, 97+12 is `m`, so `a` goes to `n` and `b` goes to `o` and `z` goes to `m`.

Always check the bounderies of the code: 0,1 and ∞ are your friends.

In math as well, you can see how things break down when you use 0 or ∞, everytime you see something divided by a variable, try to make this variable 0.

```
x = [1,2,3]
average = sum(x)/len(x)
```

What happens when you have an empty list? What happens when the list has exactly 1 element? What happens when you have infinite elements in the list?

In any problem, try to reduce it to nothing, one and everything, and each of those steps will help you to understand it better.


Look at some old code we wrote in day 81:

```
image = [
    1,3,3,3,3,3,1,
    2,4,5,4,5,4,2,
    2,4,4,5,4,4,2,
    2,4,5,4,5,4,2,
    1,3,3,3,3,3,1,
]

width = 7

for (index, pixel) in enumerate(image):
    if index > 0 and index % width == 0:
        print('')

    if pixel == 1:
        print('+', end='')
    elif pixel == 2:
        print('|', end='')
    elif pixel == 3:
        print('-', end='')
    elif pixel == 4:
        print(' ', end='')
    elif pixel == 5:
        print('*', end='')
    else:
        print("dont know what to do with: " + str(pixel))
```

Think of width as 0 and make the image with only 1 pixel and look at the code again:

```
image = [1]

for (index, pixel) in enumerate(image):
    if pixel == 1:
        print('+', end='')
```

the code becomes incredibly trivial: `if you see the pixel value 1, print '+'`.

Go back through your previous programs, and re-read them when you set various things to 0 (or empty lists) or 1 (or lists with 1 element).


## [DAY-208] if; lists

Make a game where the player captures falling things, every time they catch a thing it starts falling from a random position again, every 5th catch the difficulty increases by increasing the number of falling things.

![game-208.png](./screenshots/game-208.png "game 208 screenshot")


> thats what she wrote

```
import pgzrun
import random

HEIGHT = 800
WIDTH = 800
score = 0
player = Actor("chess/white")

dots = [Actor("rock"),Actor("flower")]
player.y = 760
game_over = False

def update():
    global game_over,score
    if keyboard.A:
        player.x -= 15 #+ score
    if keyboard.D:
        player.x += 15 #+ score
    if player.x <0:
        player.x = 0
    if player.x >790:
        player.x = 790
    for d in dots:
        d.y += 4
        if player.colliderect(d):
            d.x = random.randint(50,700)
            d.y = random.randint(10,300)
            score += 1
            if score%5==0:
                n = Actor(random.choice(["rock", "flower"]))
                n.x = random.randint(50,700)
                n.y = random.randint(10,300)
                dots.append(n)

        if d.y >790:
            game_over = True

def draw():
    screen.fill("black")
    screen.draw.text(str(score), (10,10),color = (255,255,255))
    player.draw()
    for d in dots:
        d.draw()
    if game_over == True:
        screen.fill("deepskyblue")

pgzrun.go()
```

## [DAY-209] if; lists

Make each falling object have a different speed

> her initial idea was to just change the falling object's y with a random number

```
def update():
    ...
    for d in dots:
         d.y += random.randint(1,5)
         ...
```

> second idea she had was to use the index of the thing as its speed (up to 4)

```
def update():
    ...
    i = 1
    for d in dots:
         d.y += 1
         i += 1
         if i > 4:
             i = 1
         ...
```

> her third idea was somehow to use a speed defined outside of the update() loop, but she couldnt implement it so I helped a bit

```
dots = [[Actor("rock"), 3],[Actor("flower"), 2]]

def update():
    ...
    for d in dots:
        d[0].y += d[1]
        if player.colliderect(d[0]):
            d[0].x = random.randint(50,700)
            d[0].y = random.randint(10,300)
            score += 1
            if score%5==0:
                n = Actor(random.choice(["rock", "flower"]))
                n.x = random.randint(50,700)
                n.y = random.randint(10,300)
                dots.append([n, random.choice([1,2,3])])
    ...

def draw():
    ....
    for d in dots:
        d[0].draw()
    ....
```

This pattern, keeping multiple objects close together in a small group is very important, try to practice it with other things, for example think about how you would add special powers to the falling things (slow down time, increase the player's size, increase player size and speed up time, etc)

## [DAY-210] if; lists

add 3 special items to the game

* gold: move all balls back to starting position and slow them down to maximum speed 2
* elf: reduce the amount of balls by one
* king: add 5 more balls

> thats what she wrote

```
...
gold = Actor("c3")
king = Actor("c2")
elf = Actor("c1")
elf.x = random.randint(50,700)
king.x = random.randint(50,700)
gold.x = random.randint(50,700)
...

def update()
   ...
    if gold.colliderect(player):
        for d in dots:
            d[0].y = 0
            d[1].speed = random.randint(1,2)
        gold.y = 0
        gold.x = random.randint(50,700)

    if elf.colliderect(player):
        if len(dots) > 0:
            dots.pop()
        elf.y = 0
        elf.x = random.randint(50,700)

    if king.colliderect(player):
        for i in range(5):
            n = Actor(random.choice(["rock", "flower"]))
            n.x = random.randint(50,700)
            n.y = random.randint(10,300)
            dots.append([n,random.randint(1,3)])
        king.y = 0
        king.x = random.randint(50,700)
   ...

def draw():
   ...

   elf.draw()
   king.draw()
   gold.draw()
```

## [DAY-211] classes

This is the same game but with small tweaks, to the elf increases the player size, and the king decreases it, also the player speed varies.

Just try to read the code, it is a bit convoluted and objects are calling other objects and it is a bit intimidating, but focus on the `fall()` method and follow how it is used, then check the player `move_left()` and `move_right()`

```
import pgzrun
import random

HEIGHT = 800
WIDTH = 600

class Player:
    def __init__(self, w, h):
        self.speed = 15
        self.w = w
        self.h = h
        self.x = 0
        self.y = HEIGHT - (h + 10)

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > WIDTH-10:
            self.x = WIDTH-10

    def hit(self, someActor):
        playerRect = Rect(self.x, self.y, self.w, self.h)
        return someActor.colliderect(playerRect)

    def draw(self):
        r = Rect(self.x, self.y, self.w, self.h)
        screen.draw.filled_rect(r, color="red")

class FallingThing:
    def __init__(self, image):
        self.thing = Actor(image)
        self.speed = random.choice([1,1,2,2,3])
        self.start_from_top()

    def start_from_top(self):
        self.thing.x = random.randint(50,WIDTH-50)
        self.thing.y = random.randint(10,HEIGHT/4)
        self.speed = random.choice([1,2,2,3])

    def hit(self, player, falling):
        if player.hit(self.thing):
            if self.thing.image == 'c1':
                player.w *= 2

            elif self.thing.image == 'c2':
                player.w /= 2

            elif self.thing.image == 'c3':
                for d in falling:
                    d.start_from_top()

            player.speed += random.choice([-3,3])
            if player.speed < 0:
                player.speed = 1

            falling.append(FallingThing(random.choice(["rock", "flower"])))

            self.start_from_top()
            return True
        else:
            return False

    def fall(self):
        self.thing.y += self.speed
        return self.thing.y

    def draw(self):
        self.thing.draw()

score = 0
player = Player(100, 50)
falling = [
    FallingThing("c1"),
    FallingThing("c2"),
    FallingThing("c3"),
    FallingThing(random.choice(["rock", "flower"])),
    FallingThing(random.choice(["rock", "flower"])),
    FallingThing(random.choice(["rock", "flower"])),
    FallingThing(random.choice(["rock", "flower"]))
]
game_over = False

def update():
    global game_over, score

    if game_over:
        return

    if keyboard.A:
        player.move_left()
    if keyboard.D:
        player.move_right()

    for f in falling:
        if f.hit(player, falling):
            score += 1

        if f.fall() > HEIGHT:
            game_over = True

def draw():
    screen.fill("black")

    player.draw()
    for f in falling:
        f.draw()

    if game_over == True:
        screen.fill("deepskyblue")

    screen.draw.text(str(score), (10,10),color = (255,255,255))

pgzrun.go()
```

This is a different way of writing programs, splitting things into pieces that talk to each other through messages(methods), and those pieces contain state which might or might not be modified when they receive a message, like the player.x or the thing.y. It seems like the program is simpler than the previous way you wrote, but that is not exactly true, now in order to follow what is going on you have to jump from object to object, while previously you were just able to read from top to bottom of the update() function and see what is going on.

There are new ways, and old ways of writing programs, but the truth is, large scale software programming is difficult and also very new, it is only 60 years old, we still dont know how to do it, we dont know how to teach it. There are people that come and preach: 'use only functions dont mutate state', 'use only objects with state', there are the other ones with 'always strongly encapsulate your state', or 'you should be able to follow the code so it should be just a bunch of procedures', 'decouple the logic', 'separate your concerns', 'first write a test for your program before you write the program', 'you should always program with a programming buddy as two people think better than one', use a plastic duck to help you'..

So, relax, in the end of the day the computer will execute some instructions and show few pixels on the screen. Have some fun.



## [DAY-212] PICO-8 Follow Adventure Game Tutorial

[PICO-8](https://www.lexaloffle.com/pico-8.php) is a fantasy console (virtual computer), it costs one time 15$ to buy it, and then you can play and modify all the games and have access to their source code. You can also write your own games.

For the next week we will follow [PICO-8 Top-Down Adventure Game Tutorial](https://www.youtube.com/watch?v=J1wvvbVQ5zo&list=PLdLmU93eWisKpyk1WZywUSYAq5dkCPFIv) from [Dylan Bennett](https://www.youtube.com/channel/UCY3KFjwFe1DyZYxhwHbm7Ew).

