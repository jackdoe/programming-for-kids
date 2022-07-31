```
┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐┌┬┐┬┌┐┌┌─┐
├─┘├┬┘│ ││ ┬├┬┘├─┤│││││││││││ ┬
┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴┴ ┴┴┘└┘└─┘
┌─┐┌─┐┬─┐                      
├┤ │ │├┬┘                      
└  └─┘┴└─                      
┬┌─┬┌┬┐┌─┐                     
├┴┐│ ││└─┐                     
┴ ┴┴─┴┘└─┘                                       


> by: Borislav Nikolov
> year: 2021

The parent has to know how to program.
Spend 30 minutes per day. Every day.

"Anything worth doing is worth doing badly." — G. K. Chesterton

```

<br>
<br>
<br>
<br>

<div style="page-break-before:always"></div>
# Hello World

::: warning
*This chapter is for parents, kids skip to the next one.* [day 0 - the computer](https://github.com/jackdoe/programming-for-kids#day-0-the-computer)
:::


## Why

I think modern education treats programming as 'career path', I think of that to be wrong. I treat it as literacy. Being literate lets to experience a different world than those who aren't. It is not about having a job, I can't even explain it, being literate just allows you to see the fabric of what everything is made of.

Imagine schools were teaching violin en masse, how would that go? How many kids will be able to make a decent sound? How many will drop out because they are stuck and the rest have to move on because the tests say so?

Sometimes my daughter doesn't like to code, or to read for that matter, of course the rest of the internet is so much more interesting. We are competing with hundreds of thousands of developers in Supercell and Facebook and TikTok and Netflix that train billion parameters models so they can squeeze every last bit of attention from our kids. Of course it is going to be difficult. But, I thought to myself, does that mean I should not try? So a change of approach is needed, completely individualistic and personal approach.

Maybe she will grow hating it, or even hating me. Parenting is difficult.

We are 7 months in, and so far she doesn't hate me.

## About the book

This book is for parents who know how to code and for kids who don't, but especially for parents and kids who can spend 30 minutes per day, _every day_. I am writing this book as I am teaching my daughter (10), and you know how in some cooking shows, they skip the part where the food is cooking? I wont do that. The book will be longer than it should.

Again, if your children are older, or younger, this book might not work, you could of course still find pieces that work for you.

This is more of a log of my experience so far. I am writing it as if I am talking to my daughter, so the style might be weird, but for you it should be more of an pool of examples you could use, and maybe just get ideas from the text. Try to avoid giving the book to your child and say "do this chapter", but in is also good experience to be able to do something alone.

Also its nice to print a copy so they don't just copy paste.

What you need:

* Computer
* Patience
* Internet
* Patience

If you don't have a you can buy raspberry pi 400 for 70$ or so, or something similar that you attach to your TV. If you don't have patience, buy some chamomile tea. You don't need internet subscription, but you would need a bit of internet to download python and do few google searches.

In most of the weeks you also go back, waaay back, every day you re-iterate variables and for loops, print the numbers from one to 10 forever, ask how many times to be printed, etc.

The emphasis on HTML helps with understanding hierarchy, `tr` is child of `table`, `table` is child of `body` body is child of `html`, `td` is a sister to `td` and both are children of `tr` etc, it helped a lot with my daughter understanding how the `else` is sibling to the `if` and how both are children to `while`.

Also it is very easy to debug, and inspect, and get immediate feedback. There are many 'hackers' now on tiktok or youtube that shows you how to get a lot robux(money) in roblox by inspecting the page and modifying the HTML, so I think HTML is very important to be understood, not only because it teaches hierarchy, but also it is the canvas of the web.


## Other materials

Play other games as well, https://tomorrowcorporation.com/ has some brilliant games, Human Resource Machine is great way to learn loops and conditional jumps, and 7 Billion Humans is amazing for high level concepts, including variables, recursion and sorting. Before we started with HTML we spent about 1 month with those games. They are just incredible and well worth their money.

The Robot Turtles game is amazing as well, you can find it here: https://www.thinkfun.com/products/robot-turtles/

Scratch works for some kids, mine didn't enjoy it much.

Buy few Arduino NANOs (cheap clones from amazon work as well, but you need to install ch340 driver), and some servo motors and write few super basic programs that turn the servo slowly in one direction or another. Connect `black/brown wire to gnd, red wire to 5v and orange wire to D9`, and run:

```
#include <Servo.h>
#define SERVO_PIN 9
Servo s;
void setup()  {
  s.attach(SERVO_PIN, 1000, 2000);
}

void loop()  {
  s.write(0);
  delay(500);

  s.write(60);
  delay(500);

  s.write(120);
  delay(500);
}
```

## Motivation

Sometimes there is very little motivation. Kids are super tired from school and playdates and extracurricular activities, makes it hard to spend 30 minutes per day on something. Netflix and YouTube and etc are so much more interesting than what I have to offer, it is a rigged game.. Sad that I have to compete with billion parameter models, but here we are.

Anything worth doing, is worth doing poorly. If you cant spend 30 minutes, spend 15, spend 5 minutes if you have to, or even 1. It is all worth it.

I try to spend time in the morning, at least on the weekends, and first thing after school on school days. Luckily now it is a bit easier while we work from home during the pandemic. We tried to setup time before or after dinner, and it doesn't go well.

Sometimes material incentives are also very helpful, e.g. a promise 5$ gift card, but I think you will have to find out what works for your kids.

<div style="page-break-before:always"></div>
## week - 0
## week - 000



[day-0 the computer](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-0-the-computer)

[day-0 files](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-0-files)

[day-0 ascii](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-0-ascii)

[day-0 magic](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-0-magic)

[day-0 how to google](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-0-how-to-google)

[day-1 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-1-touch-typing)

[day-2 install python](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-2-install-python)

[day-2 make a useful program](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-2-make-a-useful-program)

[day-3 touch typing using your program](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-3-touch-typing-using-your-program)

[day-4 html - basics](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-4-html---basics)

[day-5 html - basics](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-5-html---basics)

[day-6 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-000.md#day-6-touch-typing)
## week - 001



[day-7 new touch typing program](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-7-new-touch-typing-program)

[day-8 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-8-touch-typing)

[day-9 touch typing using your program](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-9-touch-typing-using-your-program)

[day-10 html - basics](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-10-html---basics)

[day-11 html - basics](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-11-html---basics)

[day-12 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-12-touch-typing)

[day-13 html](https://github.com/jackdoe/programming-for-kids/blob/master/week-001.md#day-13-html)
## week - 002



[day-14 html - tables](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-14-html---tables)

[day-15 html - more tables](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-15-html---more-tables)

[day-16 html - multiplication table](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-16-html---multiplication-table)

[day-17 html - multiplication table](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-17-html---multiplication-table)

[day-18 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-18-touch-typing)

[day-19 html - links](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-19-html---links)

[day-20 html - tree](https://github.com/jackdoe/programming-for-kids/blob/master/week-002.md#day-20-html---tree)
## week - 003



[day-21 html - view source](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-21-html---view-source)

[day-22 html - inspect](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-22-html---inspect)

[day-23 html - images](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-23-html---images)

[day-24 licenses](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-24-licenses)

[day-25 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-25-touch-typing)

[day-26 html - title](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-26-html---title)

[day-27 html - fun (js)](https://github.com/jackdoe/programming-for-kids/blob/master/week-003.md#day-27-html---fun-(js))
## week - 004



[day-28 print; functions; while; variables; conditions](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-28-print-functions-while-variables-conditions)

[day-29 print; if](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-29-print-if)

[day-30 functions; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-30-functions-lists)

[day-31 functions; if; random; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-31-functions-if-random-lists)

[day-32 lists; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-32-lists-while)

[day-33 for](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-33-for)

[day-34 love tester](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-34-love-tester)

[day-34 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-004.md#day-34-touch-typing)
## week - 005



[day-35 lists; while; continue](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-35-lists-while-continue)

[day-36 while; range; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-36-while-range-functions)

[day-37 while; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-37-while-functions)

[day-38 strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-38-strings)

[day-39 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-39-touch-typing)

[day-40 functions; strings; range](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-40-functions-strings-range)

[day-41 basics of basics](https://github.com/jackdoe/programming-for-kids/blob/master/week-005.md#day-41-basics-of-basics)
## week - 006



[day-41 lists; if; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-41-lists-if-while)

[day-42 lists; functions; grid; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-42-lists-functions-grid-while)

[day-43 if; range](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-43-if-range)

[day-44 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-44-lists)

[day-45 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-45-lists-functions)

[day-46 basic turtle](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-46-basic-turtle)

[day-47 range; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-006.md#day-47-range-while)
## week - 007



[day-48 strings; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-48-strings-functions)

[day-49 list; dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-49-list-dictionaries)

[day-50 lists; if](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-50-lists-if)

[day-51 internet awareness - scams/viruses](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-51-internet-awareness---scamsviruses)

[day-52 internet awareness - how login works](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-52-internet-awareness---how-login-works)

[day-53 basics of the internet - ip/dns](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-53-basics-of-the-internet---ipdns)

[day-54 touch typing](https://github.com/jackdoe/programming-for-kids/blob/master/week-007.md#day-54-touch-typing)
## week - 008



[day-55 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-008.md#day-55-lists-functions)

[day-56 functions; if; random](https://github.com/jackdoe/programming-for-kids/blob/master/week-008.md#day-56-functions-if-random)

[day-57 lists; functions; grid](https://github.com/jackdoe/programming-for-kids/blob/master/week-008.md#day-57-lists-functions-grid)

[day-58 continue previous day](https://github.com/jackdoe/programming-for-kids/blob/master/week-008.md#day-58-continue-previous-day)

[day-59 tuples; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-008.md#day-59-tuples-lists)

[day-60 go back in time](https://github.com/jackdoe/programming-for-kids/blob/master/week-008.md#day-60-go-back-in-time)
## week - 009



[day-61 pygame; pygamezero; coordinates](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-61-pygame-pygamezero-coordinates)

[day-62 collisions; callbacks](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-62-collisions-callbacks)

[day-63 functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-63-functions)

[day-64 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-64-lists-functions)

[day-65 functions; collisions](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-65-functions-collisions)

[day-66 schedule; callbacks; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-66-schedule-callbacks-functions)

[day-67 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-009.md#day-67-lists-functions)
## week - 010



[day-68 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-68-lists-functions)

[day-69 sockets; functions; callbacks](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-69-sockets-functions-callbacks)

[day-70 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-70-lists-functions)

[day-71 strings; integers; while; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-71-strings-integers-while-functions)

[day-72 reading code](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-72-reading-code)

[day-73 reading code](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-73-reading-code)

[day-74 strings; while; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-010.md#day-74-strings-while-lists)
## week - 011



[day-75 functions; callbacks; lists; encoding](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-75-functions-callbacks-lists-encoding)

[day-76 functions; callbacks; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-76-functions-callbacks-lists)

[day-77 lists; encode/decode](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-77-lists-encodedecode)

[day-78 coordinates; functions; callbacks](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-78-coordinates-functions-callbacks)

[day-79 lists; encoding](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-79-lists-encoding)

[day-80 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-80-lists-functions)

[day-81 lists; encoding](https://github.com/jackdoe/programming-for-kids/blob/master/week-011.md#day-81-lists-encoding)
## week - 012



[day-82 lists; strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-82-lists-strings)

[day-83 lists; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-83-lists-functions)

[day-84 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-84-lists)

[day-85 list; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-85-list-functions)

[day-86 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-86-lists)

[day-87 read/write files](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-87-readwrite-files)

[day-88 flask](https://github.com/jackdoe/programming-for-kids/blob/master/week-012.md#day-88-flask)
## week - 013



[day-89 files; strings; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-89-files-strings-lists)

[day-90 strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-90-strings)

[day-91 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-91-lists)

[day-92 command line; command line arguments; files](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-92-command-line-command-line-arguments-files)

[day-93 pydoc](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-93-pydoc)

[day-94 editors - ed/nano/vi/emacs..](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-94-editors---ednanoviemacs..)

[day-95 memory; virtual computer; instructions; strings; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-013.md#day-95-memory-virtual-computer-instructions-strings-lists)
## week - 014



[day-95 memory; machine code; virtual computer](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-95-memory-machine-code-virtual-computer)

[day-96 binary; ascii; memory](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-96-binary-ascii-memory)

[day-97 lists; ](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-97-lists-)

[day-98 lists; read/write file](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-98-lists-readwrite-file)

[day-99 classes; lists; functions; cartesian coordinates](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-99-classes-lists-functions-cartesian-coordinates)

[day-100 touch typing; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-100-touch-typing-lists)

[day-101 functions; strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-014.md#day-101-functions-strings)
## week - 015



[day-102 touch typing day](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-102-touch-typing-day)

[day-103 read file; command line arguments](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-103-read-file-command-line-arguments)

[day-104 read file; command line arguments; dictionary](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-104-read-file-command-line-arguments-dictionary)

[day-105 basics of basics](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-105-basics-of-basics)

[day-106 read/write file; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-106-readwrite-file-lists)

[day-107 lists; dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-107-lists-dictionaries)

[day-108 dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-015.md#day-108-dictionaries)
## week - 016



[day-109 touch typing day](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-109-touch-typing-day)

[day-110 find code on tiktok](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-110-find-code-on-tiktok)

[day-111 lists; random](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-111-lists-random)

[day-112 use simple dictionary](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-112-use-simple-dictionary)

[day-113 discover pythontutor](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-113-discover-pythontutor)

[day-114 simple turtle](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-114-simple-turtle)

[day-115 practical coding, control roblox with python](https://github.com/jackdoe/programming-for-kids/blob/master/week-016.md#day-115-practical-coding-control-roblox-with-python)
## week - 017



[day-116 many turtles](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-116-many-turtles)

[day-117 another text editor](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-117-another-text-editor)

[day-118 search lyrics](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-118-search-lyrics)

[day-119 facial recognition; move 78](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-119-facial-recognition-move-78)

[day-120 program on your own form a book](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-120-program-on-your-own-form-a-book)

[day-121 scam check list](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-121-scam-check-list)

[day-122 lists; random; mutate](https://github.com/jackdoe/programming-for-kids/blob/master/week-017.md#day-122-lists-random-mutate)
## week - 018



[day-123 lists; callbacks](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-123-lists-callbacks)

[day-124 bmp format, images; encoding/decoding](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-124-bmp-format-images-encodingdecoding)

[day-125 lists; dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-125-lists-dictionaries)

[day-126 read/write file](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-126-readwrite-file)

[day-127 callbacks; schedule interval](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-127-callbacks-schedule-interval)

[day-128 lists; cpu usage; resources](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-128-lists-cpu-usage-resources)

[day-129 eat your computer; memory; cpu](https://github.com/jackdoe/programming-for-kids/blob/master/week-018.md#day-129-eat-your-computer-memory-cpu)
## week - 019



[day-130 turtle; lists; classes](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-130-turtle-lists-classes)

[day-131 lists; files; dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-131-lists-files-dictionaries)

[day-132 lists; classes](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-132-lists-classes)

[day-133 touch typing; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-133-touch-typing-lists)

[day-134 lists; methods](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-134-lists-methods)

[day-134 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-134-if)

[day-135 dictionary; for](https://github.com/jackdoe/programming-for-kids/blob/master/week-019.md#day-135-dictionary-for)
## week - 020



[day-136 for; arrays; memory](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-136-for-arrays-memory)

[day-137 for; file; if](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-137-for-file-if)

[day-138 for; file; if](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-138-for-file-if)

[day-139 while; list; counter](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-139-while-list-counter)

[day-140 while; turtle; strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-140-while-turtle-strings)

[day-141 wiki; api](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-141-wiki-api)

[day-142 while](https://github.com/jackdoe/programming-for-kids/blob/master/week-020.md#day-142-while)
## week - 021



[day-143 strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-143-strings)

[day-144 strings; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-144-strings-lists)

[day-145 while](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-145-while)

[day-146 while; classes](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-146-while-classes)

[day-147 while](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-147-while)

[day-148 money](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-148-money)

[day-149 creators, consumers and ideas](https://github.com/jackdoe/programming-for-kids/blob/master/week-021.md#day-149-creators-consumers-and-ideas)
## week - 022



[day-150 while; classes](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-150-while-classes)

[day-151 classes; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-151-classes-while)

[day-152 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-152-lists)

[day-153 lists; dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-153-lists-dictionaries)

[day-154 classes](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-154-classes)

[day-155 c++](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-155-c++)

[day-156 for; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-022.md#day-156-for-while)
## week - 023



[day-157 strings; cin](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-157-strings-cin)

[day-158 if; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-158-if-while)

[day-159 strings; sizeof](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-159-strings-sizeof)

[day-160 pointers](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-160-pointers)

[day-161 if; while; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-161-if-while-functions)

[day-162 if; while; variables](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-162-if-while-variables)

[day-163 if; while; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-023.md#day-163-if-while-lists)
## week - 024



[day-164 pointers](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-164-pointers)

[day-165 if; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-165-if-while)

[day-166 if; while](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-166-if-while)

[day-167 c; printf; scanf](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-167-c-printf-scanf)

[day-168 c; while; if](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-168-c-while-if)

[day-169 c; while; if](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-169-c-while-if)

[day-170 pointers](https://github.com/jackdoe/programming-for-kids/blob/master/week-024.md#day-170-pointers)
## week - 025



[day-171 while; for; if; list](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-171-while-for-if-list)

[day-172 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-172-if)

[day-173 if; variables](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-173-if-variables)

[day-174 if; list](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-174-if-list)

[day-175 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-175-if)

[day-176 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-176-if)

[day-177 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-025.md#day-177-if)
## week - 026



[day-178 if; absolute](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-178-if-absolute)

[day-179 if; for](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-179-if-for)

[day-180 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-180-if)

[day-181 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-181-if)

[day-182 look back](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-182-look-back)

[day-183 generalization](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-183-generalization)

[day-184 generalization](https://github.com/jackdoe/programming-for-kids/blob/master/week-026.md#day-184-generalization)
## week - 027



[day-185 generalization](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-185-generalization)

[day-186 if](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-186-if)

[day-187 if; while; functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-187-if-while-functions)

[day-188 oop](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-188-oop)

[day-189 keyword arguments; string methods](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-189-keyword-arguments-string-methods)

[day-190 while](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-190-while)

[day-191 while](https://github.com/jackdoe/programming-for-kids/blob/master/week-027.md#day-191-while)
## week - 028



[day-192 class; methods](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-192-class-methods)

[day-193 richard buckland's computer](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-193-richard-buckland's-computer)

[day-194 self modifying programs](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-194-self-modifying-programs)

[day-195 loops](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-195-loops)

[day-196 loops](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-196-loops)

[day-197 interpreter](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-197-interpreter)

[day-198 coordinates](https://github.com/jackdoe/programming-for-kids/blob/master/week-028.md#day-198-coordinates)
## week - 029



[day-199 coordinates](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-199-coordinates)

[day-200 coordinates](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-200-coordinates)

[day-201 computers](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-201-computers)

[day-202 pointers](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-202-pointers)

[day-203 strategy](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-203-strategy)

[day-204 money](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-204-money)

[day-205 fetch-decode-execute](https://github.com/jackdoe/programming-for-kids/blob/master/week-029.md#day-205-fetch-decode-execute)
## week - 030



[day-206 client server](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-206-client-server)

[day-207 0; 1; infinity; how to break things down](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-207-0-1-infinity-how-to-break-things-down)

[day-208 if; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-208-if-lists)

[day-209 if; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-209-if-lists)

[day-210 if; lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-210-if-lists)

[day-211 classes](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-211-classes)

[day-212 pico-8 follow adventure game tutorial](https://github.com/jackdoe/programming-for-kids/blob/master/week-030.md#day-212-pico-8-follow-adventure-game-tutorial)
## week - 031



[day-213 pico-8 adventure game](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-213-pico-8-adventure-game)

[day-214 pico-8 follow platformer game tutorial](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-214-pico-8-follow-platformer-game-tutorial)

[day-215 make a website](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-215-make-a-website)

[day-216 directories](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-216-directories)

[day-217 directories](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-217-directories)

[day-218 variables](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-218-variables)

[day-219 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-031.md#day-219-lists)
## week - 032



[day-220 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-220-lists)

[day-221 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-221-lists)

[day-222 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-222-lists)

[day-223 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-223-lists)

[day-224 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-224-lists)

[day-225 functions](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-225-functions)

[day-226 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-032.md#day-226-lists)
## week - 033



[day-227 lists](https://github.com/jackdoe/programming-for-kids/blob/master/week-033.md#day-227-lists)

[day-228 files](https://github.com/jackdoe/programming-for-kids/blob/master/week-033.md#day-228-files)

[day-229 strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-033.md#day-229-strings)

[day-229 files; strings](https://github.com/jackdoe/programming-for-kids/blob/master/week-033.md#day-229-files-strings)

[day-230 dictionaries](https://github.com/jackdoe/programming-for-kids/blob/master/week-033.md#day-230-dictionaries)
--

The whole book: [https://github.com/jackdoe/programming-for-kids/blob/master/book.md](book.md)

if you have any ideas or feedback, make a pull request, or send me an email to programmingtime@fastmail.com


