## [DAY-227] lists

Make a touch typing game, have a list of words, pick 4 random words and wait for the player to type them, if they did it correctly, pick another 4 words, otherwise use the old words.

How it should look:

```
hello this is random
> hello this is randon
INCORRECT
hello this is random
> hello this is random
CORRECT
apple orange is amazing
> ...
```

> This is the game she wrote, I had to help with the `join`, and spent some time explaining it.

```
import random
words = ['a', 'about', 'all', 'also', 'and', 'as', 'at', 'be',
         'because', 'but', 'by', 'can', 'come', 'could', 'day',
         'do', 'even', 'find', 'first', 'for', 'from', 'get',
         'give', 'go', 'have', 'he', 'her', 'here', 'him', 'his',
         'how', 'i', 'if', 'in', 'into', 'it', 'its', 'just',
         'know', 'like', 'look', 'make', 'man', 'many', 'me',
         'more', 'my', 'new', 'no', 'not', 'now', 'of', 'on',
         'one', 'only', 'or', 'other', 'our', 'out', 'people',
         'say', 'see', 'she', 'so', 'some', 'take', 'tell',
         'than', 'that', 'the', 'their', 'them', 'then', 'there',
         'these', 'they', 'thing', 'think', 'this', 'those',
         'time', 'to', 'two', 'up', 'use', 'very', 'want', 'way',
         'we', 'well', 'what', 'when', 'which', 'who', 'will',
         'with', 'would', 'year', 'you', 'your',
         'paper', 'game', 'remember', 'person', 'english', 'dutch',
         'amsterdam', 'nothing', 'sleep', 'product', 'natural',
         'juice', 'orange', 'blue', 'green', 'together', 'friends',
         'between', 'music', 'book', 'bookstore', 'fish', 'complete',
         'width', 'weight', 'height', 'length', 'string', 'python',
         'unicode', 'backspace', 'random', 'choice', 'string', 'integer',
         'function', 'print', 'print', 'print', 'for', 'range', 'range',
         ]

def select_words(n):
    picked = []
    for i in range(n):
        word = random.choice(words)
        picked.append(word)
    return " ".join(picked)

scr=4
a = select_words(scr)
while True:
    print(a)

    s = input('> ')
    if s != a:
        print("INCORRECT") 
    else:
        print("CORRECT")
        a = select_words(scr)
        scr+=1
```


## [DAY-228] files

Google for the top 10000 most common words in the english language, and paste them into a file 'words.txt'. Then google: `how to read file in python`, and go to some of the `stackoverflow` links.

> This is what she wrote after pasting from stackoverflow:

```
import random
f = open('words.txt') # Open file on read mode
words = f.read().splitlines() # List with stripped line-breaks
f.close() # Close file

def select_words(n):
    picked = []
    for i in range(n):
        word = random.choice(words)
        picked.append(word)
    return " ".join(picked)

scr=4
a = select_words(scr)
while True:
    print(a)

    s = input('> ')
    if s != a:
        print("INCORRECT") 
    else:
        print("CORRECT")
        a = select_words(scr)
        scr+=1
```

Spend some time on chaining methods `f.read()` returns a string, then calling `.splitlines()` on the string returns a list of strings.
