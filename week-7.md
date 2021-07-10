# Chapter 7 - Week 7

```
day0: Basics of Basics
day1: Basics of Basics
day2: Basics of Basics
day3: Basics of the Internet
day4: Basics of the Internet
day5: Basics of Basics
day6: Basics of Basics
```


## [DAY-48] Basics of Basics

How big can a string be?

Your computer has limited amount of memory, usually 8 gigabytes, that is a lot of memory. 8 * 1024 megabytes * 1024 kilobytes * 1024 bytes, so 8589934592 bytes. What if we make python create a string with more characters than memory?

NB: before you try that, save all your files because you might have to restart your computer, depending on the operation system version.

```
try_me = 'x' * (8 * 1024 * 1024 * 1024)
print(len(try_me))
```

If you can not press any buttons after that, or the mouse is not working, you will have to hold the power button for 10 seconds to turn your computer off and then turn it back on.

lets try another thing

```
def forever(n):
  print(n)
  forever(n+1)

forever(1)
```

this will throw a weird error

```
RecursionError: maximum recursion depth exceeded while pickling an object
```

Don't be afraid of it, every time you call a function, a little bit of memory has to be used, and this memory is released when the function returns, now imagine a function that calls itself, so you get this:

```
forever(1)
  forever(1+1)
    forever(1+1+1)
      forever(....)
```


So the memory for those function is never released, and this error just says, you cant go and call so many functions that never return. But you will see on your system you can have around 10000 functions that are waiting for their child to return.

Play with it a bit.

```
def one(n):
  print("one", n)
  two(n+1)

def two(n):
  print("two", n)
  one(n+1)

one(1)

```
## [DAY-49] Basics of Basics

```
import random
game = [
    ['What is the capital of France?','Paris','London','Paris','Berlin','Tokyo'],
    ['What is the capital of Japan?','Tokyo','London','Paris','Berlin','Tokyo'],
    ["What is Jane's favorite food?",'Popcorn','Pizza','Popcorn','Cucumber','Sushi']
]


while True:
    quiz = random.choice(game)
    print(quiz[0])
    for index, possible in enumerate(quiz):
        if index >= 2:
            print(possible)
    answer = input('What is your answer: ')

    if answer == quiz[1]:
        print("✨✨✨ CORRECT ✨✨✨")
    else:
        print("INCORRECT")
```

see `enumerate` is quite handy, you get the index of something and its value while you are doing the `for`

```
x = ['a','b','c','d']
for index ,element in enumerate(x):
  print(index)
  print('  ' + element)
```


make it easier to read:

```
import random
QUESTION_IDX = 0
ANSWER_IDX = 1
game = [
    ['What is the capital of France?','Paris','London','Paris','Berlin','Tokyo'],
    ['What is the capital of Japan?','Tokyo','London','Paris','Berlin','Tokyo'],
    ["What is Jane's favorite food?",'Popcorn','Pizza','Popcorn','Cucumber','Sushi']
]


while True:
    quiz = random.choice(game)
    print(quiz[QUESTION_IDX])

    for index, possible in enumerate(quiz):
        if index >= ANSWER_IDX+1:
            print(possible)
    answer = input('What is your answer: ')

    if answer == quiz[ANSWER_IDX]:
        print("✨✨✨ CORRECT ✨✨✨")
    else:
        print("INCORRECT")
```

See how just using QUESTION_IDX and ANSWER_IDX instead of 0 and 1 it is easier to read. Now lets try a completely different way:

```
import random
game = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "possible": ['London','Paris','Berlin','Tokyo'],
    },
    {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo",
        "possible": ['London','Paris','Berlin','Tokyo'],
    },  
]


while True:
    quiz = random.choice(game)
    print(quiz["question"])
    for p in quiz["possible"]:
        print(' --> ' + p)
    answer = input('What is your answer: ')

    if answer == quiz["answer"]:
        print("✨✨✨ CORRECT ✨✨✨")
    else:
        print("INCORRECT")
```

This is just another way to do it, see in the list we can store those strange things. We will talk about them in a couple of weeks, I just wanted to show you how clean it is when 

## [DAY-50] Basics of Basics

Print the odd numbers from 0 to 999

```
for i in range(1000):
    if i % 2 != 0:
        print(i)
```

rock paper scissors

```
import random
game = ["rock","paper","scissors"]

rounds = 3

nameA = input("name player A: ")
nameB = input("name player B: ")
winsA = 0
winsB = 0
for i in range(rounds):
    playerA = random.choice(game)
    playerB = random.choice(game)
    print("ROUND: " + str(i + 1))
    print("playerA : " + playerA)
    print("playerB : " + playerB)
    
    if playerA == playerB:
        print("  > DRAW")
    elif playerA == "rock" and playerB == "paper":
        print("  > " + nameB + " WINS")
        winsB += 1
    elif playerA == "rock" and playerB == "scissors":
        print("  > " + nameA + " WINS")
        winsA += 1
    elif playerA == "paper" and playerB == "rock":
        print("  > " + nameA + " WINS")
        winsA += 1
    elif playerA == "paper" and playerB == "scissors":
        print("  > " + nameB + " WINS")
        winsB += 1
    elif playerA == "scissors" and playerB == "rock":
        print("  > " + nameB + " WINS")
        winsB += 1
    elif playerA == "scissors" and playerB == "paper":
        print("  > " + nameA + " WINS")
        winsA += 1
    else:
        print("WTF " + playerA + " " + playerB)

    print("---")

print(nameA + " has " + str(winsA) + " points")
print(nameB + " has " + str(winsB) + " points")
if winsA > winsB:
    print(nameA + " IS THE WINNER")
elif winsA < winsB:
    print(nameB + " IS THE WINNER")
else:
    # this will show only if we have even number of rounds
    print("THERE IS NO WINNER")
```
## [DAY-51] Basics of the Internet

