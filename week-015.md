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

CSV stands for comma separated value, its a neat way to encode a table, each column is separated by a `,`. Python has csv module in its standard library, and its very easy to load and parse csv files.


## [DAY-104] Basics of Basics

The previous approach can match only with substrings, for example we can not match "Lewis Carroll", because the author name is stored "Carroll, Lewis", in fact we can not even match on "Carroll Lewis" because we will be missing a comma.

Another way to search is if we actually split the strings, and then create an index of which word is contained in which books, very similar to whe you open the back of a book, you see a word(or a topic) and then pages at which it appears.

First just copy paste the program, and try to read it, we will go over it step by step later.

```
import sys
import re
import json

def show(book):
    id = book["id"]
    title = book["title"]
    authors = book["authors"]
    subjects = book["subjects"]
    issued = book["issued"]
    language = book["language"]

    print(">>> " + title + " <<<")
    print("    " + issued)
    print("    https://www.gutenberg.org/ebooks/" + str(id))

    print('')
    for a in authors:
        print("    Author: " + a)
    print('')
    for s in subjects:
        print("    Subject: " + s)
    print("    Language: " + language)
    print("-" * 40)

def parse(filename):
    file = open(filename)
    reader = csv.reader(file)
    books = []
    for row in reader:
        # ['Text#', 'Type', 'Issued', 'Title', 'Language', 'Authors', 'Subjects', 'LoCC', 'Bookshelves']
        if row[0] == "Text#":
        # skip the first row (header)
            continue

        id = int(row[0])
        issued = row[2]
        title = row[3].replace("\n","; ")
        language = row[4]
        authors = row[5].split("; ")
        subjects = row[6].split("; ")

        book = {
            "title": title,
            "language": language,
            "authors": authors,
            "subjects": subjects,
            "issued": issued,
            "id": id
        }
        books.append(book)

    file.close()
    return books


def normalize(s):
    # 'Alice's Adventures in Wonderland' -> 'alice's adventures in wonderland'
    return s.lower()

def tokenize(s):
    # 'alice's adventures in wonderland' -> ['alice','s','adventures','in','wonderland']
    return re.split("[^\w+]",s)

def build_search_index(books):
    index = {}

    for i,book in enumerate(books):
        tokens = set()
        for token in tokenize(normalize(book["title"])):
            k = "title:" + token
            tokens.add(k)

        for token in tokenize(normalize(book["language"])):
            k = "language:" + token
            tokens.add(k)

        for author in book["authors"]:
            for token in tokenize(normalize(author)):
                k = "author:" + token
                tokens.add(k)


        for subject in book["subjects"]:
            for token in tokenize(normalize(subject)):
                k = "subject:" + token
                tokens.add(k)

        for t in tokens:
            if not t in index:
                index[t] = []
            index[t].append(i)

    return index

def search(books, index, query):
    matching = None
    for q in query:
        if q in index:
            if matching == None:
                matching = set(index[q])
            else:
                matching.intersection_update(index[q])
        else:
            matching = set() # if one of the terms is not matching, return empty

    result = []
    if matching == None:
        return result

    for book_index in matching:
        book = books[book_index]
        result.append(book)
    return result

if len(sys.argv) == 1:
    print("usage:\n\t" + sys.argv[0] + " title:alice author:lewis")
    sys.exit(1)

data = None

try:
    f = open("search.json", mode="r")
    data = json.load(f)
    f.close()
except IOError:
    books = parse("pg_catalog.csv")
    search_index = build_search_index(books)

    data = {}
    data["search"] = search_index
    data["books"] = books

    f = open("search.json", mode="w")
    json.dump(data,f)
    f.close()

query = []
for arg in sys.argv[1:]:
    query.append(normalize(arg))

for book in search(data["books"], data["search"], query):
    show(book)
```


lets try it:

```
% python3 search.py title:Alice author:carroll author:lewis subject:children
>>> Alice's Adventures in Wonderland <<<
    2008-06-27
    https://www.gutenberg.org/ebooks/11

    Author: Carroll, Lewis, 1832-1898

    Subject: Fantasy fiction
    Subject: Children's stories
    Subject: Imaginary places -- Juvenile fiction
    Subject: Alice (Fictitious character from Carroll) -- Juvenile fiction
    Language: en

...
```

The first time you search it will be slower, but then we will persist the search index on disk, in the search.json file, and then the second time it will be significantly faster because we will not have to do the work of parsing and building the index again, but directly load the precomputed index.

So many new concepts here, but the biggest one are maps and sets.

A map is a data structure (list is a data structure as well), that allows you to find something by a key you store it with.

```
episodes = {}

episodes["naruto"] = 220
episodes["naruto shippuuden"] = 500
episodes["boruto"] = 215

print(episodes)
print(episodes["naruto"])

if "naruto" in episodes:
    print("naruto is in the map")

for k in episodes:
    print(k)

for k in episodes:
    print(k, episodes[k])
```

A set is a just a bag of things, for example when you put your toys in a bag, the bag is a set containing your toys. Lets make a set of flowers.

```
flowers = set()
flowers.add("rose")
flowers.add("camomile")
flowers.add("tulip")

if "tulip" in flowers:
    print("tulip is in the set")

for f in flowers:
    print(f)
```

You can `union` two sets of yoys by placing them into a new bag and this will contain both sets of toys, or you can `intersect` them by only taking toys that exist in both bags.

Both maps and sets are somewhat related, imagine a map that only contains keys.

This is very very shallow explanation, but will do for now, we will spend the next 3-4 months with sets and maps things will get clearer.

## [DAY-105] Basics of Basics

