## [DAY-319] lists

Given that the update() function is called by pygame zero 60 times per second (so your game can have 60fps), make a "game" that adds a new actor every 1 second.


> this is what she wrote

```
import pgzrun
import random
HEIGHT = 500
WIDTH = 500

actors=[]
counter = 0

def update():
    global counter
    counter += 1
    if counter > 60:
        act = Actor("c1")
        act.y = random.randint(0,HEIGHT)
        act.x = random.randint(0,WIDTH)
        actors.append(act)
        counter = 0
    
def draw():
    screen.clear()
    for actor in actors:
        actor.draw()
    
pgzrun.go()

```


## [DAY-320] files

Write the fizzbuzz output to a file instead of the standard output


> this is what she wrote

```
f = open("zzz.txt","w")

for i in range(100):
    if i % 15 == 0:
        f.write("fizzbuzz\n")
    elif i % 3 == 0:
        f.write("fizz\n")
    elif i % 5 == 0:
        f.write("buzz\n")
    else:
        a = str(i)
        f.write(a + "\n")

f.close()
```
