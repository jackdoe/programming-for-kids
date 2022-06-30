## [DAY-213] PICO-8 Adventure Game

> Following the guide she made the game, I used the time to specifically talk about tables and she particularly had an issue with if() looking like a function. I tried to give her more space and time to follow the tutorial on her own.

![game-213-a.png](./screenshots/game-213-a.png "game 213 a screenshot")
![game-213-b.png](./screenshots/game-213-b.png "game 213 b screenshot")


## [DAY-214] PICO-8 Follow Platformer Game Tutorial

In the next week follow the [Platformer Tutorial](https://www.youtube.com/playlist?list=PLyhkEEoUjSQtUiSOu-N4BIrHBFtLNjkyE) from [Nerdy Teachers](https://www.youtube.com/channel/UCbMjF_cWciuBUZjILNL1fyA).

Do not code while watching the video, first watch the video once, and then second time to code with the teacher.

## [DAY-215] make a website

Ask your parents to buy a domain name for you, and buy a domain and some VPS hosting, ask your parent to set it up and install a web server there, buy a domain and point it to the hosting (they know what to do.

ssh into the computer and start editing the index.html file:

```
# cd /var
# cd www
# cd html
# nano index.html

```

write `<h1>Hello</h1>` in the editor and then hit CTRL+S to save it, and then open your website through your browser and phone

> FIXME: we actually spent few days on this just talking about IP addressess, DNS, ssh and etc, but I forgot to write it down

## [DAY-216] directories

Imagine we had all the files on our computer in one place. You will have all the things you use, apps, games, documents, pictures, all in one giant blob of files.

![game-216.png](./screenshots/game-216.png "game 216 screenshot")

Even worse, imagine having only one file with all the stuff in it, one picture ends another begins, one app ends another begins, it is quite useless if you think about it like that, so just having different files for different things is already helpful for organizing your information, but adding directories which allow you to group a bunch of files together, changes the game. Having directories which can contain files or other directories allows you to organize everything to a very fine level.

BTW, there are operating systems that actually speciallize in browsing files in a different way e.g. the [Canon Cat computer](https://www.youtube.com/watch?v=jErqdRE5zpQ)

Lets say we have directory named Games, and inside we have two games, Fortnite and Minecraft, and in each of them we have some files (sound files and the game programs themselves)

```
                        Games
                      /       \
                    /           \
            minecraft            Fortnite
            /    |               /  |   \
           /     |              /    \    \
         sound  minecraft.exe  sound      fortnite.exe
          /                     |       
      zombie.mp3             falling.mp3 
      rain.mp3               song.mp3

```

You can imagine there is a path to get to song.mp3, its Games -> Fortnite -> sound -> song.mp3, you can imagine a small gnome starting from the top (the Games diretory) and going down, and on each crossroad it has to pick.

In linux (the operating system which is used by your web server) the directory we use `/` (slash) to be able to say where are we going, e.g. /Games/Fortnite/sound/song.mp3 will be how we can access the file directly, `/` is the beginning of the path or this is the "root" directory, which is a bit confusing because in linux there is also `/root` which is the `home` directory for the `root` user (the system administrator), but we call `/` the root of the file system.

Using the `cd` command allows us to move our gnome to specific part of the tree. so if we say `cd /Games` now our gnome will be in the Games directory, and from here we can access song.mp3 by just doing `Fortnite/sound/song.mp3`.


## [DAY-217] directories

> We spent the next week or so every day making few changes to the website, doing links and uploading files with `scp`, I did not document the process, but it was mainly teaching directory navigation with `cd` and `ls` and editting with `nano`. We also did few small python programs with nano just to get used to starting programs on a remote machine. It was especially interesting when there was laggy internet and you type something and it takes a while to show on screen, the realization that your editor is running on another computer was very powerful, so I suggest you simmulate the slow internet environment if you can.


## [DAY-218] variables

![game-218.png](./screenshots/game-218.png "game 218 screenshot")

Today we make the simplest game of a flling elf, make it fall and then bounce up when it reaches the end

> thats the game that she wrote, I had to help a bit with the speed_y = -5, first she just made it reset to the top, so the elf was going in circles, but after that she made it to go up when it reaches the end.

```
import pgzrun

elf = Actor("c1")
elf.y = 50

WIDTH = 800
HEIGHT = 800
speed_y = 5


def update():
    global speed_y

    elf.y += speed_y

    if elf.y > 795:
        speed_y = -5
    if elf.y < 50:
        speed_y = 5

    if keyboard.A:
        elf.x += -5

    if keyboard.D:
        elf.x += 5


def draw():
    screen.fill("black")
    elf.draw()


pgzrun.go()
```

## [DAY-219] lists

![game-219.png](./screenshots/game-219.png "game 219 screenshot")

Improve the game to have an row of monsters that you have to avoid, also make the elf bounce left and right as well. It should be gameover if you collide with any of the monsters

> this is the game she made, she did some experimentation with random, and needed a bit of help with the list of monsters

```
import pgzrun

elf = Actor("c1")
elf.y = 50

WIDTH = 800
HEIGHT = 800
game_over = False
speed_y = 5
speed_x = 5
monsters = []
monster_speed_y = 1

for i in range(20):
    monster = Actor("c1")
    monster.x = 10 + (i * 70)
    monster.y = 10
    monsters.append(monster)


def update():
    global speed_y, speed_x, game_over

    elf.y += speed_y
    elf.x += speed_x

    if elf.y > 795:
        speed_y = -5
    if elf.y < 50:
        speed_y = 5
    if elf.x > 795:
        speed_x = -5
    if elf.x < 50:
        speed_x = 5

    if keyboard.A:
        elf.x += -5

    if keyboard.D:
        elf.x += 5

    for m in monsters:
        m.y += monster_speed_y
        if m.y > 795:
            m.y = 10
        if m.colliderect(elf):
            game_over = True


def draw():
    screen.fill("black")
    elf.draw()

    for m in monsters:
        m.draw()
    if game_over == True:
        screen.fill("pink")


pgzrun.go()
```


## [DAY-219] lists

![game-219.png](./screenshots/game-219.png "game 219 screenshot")

Improve the game to have an row of monsters that you have to avoid, also make the elf bounce left and right as well. It should be gameover if you collide with any of the monsters

> this is the game she made, she did some experimentation with random, and needed a bit of help with the list of monsters

```
import pgzrun

elf = Actor("c1")
elf.y = 50

WIDTH = 800
HEIGHT = 800
game_over = False
speed_y = 5
speed_x = 5
monsters = []
monster_speed_y = 1

for i in range(20):
    monster = Actor("c1")
    monster.x = 10 + (i * 70)
    monster.y = 10
    monsters.append(monster)


def update():
    global speed_y, speed_x, game_over

    elf.y += speed_y
    elf.x += speed_x

    if elf.y > 795:
        speed_y = -5
    if elf.y < 50:
        speed_y = 5
    if elf.x > 795:
        speed_x = -5
    if elf.x < 50:
        speed_x = 5

    if keyboard.A:
        elf.x += -5

    if keyboard.D:
        elf.x += 5

    for m in monsters:
        m.y += monster_speed_y
        if m.y > 795:
            m.y = 10
        if m.colliderect(elf):
            game_over = True


def draw():
    screen.fill("black")
    elf.draw()

    for m in monsters:
        m.draw()
    if game_over == True:
        screen.fill("pink")


pgzrun.go()
```


## [DAY-220] lists

Make the elf be able to attack the monsters with a bullet.

```
...
bull =  Actor("bullet")
bull.x = -10 
bull.y = -19
bullet_speed=1
...

def update():
    ...
    if keyboard.SPACE:
        bull.x = elf.x + 10
    bull.x += 1
    ...
    for m in list(monsters):
        ...
        if m.colliderect(bull):
            monsters.remove(m)

def draw():
    ...
    bull.draw()
```

The key topic for discussion here is having bullet outside of the screen, and moving it in screen when the player hits SPACE.

And of course discussing removing from shallow clone of the list, which we have discussed many times so far, but it is still good to think about it.

```
a = [1,2,3]
b = list(a)
a.append(4)
print(a)
print(b)

c = a
c.append(5)
print(a)
print(b)
print(c)
```


## [DAY-221] lists


Make a boss that spawns after 20 mosters are defeated.

```
...
boss = Actor("c2")
boss.x = -200
boss.y = -200
counter = 0
...
def update():
    global counter
    ...
    for m in list(monsters):
        ...
        if m.colliderect(bull):
            monsters.remove(m)
            counter++
            if counter > 20:
                boss.x = 400
                boss.y = 400



def draw():
    ...
    boss.draw()
```

Using the same pattern as the player's bullet, we draw the boss off-screen, we keep a counter of how many monsters are killed and once we kill more than 20, we move the boss in the middle of the screen.
