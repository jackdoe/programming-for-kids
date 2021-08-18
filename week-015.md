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
    
    return int(len(times) / ((times[-1] - times[0]) / 60.0))
    
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
    w = random.choice(common)
    words.append([random.randint(10,WIDTH-(len(w) * 15)), random.randint(10,int(HEIGHT/3)), w])

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

clock.schedule_interval(add_word, 5)
clock.schedule_interval(move, 5)
pgzrun.go()
```


get more words with the characters you need to train from your dictionary file

use a simple program like this:

```
import sys
need = ['k','l','i','o']
for line in sys.stdin:
    missing = False
    s = line.rstrip()

    for n in need:
        if n not in s:
            missing = True
    
    if not missing and len(s) <= 7:
print(s)
```

and then get the list:

```
cat /usr/share/dict/words | python3 words.py | tr "[A-Z]" "[a-z]" | sort | uniq | sed -e "s/^/'/g" -e "s/$/',/g" | pbcopy
```
## [DAY-103] Basics of Basics

Search all the books!

First download https://www.gutenberg.org/cache/epub/feeds/pg_catalog.csv.zip, this is a list of all the books available from the gutenberg project.

Oh! the gutenberg project is absolutely amazing, they have more than 60000 books that have expired copyright.

```
import csv
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--author', help='match author name')
parser.add_argument('--title', help='match title')
parser.add_argument('--subject', help='match subject')
args = parser.parse_args()

def show(id, title, authors, subjects, issued, language):
    print(">>> " + title + " <<<")
    print("    " + issued)
    print("    https://www.gutenberg.org/ebooks/" + id)

    print('')
    for a in authors:
        print("    Author: " + a)
    print('')
    for s in subjects:
        print("    Subject: " + s)
    print("    Language: " + language)
    print("-" * 40)

file = open('pg_catalog.csv')
reader = csv.reader(file)
for row in reader:
    # ['Text#', 'Type', 'Issued', 'Title', 'Language', 'Authors', 'Subjects', 'LoCC', 'Bookshelves']
    id = row[0]
    if id == "Text#":
        # skip the first row (header)
        continue

    issued = row[2]
    title = row[3].replace("\n","; ")
    language = row[4]
    authors = row[5].split("; ")
    subjects = row[6].split("; ")

    match = 0
    need = 0
    if args.title != None:
        need += 1
        if args.title in title:
            match += 1

    if args.subject != None:
        need += 1
        for s in subjects:
            if args.subject in s:
                match += 1
                break

    if args.author != None:
        need += 1
        for a in authors:
            if args.author in a:
                match += 1
                break

    if match == need:
        show(id,title,authors,subjects,issued,language)
        
file.close()
```

now try this:

```
python3 search.py --title Alice  --author Carroll | less
```


## [DAY-104] Basics of Basics
## [DAY-105] Basics of Basics
## [DAY-106] Basics of Basics
## [DAY-107] Basics of Basics
## [DAY-108] Basics of Basics
