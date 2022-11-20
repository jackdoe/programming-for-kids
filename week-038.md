

## [DAY-260] strings

Write (in notepad), run (from cmd) and explain(on paper) the following code:
```
def encrypt(s):
    r = ''

    for character in s:
        ascii = ord(character)
        r += 'z' * ascii
        r += ' '

    return r


def decrypt(s):
    r = ''
    ascii = 0

    for character in s:
        if character == 'z':
            ascii += 1
        else:
            r += chr(ascii)
            ascii = 0

    return r

        

encrypted = encrypt('hello world')
print(encrypted)
print(decrypt(encrypted))
```

![game-260.jpg](./screenshots/game-260.jpg "game 260 screenshot")


> walk through the code, explaining each line, and trying it with sample values


## [DAY-261] lists

Find and fix the bug in the following program:

```
# [2,2,2,2,2,2,2,2,3] should become [8, 2, 1, 3]
def rle(x):
  r = []
  for v in x:
    if len(r) == 0 or r[-1] != v:
      r.append(0)
      r.append(v)
    if v == r[-1]:
      r[-2] += 1
  return r

# [8, 2, 1, 3] should become [2,2,2,2,2,2,2,2,3]
def rld(x):
  r = []

  for i in range(0, len(x), 2):
    for k in range(x[i]):
      r.append(x[i+1])

  return r


a = rle([1,1,1,1,1,1,1])
print(a)
b = rld(a)
print(b)
```

> Spend some time stepping through or print debugging, I chose to use print debugging to emphasize on "what should this code do, and how do you make sure it does what it says", but I think proper debugging can be introduced at this point, in the same time I dont want to introduce new concepts yet. Learning programming takes time, you can not rush it.


## [DAY-262] lists

Find and fix the bug in the following program (using only notepad and cmd):

```
def avg(x):
    n = 0
    sum = 0
    for i in range(1, len(x)):
        sum += x[i]
        n += 1

    return sum / n


print(avg([7,3,5]))
```


## [DAY-263] lists

find the bug in the following code (using notepad and cmd):


```
def uniq(data):
    result = []
    for inputNumber in data:
        seen = False
        for resultNumber in result:
            if inputNumber != resultNumber:
                seen = True
        if not seen:
            result.append(inputNumber)

    return result

# should print [1,2,3]
print(uniq([1, 2, 1, 1, 1, 3, 1]))
```


## [DAY-264] design

Today we will do a basic design and 3d print it, first make an account on https://www.tinkercad.com/ and then build something there (use W to attach workarea to a surface so you can easilly put one thing on top or on the side of another). 

Grab a masuring tool and get any object that you see and measure it and build it inside tinkercad.

> She did some great designs, but they are somewhat personal and I wont show them in the book. Also she was the one who found out about the W key doing temporary workarea, which makes the whole tinkercad propgram 10000 times better, and before this I was doing designs super slow and was very annoyed :)
