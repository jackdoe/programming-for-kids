## [DAY-234] lists


Make a game where a bunch of enemies are moving in random direction.

> variable names are hers, and also the numbers for the movement
```
import pgzrun
import random
game_over=False
HEIGHT=800
king=Actor("c2")
king.y=300
WIDTH=800
HEIGHT=800
lon=[]
for i in range(10):
    elf=Actor("c1")
    elf.x=random.randint(10,790)
    elf.y=random.randint(10,790)
    lon.append(elf)

def update():
    global game_over
    if keyboard.W:
        king.y-=5
    if keyboard.S:
        king.y+=5
    if keyboard.A:
        king.x-=5
    if keyboard.D:
        king.x+=5


    for e in lon:
        if king.colliderect(e):
            game_over=True
        e.x+=random.choice([-1,+1,2,+3,-9,4,5,+3,7,12])
        e.y+=random.choice([+3,+3,+4,+4,+5,+7,+1,+2,+5,+13])

    if e.y>800:
        e.y=10
    if e.x>800:
        e.x=10

def draw():
    screen.fill('black')
    if game_over==True:
        screen.fill('pink')
        
    king.draw()

    for e in lon:
        e.draw()

pgzrun.go()
```

## [DAY-235] lists

Make the previous game into jumpscare game, when enemy hits you show scary image and play scary soubd.

```
...
corgi = Actor("narutoz")
maxx=Actor("gaaras")
...
def draw():
    ...
    if game_over==True:
        screen.fill('pink')
        scary = random.choice([corgi,maxx])
        scary.draw()
        sounds.retro.play()
...
```

## [DAY-236] modules

Make one file `util.py`

```
import random
def sum(a,b,c):
    return a + b + c
    
def choice(a,b):
    if random.randint(0,1) == 1:
        return a:
    else:
        return b
```


Now make another file in the same directory:

```
import util

x = util.choice(6,7)
y = util.choice(2,4)
z = util.choice(8,9)

s = util.sum(x,y,z)

print(s)
```

We have created a "module", which is just a bunch of code grouped together that we can access.

From now on we will keep growing our `util` module with handy functions that we can use in other programs.

## [DAY-237] files

Watch [Python Tutorial: File Objects - Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM), and also try it out in your editor.


## [DAY-238] principles

The two most important concepts you have to learn are `file` and `process`, a file is a piece of data, could be text, could be machine code, could be an image, and a `process` is a running program.

At the moment you use google docs to write your school projects, and Steam or Epic to start your games, the Apple App Store or Microsoft Store to install Minecraft.. Everything is like magic, things somehow work if you press the right button and sometimes they dont work and nobody knows why. I have a different relationship with the computer, I dont use the mouse as much, and use commands to tell it what to do, from searching for files to editting them or saving them or copying them to another machine. If I need to do something I either make a program to do it or use a program that I already know, I join the output of one program into the input of another. I know which processees are running and how to stop them, which one takes more resources or is causing problems. And it has been like that since I started using computers. There is no magic, its just files and processees.


For the next weeks we will move to using the command line more and more. Using command line editors such as `nano` and commands such as `mkdir`, `ls`, `grep` and `find` to navigate make directories, list their contents, search for patterns in files and find specific files. Using `date` to see the current time and `cal` to see the calendar, `cp` to copy a file and `mv` to rename it or `cat` to show its contents.

It might seem like artificial change, from using graphical interfaces to terminal intefaces, but I think it is in the core of how you interact with the machine. How do you express your thoughts and tell it what to do.

Tomorrow we will skim through [UNIX Programming Enviornment](https://archive.org/details/UnixProgrammingEnviornment/) book from 1984, by the legends Brian W. Kernigan and Rob Pike.