Today is an important day, its Internet awareness day.

Make the most expensive drone on amazon.com cost 0$, or even -5$. As we did in the first week, open inspect click on the mouse selector (or press Control+Shift+C) and click on the price you want to change, then double click on the HTML and change it to whatever you want.

After you are done reload the page to see it is not actually changed.

Now do that on roblox, make it look like you have 999999 robux.

Go to google and search for `Speed up your internet connection`, go over the websites one by one with your parent, and observe, look at many many scams, some are very easy to fall into, some are obvious.

Open youtube.com, search for 'free energy hack' watch some of the videos, then search for 'electroboom free energy' and watch Mehdi explain why it is a scam. Search for 'be carefull what you order from facebook ads' Pleasant Green and watch how he explains a scam with ads to buy a cool looking helmet.

See the internet is a place, where you can find great things, like electroboom and pleasant green or veritasium or vsauce, but also where there are horrible things, like people selling garbage for 30$. Or people claiming 

Now with your parent, search on youtube for 'how to hack in roblox' and look at the scame, how people want to install something so they can steal your password.

## [DAY-52] Basics of the Internet

Ok now for something more serious!

Just a quick intro into cookies, when you login to a website, it stores a piece of information on your computer called a cookie, and with every request you make to the website after it sends this cookie, the website can also tell you to replace the cookie. This is how websites know you are logged in, after they check your user and password they send you a cookie with a secret value, that you use for every request, they store that value usually in a database (kind of like huge huge excel sheet, that you can quickly search in), and look it up to see if it is valid.

So imagine websites have a table like so:

|username|password|
|-|-|
|jane|123456|
|john|blabla|


It is a bit more complicated than that, because they don't store the password but "encrypted" version of the password, so instead of 123456 (which is a horrible password btw), they store the result of a cryptographic hash function, hash(salt + '___' + password), and salt is used so that the attacker has to get both the usernames, the encrypted passwords and the code that joins them in order to extract a password using some bruteforce methods.

A cryptographic hash function is like a machine where you put in a lego castle in, and it will spit out exactly 8 pieces (ot 32 or whatever the function is), and there is no easy way for you to guess what kind of castle you put in it, but you know that *always* the same castle will spit out the same 8 pieces.

So in reality the excel sheet looks a bit like this:


|username|encrypted password|salt|
|-|-|-|
|jane|4c87d9b2ecfbd99c483aedfae8045fe578912e63|someRandom123|
|john|065ce4538c7c51687270972babdeaa986f3ce1bd|someRandom435|


But that is not important, we will use the simple example for our case. When you click 'login' it will send the username and password over the internet, and their server will look in the table for this user and will check if the password matches. If it matches it will insert a row another excel sheet that looks like this:


|username|token|
|-|-|
|jane|bbd0bff806a177f082f3ba2cff33030d335c296e|

then tell your browser, hey set this cookies:

```
the username for amazon.com is 'jane'
the token is bbd0bff806a177f082f3ba2cff33030d335c296e
```

So next time when you make a request to amazon your browser will send both the user name and the token, amazon will check in the token table if this token is valid (they have expiration date as well, kind of like a real token), and then it will know you actually logged in, without your password being stored on your browser.

Now lets see how someone can login as you without knowing your password.

Login to amazon. Open chrome in private mode. Open amazon there as well, and see that on one browser you are logged in, on the private mode you are not. Now open the console(press F12) on the logged in browser and type this:

```
var cookies = []
for (cookie of document.cookie.split(";")) {
    cookies.push(cookie.replace(" ", ""))
}
console.log(cookies)
```
This will print all the cookies amazon has set on your browser in a list.


Copy the whole list of cookies, now on the private mode browser's console(press F12 to open the console) type:

```
var newCookies = ["session-id....." .. .. ] // just paste the whole string from the other browser
for (cookie of newCookies) {
    document.cookie = cookie;
}
```

Paste the whole list there, and refresh the page.

And voila! You are logged in now without typing a password. 

So if you give access to somebody to your computer, they can trivially copy your cookies and send them somewhere, and then they can login as you without even knowing your password. In fact this is a very common way to steal someone's account on social media. Ask them to paste a strange code in the console, which is usually `base64 encoded` that looks like this:

```
d = atob('dmFyIGNvb2tpZXMgPSBbXQpmb3IgKGNvb2tpZSBvZiBkb2N1bWVudC5jb29raWUuc3BsaXQoIjsiKSkgewogICAgY29va2llcy5wdXNoKGNvb2tpZS5yZXBsYWNlKCIgIiwgIiIpKQp9CmNvbnNvbGUubG9nKGNvb2tpZXMpCg==')
console.log(d)
eval(d)
```

You see how it printed your cookies? The thing that runs the code is `eval` it is kind of like double clicking on a program, but it will run the code that is inside the string you give it. If you want to see what the code does just run `console.log(atob('....'))` this will just decode the base64 encoding into a string you can read. `atob` decodes base64 string into the real string, it is kind of like in python `ord('a')` gives you 97 and `chr(97)` gives you 'a'.

Of course the code that the scammers give you is more sophisticated, it sends the cookies to their database(think excel sheet) via the internet, including all local storage and local session data, and they can just use it after that.


## [DAY-53] Basics of Basics
## [DAY-54] Basics of Basics