make the simple flower/rock drawing game by yourself

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300 
WIDTH = 300

elf = Actor("c1")
flowers = []
def update():
    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.F:
        flower = Actor("flower")
        flower.x = elf.x
        flower.y = elf.y
        flowers.append(flower)
    if keyboard.R:
        flower = Actor("rock")
        flower.x = elf.x
        flower.y = elf.y
        flowers.append(flower)
    if keyboard.Q:
        sys.exit(0)

    if elf.x < 0:
        elf.x = 10
    if elf.y < 0:
        elf.y = 10
    if elf.x > WIDTH:
        elf.x = WIDTH - 10
    if elf.y > HEIGHT:
        elf.y = HEIGHT - 10

def draw():
    screen.fill('black')
    elf.draw()
    for flower in flowers:
        flower.draw()
pgzrun.go()
```

## [DAY-106] Basics of Basics

Have some fun drawing, add more colors, change the size, enjoy!

![game-106.png](./screenshots/game-106.png "game 106 screenshot")


```
import pgzrun
import sys # for sys.exit()


HEIGHT = 800
WIDTH = 1000

elf = Actor("c1")
colors = [
    [(255,0,0), Rect(0,0,40,40)],
    [(0,255,0), Rect(60,0,40,40)],
    [(0,0,255), Rect(120,0,40,40)],
    [(0,128,128), Rect(180,0,40,40)],
    [(0,191,255), Rect(240,0,40,40)],
    [(255,215,0), Rect(300,0,40,40)],
]
color = None
pixels = []

size = 40

def make_rect_around_actor(a):
    return Rect(a.x,a.y,size,size)
def update():
    global color, pixels,size

    if keyboard.LEFT:
        elf.x -= 2
    if keyboard.RIGHT:
        elf.x += 2
    if keyboard.UP:
        elf.y -= 2
    if keyboard.DOWN:
        elf.y += 2

    if keyboard.MINUS:
        size -= 1
        if size < 1:
            size = 1
    if keyboard.EQUALS:
        size += 1
        
    if keyboard.Q:
        sys.exit(0)

    if keyboard.SPACE and color != None:
        pixels.append([
            color,
            make_rect_around_actor(elf),
        ])

    if keyboard.C:
        pixels = []
        color = None

    if keyboard.S:
        f = open("save.txt", "w")
        for p in pixels:
            (red,green,blue) = p[0]
            f.write(str(red))
            f.write(",")
            f.write(str(green))
            f.write(",")
            f.write(str(blue))
            f.write(",")
            f.write(str(p[1].x))
            f.write(",")
            f.write(str(p[1].y))
            f.write(",")
            f.write(str(p[1].width))
            f.write(",")
            f.write(str(p[1].height))
            f.write("\n")
        f.close()

    if keyboard.L:
        pixels = []

        f = open("save.txt", "r")

        lines = f.readlines()
        for l in lines:
            (red,green,blue,x,y,w,h) = l.split(",")
            pixels.append([
                (float(red),float(green),float(blue)),
                Rect(float(x),float(y), float(w), float(h))
            ])

        f.close()
    if keyboard.k_1:
        color = colors[0][0]
    if keyboard.k_2:
        color = colors[1][0]
    if keyboard.k_3:
        color = colors[2][0]
    if keyboard.k_4:
        color = colors[3][0]
    if keyboard.k_5:
        color = colors[4][0]
    if keyboard.k_6:
        color = colors[5][0]
               
    if keyboard.D:
        drop = make_rect_around_actor(elf)
        for p in list(pixels):
            if drop.colliderect(p[1]):
                pixels.remove(p)

    for c in colors:
        if elf.colliderect(c[1]):
            color = c[0]

def draw():
    screen.fill('black')

    for c in colors:
        screen.draw.filled_rect(c[1], c[0])

    for p in pixels:
        screen.draw.filled_rect(p[1], p[0])

    if color != None:
        screen.draw.rect(make_rect_around_actor(elf), color)

    elf.draw()
    screen.draw.text(str(len(pixels)), topleft=(10,10))

pgzrun.go()
```
## [DAY-107] Basics of Basics

count the words in a file

```
f = open("week-015.md","r")
count = []

for line in f.readlines():
    for word in line.rstrip().split(" "):
        found = False
        for counted in count:
            if counted[0] == word:
                counted[1]+= 1
                found = True
                break
        if not found:
            count.append([word, 1])

f.close()

print(count)
```

use a dictionary

```
f = open("week-015.md","r")
count = {}

for line in f.readlines():
    for word in line.rstrip().split(" "):
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

f.close()

for k in count:
    print(count[k], k)
```

get the unique words in a file

```

f = open("week-015.md","r")
unique = set()

for line in f.readlines():
    for word in line.rstrip().split(" "):
        unique.add(word)

f.close()

print(unique)

```

lets read the file 1 byte at a time:

```
f = open("week-015.md","r")
word = ''
count = {}
while True:
    byte = f.read(1)
    if not byte:
        break
    if byte == ' ' or byte == '\n':
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
        word = ''
    else:
        word += byte
f.close()

for k in count:
    print(count[k], k)
```

use sys.stdin to read the standard input

```
import sys
count = {}

for line in sys.stdin.readlines():
    for word in line.rstrip().split(" "):
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

for k in count:
    print(count[k], k)
```
then try use the output of `cat` to print the contents of week-015.md and then `|` pipe it to your word counting program

```
$ cat week-015.md | python3 count.py
```

if you want to sort by most common words:

```
cat week-015.md | python3 count.py | sort -n
```

## [DAY-108] Basics of Basics
