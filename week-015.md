# Chapter 14 - Week 14

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of Basics
day4: Basics of Basics
day5: Basics of Basics
day6: Basics of Basics
```

## [DAY-102] Basics of Basics
Whole day touch typing!

Modify the program to print some score and words per minute, and try to imptove your score.

```
import pgzrun
import random
import time

HEIGHT = 800
WIDTH = 600

words = []
text = ''
game_over = False
beep = tone.create('A3', 0.5)
pause = False
score = 0
times = []
def words_per_minute():
    if len(times) < 2:
        return 0
    
    return int((times[-1] - times[0]) / len(times) * 60)
    
def move():
    global game_over
    if pause:
        return
    for w in words:
        w[1]+= random.randint(10,15)
        if w[1] > HEIGHT:
            game_over = True

def add_word():
    if pause:
        return
    common = ['a','about','all','also','and','as','at','be','because','but','by','can','come','could','day',
              'do','even','find','first','for','from','get','give','go','have','he','her','here','him','his',
              'how','i','if','in','into','it','its','just','know','like','look','make','man','many','me',
              'more','my','new','no','not','now','of','on','one','only','or','other','our','out','people',
              'say','see','she','so','some','take','tell','than','that','the','their','them','then','there',
              'these','they','thing','think','this','those','time','to','two','up','use','very','want','way',
              'we','well','what','when','which','who','will','with','would','year','you','your',
              'paper','game','remember','person','english','dutch','amsterdam','nothing','sleep','product','natural',
              'juice','orange','blue','green','together','friends','between','music','book','bookstore','fish','complete',
              'width','weight','height','length','string','python','unicode','backspace','random','choice','string','integer',
              'function','print','print','print','for','range','range',
    ]
    words.append([random.randint(10,WIDTH-70), random.randint(10,int(HEIGHT/3)), random.choice(common)])

def on_key_down(key, mod, unicode):
    global text, pause, score_words, score
    if key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:-1]
    elif key == keys.SPACE:
        pause = not pause
    elif len(unicode) > 0 and ord(unicode) >= 65 and ord(unicode) <= 125:
        text += unicode
        for w in list(words):
            if w[2] == text:
                score += 1
                words.remove(w)
                if len(words) < 4:
                    add_word()

                text = ''
                beep.play()

                times.append(time.time())


def draw():
    if game_over:
        screen.fill('pink')
    elif pause:
        screen.fill('magenta')
    else:
        screen.fill('black')

        screen.draw.text("score: " + str(score) + " wpm: " + str(words_per_minute()), (10,10), color=(0,255,0), fontsize=15,fontname="437-win")

        for w in words:
            screen.draw.text(w[2], (w[0],w[1]), fontsize=20,fontname="437-win")

        screen.draw.text(text, (WIDTH/2,HEIGHT - 40), color=(255,0,0), fontsize=40,fontname="437-win")

for i in range(5):
    add_word()

clock.schedule_interval(add_word, 2)
clock.schedule_interval(move, 1)
pgzrun.go()
```


## [DAY-103] Basics of Basics
## [DAY-104] Basics of Basics
## [DAY-105] Basics of Basics
## [DAY-106] Basics of Basics
## [DAY-107] Basics of Basics
## [DAY-108] Basics of Basics