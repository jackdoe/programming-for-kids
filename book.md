
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
*This chapter is for parents, kids skip to the next one.* [day 0 - the computer](#day-0-the-computer)
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

## week - 000



[day-0 the computer](#day-0-the-computer)

[day-0 files](#day-0-files)

[day-0 ascii](#day-0-ascii)

[day-0 magic](#day-0-magic)

[day-0 how to google](#day-0-how-to-google)

[day-1 touch typing](#day-1-touch-typing)

[day-2 install python](#day-2-install-python)

[day-2 make a useful program](#day-2-make-a-useful-program)

[day-3 touch typing using your program](#day-3-touch-typing-using-your-program)

[day-4 html - basics](#day-4-html---basics)

[day-5 html - basics](#day-5-html---basics)

[day-6 touch typing](#day-6-touch-typing)
## week - 001



[day-7 new touch typing program](#day-7-new-touch-typing-program)

[day-8 touch typing](#day-8-touch-typing)

[day-9 touch typing using your program](#day-9-touch-typing-using-your-program)

[day-10 html - basics](#day-10-html---basics)

[day-11 html - basics](#day-11-html---basics)

[day-12 touch typing](#day-12-touch-typing)

[day-13 html](#day-13-html)
## week - 002



[day-14 html - tables](#day-14-html---tables)

[day-15 html - more tables](#day-15-html---more-tables)

[day-16 html - multiplication table](#day-16-html---multiplication-table)

[day-17 html - multiplication table](#day-17-html---multiplication-table)

[day-18 touch typing](#day-18-touch-typing)

[day-19 html - links](#day-19-html---links)

[day-20 html - tree](#day-20-html---tree)
## week - 003



[day-21 html - view source](#day-21-html---view-source)

[day-22 html - inspect](#day-22-html---inspect)

[day-23 html - images](#day-23-html---images)

[day-24 licenses](#day-24-licenses)

[day-25 touch typing](#day-25-touch-typing)

[day-26 html - title](#day-26-html---title)

[day-27 html - fun (js)](#day-27-html---fun-(js))
## week - 004



[day-28 print; functions; while; variables; conditions](#day-28-print-functions-while-variables-conditions)

[day-29 print; if](#day-29-print-if)

[day-30 functions; lists](#day-30-functions-lists)

[day-31 functions; if; random; lists](#day-31-functions-if-random-lists)

[day-32 lists; while](#day-32-lists-while)

[day-33 for](#day-33-for)

[day-34 love tester](#day-34-love-tester)

[day-34 touch typing](#day-34-touch-typing)
## week - 005



[day-35 lists; while; continue](#day-35-lists-while-continue)

[day-36 while; range; functions](#day-36-while-range-functions)

[day-37 while; functions](#day-37-while-functions)

[day-38 strings](#day-38-strings)

[day-39 touch typing](#day-39-touch-typing)

[day-40 functions; strings; range](#day-40-functions-strings-range)

[day-41 basics of basics](#day-41-basics-of-basics)
## week - 006



[day-41 lists; if; while](#day-41-lists-if-while)

[day-42 lists; functions; grid; while](#day-42-lists-functions-grid-while)

[day-43 if; range](#day-43-if-range)

[day-44 lists](#day-44-lists)

[day-45 lists; functions](#day-45-lists-functions)

[day-46 basic turtle](#day-46-basic-turtle)

[day-47 range; while](#day-47-range-while)
## week - 007



[day-48 strings; functions](#day-48-strings-functions)

[day-49 list; dictionaries](#day-49-list-dictionaries)

[day-50 lists; if](#day-50-lists-if)

[day-51 internet awareness - scams/viruses](#day-51-internet-awareness---scamsviruses)

[day-52 internet awareness - how login works](#day-52-internet-awareness---how-login-works)

[day-53 basics of the internet - ip/dns](#day-53-basics-of-the-internet---ipdns)

[day-54 touch typing](#day-54-touch-typing)
## week - 008



[day-55 lists; functions](#day-55-lists-functions)

[day-56 functions; if; random](#day-56-functions-if-random)

[day-57 lists; functions; grid](#day-57-lists-functions-grid)

[day-58 continue previous day](#day-58-continue-previous-day)

[day-59 tuples; lists](#day-59-tuples-lists)

[day-60 go back in time](#day-60-go-back-in-time)
## week - 009



[day-61 pygame; pygamezero; coordinates](#day-61-pygame-pygamezero-coordinates)

[day-62 collisions; callbacks](#day-62-collisions-callbacks)

[day-63 functions](#day-63-functions)

[day-64 lists; functions](#day-64-lists-functions)

[day-65 functions; collisions](#day-65-functions-collisions)

[day-66 schedule; callbacks; functions](#day-66-schedule-callbacks-functions)

[day-67 lists; functions](#day-67-lists-functions)
## week - 010



[day-68 lists; functions](#day-68-lists-functions)

[day-69 sockets; functions; callbacks](#day-69-sockets-functions-callbacks)

[day-70 lists; functions](#day-70-lists-functions)

[day-71 strings; integers; while; functions](#day-71-strings-integers-while-functions)

[day-72 reading code](#day-72-reading-code)

[day-73 reading code](#day-73-reading-code)

[day-74 strings; while; lists](#day-74-strings-while-lists)
## week - 011



[day-75 functions; callbacks; lists; encoding](#day-75-functions-callbacks-lists-encoding)

[day-76 functions; callbacks; lists](#day-76-functions-callbacks-lists)

[day-77 lists; encode/decode](#day-77-lists-encodedecode)

[day-78 coordinates; functions; callbacks](#day-78-coordinates-functions-callbacks)

[day-79 lists; encoding](#day-79-lists-encoding)

[day-80 lists; functions](#day-80-lists-functions)

[day-81 lists; encoding](#day-81-lists-encoding)
## week - 012



[day-82 lists; strings](#day-82-lists-strings)

[day-83 lists; functions](#day-83-lists-functions)

[day-84 lists](#day-84-lists)

[day-85 list; functions](#day-85-list-functions)

[day-86 lists](#day-86-lists)

[day-87 read/write files](#day-87-readwrite-files)

[day-88 flask](#day-88-flask)
## week - 013



[day-89 files; strings; lists](#day-89-files-strings-lists)

[day-90 strings](#day-90-strings)

[day-91 lists](#day-91-lists)

[day-92 command line; command line arguments; files](#day-92-command-line-command-line-arguments-files)

[day-93 pydoc](#day-93-pydoc)

[day-94 editors - ed/nano/vi/emacs..](#day-94-editors---ednanoviemacs..)

[day-95 memory; virtual computer; instructions; strings; lists](#day-95-memory-virtual-computer-instructions-strings-lists)
## week - 014



[day-95 memory; machine code; virtual computer](#day-95-memory-machine-code-virtual-computer)

[day-96 binary; ascii; memory](#day-96-binary-ascii-memory)

[day-97 lists; ](#day-97-lists-)

[day-98 lists; read/write file](#day-98-lists-readwrite-file)

[day-99 classes; lists; functions; cartesian coordinates](#day-99-classes-lists-functions-cartesian-coordinates)

[day-100 touch typing; lists](#day-100-touch-typing-lists)

[day-101 functions; strings](#day-101-functions-strings)
## week - 015



[day-102 touch typing day](#day-102-touch-typing-day)

[day-103 read file; command line arguments](#day-103-read-file-command-line-arguments)

[day-104 read file; command line arguments; dictionary](#day-104-read-file-command-line-arguments-dictionary)

[day-105 basics of basics](#day-105-basics-of-basics)

[day-106 read/write file; lists](#day-106-readwrite-file-lists)

[day-107 lists; dictionaries](#day-107-lists-dictionaries)

[day-108 dictionaries](#day-108-dictionaries)
## week - 016



[day-109 touch typing day](#day-109-touch-typing-day)

[day-110 find code on tiktok](#day-110-find-code-on-tiktok)

[day-111 lists; random](#day-111-lists-random)

[day-112 use simple dictionary](#day-112-use-simple-dictionary)

[day-113 discover pythontutor](#day-113-discover-pythontutor)

[day-114 simple turtle](#day-114-simple-turtle)

[day-115 practical coding, control roblox with python](#day-115-practical-coding-control-roblox-with-python)
## week - 017



[day-116 many turtles](#day-116-many-turtles)

[day-117 another text editor](#day-117-another-text-editor)

[day-118 search lyrics](#day-118-search-lyrics)

[day-119 facial recognition; move 78](#day-119-facial-recognition-move-78)

[day-120 program on your own form a book](#day-120-program-on-your-own-form-a-book)

[day-121 scam check list](#day-121-scam-check-list)

[day-122 lists; random; mutate](#day-122-lists-random-mutate)
## week - 018



[day-123 lists; callbacks](#day-123-lists-callbacks)

[day-124 bmp format, images; encoding/decoding](#day-124-bmp-format-images-encodingdecoding)

[day-125 lists; dictionaries](#day-125-lists-dictionaries)

[day-126 read/write file](#day-126-readwrite-file)

[day-127 callbacks; schedule interval](#day-127-callbacks-schedule-interval)

[day-128 lists; cpu usage; resources](#day-128-lists-cpu-usage-resources)

[day-129 eat your computer; memory; cpu](#day-129-eat-your-computer-memory-cpu)
## week - 019



[day-130 turtle; lists; classes](#day-130-turtle-lists-classes)

[day-131 lists; files; dictionaries](#day-131-lists-files-dictionaries)

[day-132 lists; classes](#day-132-lists-classes)

[day-133 touch typing; lists](#day-133-touch-typing-lists)

[day-134 lists; methods](#day-134-lists-methods)

[day-134 if](#day-134-if)

[day-135 dictionary; for](#day-135-dictionary-for)
## week - 020



[day-136 for; arrays; memory](#day-136-for-arrays-memory)

[day-137 for; file; if](#day-137-for-file-if)

[day-138 for; file; if](#day-138-for-file-if)

[day-139 while; list; counter](#day-139-while-list-counter)

[day-140 while; turtle; strings](#day-140-while-turtle-strings)

[day-141 wiki; api](#day-141-wiki-api)

[day-142 while](#day-142-while)
## week - 021



[day-143 strings](#day-143-strings)

[day-144 strings; lists](#day-144-strings-lists)

[day-145 while](#day-145-while)

[day-146 while; classes](#day-146-while-classes)

[day-147 while](#day-147-while)

[day-148 money](#day-148-money)

[day-149 creators, consumers and ideas](#day-149-creators-consumers-and-ideas)
## week - 022



[day-150 while; classes](#day-150-while-classes)

[day-151 classes; while](#day-151-classes-while)

[day-152 lists](#day-152-lists)

[day-153 lists; dictionaries](#day-153-lists-dictionaries)

[day-154 classes](#day-154-classes)

[day-155 c++](#day-155-c++)

[day-156 for; while](#day-156-for-while)
## week - 023



[day-157 strings; cin](#day-157-strings-cin)

[day-158 if; while](#day-158-if-while)

[day-159 strings; sizeof](#day-159-strings-sizeof)

[day-160 pointers](#day-160-pointers)

[day-161 if; while; functions](#day-161-if-while-functions)

[day-162 if; while; variables](#day-162-if-while-variables)

[day-163 if; while; lists](#day-163-if-while-lists)
## week - 024



[day-164 pointers](#day-164-pointers)

[day-165 if; while](#day-165-if-while)

[day-166 if; while](#day-166-if-while)

[day-167 c; printf; scanf](#day-167-c-printf-scanf)

[day-168 c; while; if](#day-168-c-while-if)

[day-169 c; while; if](#day-169-c-while-if)

[day-170 pointers](#day-170-pointers)
## week - 025



[day-171 while; for; if; list](#day-171-while-for-if-list)

[day-172 if](#day-172-if)

[day-173 if; variables](#day-173-if-variables)

[day-174 if; list](#day-174-if-list)

[day-175 if](#day-175-if)

[day-176 if](#day-176-if)

[day-177 if](#day-177-if)
## week - 026



[day-178 if; absolute](#day-178-if-absolute)

[day-179 if; for](#day-179-if-for)

[day-180 if](#day-180-if)

[day-181 if](#day-181-if)

[day-182 look back](#day-182-look-back)

[day-183 generalization](#day-183-generalization)

[day-184 generalization](#day-184-generalization)
## week - 027



[day-185 generalization](#day-185-generalization)

[day-186 if](#day-186-if)

[day-187 if; while; functions](#day-187-if-while-functions)

[day-188 oop](#day-188-oop)

[day-189 keyword arguments; string methods](#day-189-keyword-arguments-string-methods)

[day-190 while](#day-190-while)

[day-191 while](#day-191-while)
## week - 028



[day-192 class; methods](#day-192-class-methods)

[day-193 richard buckland's computer](#day-193-richard-buckland's-computer)

[day-194 self modifying programs](#day-194-self-modifying-programs)

[day-195 loops](#day-195-loops)

[day-196 loops](#day-196-loops)

[day-197 interpreter](#day-197-interpreter)

[day-198 coordinates](#day-198-coordinates)
## week - 029



[day-199 coordinates](#day-199-coordinates)

[day-200 coordinates](#day-200-coordinates)

[day-201 computers](#day-201-computers)

[day-202 pointers](#day-202-pointers)

[day-203 strategy](#day-203-strategy)

[day-204 money](#day-204-money)

[day-205 fetch-decode-execute](#day-205-fetch-decode-execute)
## week - 030



[day-206 client server](#day-206-client-server)

[day-207 0; 1; infinity; how to break things down](#day-207-0-1-infinity-how-to-break-things-down)

[day-208 if; lists](#day-208-if-lists)

[day-209 if; lists](#day-209-if-lists)

[day-210 if; lists](#day-210-if-lists)

[day-211 classes](#day-211-classes)

[day-212 pico-8 follow adventure game tutorial](#day-212-pico-8-follow-adventure-game-tutorial)
## week - 031



[day-213 pico-8 adventure game](#day-213-pico-8-adventure-game)

[day-214 pico-8 follow platformer game tutorial](#day-214-pico-8-follow-platformer-game-tutorial)

[day-215 make a website](#day-215-make-a-website)

[day-216 directories](#day-216-directories)

[day-217 directories](#day-217-directories)

[day-218 variables](#day-218-variables)

[day-219 lists](#day-219-lists)
## week - 032



[day-220 lists](#day-220-lists)

[day-221 lists](#day-221-lists)

[day-222 lists](#day-222-lists)

[day-223 lists](#day-223-lists)

[day-224 lists](#day-224-lists)

[day-225 functions](#day-225-functions)

[day-226 lists](#day-226-lists)
## week - 033



[day-227 lists](#day-227-lists)

[day-228 files](#day-228-files)

[day-229 strings](#day-229-strings)

[day-229 files; strings](#day-229-files-strings)

[day-230 dictionaries](#day-230-dictionaries)

[day-231 dictionaries](#day-231-dictionaries)

[day-232 dictionaries](#day-232-dictionaries)

[day-233 scope](#day-233-scope)
## week - 034



[day-234 lists](#day-234-lists)

[day-235 lists](#day-235-lists)

[day-236 modules](#day-236-modules)

[day-237 files](#day-237-files)

[day-238 principles](#day-238-principles)

[day-239 directories](#day-239-directories)

[day-240 for](#day-240-for)
## week - 035



[day-241 lists](#day-241-lists)

[day-242 lists](#day-242-lists)

[day-243 lists](#day-243-lists)

[day-242 lists](#day-242-lists)

[day-243 lists; strings](#day-243-lists-strings)

[day-244 files; strings](#day-244-files-strings)

[day-245 lists](#day-245-lists)
## week - 036



[day-246 strings](#day-246-strings)

## [DAY-0] The Computer

All modern computers(laptops, phones, pc master race rgb monsters, etc) have somewhat similar components: Processor, Memory, Video Card, Disk and USB controller, WiFi card etc. Some of them are in one single chip and you cant even see them anymore, but they are there. For example there are chips that have Processor and Video Card together. The term for processor is actually CPU - Central processing unit, but we called it processors when we were kids and it kind of make sense, since it processes stuff.

```
+------------------+
|                  |
|  [           ]   |
|  [ Processor ]   |
|  [           ]   |
|                  |
|  [ Memory ]      |
|  [ Memory ]      |
|                  |
|  [ Video Card ]--+------> monitor
|                  |
|  [ Disk ]        |
|                  |  +---> iphone
|                  |  +---> mouse
|  [ USB ]---------+--+---> keyboard
|                  |
|  [ WiFi ]        |
|  [ ... ]         |
+------------------+

```

Memory (also called RAM), is the place where programs exist to be run by the CPU, it loads its instructions from there, and the instructions tells it what to do, it can write back to memory, or read from a different place or write something to the disk controller or to the video card, etc. Basically the most important stuff happens between the processor and the RAM (which stands for Random Access Memory). It is Random Access because the processor can just go and read or write to specific place, which is pretty cool. 

Everything in the RAM disappears when you turn off the computer, so usually the programs and all kinds of information is persistently stored on the Disk. Which is called disk because it used to be spinning, but now most computers have SSD disks which are not *disks* at all, google 'SSD versus spinning disk' if you want to find more. So when the computer starts it will load some information from the disk into memory and start the operating system, which is just a program, not very different than the one you wrote for the touch typing, it takes input, does something with it and then has some output.


## [DAY-0] Files

When you store something to disk you usually store it as a file, files can be all kinds, only text, or images, or just raw binary data used for different purposes. Text files are literally that, file that contains text, later you will learn that there is no such thing as text to the computer, all is just bits of information, but we (the humans) decided it is quite useless to look at some numbers of information, so our programs display information in different way, for example the file can contain the number 97 in its raw form 01100001, and if seen from a text editor, it will show the letter 'a', but if seem from image editor it might use it to show some blue-ish color, colors are stored in 4 numbers: transparency(called alpha), red,green and blue, but different formats use different way to store the colors, so it will depend on which format does the program think it is going to display.

See it is all in the eye of the beholder, the file still contains only 97 (01100001), but each program will decide what to do with it.

There are also Directories(also called Folders) (which in many file systems are also files.. but we will get to that later), that can contain files or other directories. Example structure looks like:

```

/
├─ home/
│  ├─ jack/
│  |  ├─ type.py
│  |  ├─ example.txt
│  |  ├─ image.jpg

```

The word File is used because people that made those things up were thinking of filing cabinet, with lots of folders that contains pieces of paper.

```
  /
  /
 /____________________
 |________  __________
 /_____  /||   |
|".___."| ||   |
|_______|/ |   |
 || .___."||  /
 ||_______|| /
 |_________|/ Felix Lee
 
```

> See how those pictures have sometimes names attached to them. Those are their creators, some pictures are from the 80s, so it is amazing we can still find out who made them. You should always attribute the work of an artist.

So the name 'File' and 'Folder' is used. If people were thinking of libraries I guess we would've been using Book for a file and Shelve for Folder? Anyway, my point is: all things have names, some of the names are strange and old, so don't worry if they make no sense.


## [DAY-0] ASCII

Computers do not understand text, so when you see text it is usually some number that is displayed as a character, for example 65 is A, 66 is B, and so on. About 60 years ago some people agreed on a common way to map number to character, called THE ASCII STANDARD, super fancy name, for such a simple thing.

```
32  SPC   64  @    96  `
33  !     65  A    97  a
34  "     66  B    98  b
35  #     67  C    99  c
36  $     68  D   100  d
37  %     69  E   101  e
38  &     70  F   102  f
39  '     71  G   103  g
40  (     72  H   104  h
41  )     73  I   105  i
42  *     74  J   106  j
43  +     75  K   107  k
44  ,     76  L   108  l
45  -     77  M   109  m
46  .     78  N   110  n
47  /     79  O   111  o
48  0     80  P   112  p
49  1     81  Q   113  q
50  2     82  R   114  r
51  3     83  S   115  s
52  4     84  T   116  t
53  5     85  U   117  u
54  6     86  V   118  v
55  7     87  W   119  w
56  8     88  X   120  x
57  9     89  Y   121  y
58  :     90  Z   122  z
59  ;     91  [   123  {
60  <     92  \   124  |
61  =     93  ]   125  }
62  >     94  ^   126  ~
63  ?     95  _

```

Try to decode: 110 105 99 101 32 119 111 114 107 33

## [DAY-0] Magic

```
 ______________     _             _,-----------._        ___
|              |   (_,.-      _,-'_,-----------._`-._    _)_)
| THE _  _  _  |      |     ,'_,-'  ___________  `-._`.
| |  / \|_)| \ |     `'   ,','  _,-'___________`-._  `.`.
| |__\_/| \|_/ |        ,','  ,'_,-'     .     `-._`.  `.`.
|              |       /,'  ,','        >|<        `.`.  `.\
| OF THE  _ _  |      //  ,','      ><  ,^.  ><      `.`.  \\
| |_)||\|/_(_  |     //  /,'      ><   / | \   ><      `.\  \\
| | \|| |\_|_) |    //  //      ><    \/\^/\/    ><      \\  \\
|______________|   ;;  ;;              `---'              ::  ::
                   ||  ||              (____              ||  ||
 DOORS OF DURIN   _||__||_            ,'----.            _||__||_
                 (o.____.o)____        `---'        ____(o.____.o)
                   |    | /,--.)                   (,--.\ |    |
                   |    |((  -`___               ___`   ))|    |
                   |    | \\,'',  `.           .'  .``.// |    |
                   |    |  // (___,'.         .'.___) \\  |    |
                  /|    | ;;))  ____) .     . (____  ((\\ |    |\
                  \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                   |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                   |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                   |    |,\  /,                     ,\  /,|    |
                   |    ||: : )          .          ( : :||    |
                  /|    |:; |/  .      ./|\,      ,  \| :;|    |\
                  \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                   |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                   |   `..   ,' `'       '       `  `.   ,.'   |
                   |    ||  :                         :  ||    |
                   |    ||  |                         |  ||    |
                   |    ||  |                         |  ||    |
                   |    |'  |            _            |  `|    |
                   |    |   |          '|))           |   |    |
                   ;____:   `._        `'           _,'   ;____:
                  {______}     \___________________/     {______}
              SSt |______|_______________________________|______|
```

Have you seen The Lord of the Rings? Do you remember the Door of Durin? Where Gandalf couldn't remember how to enter and the fellowship almost got eaten?

The experience through this book will feel like that. Sometimes you will be stuck, and I mean really really stuck, and at some point, as if the cosmos itself colludes, something will click, and you will level up. Sadly I can not know when this will happen to **you**, as every person is different.

## [DAY-0] How to Google

Anything you don't know how to do, you should use google to search for answers. However it is not easy to know what is good link to read and what is not, try to read from verified sources, like wikipedia, python.org, stackoverflow, mozilla and university websites, ask your parent to help.

There is a lot of scams on the internet, you will open websites that claim you have viruses on your computer and you need to pay 20$ to clean it, or that you need to install this amazing program that will speed up your internet. Sometimes on very trusted websites you will see ads that are pure scams, for example ads that looks like Download buttons to get the program you wanted, but it will just download a virus.

Its getting increasingly difficult to distinguish between good and bad information as well, some websites are just poorly written articles, so they can make people clicking on them in order to get money from ads. With time, and with the help of your parent you will learn how to recognize the good articles.

The rules about how to use the internet are:

* The internet is sus!
* Never put your real name or phone number or address anywhere
* Never download anything unless your parent approves
* Never run anything you downloaded (sometimes downloads just start automatically)
* Don't trust messages like 'click here to get free iPhone' or 'clean your computer for free'
* Always ask your parent for help if you are not sure.

There is noting free on the internet. Even this book, even though I am writing it for free, and you can get it for free, but I am hosting it on GitHub (and I don't pay for that), and GitHub, and therefore Microsoft, knows you are reading it, and later they will use that information to show you better ads, or maybe they will use it for some other purpose, like to train a machine to create artificial text, but one thing you must remember is that there is nothing free on the internet.

## [DAY-1] Touch Typing

Touch typing is just typing without looking, if you are super slow while typing you will get frustrated too soon.

Use https://www.keybr.com/ or ask someone to recommend you something. After using the touch typing app for few days, write your own.


## [DAY-2] Install python

In general the first thing you should do when you don't know how to do something is to google it.

So google 'how to install python', you will see lots of results, some of them will tell you how to install the old version of python, and some will be for the too old or too new version of windows. This makes things a bit more difficult.

Try to download from https://www.python.org/downloads/ and do it yourself, ask your parent for help if you are stuck.


## [DAY-2] Make a useful program

After you have installed python3 run IDLE (ask your parent for help) and go to File -> New File and type:

```
import random
letters = 'fjfjfjfjfjfjjfghghghgaa;a;a;abcdefghijklmnopqrstuvwxyz'
difficulty = 2

while True:
    q = ''
    for i in range(difficulty):
        q = q + random.choice(letters)

    a = input(q + ': ')
    if a == q:
        difficulty += 1
    else:
        if difficulty > 2:
            difficulty -= 1
```

Then hit F5 (this will ask you to save the file as well) to run the program. If it is too easy, try adjusting the difficulty or the letters.

The program will ask you to type some letters, after you are done, hit enter, and it will ask you for more or less letters. It will keep doing that forever. It kind of looks like this:

```
aj: aj
akg: akg
jjgh: jjgh
```

If you type it correctly, it will ask for a bigger sequence of characters, and if you make mistake it will ask for smaller. 

Don't rush it.

Place your fingers properly on the keyboard, open https://images.google.com and search for 'touch typing' you will see many images of how to place your fingers.


## [DAY-3] Touch Typing using your program

Open IDLE again, go to File -> Open File, and find where you saved your program, then double click to open it. After opened hit F5 and it will start again.

Spend the rest of the time for the day touch typing. Don't rush it. Place your fingers properly on the keyboard and slowly type the letters.

> Spend the whole day touch typing and making and opening new files in IDLE and notepad; I cant stress enough how important it is for the kid to be independent to be able on its own to make or open a file.


## [DAY-4] HTML - Basics

We will start with HTML.

Making a page can be a bit overwhelming, so just start small. for example:

Open notepad and make a file on your desktop named "first.html", then write in it:

```
<html>
  <body>
   <h1>welcome!</h1>
   <p>this is my page</p>
  </body>
</html>
```

Open Windows Explorer and find the file on your desktop and double click on it. 

Congrats! You have made your first web page!


Now try this:

```
<html>
  <body>
    <marquee>
      <h1>check this out!</h1>
    </marquee>
    <mark>Why would somebody use this?</mark>
  </body>
</html>
```

The rest of the day you will just try some other examples:

List:

```
<html>
  <body>
    <ul>
      <li>first <b>item</b></li>
      <li>second <i>item</i></li>
      <li>third</li>
    </ul>
  </body>
</html>
```

Horizontal Line:

```
<html>
  <body>
    first
    line<br>
    second line<br>
    <hr>
    third line<br>
  </body>
</html>
```

'br' means line break, when the browser sees it know it has to show whatever comes next on another line, 'hr' means horizontal rule,just like when you take your ruler and draw a line from left to right in the text book. You see, even though you write things in separate lines (like the word first and line are clearly on separate lines), the browser will not know what to do until you tell it to 'br'. Maybe in school you had a project you have to use PowerPoint to make a presentation? With the special words ul, li, br, hr, h2 and b you can make your own presentation in HTML!


## [DAY-5] HTML - Basics

The app you are using right now to see this website is called a web browser, I don't know if kids still call it like that, but adults do.

First the browser app downloads the web page, which is just a normal text file (it is what you see when you click on View Source), then it has to process it, in the same way you read pigpen code or ascii code, you look symbol by symbol and try to make sense out of it by making it into letters you understand.

It looks for word between '<' and then '>', when it sees '<' it knows what ever is between '<' and '>' is important word. Then it has kind of a table so it know what to do with different words, when it sees 'b' it knows that whatever is inside is gonna get **bold**. There are many words like that you should try for yourself 'b' 'i' 'u' 'h1', and many more.

For example, try this on your page: `<b>this is bold</b>`


## [DAY-6] Touch Typing

Spend half the time using your program and half the time on keybr.com.
## [DAY-7] New Touch Typing Program

Make new file on your desktop, touchtyping.html and type in it:

```
<center>
  <pre style="font-size: 30px; letter-spacing: 4px;" id="question"></pre>
</center>

<script>
var makeNewQuestion = function() {
  var letters = 'fjfjfjfjfjfjjfghghghgaa;a;a;abcdefghijklmnopqrstuvwxyz'
  var difficulty = 10
  var q = []
  for (var i = 0; i < difficulty; i++) {
    q.push(letters.charAt(Math.floor(Math.random() * letters.length)));
  }
  return q
}

var currentQuestion = makeNewQuestion()
var questionElement = document.getElementById("question")
questionElement.innerHTML = currentQuestion.join("")

var position = 0
document.body.addEventListener('keydown', (e) => {
  if (e.key == currentQuestion[position]) {
    position++
    if (position == currentQuestion.length) {
      currentQuestion = makeNewQuestion()
      position = 0
    } else {
      currentQuestion[position-1] = '<b>' + currentQuestion[position-1] + '</b>'
    }
    questionElement.innerHTML = currentQuestion.join("")
  }
})
</script>
```

Don't worry about what it all means. Just type it character by character. Now double click on the file and try out your program, just start typing as the web page is open, and characters will become bold as you type them.

## [DAY-8] Touch Typing

Today just spend the day chilling on keybr.com

> We spend considerable amount of time on touchtyping and learning english, not all the time spent is reflected in the book, but at least 2 times per week, either on our own practice programs or keybr.com, by day 190 my daughter is at around 50 words per minute and blind typing. The amount spend typing builds really good relationship with the computer, as it has extremely smooth learning curve, and sense of progression. In contrast with programming which is a learning staircase, with walls you have to break through, and sometimes you have to spend months on the same level until the puzzle pieces click together. Some days when she is frustrated or tired I just ask her to type for 20-30 minutes while listening to music, which turns into a bit of meditating experience.

## [DAY-9] Touch Typing using your program

Open touchtyping.html and spend the day using your awesome program. Once you open it, right click and then click on `View Source` to remember that you actually wrote this! Good job!

## [DAY-10] HTML - Basics

From now on the HTML examples will be more code and less text, so you just have to go through them with your parent.

```
<html>
    <body>
        <h2>welcome!</h2>
        <p>
            this is my <b>first web page</b> it has also <i>weird twist</i>!
        </p>
        <hr>
        <p>
            and a line
        </p>
    </body>
</html>
```

Try to touch type as you are writing this, no need to hurry.

```
<html>
<body>
    <h2>welcome!</h2>
    <p>
        this is my <b>first web page</b>!
    </p>
    and it has a bug!<br>
    <button onclick="document.body.appendChild(this.cloneNode(true))">🐛</button>
</body>
</html>
```

This is a funny one, you might not know how to write 🐛, but just google 'bug emoji' and copy it from there. After you open the web page, click on the bug to see what happens.

You see we add this `onclick=...` which is code that is going to run every time you click on the bug, and what this code does it copies the button and adds it to the page, including the `onclick=..` stuff, so the other button you can press and it will copy itself again!

Try to add more buttons by yourself with other emojis, 🏍️, 🏂, 🐓 or 🐧 for example.


## [DAY-11] HTML - Basics

Making a presentation with HTML

```
<html>
    <body style="font-size: 24px;">
        <h1>Presentation For School</h1>
        <small>by: John, from class 4</small>
        <br>
        <br>
        <br>
        <br>
        <br>
        <hr>

        <h1>First Slide</h1>
        <ul>
            <li>Something</li>
            <li>very <b>important</b></li>
            <li>and very <i>strange</i></li>
        </ul>
        <br>
        <br>
        <br>
        <hr>
        <h1>Second Slide</h1>
        <ul>
            <li>Something Else</li>
            <li>very <u>underline</u></li>
            <li>and very <del>weird</del></li>
        </ul>
        <br>
        <br>
        <br>
        <hr>
        <h1>Third Slide</h1>
        <ul>
            <li>... surely we can come up with a line</li>
            <li>... and another line</li>
        </ul>
        <br>
        <br>
        <br>
        <hr>
    </body>
</html>
```

## [DAY-12] Touch Typing

Use your program to touch type or go to keybr.com. 

Don't rush.


## [DAY-13] HTML

This day is completely free style, try to put all kinds of HTML words inside each other, for example:

```
<html>
  <body>
    <marquee>
      <ul>
        <li>
          <h1>
            <i>
              hello
            </i>
          </h1>
        </li>
      </ul>
    </marquee>
  </body>
</html>
```

Try to add the self cloning 🐛 button to that page.
## [DAY-14] HTML - Tables

Tables are amazing, in fact, tables are one of the things that makes the modern world work. In your school for example, there is a table with the name of each student and their score. Or in your TV there is a table with each program number and the program there (e.g. 24 is 24 Kitchen). On your iPhone there are many programs that use many tables internally to make decisions. There is of course the ASCII table, which can tell you how to get from a character to its raw representation and the other way around. The periodic table is also a famous example. The table on the bus stop tells you which bus will come at what time.

We use tables everywhere.

Here are few examples:

| power | pokemons |
|-|-|
| electiricy | Pikachu |
| fire | Charmander |
| grass | Bulbasaur  |
| poison | Bulbasaur  |


Or something you have probably seen, a multiplication table:

| a | x | b | =  |
|---|---|---|----|
| 5 | * | 5 | 25 |
| 5 | * | 6 | 30 |
| 5 | * | 7 | 37 |


Make new file (or open the some old html page) and type this:
```
<html>
  <body>
    <table border="10">
      <tr><th>Name</th><th>Year</th></tr>

      <tr>
        <td>
            Donald Duck
        </td>
        <td>
            1937
        </td>
      </tr>
      <tr>
        <td>
            Daisy Duck
        </td>
        <td>
            1940 
        </td>
      </tr>
      <tr>
        <td>
            Scrooge McDuck
        </td>
        <td>
            1947
        </td>
      </tr>
      <tr>
        <td>
            Ludwig Von Drake
        </td>
        <td>
            1961
        </td>
      </tr>
    </table>
  </body>
</html>
```

Only 3 new tags we have to learn `table, tr, td, th` are the main things we will work with, `tr` means table row and `td` is table data cell, or a column, `th` is table header. All the html key words you have learned so far are called `tags` or `elements`.

Make `<table border="100">` and see what happens.

## [DAY-15] HTML - More tables

```
<html>
  <body>
    <table border="10">
      <tr><th>Name</th><th>Year</th></tr>

      <tr>
        <td>
            <marquee>
              hello world
            </marquee>
        </td>
        <td>
          <marquee>
            hello universe
          </marquee>
        </td>
      </tr>
      <tr>
        <td>
            <b>this does not move</b>
        </td>
        <td>
            <marquee>
              <i>this is italic</i>
            </marquee>
        </td>
      </tr>
    </table>
  </body>
</html>
```

Now make list in a table

```
<table border=100>
  <tr>
    <td>
      <ul>
        <li>a</li>
        <li>b</li>
        <li>c</li>
      </ul>
    </td>
    <td>
      <ol>
        <li>a</li>
        <li>b</li>
        <li>c</li>
      </ol>
    </td>
  </tr>
</table>
```

Super small difference between `ul` and `ol`, one means 'unordered list' and the other one 'ordered list', so if you use `ol` every `li` will have its own number




## [DAY-16] HTML - Multiplication table

Start writing the whole multiplication table
(will take more than 1 day)

## [DAY-17] HTML - Multiplication table
Finish writing the whole multiplication table.

## [DAY-18] Touch Typing
Spend the day touch typing.

## [DAY-19] HTML - Links

The most powerful feature of HTML is to be able to link to another place in the internet, try this:

```
<html>
    <body>
        hi, <a href="https://wikipedia.com">click here</a> to go to wikipedia
    </body>
</html>
```

The `a` tag with its `href` attribute is one of the most important things of the modern internet, it means I can have a web page, and I can link to someone else's web page, and they can link to someone else and so on..

Whatever is in the `href` attribute this is where the browser will go after you click on whatever is inside the `<a></a>`, in our case `click here`. So after you click on `click here` your browser will go to wikipedia.com, and from there when you click somewhere it will go to wherever that `a`'s `href` points to.

## [DAY-20] HTML - Tree

Rainbow:

```
<html>
    <body>
        <h1>🌈</h1>
        <h1 style="color: red;">red</h1>
        <h1 style="color: orange">orange</h1>
        <h1 style="color: yellow">yellow</h1>
        <h1 style="color: green">green</h1>
        <h1 style="color: blue">blue</h1>
        <h1 style="color: indigo">indigo</h1>
        <h1 style="color: violet">violet</h1>
    </body>
</html>
```

You dont always need `html` and `body`, the most browsers will show a page anyway, but it is good practice to do it proper and use `html` and `body` tags. Anyway, the next example is not "up to code".

IT will make a sheep that follows your mouse, its pretty cool.

```
<div id='sheep' style='position:absolute'>🐑</div>
<script>
    var sheep = document.getElementById('sheep')
    document.body.onmousemove = (e) => {
        sheep.style.left = (e.clientX - 5 + 'px');
        sheep.style.top = (e.clientY - 5 + 'px');
    }
</script>
```

And a ghost button! it will remove itself when you press it.

```
<button onclick="this.parentNode.removeChild(this)">👻</button>
```

The way it works is `onclick=...` will call the code when you click on the button, in this case it says, "whoever *my* parent is, tell it to remove myself form its children list".

You see, HTML is like a tree, let me show you.

lets say our page is:

```
<html>
  <body>
    <table border="10">
      <tr><th>Name</th><th>Year</th></tr>

      <tr>
        <td>
            <mark>
              hello
            </mark>
        </td>
        <td>
          <h1>
            world
          </h1>
        </td>
      </tr>
      <tr>
        <td>
            <b>move</b>
        </td>
        <td>
            <marquee>
              <i>italic</i>
            </marquee>
        </td>
      </tr>
    </table>
  </body>
</html>
```

It actually is a tree, every tag has children, and siblings 
```
                 <html>
                   |
                 <body>
                   |
                 <table>
                /   |   \
               /    |    \
              /     |     \
             /      |      \
            /       |       \
           /        |        \
        <tr>      <tr>       <tr>         <--- siblings, same parent
         /\        / \        / \
        /  \      /   \      /   \
      <th> <th> <td>  <td>  <td> <td>     <--- the two td with same parent
      |      |    |     |    |     |           are siblings
     Name  Year <mark> <h1> <b>  <marquee>
                  |      |   |      |
                hello world move   <i>
                                    |
                                  italic
       
```

Well trees in the world are actually the other way around haha. Leave it to programmers to not know how to make a tree :)

```

                                  italic
                                    |
                hello world move   <i>
                  |      |   |      |
     Name  Year <mark> <h1> <b>  <marquee>
      |      |    |     |    |     |
      <th> <th> <td>  <td>  <td> <td>
        \  /      \   /      \   /
         \/        \ /        \ /
        <tr>      <tr>       <tr>
           \        |        /
            \       |       /
             \      |      /
              \     |     /
               \    |    /
                \   |   /
                 <table>
                   |
                 <body>
                   |
                 <html>
```

But you can see how all things that have the same parent are related, like brothers and sisters.

This is very important, we will spend the next week thinking about it as well.
## [DAY-21] HTML - View Source

Browsers on laptops or pcs will allow you to rightclick on any page and then click on `View page source`, this will show you the HTML of the page your are looking at.

Open https://archive.org then right click on the pager and then click on `View page source`.

We will spend the rest of the day looking at some page sources

* https://archive.org
* https://www.spacejam.com
* https://www.asciiart.eu/
* https://www.wikipedia.org
* https://www.gutenberg.org/
* https://digitalcomicmuseum.com/
* https://www.terrypratchettbooks.com/
* https://www.goodreads.com/

## [DAY-22] HTML - Inspect


Make new html file and write the following example:

```
Right click on this page, click Inspect and then go to Console.
<script>
    console.log('🐺🐺🐺🐺 You can see that in the console. 🐺🐺🐺🐺')
    console.log('🐺🐺🐺🐺 type 12312*18237978123 in the console and see what happens. 🐺🐺🐺🐺')
</script>
```

Open the file and then click F12, or right click on the page and click Inspect. You will see the logs.

This will open the developer tools of your browser, you will be able to see the console, where you can run small programs or see the errors and the logs of the current page. Try writing `12312*18237978123` in the console and see the result.

In the inspector you can also modify the HTML that you see. This wont modify the actual page on the server you are downloading from, but you can try things to see how they would look. There are actually many scammers that use this method to lie to people as if they are giving them money, or they say 'I will teach you how to add 10000 robux to your account if you pay me 5$' and they just show you how to inspect and edit the html you see. This does not actually give you robux of course, it just modifies your local version of the html to show different value and after you reload the page you will see the old value.

Lets try it. Make a new file with this content:

```
<html>
  <body>
    Your Robux Balance is: <b>0$</b>
  </body>
</html>
```

Open the file and then right click on `0$` and click inspect. Then you will see `<b>0$</b>` if you double click on it, you will be able to change it, and you will see the new version. Now reload the page, and you will see the old value is back.


## [DAY-23] HTML - Images

To show an image you need the `img` tag, and give it `src` attribute with the address of the image, for example if I want to display https://picsum.photos/id/237/200/300 I have to do type it like this:

```
<html>
  <body>
    <img src="https://picsum.photos/id/237/200/300">
    <img src="https://picsum.photos/id/40/200/300">
  </body>
</html>
```

Lets put the images in a table:

```
<html>
  <body>
    <table>
      <tr>
        <td>
          <img src="https://picsum.photos/id/237/200/300">
        </td>
        <td>
          <img src="https://picsum.photos/id/40/200/300">
        </td>
      </tr>
    </table>
  </body>
</html>
```

Now of course we can have `img` in `a`, try this:

```
<html>
  <body>
    <table>
      <tr>
        <td>
          <a href="https://wikipedia.com">
            <img src="https://picsum.photos/id/237/200/300">
          </a>
        </td>
        <td>
          <a href="https://gutenberg.org">
            <img src="https://picsum.photos/id/40/200/300">
          </a>
        </td>
      </tr>
    </table>
  </body>
</html>
```

Now you can click on the dog or the nose and it will lead you to the pages you link to.

Is it possible to have `img` and text in `a`? Well I am glad you asked!

```
<html>
  <body>
    <table>
      <tr>
        <td>
          <a href="https://wikipedia.com">
            <img src="https://picsum.photos/id/237/200/300">
            <br>
            This dog leads to wikipedia
          </a>
        </td>
        <td>
          <a href="https://gutenberg.org">
            <img src="https://picsum.photos/id/40/200/300">
            <br>
            This cat (I think) leads to guttenberg.org
          </a>
        </td>
      </tr>
    </table>
  </body>
</html>
```

I even have `<br>` in the `a`, now you can click either on the image or on the text.

There is one more very important attribute of the `img` tag, and this is the `alt` attribute, it is used by people who are blind or visually impaired to know what kind of picture is on the page. In our example we can put `alt="puppy"` on the puppy picture.

```
<p>
  Hello, and welcome to my page.
  I hope you will like this image.
</p>
<img src="https://picsum.photos/id/237/200/300" alt="puppy">
```

If a blind person visits this page, they use a screen reader that reads most of the text on the page, and if we have `alt` attribute on images it will say `Image ...` and whatever the value of `alt` is, in our case "puppy". So the reader will say:

```
Hello, and welcome to my page. I hope you will like this image. 

Image puppy.
```

If you have an image that has no information, like it is just there to make the site pretty, use `alt=""` then the screen reader will skip it.


## [DAY-24] Licenses

If you take a picture of something you are the owner of that picture, and you can put it on your website and say you have the rights of that picture. It is up to you to decide if people should link to it by deciding what under license you will publish the image. There are many licenses you can choose from, there are some that say 'this picture is free for anyone to do whatever they want' or 'you can republish the picture but you cant make money selling it' or 'you can publish it but not print it in books' etc etc.

Complicated stuff this licensing, but the thing you have to remember, it is up to the creator to decide under what license their work can be distributed.

Some licenses you can check out with your parents:

* Creative Commons Licenses CC-BY https://creativecommons.org/licenses/
* GPL https://www.gnu.org/licenses/gpl-3.0.en.html
* MIT License https://opensource.org/licenses/MIT
* Apache License https://www.apache.org/licenses/LICENSE-2.0
* Public Domain https://en.wikipedia.org/wiki/Public-domain-equivalent_license
* Copyright https://en.wikipedia.org/wiki/Copyright

When you want to use someone else's work and it is not clear what license it uses, it is best to ask them. At least that is what I do. People are usually nice and they give me permission to use their work.

It is somewhat controversial what is the right way forward, which license to use and what is the best for you and for the world. Ask to your parent about what happens when you take a picture of a painting of a picture of a video and then you edit the video to include the picture you took in it..

Check out https://tldrlegal.com/ for super short description of licenses

## [DAY-25] Touch Typing

relax and spend the day touch typing

## [DAY-26] HTML - Title

```
<html>
  <head>
    <title>THIS IS SPARTA</title>
  </head>
  <body>
    <marquee>
      <ul>
        <li>
          <a href="https://wikipedia.com">click me</a>
        </li>
        <li>
          <mark>hello world</mark>
        </li>
      </ul>
    </marquee>
  </body>
</html>
```

Usually bodies have a `<head>` hehe.

In html in the `head` tag you can put things that will help the browser. For example, what is the `title` of this page? or what language is this page? Who is the author of this page? etc..

You can also put there some style, changing the body's background color, or the color of the text in the `h1` or `p`:

```
<html>
  <head>
    <style>
      body {
        background: blue;
      }
      p {
        color: pink;
      }
      h1 {
        color: cyan;
      }
    </style>
    <title>some title</title>
  </head>
  <body>
    <center>
      <p>
        Hello Universe
      </p>
      <h1>hello world</h1>
    </center>
  </body>
</html>
```

The _language_ we use inside the `style` tag is called `CSS`, and it is quite simple (on its surface). We wont get deep into it for a while, but if you are interested check out at https://developer.mozilla.org/en-US/docs/Web/CSS

You see how in certain tags we can use different language, not html, like in `<style>` we use CSS, in `<script>` we use JavaScript, we are going to do more work with it soon, but you can check out at https://developer.mozilla.org/en-US/docs/Web/JavaScript

## [DAY-27] HTML - Fun (JS)

Many buttons

```
<button onclick="makeManyButtons()">🤖</button>
<script>
    function makeManyButtons() {
        // try to make million buttons!

        for(var i = 0; i < 100; i++) {
            var button = document.createElement('button')
            button.innerText = '🐹'
            document.body.appendChild(button)
        }
    }
</script>
```

Replicator

```
<button onclick="replicate(10,'🦊')">🤖</button>
<script>
    function replicate(n,buttonText) {
        // try to make million buttons!

        for(var i = 0; i < n; i++) {
            var button = document.createElement('button')
            button.onclick = function () {
                replicate(20,'🦓')
            };
            button.innerText = buttonText
            document.body.appendChild(button)
        }
    }
</script>
```


Canvas

```
<html>
<body style="padding: 0; margin: 0">
<canvas id="squares"></canvas>
<script>
var canvas=document.getElementById('squares');
var ctx=canvas.getContext("2d");
canvas.width=window.innerWidth;
canvas.height=window.innerHeight;

function draw() {
   ctx.fillStyle= '#' + Math.floor(Math.random()*16777215).toString(16);
   ctx.globalAlpha=0.5;

   var size=Math.floor((Math.random()) * 60) + 1;
   var x = Math.floor(Math.random()*canvas.width)
   var y = Math.floor(Math.random()*canvas.height)

   ctx.fillRect(x, y, size, size);
};

setInterval(draw,10);
// why dont you try to make them rectangles instead of squares?
// or maybe even circles? google for 'canvas fillRect' and 'canvas arc'
</script>
</body>
</html>
```

The last one is quite crazy! But I am sure you will like the result when done.
## [DAY-28] Print; Functions; While; Variables; Conditions

Make a new file form IDLE, and write in it:
```
print("Hi!")
```

Hit F5 and enjoy!

Your first(or second) python program.. Quite useless, but nevertheless. A program is a program!

`print()` is called a function, functions are kind of mini useful programs, this one will print whatever you tell it. In this case `print("Hi!")` will output `Hi!`. Pretty amazing, I hope one day to explain to you what goes into showing a character on your screen. Remind me to show you Ben Eater's 6502 videos when you grow up.

`"Hi!"` is a string, strings are just series of characters, you can make them in python with `"something"` or `'something'`, either single quotes or double quotes.

```
while True:
  print("Hi!")
```

`while True` that means forever. so you will see:

```
Hi!
Hi!
Hi!
Hi!
Hi!
Hi!
Hi!
Hi!
...

```

Hi forever.


```
while 1 == 1:
  print("Hi!)
```

`1 == 1` is also True, so this is the same as `while True`

So `while <condition>` will keep running the code **inside** it, while the condition holds true, which in the case of `1 == 1` will always be the case.

```
while True:
  zzz = input("what is your name: ")
  print(zzz)
```


`input` asks you to type something, and it returns whatever you typed.

`zzz = input(....)` takes whatever input returns, and puts it into memory that we can use later. `zzz` is just a name I picked so I can refer to this value later in the program, in this case on the next line when I do `print(zzz)`

`print(name)` prints whatever is in the memory pointed by `zzz`.

`zzz` is called a `variable`, you can choose the names of your variables, and `zzz` is surely a poor name, because if I use it 100 lines later in the code, I will forget what kind of information it stores, so usually we give names of the variables that make sense, for example:

```
while True:
  name = input("what is your name: ")
  print(name)
```

A group of statements with common parent, is called **code block**, in python we use spaces to say what belongs where, so the closest `while,for,if,elif,else` going up is the parent.

```
while True:
  name = input("what is your name: ")
    print(name)
```

Will throw an error: `IndentationError: unexpected indent` because it makes no sense, there is no valid parent to `print`, This is quite unique in python, most other languages make code blocks with `{}`, but python makes it prettier and easier to read by using indentation (the spaces/tabs). `print(name)` has 4 spaces, while `name = input..` has 2 spaces, so python expect everything in the `while:` to have 2 spaces unless a new block starts.

```
while True:
  name = input("what is your name: ")
  if name == "pikachu":
    print(name)
```

This works fine, `print(name)` now has valid parent that also has a parent.

```
while True:
  | \
  |  \
  |   \
  |    \
 if:   name = input
  |
print(name)
```

`while True` has two children, `name = input ..` and `if name == ..` so they must have same indentation, then `if ..:` also expects a code block, so the children of  `if name == ..` need to have one more indentation to whatever indentation the `if` had.

Anyway..

Don't worry too much about it, just don't panic when you see `IndentationError`, and I can promise you, you will see a lot of those. Look at where you got the spaces wrong, and if the block has correct parent.

You have seen by now in JavaScript we use `{}` to group statements into blocks.

```
if (name == "pikachu") {
  console.log("pikaaaachuuuuu")
  console.log("evolutiooonn!")
}
```

Now lets break out of the loop!

```
while True:
  name = input("what is your name: ")
  if name == "pikachu":
    break
```

`if name == "pikachu":` will run the code inside `if` if whatever is in the `name` variable is equal to the string "pikachu". In this case its only 1 instruction inside it, the `break` instruction.

`break` breaks out of the closest `while` loop, so basically this program will ask what is your name until you type pikachu. It is a bit boring because we never actually print what you typed.

```
while True:
  name = input("what is your name: ")
  print(name)
  if name == "pikachu":
    break

print("DONE")
```

There we go, now it will ask you to type a name, it will print whatever name you typed, and then it will check if the name is equal to "pikachu" it will break the while loop and stop asking. We can actually write this program in a different way. After you break out of the loop, it just continues to execute the program below, in this case will print DONE.

```
name = ''
while name != "pikachu":
  name = input("what is your name: ")
  print(name)

print("DONE")
```

MAGIC!

we start by making name equal to empty string, a string with no characters, and then we check is the statement `name != "pikachu"` True? If this is True we will execute the code **inside** the while loop, after the last instruction in the loop, the program jumps back to `while name != "pikachu"` and checks again is name still not equal to "pikachu"? if the statement is False it will not run the code **inside** but will continue, in the above example it will print DONE, because this is the first thing **after** the while loop.

Lets make a more complicated one, this one will ask you what is your name, and if you answer pikachu will print pikaaaaaaachuuuuu and stop, any other answer it will print "Hello, " + answer, so if you type "Jane" it will show "Hello, Jane" and it will ask again.

```
while True:
  name = input("what is your name: ")
  if name == "pikachu":
    print("pikaaaaaaachuuuuu")
    break
  else:
    print("Hello, " + name)
```


In python you can add two strings, if you type "charmander" for name, `x = "Hello, " + name`  will make x to be equal to "Hello, charmander". You can't do `"hello" - name`, but you can do `"hello" * 5` and get "hellohellohellohellohello".



`while,if,else,break` are keywords, kind of like `<html>` and `<body>`, `<h1>` etc, those are coming from python itself. There are not many python keywords, for reference, this is the **complete** list:

```
False
True
None

and      ->   name == "pikachu" and age == "33"
or       ->   name == "pikachu" or name == "charmander"
not      ->   not name == "pikachu" is the same as name != "pikachu"

for      -> used if you know how many times you want to do something
while    -> do something until condition is True
break    -> break out of the for or while loop 
continue -> go to the start of the while/for loop and continue from there

if       -> if something is true
elif     -> else if something else is true
else     -> else do this

in       -> checks if something is in somethhing else, e.g. "pika" in name
def      -> make a function

as
assert
async
await
class
del
except
finally
from
global
import
is
lambda
nonlocal
pass
raise
return
try
with
yield
```

THATS THE WHOLE LANGUAGE, there are no more keywords.



## [DAY-29] Print; If

```
print("Welcome to the forest!")
print("This is a world of magic and wonders. You are on a cross road, you can go north east south or west.")
print("South leads to the swamps, where the aligators live")
print("West leads to the mountains, where the yeti lives")
print("North leads to the jungle, where the tigres live")
print("East leads to the desert, where the meerkats live")
print("")

what = input("what would you do next: ")

if what == "east":
  print("Welcome to the desert")
  print("It is very hot, and you need remember to put sun screen.")
  print("Oh, you remember to put your hat as well.")
  print("In the distance you see a meerkat approaching.")
  print("What would you do? Run or Fight the meerkat?")
  print("")

  what = input("what would you do next: ")
  if what == "run":
    print("You start running, and the meerkat is super fast, it catches you in no time.")
  elif what == "fight":
    print("You try to fight it, but turns out it was friendly and wants to become your friend.")
    print("What would you do?")
    print("")
    what = input("Do you want to be its friend: ")

    if what == "yes":
      print("Great! Now the meerkat wants to introduce you to his family.")
    elif what == "no":
      print("The meerkat starts crying!")

  else:
    print("I dont understand: " + what)
```

That is a lot of typing.

In python there are few very important things. First even though it doesn't look like it, it is actually a tree, like HTML tree. The parent of `print("The meerkat starts crying!")` is `elif what == "no":`

```
                    |
                    |
              if what == "east"
                   |
                 / |  \
                /  |   \
               /   |    \
              /    |     \
             /     |      \
          if      else    elif
    what == "run"  |     what == "fight
          |        |        |
        print   print      / \
                          /   \
                         /     \
                        /       \
                      if        elif
                what == "yes" what == "no"
                     |            |
                  [ ... ]      [ ... ]
```

Lets discuss another example:

```
a = "he"
b = "ll"
c = "o"
if a == "he":
  if b == "ll":
    if c == "o":
      print("hello")
```

Can you tell who is the parent of who?

BTW, you can also use `and`, `or` and `not` when you want to see if something is `True`

```
a = "he"
b = "ll"
c = "o"
if a == "he" and b == "ll" and c == "o":
  print("hello")
```

## [DAY-30] Functions; Lists

Our game is quite limited, and a quick step to improve it is to make you ask where you want to go until you pick one of the options.

```
def ask(possible_answers):
  answer = ''
  print("---") # print empty line
  while True:
    answer = input("> What would you do next: ")
    if answer not in possible_answers:
      print("> try again, it must be one of:", possible_answers)
    else:
      return answer

print("Welcome to the forest!")
#...

what = ask(["east","west","north","south"])

if what == "east":
  print("Welcome to the desert")
  #...

  what = ask(["run","fight"])
  if what == "run":
    print("You start running, and the meerkat is super fast, it catches you in no time.")
  elif what == "fight":
    print("You try to fight it, but turns out it was friendly and wants to become your friend.")
    # ...
    what = ask(["yes","no"])
    if what == "yes":
      print("Great! Now the meerkat wants to introduce you to his family.")
    elif what == "no":
      print("The meerkat starts crying!")
elif what == "north":
  print("Welcome to the north pole, it is super cold here.")

```

`ask` is a function, just like `print` or `input`, it will keep asking you `> What would you do next: ` until the answer you type is in the possible_answers list, and if it is it will return it to wherever it is called from. So when we have `zzz = ask(["yes","no"]` the value of `zzz` will be whatever is returned from `ask`. Same as `name = input("what is your name)` will put in `name` whatever is returned from `input` which is whatever you typed on your keyboard.

To make a function in python you need to use the `def` keyword.

```
def sum(a,b):
  return a + b

r = sum(1737,1231231)
print(r)
```

Whatever is between `def` and `(` is the name of the function, in the above example its `sum`. Between `()` you put in the name of the variables you expect to use when someone calls your function. I want to sum two numbers, I dont know what the numbers are, so I just make two variables `a, b` and expect whoever calls my function to give me the numbers, like `r = sum(1737,1231231)`


## [DAY-31] Functions; If; Random; Lists

FIGHT TO THE DEATH!

```
import random
import time

def fight(playerHP, enemyHP, enemy_name):
  # fight to the death!

  while playerHP >= 0 and enemyHP >= 0:  
    punch = random.randint(0, 20)
    if random.choice(["player","enemy"]) == "player":
      playerHP = playerHP - punch
      print("<"+enemy_name+"> hits you for " + str(punch) + ", " + str(playerHP) + " left")
    else:
      enemyHP = enemyHP - punch
      print("you hit <"+enemy_name+"> for " + str(punch) + ", " + str(enemyHP) + " left")

    time.sleep(1)

  return playerHP


fight(100, 50, "meerkat")
```

`import` imports a module.

`random` and `time` those are the `modules` you import, modules are just a group of functions that you can use, for example `time.sleep(1)` makes python sleep for 1 second, it calls the function `sleep()` in the `time` module. `random.choice()` you can give a list of things to choose from, and it will randomly select one of the list. `random.randint(0,20)` means give me a random number between 0 and 20.

`str` is needed to convert integer to string, because 1 is not the same as "1", "1" is actually the ASCII value of the character 1, so somehow we have to convert the raw number 1 to ASCII code 61, and `str()` does that.

lets use it now in our dungeon game

```
import random
import time

def ask(possible_answers):
  ...

def fight(playerHP, enemyHP, enemy_name):
  ...

...

health = 100

what = ask(["east","west","north","south"])
if what == "east":
  ...
  what = ask(["run","fight"])
  if what == "run":
    ...
  elif what == "fight":
    meerkatHP = 50
    health = fight(health, meerkatHP, "meerkat")
    if health <= 0:
      print("GAME OVER! THE MEERKAT BEAT YOU")
    else:
      print("You won against the meerkat, you have " + str(health) + " HP left))
```


## [DAY-32] Lists; While

Today you have to make only two programs:

```
bad = ["broccoli","chocolate","pineapple"]

while True:
  food = input("what is your favorite food: ")
  if food in bad:
    print("ewwwww I hate " + food)
  else:
    print("yumm, I love " + food)
```


And the second one:

```
bad = ["broccoli","chocolate","pineapple"]
good = ["pizza","popcorn"]
while True:
  food = input("what is your favorite food: ")
  if food in bad:
    print("ewwwww I hate " + food)
  elif food in good:
    print("yumm, I love " + food)
  else:
    print("I have never tried " + food)
```

Great job!

Spend the rest of the day touch typing.

## [DAY-33] For

`for` does something number of times, if I want to print the numbers from 0 to 99, I could do:
```
for i range(100):
  print(i)
```

or

```
for i in range(10, 20):
  print(i)
```
will print the numbers from 10 to 19

```
colors =  ["red","green","blue"]
for color in colors:
  print(color)
```

will print each of the elements in the list. If you want to print each character of a string in a similar way you can do:

```
name = "jack"
for c in name:
  print(c)
```

prints:

```
j
a
c
k
```


## [DAY-34] Love Tester

```
def love_test(a,b):
  sum = 0
  for c in a+b:
    print(c + ': ' + str(ord(c)))
    sum += ord(c)

  print('sum is:' + str(sum))
  return sum % 100


while True:
  nameA = input("first name: ")
  nameB = input("second name: ")

  print("love test: " + str(love_test(nameA,nameB)))
```

`ord` takes the ascii code of a character.

`%` is the remainder, so `109 % 100` is 9, basically what is left after you can cleanly divide two numbers, `812 % 100` is 12, you can fit 100 in 819 exactly 8 times, and then there is 12 left, this 12 is the remainder.

So in this program we take two names into the variables `nameA` and `nameB` and then we give them to the love_test function, which sums the ascii code of `nameA+nameB`, and then returns the remainder of 100.

```
first name: jack
second name: jane
j: 106
a: 97
c: 99
k: 107
j: 106
a: 97
n: 110
e: 101
sum is:823
love test: 23
```

BTW, now you know how those "professional" love testers are made, so if you use https://www.lovetester.nl/ or something similar.. don't read too much into the result. You can easily tweak it to do whatever you want.


## [DAY-34] Touch Typing

Whoaa it has been a difficult week.

Relax with some touch typing.


## [DAY-35] Lists; While; Continue

This week there will be less talking and more programming.


Make a program to help you to decide what to do:

```
import random

possible = ["nothing"]
while True:
  x = input("What would you like to do: ")
  if x == "done":
    break
  else:
    possible.append(x)

what = random.choice(possible)
print("possible choices: ")
print(possible)
print("the magic 8 ball decided: " + what)
```


Make a program to help you multiply two numbers:

```
while True:
  a = int(input("first number: "))
  b = int(input("second number: "))
  print(a, "*", b, "=", a*b)
```

Here I do a little trick, and make print print numbers instead of making them into string by passing it as separate parameters to the print function. otherwise I have to do:

```
while True:
  a = int(input("first number: "))
  b = int(input("second number: "))
  print(str(a) + " *" + str(b) + "=" + str(a*b))

```


What is your spy name?

```
name = input("what is your name: ")
print("Your spy name is: " + name[0] + name[1])
```

You can get individual characters from string by picking them up with `[]` so if name is 'jane' then `name[0]` is 'j'


Make a calculator
```
while True:
  a = int(input("first number: "))
  b = int(input("second number: "))
  op = input("operation * / + :")
  result = 0
  if op == "*":
    result = a * b
  elif op == "/":
    result = a/b
  elif op == "+":    
    result = a+b
  else:
    print("I dont understand " + op)
    continue
  print(a,op,b,'=',result)
```

See how we use `continue` to not print a result if we don't understand the operation. `continue` jumps to the beginning of the loop.



## [DAY-36] While; Range; Functions

Print the numbers from 0 to 9 FOREVER

```
while True:
  for i in range(10):
    print(i)
```

Print each character of a string:

```
name = input("what is your name: ")
for c in name:
  print(c)
```

Sum the numbers from 0 to 99

```
sum = 0

for i in range(100):
  sum = sum + i
print(sum)

```

Print all the prime numbers from 0 to 100:

```
def is_prime(n):
  if n == 1 or n == 0:
    return False

  for i in range(2, n):
    if n % i == 0:
      return False

  return True

for i in range(100):
  print(i, is_prime(i))
```

multiply two numbers:

```
a = int(input("number 1: "))
b = int(input("number 2: "))
c = a * b

print(c)
```


Timer:

```
import time

s = int(input("how many seconds: "))
for i in range(s):
  print(i)
  time.sleep(1)

print(s, "SECONDS ARE OVER")
```

## [DAY-37] While; Functions

Clock 

```
import datetime
import time
import os

while True:
  os.system('clear')
  now = datetime.datetime.now()
  print(now)
  time.sleep(1)

```

Calendar

```
def show(calendar):
    for row in calendar:
        for day in row:
            print(day,end=' ')
        print('')

june = [
    ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'],
    ['  ', '  ', ' 1', ' 2', ' 3', ' 4', ' 5'],
    [' 6', ' 7', ' 8', ' 9', '10', '11', '12'],
    ['13', '14', '15', '16', '17', '18', '19'],
    ['20', '21', '22', '23', '24', '25', '26'],
    ['27', '28', '29', '30', '  ', '  ', '  '],
]

show(june)
```

Growing list of food.

```
food = []

while True:
  what = input("what is your favorite food: ")
  food.append(what)
  print(what)
```


Guessing game

```
colors = ["red","green","blue"]
score = 0
while True:
  guess = input("guess a color: ")
  if guess in colors:
    print("good guess! I like " + guess)
  else:
    print("nop, I dont like " + guess)
```

Guess again

```
def is_in_list(list,what):
  for element in list:
    if element == what:
      return True
  return False

colors = ["red","green","blue"]
score = 0
while True:
  guess = input("guess a color: ")
  if is_in_list(colors, guess):
    print("good guess! I like " + guess)
  else:
    print("nop, I dont like " + guess)
```

## [DAY-38] Strings

What was your name again?

```
for i in range(10):
  name = input("what is your name: ")
  print(i)
  print(name)
```

First and last letter:

```
name = input("what is your name: ")
print("first letter: " + name[0])
print("last letter: " + name[len(name)-1])
```

to get the last letter we have to count however letters are in the whole name, so `len(name)` will return 4 for 'jane' and it counts from 1

```
len("jane"):

j a n e
1 2 3 4


len("ja")

j a
1 2

```

but when we are using `[0]` to get to specific character from a string or element from a list, it counts from 0, so

```
j a n e
0 1 2 3

name = "jane"
name[0] is j
name[1] is a
name[2] is n
name[3] is e

len(name) is 4 (because len counts from 1)
so name[len(name) - 1], is name[4 - 1] or name[3] which is the last letter
```


Make a Line

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

line(20, '#')
line(30, '*')
line(40, '_')
```

Make a triangle

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

for i in range(100):
  line(i,'*')
  print('')
```

Make a beam

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

for i in range(50):
  line(i, ' ')
  line(i, '*')
  print('')
```

Make a box

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

def box(width,height,symbol):
    for y in range(height):
        line(width,symbol)
        print('')

box(16,20)
box(10,20,'#')
box(15,13,'*')
```

## [DAY-39] Touch Typing

Do some touch typing.

## [DAY-40] Functions; Strings; Range


Make inverse beam

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

count = 50
for i in range(count):
  line(count - i, ' ')
  line(i, '*')
  print('')
```

Make a tree

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

count = 50
for i in range(count):
  half = int((count-i)/2)
  line(half , ' ')
  line(i, '*')
  print('')
```

Inverse

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

count = 50
for i in range(count):
  line(count-i, '*')
  print('')
```

Inverse tree

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

count = 50
for i in range(count):
  half = int(i/2)
  line(half , ' ')
  line(count-i, '*')
  print('')
```


Art

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')

while True:
  count = 10
  for i in range(count):
    line(count-i, '*')
    print('')

  for i in range(count):
    line(i, '#')
    print('')
```

Looks so pretty!

```
#
##
###
####
#####
######
#######
########
#########
**********
*********
********
*******
******
*****
****
***
**
*

#
##
###
####
#####
######
#######
########
#########
**********
*********
********
*******
******
*****
****
***
**
*

```

## [DAY-41] Basics of Basics

More Art

```
import random

def line(width, symbol):
    for x in range(width):
        print(symbol,end='')


symbols = ['*','#','%','^','&']
while True:
  count = random.randint(5,80)

  symbol = random.choice(symbols)
  for i in range(count):
    line(count-i, symbol)
    print('')

  symbol = random.choice(symbols)
  for i in range(count):
    line(i, symbol)
    print('')
```


Staircase

```
def line(width, symbol):
    for x in range(width):
        print(symbol,end='')


count = 100
for i in range(0, count, 5):
  line(i, '*')
  print('')

```

Range is so cool, and you didnt even notice!

Try this:
```
for i in range(0, 100, 10):
  print(i)
```

it will print 
```
0
10
20
30
40
50
60
70
80
90
```

so every 10th number, now try:

```
for i in range(0, 100, 5):
  print(i)
```

and

```
for i in range(0, 100, 2):
  print(i)
```

Of course you dont have to start counting from 0:

```
for i in range(50, 100, 2):
  print(i)
```

Do some touch typing if there is time left.
## [DAY-41] Lists; If; While

```
import random

words = ["pizza","pikachu","ball","pokemon"]

while True:
  word = random.choice(words)
  guessed = []
  life = 10
  while True:
    
    print('*' * 10, ' HANGMAN ', '*' * 10)

    matching = 0
    for c in word:
      if c in guessed:
        print(c,end='')
        matching = matching + 1
      else:
        print('-',end='')
    print('')
    print('*' * 31)
    

    if matching == len(word):
      print('congratz you won!')
      break

    character = input("guess a character: ")
    if character in word:
      guessed.append(character)
    else:
      print(character + " is not in the word, " + str(life) + ' lives left') 
      life = life - 1
      if life == 0:
        print('you lost!')
        break
```


## [DAY-42] Lists; Functions; Grid; While

World without a player

```
def render(world):
  for row in world:
    for col in row:
      print(col,end=' ')
    print('')

def empty():
  return  [
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
]

world = empty()

render(world)
while True:
  row = int(input("which row (count from 0): "))
  col = int(input("which column (count from 0): "))

  world[row][col] = 'x'
  render(world)

```

World with a player

```
def render(world):
  for row in world:
    for col in row:
      print(col,end=' ')
    print('')

def empty():
  return  [
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
]

world = empty()
player_row = 0
player_col = 0
world[player_row][player_col] = 'x'

render(world)
while True:
  direction = input("which direction: ")
  
  world[player_row][player_col] = '*'
  if direction == "up":
    player_row = player_row - 1
  elif direction == "down":
    player_row = player_row + 1
  elif direction == "left":
    player_col = player_col - 1
  elif direction == "right":
    player_col = player_col + 1

  world[player_row][player_col] = 'x'
  render(world)

```

## [DAY-43] If; Range


Even and Odd

```
number = int(input("give me a number: "))
if number % 2 == 0:
  print("this number is even")
else:
  print("this number is odd")
```


Fizz Buzz

Print integers 1 to N, but print "fizz" if an integer is divisible by 3, "buzz" if an integer is divisible by 5, and "fizzbuzz" if an integer is divisible by both 3 and 5.

```
n = 100

for i in range(1,n+1):
  if i % 5 == 0 and i % 3 == 0:
    print("fizz buzz")
  elif i % 3 == 0:
    print("fizz")
  elif i % 5 == 0:
    print("buzz")
  else:
    print(i)
```

or different version

```
n = 100
for i in range(1,n+1):
  fizzbuzzing = False
  if i % 3 == 0:
    fizzbuzzing = True
    print("fizz", end = '')

  if i % 5 == 0:
    fizzbuzzing = True
    print("buzz", end = '')

  if not fizzbuzzing:
    print(i, end = '')

  print('')
```

There are many ways to write this, lets just have fun.

```
n = 100
numbers = []

# first make empty list with 100 elements
for i in range(1, n+1):
  numbers.append('')

# then fill in the fizzes
for i in range(1, n+1):
  if i % 3 == 0:
    numbers[i-1] += 'fizz'

# then fill in the buzzess
for i in range(1, n+1):
  if i % 5 == 0:
    numbers[i-1] += 'buzz'

# then fill in the numbers
for i in range(1, n+1):
  if numbers[i-1] == '':
    numbers[i-1] = i

# then we print it
for x in numbers:
  print(x)
```

Haha this is a funny way to make fizzbuzz. See first it puts fizz if you can divide it by 3, and then buzz if you can divide it by 5, but if there was already fizz there it will just add if with `+=`, so it automatically works to put fizzbuzz for 15.

## [DAY-44] Lists

Reviews

```
reviews =[5,3,2,4,1,2,3,4,2,1,5,5,3,2]

sum = 0
for r in reviews:
  sum += r

rating = sum / len(reviews)
print(str(rating) + "⭐ out ot 5")
```

Icecream Maker

```
import random
flavors = ['vanilla','chocolate','blue','banana','bluberry']

flavorA = random.choice(flavors)
flavorB = random.choice(flavors)

print(flavorA + " + " + flavorB)
```

Spend the rest of the day touch typing.

## [DAY-45] Lists; Functions

Different touch typing

```
import random
vowels  = ['a', 'e', 'i', 'o', 'u', 'y']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

def make_word(n_chars):
  word = ''

  for i in range(n_chars):
    if random.randint(1,100) < 40:
      word += random.choice(vowels)
    else:
      word += random.choice(consonants)
  return word

def make_sentence(n_words):
  sentence = ''
  for i in range(n_words):
    sentence += make_word(random.randint(3,6))
    sentence += ' '

  # this will remove the last element from the sentence string
  # so we dont have empty space in the end
  return sentence[:-1]

while True:
  sentence = make_sentence(random.randint(10,20))
  print(sentence)
  guess = input('write the sentence: ')
  if guess != sentence:
    print("SORRY")
  else:
    print("GOOD JOB")
```

spend the rest of the day trying it out

## [DAY-46] Basic Turtle

Some turtle!

```
import turtle
turtle.circle(30)
```

Many circles

```
import turtle
for i in range(30):
  turtle.circle(i)
```

Bigger circles

```
import turtle

turtle.color("blue")
for i in range(30):
  turtle.circle(50 + i)
```

Smile

```
import turtle

turtle.color("blue")
turtle.circle(100)
turtle.penup()
turtle.goto(60,120)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(20,120)
turtle.pendown()
turtle.circle(20)
turtle.penup()
turtle.goto(-30,20)
turtle.pendown()
turtle.right(45)
turtle.circle(20, 120)
```


## [DAY-47] Range; While

Try to make a program that prints a symbol N times, where N is coming from the user input.

Try by yourself.

## [DAY-48] Strings; Functions

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
## [DAY-49] List; Dictionaries

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

## [DAY-50] Lists; If

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
## [DAY-51] Internet Awareness - Scams/Viruses

Today is an important day, its Internet awareness day.

Make the most expensive drone on amazon.com cost 0€, or even -5€. As we did in the first week, open inspect click on the mouse selector (or press Control+Shift+C) and click on the price you want to change, then double click on the HTML and change it to whatever you want.

After you are done reload the page to see it is not actually changed.

Now do that on roblox, make it look like you have 999999 robux.

Go to google and search for `Speed up your internet connection`, go over the websites one by one with your parent, and observe, look at many many scams, some are very easy to fall into, some are obvious.

Open youtube.com, search for 'free energy hack' watch some of the videos, then search for 'electroboom free energy' and watch Mehdi explain why it is a scam. Search for 'be carefull what you order from facebook ads' Pleasant Green and watch how he explains a scam with ads to buy a cool looking helmet.

See the internet is a place, where you can find great things, like electroboom and pleasant green or veritasium or vsauce, but also where there are horrible things, like people selling garbage for 30$. Or people claiming 

Now with your parent, search on youtube for 'how to hack in roblox' and look at the scame, how people want to install something so they can steal your password.

## [DAY-52] Internet Awareness - How Login Works

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
console.log(JSON.stringify(cookies))
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

That is why if you open facebook.com and press F12 you will see giant message:

```
STOP STOP STOP

This is a browser feature intended for developers. If someone has told you to copy and paste something here to enable a Facebook feature or "hack" someone else's account, it is a scam and they are trying to access your Facebook account.
```

When you Logout from somewhere, they delete the token on their side, so the next time a request is made, they know you are not logged in anymore. That is why its important to logout if you use someone else's computer to login.


## [DAY-53] Basics of the Internet - IP/DNS

The internet is a mess, a mess of things that talk to each other. Each of the things has their own IP address (ip stands for internet protocol), for example open https://1.1.1.1 you see this is a simple ip address of a popular DNS server (dns is a system we use to resolve names into ip addresses, e.g. facebook.com is 31.13.64.35). You can check the ip address by searching 'whats my ip' on google, and because your browser has to connect to google's server and they connect through their IP addresses, so google knows your IP. Of course it is a bit more complicated than that, but for now this will do.

The other most important thing is domain names, like facebook.com and yahoo.com or amazon.de. We need names otherwise everyone will have to remember 31.13.64.35 to open facebook.. which is not easy. To find out the ip of facebook.com you need to ask a .com server about which server is responsible for facebook.com, and then ask this server about what is the ip address of www.facebook.com. The whole system is like a tree.

```
        ROOT
         "."
        / | \
       /  |  \
    .de .com .io
     /    |
 amazon  /|\
        / | \
       /  |  \
      /   |   \
     /    |    \
 amazon netflix yahoo

```

your internet provider gives you your ip address and also a convenient name server to use, you can also use other name servers like 1.1.1.1 or 8.8.8.8, keep in mind, whoever nameserver you use, knows which websites you visit, because you have to ask them about the ip address of each website you visit.

A lot of scammers also ask you to change your dns server, they lie about getting faster internet and etc, but you see, if you ask a scammer's dns server 'what is the ip address of facebook.com', and they say 'well its 12.12.12.12' or whatever their server's address is, they can show you a webpage that looks like facebook, but its theirs, and when you login they can get your password. Remember when you login your browser sends the password to the other server that has to check it, so they can steal it that way.

To prevent this kind of attacks modern browsers use something called HTTPS, or secure http, you see a small closed lock on the address bar, and when you click it it will say 'Connection is secure', that means that it verified that the website you opened is actually the website you think it is. There are ways to attack this as well, but it is not trivial, and someone has to have physical access to your computer to install a new Trusted Certificate Authority (which we will explain way later).

But one more reason to be sus of people using your computer. Not only they can steal your cookies, but they can also install a new Trusted CA, change the DNS and then intercept all your requests.

## [DAY-54] Touch Typing

Touch typing day is finally here! Enjoy keybr.com!



## [DAY-55] Lists; Functions

Tic Tac Toe

```
def empty_game():
    game = [
      [' ','a','b','c','d'],
      ['1','-','-','-','-'],
      ['2','-','-','-','-'],
      ['3','-','-','-','-'],
      ['4','-','-','-','-']
    ]
    return game

def show_game(game):
    for row in game:
        #[' ','a','b','c','d']
        #...
        for col in row:
            #' '
            #'a'
            #'b'
            print (col, end=' ')
        print('')


g = empty_game()
x_or_zero='x'
while True:
    show_game(g)
    p = input('place ' + x_or_zero + ': ')

    if p == 'a1':
        g[1][1]=x_or_zero
    if p == 'a2':
        g[2][1]=x_or_zero
    if p == 'a3':
        g[3][1]=x_or_zero
    if p == 'a4':
        g[4][1]=x_or_zero

    if p == 'b1':
        g[1][2]=x_or_zero
    if p == 'b2':
        g[2][2]=x_or_zero
    if p == 'b3':
        g[3][2]=x_or_zero
    if p == 'b4':
        g[4][2]=x_or_zero

    if p == 'c1':
        g[1][3]=x_or_zero
    if p == 'c2':
        g[2][3]=x_or_zero
    if p == 'c3':
        g[3][3]=x_or_zero
    if p == 'c4':               
        g[4][3]=x_or_zero

    if p == 'd1':
        g[1][4]=x_or_zero    
    if p == 'd2':
        g[2][4]=x_or_zero
    if p == 'd3':
        g[3][4]=x_or_zero
    if p == 'd4':
        g[4][4]=x_or_zero


    if p == 'clear':
        g = empty_game()

        
    if x_or_zero =='x':
        x_or_zero = '0'
    else:
        x_or_zero='x'

```

Spend the rest of the day playing.

## [DAY-56] Functions; If; Random

Trivia game

```
def check(question, answer):
    x = input(question + ": ")
    if x == answer:
        return True
    else:
        return False


score = 0
if check("which animal lives on the north pole?", "polar bear"):
    score += 1
if check("which animal lives in the jungle?", "tiger"):
    score += 1

print("your score is: " + str(score))
```

Math test:

```
import random

while True:
    a = random.randint(1,10)
    b = random.randint(1,10)

    r = int(input("what is " + str(a) + " * " + str(b) + "? " ))

    if r == a * b:
        print("Correct!")
    else:
        print("Incorrect, the answer was: " + str(a * b))
```

Random characters

```
import random

while True:
    x = random.randint(ord('a'), ord('z'))
    print(chr(x))
```


## [DAY-57] Lists; Functions; Grid

Snake

```
import random
APPLE_SYMBOL = '@'

def render(world):
  for row in world:
    for col in row:
      print(col,end=' ')
    print('')

def empty():
  return  [
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
  ['-','-','-','-'],
]

def snake_eats_itself(positions, current_col, current_row):
    for (col,row) in positions:
        if col == current_col and row == current_row:
            return True

def place_apple(world):
    # just place it on a random square from all possible squares
    possible = []
    for index_row in range(len(world)):
        for index_col in range(len(world[index_row])):
            if world[index_row][index_col] == '-':
                possible.append((index_col,index_row))

    if len(possible) == 0:
        # we cant place an apple
        return False
    else:
        (col,row) = random.choice(possible)
        world[row][col] = APPLE_SYMBOL
        return True
    
world = empty()
player_row = 0
player_col = 0
player_history = []

world[player_row][player_col] = '%'
player_history.append((player_col,player_row))


place_apple(world)
render(world)


while True:
  direction = input("which direction: ")
  
  world[player_row][player_col] = '='
  if direction == "u":
    player_row = player_row - 1
  elif direction == "d":
    player_row = player_row + 1
  elif direction == "l":
    player_col = player_col - 1
  elif direction == "r":
    player_col = player_col + 1
  else:
      print("try again, u for up/d for down/l for left/r for right")
      continue
  if snake_eats_itself(player_history, player_col, player_row):
      print("GAME OVER")
      break

  if world[player_row][player_col] == APPLE_SYMBOL:

      world[player_row][player_col] = '$'
      if not place_apple(world):
          print("YOU WON!")
          break
  else:
      world[player_row][player_col] = '%'

  player_history.append((player_col,player_row))

  render(world)

```

## [DAY-58] Continue Previous Day

Keep working on the snake game if you are not done. if you are do touch typing

## [DAY-59] Tuples; Lists

Tuples are kind of like lists that you cant grow or shrink, but also you usually assign meaning to each of the positions, for example

```
position = (1,2)

(x,y) = position
print(x)
print(y)
```

it can have more elements

```
posittion = (1,2,3)
(width,depth,height) = position

print(width)
print(depth)
print(height)
```

You see how we used it in the snake game, to make a list of tuples, where we had the player history.

```
positions = [(1,2),(3,4),(5,6)]
print(positions)
for p in positions:
    print(p)
    (x,y) = p
    print(x)
    print(y)
```

It is quite handy when you know you have pairs of data, like X and Y position or Season number and Episode number.

```
favorite_miraculous = [(3,1),(3,2),(2,1)]

for m in favorite_miraculous:
    (season,episode) = m
    print(str(season) + " season episode: " + str(episode))
```

Or more than 2 pieces, you can hold however many you want, but it usually is you that assign meaning to each position, like in the above case, the first element we decide is season, and the second one we decide is episode

## [DAY-60] Go Back In Time

Back to the beginning.

* Write a program to make a spy name
* Write a program to ask for favorite food
* Write a program to ask what is your name forever


## [DAY-61] PyGame; PyGameZero; Coordinates

open `cmd` and run:

```
pip install pygame
pip install pgzero
```

then make a circle

```
import pgzrun
WIDTH = 400
HEIGHT = 400
 
def draw():
    screen.clear()
    x = WIDTH/2
    y = WIDTH/2
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

Now lets move it:

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400

x = WIDTH/2
y = WIDTH/2

def on_mouse_down(pos):
    global x,y
    (mouse_x, mouse_y) = pos

    x = mouse_x
    y = mouse_y


def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

Move it with keyboard

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
STEP = 10
x = WIDTH/2
y = WIDTH/2


def on_key_down(key):
    global x,y
    if key == keys.LEFT:
        x -= STEP
    elif key == keys.RIGHT:
        x += STEP
    elif key == keys.UP:
        # coordinates start 0,0 on the upper left corner
        y -= STEP
    elif key == keys.DOWN:
        y += STEP

def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

Lets say we have 400 width and 300 height window

```
(0,0)
  +---------------------------+
  |                           |
  |                           |
  |                           |
  |                           |
  |                           |
  |                           |
  +---------------------------+
                          (400, 300)
```

top left corner is y = 0 and x = 0, bottom right is `x = 400` and `y = 300`. So when we move 'UP' with the keyboard we actually have to decrease `y` instead of increasing it like in `turtle`, where 0,0 is in the center of the screen, so top left is `(-half_x, -half_y)` and bottom right is `(half_x, half_y)`

## [DAY-62] Collisions; Callbacks


Smooth movement.

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
STEP = 10
x = WIDTH/2
y = WIDTH/2


def update():
    global x,y
    if keyboard.LEFT:
        x -= STEP
    elif keyboard.RIGHT:
        x += STEP
    elif keyboard.UP:
        y -= STEP
    elif keyboard.DOWN:
        y += STEP

def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.circle(pos, radius, 'white')
 
pgzrun.go()
```

`pgzero` will call your `update` function 60 times per second, and now it will just check at the time of the call, is `keyboard.UP`, and if it is it will just move. Which is completely different, where each time you press the `up` key the `on_key_down` function is called. So previously you had ot press the key every time to move, now you can just hold it.

Where do those `keyboard` and `screen` magic variables come from? In python there is such thing as `__builtin__` which literally adds new keywords, kind of like `input` or `print`, when you `import pgzrun` it will import also those builtins. `Actor`, `Rect`, `keyboard` etc.. you can check them at https://pygame-zero.readthedocs.io/en/stable/builtins.html

COLLIDE!

![game-62.png](./screenshots/game-62.png "game 62 screenshot")


```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
STEP = 10
x = WIDTH/2
y = WIDTH/2

box = Rect((20,20),(100,100))

game_over = False


def update():
    global x, y, game_over
    if keyboard.LEFT:
        x -= STEP
    elif keyboard.RIGHT:
        x += STEP
    elif keyboard.UP:
        y -= STEP
    elif keyboard.DOWN:
        y += STEP

    if box.collidepoint((x,y)):
        game_over = True

def draw():
    screen.clear()
    pos = (x,y)
    radius = 30
    screen.draw.rect(box, color="red")
    screen.draw.circle(pos, radius, 'white')

    if game_over:
        screen.draw.text("GAME OVER", (50, 30), color="blue")
 
pgzrun.go()

```

## [DAY-63] Functions

Catch the snake

![game-63.png](./screenshots/game-63.png "game 63 screenshot")

Make images/ folder and download the images from https://github.com/jackdoe/programming-for-kids. When you say `Actor("c1")` it will look for `c1.png` in images/ folder in the current directory.

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
elf = Actor("c1")
snake = Actor("snake")
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def update():
    global game_over, speed, score
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0

    if elf.colliderect(snake):
        score += 1
        speed += 1
        place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))                         
pgzrun.go()

```


## [DAY-64] Lists; Functions

Many Snakes

![game-64.png](./screenshots/game-64.png "game 64 screenshot")

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 1
speed = 1
elf = Actor("c1")
snakes = []
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snakes():
    global snakes
    snakes = []
    for i in range(score):
        snake = Actor("snake")
        snake.x = random.randint(10,WIDTH-10)
        snake.y = random.randint(10,HEIGHT-10)
        snakes.append(snake)

place_snakes()

def update():
    global game_over, speed, score, snakes
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0
        snakes = []
        place_snakes()
    for s in snakes:
        if elf.colliderect(s):
            score += 1
            speed += 1
            place_snakes()

def draw():
    screen.fill('black')
    elf.draw()
    for s in snakes:
        s.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))                         
pgzrun.go()
```
## [DAY-65] Functions; Collisions

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
game_over = False
elf = Actor("c1")
snake = Actor("snake")
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def update():
    global game_over, speed, score
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0

    if elf.colliderect(snake):
        score += 1
        speed += 1
        place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))                         
pgzrun.go()

```


## [DAY-66] Schedule; Callbacks; Functions

Catch as many snakes as you can in 5 seconds.

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

game_over = False
score = 0
speed = 1
elf = Actor("c1")
snake = Actor("snake")
elf.x = WIDTH/2
elf.y = HEIGHT/2
def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def time_is_up():
    global game_over
    game_over = True

def update():
    global game_over, speed, score
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0

    if elf.colliderect(snake):
        score += 1
        speed += 1
        place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))

    if game_over:
        screen.fill('blue')
        screen.draw.text("GAME OVER, Score: "+ str(score), color="white", topleft=(10,10))

clock.schedule(time_is_up, 5)
pgzrun.go()
```


You see we just overwrite the screen with 'blue' and write another text, but you can still move in the back and the score will update if you catch a sneak.

If you want to stop the hero to move outside of the window, simply restrict elf.x and elf.y to be smaller than 0 or bigger than WIDTH and HEIGHT

Example:


```
def update():
    ...
    if keyboard.left:
        elf.x = elf.x-speed
        if elf.x > WIDTH:
            elf.x = WIDTH

```

## [DAY-67] Lists; Functions

Cross the road. Work with your parent to find images for the game, you need few cars, fox and a door. If not just use the existing assets from your images/ folder

```
import pgzrun
import random

HEIGHT = 1000
WIDTH = 1200

score = 0
step = 5
coin_speed = 1
fox = Actor("fox")
gate = Actor("door")
gate.y = HEIGHT - 50
gate.x = WIDTH/2 - 20
cars=[
    [Actor("car-2"),Actor("car-5"),Actor("car-3")],
    [Actor("car-1"),Actor("car-5")],
    [Actor("car-3"),Actor("car-4"),Actor("car-2")],
]

for a in cars:
    for (coin_index,f) in enumerate(a):
        f.x += coin_index * int(WIDTH/len(a)) + 30
def move_coins():
    for (index,a) in enumerate(cars):
        for (coin_index, f) in enumerate(a):
           
            f.y = (index * int(HEIGHT/len(cars))) + int(HEIGHT/len(cars))/2
            f.x += coin_speed
            if f.x > WIDTH:
                f.x = 0

game_over = False
move_coins()

def update():
    global score
    global step
    global game_over
    global coin_speed
    if keyboard.left:
        fox.x = fox.x-step
        if fox.x <0:
            fox.x=0
    if keyboard.right:
        fox.x = fox.x+step
        if fox.x >WIDTH:
            fox.x=WIDTH
    if keyboard.up:
        fox.y =fox.y-step
        if fox.y <0:
            fox.y=0
    if keyboard.down:
        fox.y= fox.y+step
        if fox.y >HEIGHT:
            fox.y=HEIGHT
    if keyboard.R:
        game_over = False
        score = 0
        fox.x = 0
        fox.y = 0
        coin_speed = 1
    for i in cars:
        for s in i:
            if fox.colliderect(s):
                game_over = 1 == 1

    if fox.colliderect(gate):
        fox.x = 0
        fox.y = 0
        score += 1
        coin_speed += 2
    move_coins()

def draw():
    screen.fill('black')
    fox.draw()
    gate.draw()

    for i in cars:
        for k in i:
            k.draw()
    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))
    if game_over:
        screen.fill("blue")
        screen.draw.text("Final Score: "+ str(score), color="white", topleft=(10,10),fontsize=60)    
                         
pgzrun.go()
```

## [DAY-68] Lists; Functions

Shoot bullets and remove them from the list, play sound, and also level up after killing 3 snakes!


![game-68.png](./screenshots/game-68.png "game 68 screenshot")

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
elf = Actor("c1")
snake = Actor("snake")
beep = tone.create('A3', 0.5)

elf.x = WIDTH/2
elf.y = HEIGHT/2
bullets = []

def place_snake():
    snake.x = random.randint(10,WIDTH-10)
    snake.y = random.randint(10,HEIGHT-10)

place_snake()

def bullet_out_of_screen():
    # just delete the first bullet
    bullets.pop(0)

def on_key_down(key):
    if key == keys.SPACE:
        b = Actor("bullet2")
        b.x = elf.x + 5
        b.y = elf.y
        animate(b, pos=(WIDTH + 100, elf.y), tween='accelerate', on_finished=bullet_out_of_screen)
        bullets.append(b)

def update():
    global game_over, speed, score, bullets
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0
        elf.image = "c1"
        bullets = []

    for b in bullets:
        if b.colliderect(snake):
            score += 1
            speed += 1
            if score == 3:
                elf.image = "c2"
            beep.play()
            place_snake()

def draw():
    screen.fill('black')
    elf.draw()
    snake.draw()
    for b in bullets:
        b.draw()

    screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))

pgzrun.go()
```

You see how we are adding, bullets to a list every time you press 'space'. Now the problem is we need to clean up that list at some point, otherwise it will grow a lot, and every time we do `for b in bullets` it will bet slower and slower. Computers can only do so many things per second.

So when the animation finishes, it will call `bullets_out_of_screen`, and from there we just say `bullets.pop(0)` which will remove the first element in the list of bullets, which is the oldest bullet. So if you press space 5 times, the list will have 5 items, and each of them will finish and will remove the first element.

Lets say you pressed space 3 times, and shot 3 bullets, so the list, and how the bullets are traveling kindof looks like this:

```
0 -> bbbbbbbbbbbbbb
1 -> bbbbbbb
2 -> bbbb
```

So you see when 0 finishes because it is the oldest, when it does bullets.pop(0), it will actually delete itself.

pretty cool!

## [DAY-69] Sockets; Functions; Callbacks

![game-69.png](./screenshots/game-69.png "game 69 screenshot")

Multiplayer!

```
import pgzrun
import socket
import threading
import sys

HEIGHT = 200
WIDTH = 200
MULTIPLAYER_PORT = 5025
OTHER_COMPUTER_IP = "192.168.0.10"

speed = 4
me = Actor("c1")
other = Actor("c2")

me.x = WIDTH/2
me.y = HEIGHT/2

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("0.0.0.0", MULTIPLAYER_PORT))

data = None
def multiplayer():
    global data
    while True:
        data, addr = socket.recvfrom(1024)

def update():
    if data != None:
        message = data.decode("utf8")
        (x,y) = message.split(":")

        other.x = float(x)
        other.y = float(y)


def on_key_down(key):
    if key == keys.LEFT:
        me.x = me.x-speed
    if key == keys.RIGHT:
        me.x = me.x+speed
    if key == keys.UP:
        me.y = me.y-speed
    if key == keys.DOWN:
        me.y= me.y+speed

    if key == keys.Q:
        sys.exit(0)

    message = bytearray(str(me.x) + ':' + str(me.y),"utf8")
    socket.sendto(message, (OTHER_COMPUTER_IP, MULTIPLAYER_PORT))

def draw():
    screen.fill('black')
    me.draw()
    other.draw()


threading.Thread(target=multiplayer).start()

pgzrun.go()
```

There are two important parts here, first is the `socket` and then the `Thread`. For now we will leave them a mystery. But basically every time you press the UP/DOWN/LEFT/RIGHT key your computer sends a message "currentX:currentY" to the other computer, and when the other computer receives it, it stores it in the global `data` variable, then in the `update` function it splits the message by `:` and extract the `x` and `y` and sets it to the `other` actor.

The `multiplayer()` function runs in a separate thread, or you can think of a separate process, so we are doing two things in the same time, the game loop (which is one `while True`) and the multiplayer loop which is also `while True`.


## [DAY-70] Lists; Functions

print numbers in a list

```
data = [1,2,3,4,5]
for item in data:
    print(e)
```


```
list_of_lists = [[1,2,3,4,5], [1,2,3], [4,5,6]]
for l in list_of_lists:
    for item in l:
        print(item)
```


```
list_of_list_of_lists = [[[1,2,3,4,5], [1,2,3], [4,5,6]], [[1,2,3,4,5], [1,2,3], [4,5,6]]]
for list_of_lists in list_of_list_of_lists:
    for l in list_of_lists:
        for item in l:
            print(item)
```


```
list_of_list_of_list_of_lists = [
    [
        [
            [1,2,3,4,5],
            [1,2,3],
            [4,5,6]
        ],
        [
            [1,2,3,4,5],
            [1,2,3],
            [4,5,6]
        ]
    ],
    [
        [
            [1,2,3,4,5],
            [1,2,3],
            [4,5,6]
        ],
        [
            [1,2,3,4,5],
            [1,2,3],
            [4,5,6]
        ]
    ],
]

for list_of_list_of_lists in list_of_list_of_list_of_lists:
    for list_of_lists in list_of_list_of_lists:
        for l in list_of_lists:
            for item in l:
                print(item)
```


```
def sum(x):
    r = 0
    for item in x:
        r += item
    return r

data = [1,2,3,4,5]
print(sum(data))
```


```
def sum(x):
    r = 0
    for l in x:
        for item in l:
            r += item
    return r

data = [[1,2,3,4,5], [1,2,3,4,5]]
print(sum(data))
```

## [DAY-71] Strings; Integers; While; Functions
make a calculator

```
while True:
    n1 = int(input("number 1: "))
    n2 = int(input("number 2: "))
    op = input("operation +/-* : ")
    r = 0

    if op == "quit":
        break
    elif op == "+":
        r = n1 + n2
    elif op == "-":
        r = n1 - n2
    elif op == "*":
        r = n1 * n2
    else:
        print("i dont know " + op)
        continue

    print(n1, op, n2, '=',r)

```

sum numbers from input

```
def sum(x):
    r = 0
    for item in x:
        r += item
    return r

x = []
while True:
    k = input("enter number: ")
    x.append(int(k))
    print(x)
    print(sum(x))

```
## [DAY-72] Reading Code

Reading code is even more important than writing it, and it is more difficult than reading a book, because the story does not develop top to bottom. You have to see the important pieces, and how they are linked together. Where are things assigned and changed and how are those pieces related. For example in the touch typing program, you have a couple of functions, you can study them on their own, and know what they do, and then see how they are used and make sense of the whole program, without even running it.

We will go over a couple of programs we wrote before, the rock paper scissors game, the bullet shooting game, and one of the touch typing programs.

![day-72-0.jpg](./reading/day-72-0.jpg "day 72 example 0")

![day-72-1.jpg](./reading/day-72-1.jpg "day 72 example 1")

![day-72-2.jpg](./reading/day-72-2.jpg "day 72 example 2")


Those are just examples, you have to print the programs and go over them with your parent.

## [DAY-73] Reading Code

More reading today, those are a couple of examples from the earlier days, the love tester, the fight function from the text game, the hangman game and first touch typing program.


![day-73-0.jpg](./reading/day-73-0.jpg "day 73 example 0")

![day-73-1.jpg](./reading/day-73-1.jpg "day 73 example 1")

![day-73-2.jpg](./reading/day-73-2.jpg "day 73 example 2")

![day-73-3.jpg](./reading/day-73-3-0.jpg "day 73 example 3")

Again you can use something else as well, those are just the ones I picked. Be messy with the pencil, connect things together!

## [DAY-74] Strings; While; Lists

Today its up to you what to write, my kid came up with those programs:

1. Ask forever what your favorite sport is, if yours is not here use https://emojipedia.org/ to find good emojis.

```
while True:
    k = input('what is your favorite sport: ')

    if k == 'soccer':
        print('⚽')
    elif k ==  'hockey':
        print('🏑')
    elif k == 'tennis':
        print('🎾')
    elif k == 'volleyball':
        print('🏐')
    elif k == 'table tennis':
        print('🏓')
    elif k == 'baseball':
        print('⚾')
    elif k == 'basketball':
        print('🏀')
    elif k == 'golf':
        print('🏌️‍♂️')
    else:
        print('i dont now ' +k)
```

2. and one simple, append and pop from a list.

```
k = []
while True:
    s = input('What are you thinking of: ')
    if s == 'pop':
        k.pop(0)
    else:
        k.append(s)
    print(k)
```

## [DAY-75] Functions; Callbacks; Lists; Encoding

![game-75.png](./screenshots/game-75.png "game 75 screenshot")


Enemies come to get you, and you shoot half moons at them. pretty cool.

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

score = 0
speed = 1
elf = Actor("c1")

beep = tone.create('A3', 0.5)
elf.x = 10
elf.y = HEIGHT/2

game_over = False

bullets = []
enemies = []

def make_enemies():
    level = int(score / 5) + 1

    duration = (5 - level)
    if duration < 1:
        duration = 1

    for i in range(level):
        snake = Actor("snake")    
        snake.x = WIDTH-20
        snake.y = random.randint(10,HEIGHT-10)
        animate(snake, pos=(-100, snake.y), tween='accelerate', duration=duration)
        enemies.append(snake)

def bullet_out_of_screen():
    bullets.pop(0)

def on_key_down(key):
    if key == keys.SPACE:
        b = Actor("bullet2")
        b.x = elf.x + 5
        b.y = elf.y
        animate(b, pos=(WIDTH + 100, elf.y), tween='accelerate', on_finished=bullet_out_of_screen)
        bullets.append(b)

def update():
    global game_over, speed, score, bullets, enemies
    if keyboard.left:
        elf.x = elf.x-speed
    if keyboard.right:
        elf.x = elf.x+speed
    if keyboard.up:
        elf.y = elf.y-speed
    if keyboard.down:
        elf.y= elf.y+speed
    if keyboard.R:
        speed = 1
        score = 0
        bullets = []
        enemies = []
        game_over = False

    hit = []
    for b in bullets:
        for e in enemies:
            if b.colliderect(e):
                hit.append(e)

    if len(hit) > 0:
        score += len(hit)
        if speed < 4:
            speed += 1
        beep.play()
        for e in hit:
            enemies.remove(e)

    for e in enemies:
        if e.colliderect(elf):
            game_over = True

def draw():
    if game_over:
        screen.fill('black')
        screen.draw.text("GAME OVER", color="white", topleft=(10,10))
    else:
        screen.fill('black')
        elf.draw()

        for b in bullets:
            b.draw()

        for e in enemies:
            e.draw()

        screen.draw.text("Score: "+ str(score), color="white", topleft=(10,10))


make_enemies()
clock.schedule_interval(make_enemies, 2)

pgzrun.go()
```
![day-75-1.jpg](./reading/day-75-1.jpg "day 75 example 1")



tic tac toe but with one character variable names

```
x = [
        #  0    1    2     3
        ['〰️','🅰️','🅱️','🅾️'], # 0 
        ['🥇','〰️','〰️','〰️'], # 1
        ['🥈','〰️','〰️','〰️'], # 2
        ['🥉','〰️','〰️','〰️'], # 3
        
    ]

k = '🛹'

while True:
    for i in x:
        for s in i:
            print(s,end=' ')
        print('')


    l = input(k + ": ")

    if l == 'a1':
        x[1][1]=k
    elif l == 'a2':
        x[2][1]=k
    elif l == 'a3':
        x[3][1]=k

    elif l == 'b1':
        x[1][2]=k
    elif l == 'b2':
        x[2][2]=k
    elif l == 'b3':
        x[3][2]=k

    elif l == 'o1':
        x[1][3]=k
    elif l == 'o2':
        x[2][3]=k
    elif l == 'o3':
        x[3][3]=k
    else:
        continue
    
    if k == '🛹':
        k = '⚽'
    else:
        k = '🛹'

```

30 and back

```
for i in range(1,31):
    print(i)
for i in range(1,31):
    print(30 - i)
```

football mania

```
d = 30
while True:
    for i in range(1,d):
        print('⚽' * i)
    for i in range(1,d):
        h = (d - i)
        print('⚽' * h)
```

## [DAY-76] Functions; Callbacks; Lists


![game-76.png](./screenshots/game-76.png "game 76 screenshot")

A game of tag! The elf is robin hood, running away from the king. The elf plays with WASD and the king plays with up/down/left/right.

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

speedA = 3
speedB = 3

playerA = Actor("c1")
playerB = Actor("c2")

playerA.x = 10
playerA.y = HEIGHT - 40

playerB.x = 10
playerB.y = 40

game_over = False

def random_speed():
    global speedA, speedB
    speedA = random.randint(1,5)
    speedB = random.randint(1,5)

def on_key_down(key):
    global game_over

    # player A
    if key == keys.A:
        playerA.x -= speedA
    if key == keys.D:
        playerA.x += speedA
    if key == keys.W:
        playerA.y -= speedA
    if key == keys.S:
        playerA.y += speedA

    # player B
    if key == keys.LEFT:
        playerB.x -= speedB
    if key == keys.RIGHT:
        playerB.x += speedB
    if key == keys.UP:
        playerB.y -= speedB
    if key == keys.DOWN:
        playerB.y += speedB

def update():
    global game_over
    if playerA.colliderect(playerB):
        game_over = True
    
def draw():
    if game_over:
        screen.fill('black')
        screen.draw.text("GAME OVER", color="white", topleft=(10,10))
    else:
        screen.fill('black')
        screen.draw.text("RUN! elf: " + str(speedA) + " king: " + str(speedB) , color="white", topleft=(10,10))
        playerA.draw()
        playerB.draw()

clock.schedule_interval(random_speed, 2)

pgzrun.go()
```


Basic math quiz

```
import random
while True:
    k = random.randint(1,13)
    s = random.randint(1,13)
    r = k * s
    g = int(input('How much is '+str(k) +'*' +str(s) + ': '))
    if g == r:
        print('Wow nice job its CORRECT')
    else:
        print('wrong the answer was: ' + str(r))
```

7 days average

```
x = [1231,5123,6737,6725,6261,2664,62561]
n = len(x)

print(x)
print(n)

sum = 0
for i in x:
    sum += i

print('sum: ' + str(sum))
print('average: ' + str(sum/n))
```

## [DAY-77] Lists; Encode/Decode

morse code translator

```
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',']
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/','.-.-.-','--..--']

print(len(morse))
print(len(alphabet))

for i in range(len(alphabet)):
    print(alphabet[i] + " -> " + morse[i])

text = '.... . .-.. .-.. --- / .-- --- .-. .-.. -.. .-.-.- / - .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. . .-.-.- / - .... . .-. . / .- .-. . / -- .- -. -.-- / -.-. --- -.. . ... --..-- / -... ..- - / - .... .. ... / --- -. . / .. ... / .--. .-. . - - -.-- / -.-. --- --- .-.. --..-- / --. --- --- -.. / .--- --- -... / - .-. .- -. ... .-.. .- - .. -. --. / .. - .-.-.-'.split(' ')
for word in text:
    found = False
    for i in range(len(morse)):
        x = morse[i]
        if x == word:
            print(alphabet[i], end = '')
            found = True
    if not found:
        print(word , end='')
```

## [DAY-78] Coordinates; Functions; Callbacks

![game-78.png](./screenshots/game-78.png "game 78 screenshot")

Small modifications to the previous game, gold in the middle moves the king away, randomize the elf position every 2 seconds

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

speedE = 3
speedK = 3

elf = Actor("c1")
king = Actor("c2")
gold = Actor("c3")

gold.x = WIDTH/2
gold.y = HEIGHT/2
elf.x = 10
elf.y = HEIGHT - 40
king.x = 10
king.y = 40

game_over = False

def random_speed():
    global speedE, speedK
    speedE = random.randint(3,5)
    speedK = random.randint(2,5)

def random_place():
    elf.x = random.randint(0,WIDTH)
    elf.y = random.randint(0,HEIGHT)

def update():
    global game_over

    # elf
    if keyboard.A:
        elf.x -= speedE
    if keyboard.D:
        elf.x += speedE
    if keyboard.W:
        elf.y -= speedE
    if keyboard.S:
        elf.y += speedE

    # king
    if keyboard.left:
        king.x -= speedK
    if keyboard.right:
        king.x += speedK
    if keyboard.up:
        king.y -= speedK
    if keyboard.down:
        king.y += speedK

    if keyboard.SPACE:
        elf.image = 'snake'
        random_speed()

    if keyboard.R:
         game_over = 1==2
         elf.x = 10
         elf.y = HEIGHT - 40
         king.x = 10
         king.y = 40
         
    if elf.x < 0:
        elf.x = 0
    if elf.x > WIDTH:
        elf.x = WIDTH
    if elf.y < 0:
        elf.y = 0
    if elf.y > HEIGHT:
        elf.y = HEIGHT


    if king.x < 0: 
        king.x = 0
    if king.x > WIDTH:
        king.x = WIDTH
    if king.y < 0:
        king.y = 0
    if king.y > HEIGHT:
        king.y = HEIGHT

    if elf.colliderect(gold):
        king.x = WIDTH
        king.y = HEIGHT

    if king.colliderect(gold):
        game_over = True

    if elf.colliderect(king):
        game_over = True
    
def draw():
    if game_over:
        screen.fill('black')
        screen.draw.text("GAME OVER", color="white", topleft=(10,10))
    else:
        screen.fill('black')
        screen.draw.text("RUN! elf: " + str(speedE) + " king: " + str(speedK) , color="white", topleft=(10,10))
        elf.draw()
        king.draw()
        gold.draw()

clock.schedule_interval(random_speed, 2)
clock.schedule_interval(random_place, 5)

pgzrun.go()
```

Explanation about setting x and y to be random:

![day-78-explain.png](./reading/day-78-explain.png "day 78 explain coordinates")

Write a program to compute the average of a list of numbers:

![day-78-a.jpg](./reading/day-78-a.jpg "day 78 average of list of numbers")

Decode morse code:

![day-78-c.jpg](./reading/day-78-c.jpg "day 78 decode morse code")



## [DAY-79] Lists; Encoding

morse code agian

```
alphabet = ['a','b','c','d','e']
morse = ['.-','-...','-.-.','...','.']


for i in range(len(alphabet)):
    print(alphabet[i])
    print(morse[i])

text = ['.-..','.','.-..','.-']

for word in text:
    for c in range(len(morse)):
        if word == morse[c]:
            print(alphabet[c])
```

## [DAY-80] Lists; Functions

![game-80.png](./screenshots/game-80.png "game 80 screenshot")


PONG (almost)

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

left = Actor("c1")
left.x = 10
left.y = HEIGHT/2

right = Actor("c2")
right.x = WIDTH - 10
right.y = HEIGHT/2

ball = Actor("bullet")
ball.x = WIDTH/2
ball.y = HEIGHT/2

game_area = Rect((0, 0), (WIDTH, HEIGHT))

game_over = False

def send_ball_to(direction):
    duration = 3
    if direction == 'left':
        animate(ball, pos=(-100, random.randint(0,HEIGHT)), tween='linear', duration=duration)
    else:
        animate(ball, pos=(WIDTH + 100, random.randint(0,HEIGHT)), tween='linear', duration=duration)

def update():
    global game_over
    speed = 3

    if keyboard.R:
        ball.x = WIDTH/2
        ball.y = HEIGHT/2
        send_ball_to('left')
        game_over = False

    if keyboard.W:
        left.y -= speed
    if keyboard.S:
        left.y += speed

    if keyboard.up:
        right.y -= speed
    if keyboard.down:
        right.y += speed

    if left.colliderect(ball):
        send_ball_to('right')

    if right.colliderect(ball):
        send_ball_to('left')

    if not ball.colliderect(game_area):
        game_over = True

def draw():
    if game_over:
        screen.fill('black')
        screen.draw.text("GAME OVER", color="white", topleft=(10,10))
    else:
        screen.fill('black')
        left.draw()
        right.draw()
        ball.draw()
        screen.draw.rect(game_area, (200, 0, 0))

send_ball_to('left')

pgzrun.go()
```


![day-80-a.jpg](./reading/day-80-a.jpg "day 80 reading pong")

average of two lists

![day-80-b.jpg](./reading/day-80-b.jpg "day 80 reading average of two lists")


## [DAY-81] Lists; Encoding

First image

```
+-----+
| * * |
|  *  |
| * * |
+-----+
```


list of lists with pixels

```
image = [
    [1,3,3,3,3,3,1],
    [2,4,5,4,5,4,2],
    [2,4,4,5,4,4,2],
    [2,4,5,4,5,4,2],
    [1,3,3,3,3,3,1],
]

for row in image:
    for pixel in row:
        if pixel == 1:
            print('+', end='')
        elif pixel == 2:
            print('|', end='')
        elif pixel == 3:
            print('-', end='')
        elif pixel == 4:
            print(' ', end='')
        elif pixel == 5:
            print('*', end='')
        else:
            print("dont know what to do with: " + str(pixel))
    print('')
```

just a list of pixels

```
image = [
    1,3,3,3,3,3,1,
    2,4,5,4,5,4,2,
    2,4,4,5,4,4,2,
    2,4,5,4,5,4,2,
    1,3,3,3,3,3,1,
]

width = 7

for (index, pixel) in enumerate(image):
    if index > 0 and index % width == 0:
        print('')

    if pixel == 1:
        print('+', end='')
    elif pixel == 2:
        print('|', end='')
    elif pixel == 3:
        print('-', end='')
    elif pixel == 4:
        print(' ', end='')
    elif pixel == 5:
        print('*', end='')
    else:
        print("dont know what to do with: " + str(pixel))
```

some fun with lists
```
x = ['a','b','c','d']
m = ['w','x','y','z']
d = ['g','h','j','k']

# a -> 0
# b -> 1
# c -> 2

for i in range(len(x)):
    print(i,end=' ')
    print(x[i],end=' ')
    print(m[i],end=' ')
    print(d[i])
```

how similar are lists and strings

```
x = 'hello'

for i in range(len(x)):
    print(i,end=' ')
    print(x[i])
```

similar, but not quite, you cant change the inside of a string, but you can change the inside of a list.

```
x = ['h','e','l','l','o']
y = 'hello'

x[2] = 'm'
y = 'hemlo'

for i in range(len(x)):
    print(i,end=' ')
    print(x[i], end=' ')
    print(y[i])
```

sum many lists
```
a = [6,3,2]
b = [78,21,1]
c = [123,5,1]

sum = 0
for i in range(len(a)):
    sum += a[i] + b[i] + c[i]

print(sum)
```

another way to sum

```
a = [6,3,2]
b = [78,21,1]
c = [123,5,1]

sum = 0

for x in a:
    sum += x

for x in b:
    sum += x

for x in c:
    sum += x

print(sum)
```

## [DAY-82] Lists; Strings

![game-82.png](./screenshots/game-82.png "game 82 screenshot")

simple game with history, press S to save your position to a list of positions, and then B to go back in time

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

player = Actor("c1")
player.x = WIDTH/2
player.y = HEIGHT/2

history = []

def on_key_down(key):
    speed = 3
    
    if key == keys.UP:
        player.y -= speed
    if key == keys.DOWN:
        player.y += speed
    if key == keys.LEFT:
        player.x -= speed
    if key == keys.RIGHT:
        player.x += speed

    if key == keys.S:
        position = [player.x, player.y]
        history.append(position)

        print('append', history)

    if key == keys.B and len(history) > 0:        
        last = history.pop()
        player.x = last[0]
        player.y = last[1]

        print('pop', history)


def draw():
    screen.fill('black')
    player.draw()

pgzrun.go()
```

Two players, and more positions

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200
player1 = Actor("c1")
player2 = Actor('c2')
history = []

def on_key_down(key):
    speed = 10
    if key == keys.W:
        player1.y-= speed
    if key == keys.A:
        player1.x-=speed
    if key == keys.S:
        player1.y += speed
    if key == keys.D:
        player1.x += speed


    if key == keys.UP:
        player2.y-= speed
    if key == keys.LEFT:
        player2.x-=speed
    if key == keys.DOWN:
        player2.y += speed
    if key == keys.RIGHT:
        player2.x += speed

        
    if key == keys.F:
        positions = [player1.x,player1.y,player2.x,player2.y]
        history.append(positions)
        print('push', history)
    if key == keys.G:
        if len(history) > 0:
            positions = history.pop()
            player1.x = positions[0]
            player1.y = positions[1]
            player2.x = positions[2]
            player2.y = positions[3]
            print('pop', history)
        
def draw():
    screen.fill('black')
    player1.draw()
    player2.draw()
pgzrun.go()
```

More lists

```
a = ['h','w','e']
b = ['e','o','a']
c = ['l','r','r']
d = ['l','l','t']
e = ['o','d','h']

sum1 = ''
sum2 = ''

sum1 = a[0] + b[0] + c[0] + d[0] + e[0]
sum2 = a[1] + b[1] + c[1] + d[1] + e[1]

print(sum1)
print(sum2)

sum = []
for i in range(len(a)):
    sum.append('')
    sum[i] = a[i] + b[i] + c[i] + d[i] + e[i]


print(sum)
```

sum from the input

```
list = []
while True:
    integer = int(input('enter a number: '))
    list.append(integer)
    sum = 0
    for i in list:
        sum += i
        
    print(list, sum)
```

## [DAY-83] Lists; Functions

![game-83.png](./screenshots/game-83.png "game 83 screenshot")


```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

player = Actor("c1")
player.x = WIDTH/2
player.y = HEIGHT/2

things = []

def on_key_down(key):
    speed = 10

    if key == keys.UP:
        player.y -= speed
    if key == keys.DOWN:
        player.y += speed
    if key == keys.LEFT:
        player.x -= speed
    if key == keys.RIGHT:
        player.x += speed

    if key == keys.F:
        thing = Actor("flower")
        thing.x = player.x
        thing.y = player.y

        things.append(thing)

    if key == keys.R:
        thing = Actor("rock")
        thing.x = player.x
        thing.y = player.y

        things.append(thing)


def draw():
    screen.fill('black')
    player.draw()
    for t in things:
        t.draw()

pgzrun.go()
```

With a function, so we can add more keys faster and we dont duplicate that much code

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

player = Actor("c1")
player.x = WIDTH/2
player.y = HEIGHT/2

things = []
def place_thing(kind):
    thing = Actor(kind)
    thing.x = player.x
    thing.y = player.y

    things.append(thing)

def on_key_down(key):
    speed = 15
    
    if key == keys.UP:
        player.y -= speed
    if key == keys.DOWN:
        player.y += speed
    if key == keys.LEFT:
        player.x -= speed
    if key == keys.RIGHT:
        player.x += speed

    if key == keys.F:
        place_thing("flower")

    if key == keys.R:
        place_thing("rock")

    if key == keys.K:
        place_thing("c2")

def draw():
    screen.fill('black')
    player.draw()
    for t in things:
        t.draw()

pgzrun.go()
```

Now we can make a map, just add the kind of thing, its x and y position in a list and print it, after we are done building the map we can use it later

```
...
game_map = []
def place_thing(kind):
    thing = Actor(kind)
    thing.x = player.x
    thing.y = player.y

    things.append(thing)
    game_map.append([kind, thing.x, thing.y])
    print(game_map)
...    
```

use the map:

![game-83-a.png](./screenshots/game-83-a.png "game 83-a screenshot")

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

player = Actor("c1")
player.x = WIDTH/2
player.y = HEIGHT/2

things = []
def place_thing(kind,x,y):
    thing = Actor(kind)
    thing.x = x
    thing.y = y
    things.append(thing)

def on_key_down(key):
    speed = 15
    
    if key == keys.UP:
        player.y -= speed
    if key == keys.DOWN:
        player.y += speed
    if key == keys.LEFT:
        player.x -= speed
    if key == keys.RIGHT:
        player.x += speed
def draw():
    screen.fill('black')
    player.draw()
    for t in things:
        t.draw()

game_map = [['rock', 100.0, 55.0], ['flower', 100.0, 85.0], ['c2', 100.0, 130.0], ['c2', 70.0, 130.0], ['c2', 55.0, 130.0], ['c2', 40.0, 130.0], ['c2', 25.0, 130.0], ['c2', 25.0, 100.0], ['c2', 25.0, 85.0], ['c2', 25.0, 70.0], ['c2', 25.0, 55.0], ['c2', 25.0, 40.0], ['c2', 25.0, 25.0], ['c2', 40.0, 25.0], ['c2', 55.0, 25.0], ['c2', 70.0, 25.0], ['c2', 85.0, 25.0], ['c2', 100.0, 25.0], ['c2', 115.0, 25.0], ['c2', 130.0, 25.0], ['c2', 145.0, 25.0], ['c2', 145.0, 40.0], ['c2', 145.0, 55.0], ['c2', 145.0, 70.0], ['c2', 145.0, 85.0], ['c2', 145.0, 100.0], ['c2', 145.0, 115.0], ['c2', 145.0, 130.0], ['c2', 130.0, 130.0], ['c2', 115.0, 130.0], ['c2', 100.0, 130.0], ['c2', 85.0, 130.0], ['c2', 25.0, 115.0]]
for g in game_map:
    place_thing(g[0],g[1],g[2])

pgzrun.go()
```


![game-83-b.png](./screenshots/game-83-b.png "game 83-a screenshot")
![game-83-c.png](./screenshots/game-83-c.png "game 83-c screenshot")

Another way to do it, press S to print the list of things, and then paste it in the game[] list to use it, D deletes things where you stand, and U removes the last thing

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

player = Actor("c1")

things = []

game = []
for g in game:
    t = Actor(g[0])
    t.x = g[1]
    t.y = g[2]
    things.append(t)

def on_key_down(key):
    speed = 10

    if key == keys.UP:
        player.y -= speed
    if key == keys.DOWN:
        player.y += speed
    if key == keys.LEFT:
        player.x -= speed
    if key == keys.RIGHT:
        player.x += speed
        
    if key == keys.F:
        f = Actor("flower")
        f.x = player.x
        f.y = player.y
        things.append(f)
    if key == keys.R:
        f = Actor("rock")
        f.x = player.x
        f.y = player.y
        things.append(f)

    if key == keys.U:
         things.pop()

    if key == keys.D:
        collide = []
        for t in things:
            if player.colliderect(t):
                collide.append(t)

        for t in collide:
            things.remove(t)
    
    if key == keys.S:
        positions = []
        for t in things:
            positions.append([t.image,t.x,t.y])
        print(positions)

def draw():
    screen.fill('black')
    player.draw()
    for t in things:
        t.draw()

pgzrun.go()
```

## [DAY-84] Lists

![game-84.png](./screenshots/game-84.png "game 84 screenshot")

Lets visualize the list, try to delete from the middle, and see how the indexes change.


```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

player = Actor("c1")

things = []

def on_key_down(key):
    speed = 10

    if key == keys.UP:
        player.y -= speed
    if key == keys.DOWN:
        player.y += speed
    if key == keys.LEFT:
        player.x -= speed
    if key == keys.RIGHT:
        player.x += speed

    if key == keys.F:
        f = Actor("flower")
        f.x = player.x
        f.y = player.y
        things.append(f)
    if key == keys.R:
        f = Actor("rock")
        f.x = player.x
        f.y = player.y
        things.append(f)

    if key == keys.U:
         things.pop()

    if key == keys.D:
        collide = []
        for t in things:
            if player.colliderect(t):
                collide.append(t)

        for t in collide:
            things.remove(t)

def draw():
    screen.fill('black')
    player.draw()

    
    for i in range(len(things)):
        t = things[i]
        t.draw()
        screen.draw.text(str(i), color=(255,255,255), topleft=(t.x,t.y))
        if i > 0:
            p = things[i-1]
            screen.draw.line((p.x,p.y), (t.x,t.y), (255,255,255))
pgzrun.go()
```

spend more time thinking about connecting previous and current elements from a list, think about how to do it the other way around, from current element to next:

```
# change this to go from t to the next element of things, instead from t to previous
for i in range(len(things)):
    t = things[i]
    ...
    if i > 0:
        p = things[i-1]
        ...
```

## [DAY-85] List; Functions

This day is more about reading than writing, those are few different examples you can use

![game-85.png](./screenshots/game-85.png "game 85 screenshot")


don't let the **zombie** flowers overrun you, smash them with rocks


```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

game_over = False

elf = Actor("c1")
elf.x = WIDTH/2
elf.y = HEIGHT-20
flowers = []
rocks = []

game_area = Rect((0, 0), (WIDTH, HEIGHT-40))

def add_one_row():
    lastY = 0
    if len(flowers) > 0:
        f = flowers[len(flowers)-1]
        lastY = f.y
    
    for i in range(20, WIDTH-10, 20):
        f = Actor("flower")
        f.x = i
        f.y = lastY + 10
        flowers.append(f)

def rock_out_of_screen():
    if len(rocks) > 0:
        rocks.pop(0)

def on_key_down(key):
    speed = 10
    if key == keys.LEFT:
        elf.x -= speed
    if key == keys.RIGHT:
        elf.x += speed
        
    if key == keys.SPACE:
        rock = Actor("rock")
        rock.x = elf.x
        rock.y = elf.y - 20
        animate(rock,pos=(rock.x, -100), on_finished=rock_out_of_screen)
        rocks.append(rock)

def update():
    global game_over
    hit = []
    for b in rocks:
        for f in flowers:
            if b.colliderect(f) and random.randint(0,10) > 7:
                hit.append(f)

    for h in hit:
        flowers.remove(h)

    for f in flowers:
        if not f.colliderect(game_area):
            game_over = True


def draw():
    if game_over:
        screen.draw.text("GAME OVER", color="white", topleft=(10,10))
    else:
        screen.fill('black')
        elf.draw()
        for f in flowers:
            f.draw()
        for r in rocks:
            r.draw()

        screen.draw.rect(game_area, (200, 0, 0))

add_one_row()
clock.schedule_interval(add_one_row, 5)

pgzrun.go()
```

![game-85-a.png](./screenshots/game-85-a.png "game 85-a screenshot")

```
import turtle as t

size = 10

t.pensize(size)
t.left(45)
t.forward(90)
t.circle(45,extent=180)
t.right(90)
t.circle(45,extent=180)
t.forward(90)
t.penup()
t.goto(-35,-35)
t.pendown()
t.write('i love python')
t.penup()
```

![game-85-b.png](./screenshots/game-85-b.png "game 85-b screenshot")


```
import  turtle as t
import datetime
import time
def deg(h,m,s):
	hDeg=(h*3600+m*60+s)/(3600*12)*360
	mDeg=(m*60+s)/3600*360
	sDeg=360/60*s
	
	return (90+hDeg,90+mDeg,90+sDeg)
	
	
def show(h, size):
	(hDeg,m,s) = deg(h,0,0)
	
	t.penup()
	t.goto(0, size)
	t.pencolor('white')
	t.setheading(hDeg)
	t.forward(size)
	t.write(str(h))
	
def klok(size, h, m, s):
	t.reset()
	(hDeg,mDeg,sDeg) = deg(h,m,s)
	
	t.pendown()
	t.pensize(7)
	t.bgcolor('black')
	t.pencolor('lime')
	
	t.circle(size)
	
	t.penup()
	t.goto(0, size)
	t.setheading(hDeg)
	t.pendown()
	t.pencolor('springgreen')
	t.forward(size/3)
	
	
	t.penup()
	t.goto(0, size)
	t.setheading(mDeg)
	t.pendown()
	t.pencolor('lawngreen')
	t.forward(size/2)
	t.penup()
	t.pencolor('cyan')
	t.goto(0, size)
	t.setheading(sDeg)
	t.pendown()
	t.forward(size-25)
	t.penup()
	
size = 150
while True:
	now = datetime.datetime.now()
	klok(size,now.hour, now.minute, now.second)

	for h in range(1, 13):
		show(h,size)
	time.sleep(10)
```

![game-85-c.png](./screenshots/game-85-c.png "game 85-c screenshot")

Just one rock that hits the zombies above you

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

game_over = False

elf = Actor("c1")
elf.x = WIDTH/2
elf.y = HEIGHT-20
rock = Actor("rock")
rock.x = elf.x + 10
rock.y = elf.y - 20

flowers = []

def add_one_row():
    lastY = 0
    if len(flowers) > 0:
        f = flowers[len(flowers)-1]
        lastY = f.y
    
    for i in range(20, WIDTH-10, 20):
        f = Actor("flower")
        f.x = i
        f.y = lastY + 10
        flowers.append(f)

def on_key_down(key):
    speed = 10
    if key == keys.LEFT:
        elf.x -= speed
    if key == keys.RIGHT:
        elf.x += speed
    if key == keys.UP:
        elf.y -= speed
    if key == keys.DOWN:
        elf.y += speed
        

def update():
    global game_over
    hit = []
    for f in flowers:
        if rock.colliderect(f) and random.randint(0,10) > 7:
            hit.append(f)

    for h in hit:
        flowers.remove(h)

    rock.x -= 1
    if rock.x < elf.x - 10:
        rock.x = elf.x + 10

    rock.y = elf.y - 20


def draw():
    screen.fill('black')
    elf.draw()
    rock.draw()
    for f in flowers:
        f.draw()

add_one_row()
clock.schedule_interval(add_one_row, 5)

pgzrun.go()
```

![day-85.jpg](./reading/day-85.jpg "day 85 reading")


## [DAY-86] Lists


![game-86.png](./screenshots/game-86.png "game 86 screenshot")

SNAKE

```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

snake = Actor("c1")
snake.x = WIDTH/2
snake.y = HEIGHT-20

apple = Actor("flower")
apple.x = WIDTH/2
apple.y = HEIGHT/2

snake_size = 20
snake_speed = 1
steps = []
direction = "up"
step_size = 1
game_over = False
game_area = Rect(0,0,WIDTH,HEIGHT)
def on_key_down(key):
    global direction

    if key == keys.LEFT:
        direction = "left"
    if key == keys.RIGHT:
        direction = "right"
    if key == keys.UP:
        direction = "up"
    if key == keys.DOWN:
        direction = "down"

def update():
    global snake_size, game_over, snake_speed, steps

    s = Actor("snake")
    s.x = snake.x
    s.y = snake.y
    steps.append(s)
    if len(steps) > snake_size:
        steps = steps[-snake_size:]

    if direction == "left":
        snake.x -= step_size
    if direction == "right":
        snake.x += step_size
    if direction == "up":
        snake.y -= step_size
    if direction == "down":
        snake.y += step_size
    
    if snake.colliderect(apple):
        apple.x = random.randint(0,WIDTH)
        apple.y = random.randint(0,HEIGHT)
        snake_size += step_size * 10

    if not snake.colliderect(game_area):
        game_over = True

def draw():
    screen.fill('black')

    if game_over:
        screen.draw.text("GAME OVER", color="white", topleft=(10,10))
    else:
        screen.draw.rect(game_area, (255,0,0))
        for s in steps:
            s.draw()
        snake.draw()
        apple.draw()

pgzrun.go()
```

There are few key moments to emphasize, but the most important one is `steps = steps[-snake_size:]`.

Try this in IDLE:

```
x = [1,2,3,4]
print(x[-1])
```

It will print '4', so in python you can get elements from the back of the list, just as easily as the front, try `x[-2]`, now try to get multiple elements from a list, `y = x[0:2]`, it will make new list `[1,2]`, it is a bit like this code:

```
x = [1,2,3,4]
y = []
for i in range(0,2):
    y.append(x[i])
```

Now you can also ask python to give you the first 2 elements by saying `x[0:2]` or you can ask it for the elements *after* the second one by doing `x[2:len(x)]`, you can omit 0 and `len(x)` so it is a bit shorter, `x[:2]` and `x[2:]`. Sometimes you want the last 2 elements, to do that just say `x[-2:len(x)]` or `x[-2:]` and that's how we are getting the last `snake_size` elements of the `steps` list.

Again, `x[-2:len(x)]` just means from -2 elements from the end if the list, until the end of the list. It looks scary though.

Similar to this code:

```
x = [1,2,3,4]
y = []
for i in range(len(x)-2,len(x)):
    y.append(x[i])
```

## [DAY-87] Read/Write Files

Its File time!

First lets make a new file, called day-87.txt and we will open it in "w" mode, which means "write", so once we do `f.write` it will start from the beginning of the file, we can use "a" (for append) mode as well that would continue appending to the end of the file

```
f = open("day-87.txt", "w")

while True:
    a = input("what do you want to write: ")
    if a == "quit":
        break
    f.write(a + "\n")

f.close()
```

Now you can open day-87.txt with Notepad or some other text editor and see what you wrote.

It is important to remember this pattern

1. Open
2. Read or Write
3. Read or Write
4. Read or Write
5. Read or Write
6. ...
7. Close

lets see how you read a file:

```
f = open("day-87.txt", "r")
data = f.read()
print(data)
```

Make a game that persists the player position.


```
import pgzrun
import random

HEIGHT = 200
WIDTH = 200

elf = Actor("c1")
elf.x = WIDTH/2
elf.y = HEIGHT-20

try:
    x = open("day-87-x.txt", "r")
    elf.x = float(x.read())
    x.close()
    
    y = open("day-87-y.txt", "r")
    elf.y = float(y.read())
    y.close()
except IOError:
    pass

def on_key_down(key):
    speed = 10
    if key == keys.LEFT:
        elf.x -= speed
    if key == keys.RIGHT:
        elf.x += speed
    if key == keys.UP:
        elf.y -= speed
    if key == keys.DOWN:
        elf.y += speed

    if key == keys.S:
        x = open("day-87-x.txt", "w")
        x.write(str(elf.x))
        x.close()

        y = open("day-87-y.txt", "w")
        y.write(str(elf.y))
        y.close()


def draw():
    screen.fill('black')
    elf.draw()

pgzrun.go()
```

open `day-87-x.txt` and `day-87-y.txt` to see the positions of X and Y of the elf after you press `S`.

One other patter you will see is:

```
try:
    try to do something
except some error:
    handle error
```

There are many many things that could go wrong when you write to or read a file, for example when you read the file might not be created, or you might have no access to read it, or when you write the disk might be full, and there is no more space.

In our example we don't check if our write fails, so if your disk is full the game will crash, but in the beginning we do check for IOError in case the reading fails, and it will if the files are not created yet the very first time you start the game and there is no save yet.



## [DAY-88] Flask

Reading exercise, a lot of unfamiliar code

```
from flask import Flask, redirect, request,make_response
import random
app = Flask(__name__)

tokens = {}

@app.route('/')
def index():
    token = request.cookies.get('token')
    if token in tokens:
        response = make_response("""
        welcome to the secure section of the website,
        <a href="/logout">click here to logout
        """)
        return response

    
    response = make_response("""
        <html>
        <form action="/login" method="post">
        user: <input name="user">
        pass: <input type="password" name="pass">
        <input type="submit">
        </form>
        </html>
        """)
    return response

@app.route('/logout')
def logout():
    token = request.cookies.get('token')
    try:
        del tokens[token]
    except KeyError:
        pass

    response = make_response(redirect('/'))
    response.set_cookie('token', '')
    return response

@app.route('/login', methods = ['POST'])
def login():
    user = request.form['user']
    password = request.form['pass']
    if user == "admin" and password == "123":
        token = str(random.randint(0,10000000))
        tokens[token] = "admin"

        response = make_response(redirect('/'))
        response.set_cookie('token', token)
        return response
    else:
        return "access denied"
    
if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
```

start the script, see what it does, try to debug how `tokens` changes. Inspect your cookies, try to hack it, login from private mode and steal the cookie from the console.
## [DAY-89] Files; Strings; Lists

super simple text editor

![game-89.png](./screenshots/game-89.png "game 89 screenshot")

Reading exercise, make a text editor, save with `ctrl+s` and quit with `ctrl+q`

```
import pgzrun
import random

HEIGHT = 480
WIDTH = 640
filename = "example.py"
lines = [[]]
cursor_row = 0
cursor_col = 0

try:
    x = open(filename, "r")
    for c in x.read():
        if c== '\n' or c == '\r':
            lines.append([])
            cursor_row += 1
            cursor_col = 0
        else:
            lines[cursor_row].append(c)
            cursor_col += 1

    x.close()
except IOError:
    pass

def lines_to_string():
    s = ''
    for r in lines:
        for c in r:
            s += c
        s += '\n'
    return s

def on_key_down(key, mod, unicode):
    global cursor_row, cursor_col

    if key == keys.Q and mod == keymods.LCTRL:
        exit()
    if key == keys.S and mod == keymods.LCTRL:
        x = open(filename, "w")
        s = lines_to_string()
        x.write(s)
        x.close()

    elif key == keys.LEFT:
        if cursor_col > 0:
            cursor_col -= 1
    elif key == keys.RIGHT:
        if cursor_col < len(lines[cursor_row]):
            cursor_col += 1
    elif key == keys.UP:
        if cursor_row > 0:
            cursor_row -= 1
            if cursor_col > len(lines[cursor_row]):
                cursor_col = len(lines[cursor_row])
    elif key == keys.DOWN:
        if cursor_row < len(lines) - 1:
            cursor_row += 1
            if cursor_col > len(lines[cursor_row]):
                cursor_col = len(lines[cursor_row])


    elif key == keys.BACKSPACE:
        if cursor_col == 0:
            if cursor_row >= 1:
                row = lines.pop(cursor_row)
                cursor_col = len(lines[cursor_row-1])
                for c in row:
                    lines[cursor_row-1].append(c)
                cursor_row -= 1
        else:
            row = lines[cursor_row]
            if len(row) > 0:
                cursor_col -= 1
                row.pop(cursor_col)


    elif key == keys.RETURN:
        # get the rest of the lines
        left = []
        right = []
        if cursor_col < len(lines[cursor_row]):
            # split the line if we are pressing enter in the middle
            row = lines[cursor_row]

            left = row[:cursor_col]
            right = row[cursor_col:]

            if cursor_row < len(lines):
                lines[cursor_row] = left

        cursor_col = 0
        cursor_row += 1
        lines.insert(cursor_row, right)

    elif len(unicode) > 0 and ord(unicode) >= 20 and ord(unicode) <= 125:
        lines[cursor_row].insert(cursor_col, unicode)
        cursor_col += 1

def draw():
    screen.fill('black')
    screen.draw.text(filename + ", " + str(cursor_row) + ":" + str(cursor_col), (0,0), fontsize=20,fontname="437-win", color="green")

    x = 0
    y = 30
    stepX = 10
    stepY = 22

    for (index_row, row) in enumerate(lines):
        for (index_col, c) in enumerate(row):
            screen.draw.text(c, (x,y), fontsize=20,fontname="437-win")
            x += stepX
        y += stepY
        x = 0

    cursorX = cursor_col * stepX
    cursorY = 30 + (cursor_row * stepY)

    screen.draw.rect(Rect((cursorX,cursorY,stepX,stepY)), (255,0,0))

pgzrun.go()
```

write some python, and then run it with `python3 example.py`


## [DAY-90] Strings

![game-90.png](./screenshots/game-90.png "game 90 screenshot")

Write a super simple text editor. Start by thinking about the problem. How can you display a character on the screen? How can you get the input from the user? How are you going to deal with new lines?

```
import pgzrun

HEIGHT = 480
WIDTH = 640

text = ''

def on_key_down(key, mod, unicode):
    global text

    if key == keys.Q and mod == keymods.LCTRL:
        exit()


    elif key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:len(text)-1]

    elif key == keys.RETURN:
        text += '\n'

    elif len(unicode) > 0 and ord(unicode) >= 20 and ord(unicode) <= 125:
        text += unicode

def draw():
    screen.fill('black')
    x = 0
    y = 0
    stepX = 10
    stepY = 22

    for c in text:
        if c == '\n':
            y += stepY
            x = 0
        else:
            screen.draw.text(c, (x,y), fontsize=20,fontname="437-win")
            x += stepX

    screen.draw.rect(Rect((x,y,stepX,stepY)), (255,0,0))

pgzrun.go()
```

This is kind of what `screen.draw.text` does, you can of course just do `screen.draw.text(text, (0,0), fontsize=20,fontname="437-win")` and it will work fine, instead of displaying character by character and computing our own char spacing, but what is the fun in that? Also this way we are one step closer to be able to move the cursor left and right so we can edit in the middle of the text.

## [DAY-91] Lists

list your favorite games, and rank them

```
games = [
    ["mario smash bros", 3],
    ["mario party", 4],
    ["super mario", 2]
]

while True:
    for game in games:
        print(game[0])
    what = input("which game are you interested in: ")
    for game in games:
        if what in game[0]:
            print("i like " + game[0] + ", score: " + str(game[1]))
```

print the lyrics of songs:

```
songs = [
    ["wellerman", """There once was a ship that put to sea
The name of the ship was the Billy of Tea
The winds blew up, her bow dipped down
Oh blow, my bully boys, blow (huh)

Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go"""],
]

while True:
    what = input("which song are you interested in: ")
    for song in songs:
        if what in song[0]:
            print('-' * 40)
            print(song[1])
            print('-' * 40)
```
## [DAY-92] Command Line; Command Line Arguments; Files

Today is command line day.

> First quickly go back to the start and read about files and folders (directories).

The same way functions can get parameters, your program can get parameters as well, try this:

```
import sys
print(sys.argv)
```

save it as `a.py` and then run `python3 a.py hello those are paremeters` from the Terminal app, you will see `['a.py', 'hello', 'those', 'are', 'paremeters']`, sys.argv[0] is the name of the program, and then the parameters you gave it.

Now lets make few handy programs to help us with our command line:

---

xcat.py

```
import sys

x = open(sys.argv[1], "r")
data = x.read()
print(data)
```

---

xls.py
```
import os
import sys

files = os.listdir(sys.argv[1])
files.sort()

for f in files:
    if os.path.isdir(f):
        print(f + "/")
    else:
        print(f)
```

---

xed.py

```
import sys
import os

text = ''

filename = sys.argv[1]

try:
    f = open(filename, "r")
    text = f.read()
    f.close()
except IOError:
    pass

while True:
    what = input("> ")
    if what == '?':
        print("""
        * ? - help
        * p - print
        * s - save
        * d [n] - delete last N lines
        * a text - append text to the end
        """)
    elif what == 'q':
        sys.exit(0)
    elif what == 'p':
        print(text, end = '')
    elif what == 's':
        f = open(filename, "w")
        f.write(text)
        f.close()
    elif what[0] == 'a' and what[1] == ' ':
        text += what[2:] + '\n'
    elif what[0] == 'd':
        lines = text.split('\n')

        n = 1
        if len(what) > 2:
            n = int(what[2:])

        for i in range(0, n):
            lines.pop()

        text = "\n".join(lines)


    else:
        print("* use ? for help")
```

---

OK now we have a text editor, a program to list files, and a program to print the file's content, now we can use our programs to write more programs :)

try this:

```
$ python3 xed,py example.py
> a for i in range(100)
> a   print(i)
> p
> s

$ python3 xls.py .
$ python3 xcat.py example.py
$ python3 example.py
```

## [DAY-93] PyDoc

Reading docs. type this in the terminal: `pydoc3 open` `pydoc3 input` `pydoc3 print` and `pydoc3 pgzero.actor`.

Lets take `open` as an example.

```
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.

    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.

    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.

    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.

    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:

    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.

    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.

    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.

    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.

    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:

    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.

    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.

    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.

    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).

    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.

    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
```

It's a lot! But I guarantee you its the best way to learn about something, the people who wrote the `open` function, wrote text to help anyone who is going to use it, describging what it does and how it behaves. It is always worth reading the docs of functions you are going to use. Sometimes they are not very good, but it is worth checking it out.

The other way find things is to google `python3 open` and you will usually see stackoverflow answers and maybe some examples, in many cases they will be incomplete or wrong, or pure scam 'pay 10$ to buy our video to learn how to use python3 open'


You can also do pydoc3 on modules, e.g. `pydoc3 sys` or `pydoc3 sys.argv`. Sometimes it might look a bit intimidating, but its usually much better than using google.

Try also `pydoc3 pgzero`, `pydoc3 pygame` and `pydoc3 pygame.Rect`. There is also a way to find documentation for the command line programs, try `man python3`, `man` from `manual`, if you want to search for something use `man -k something` for example `man -k python`.

## [DAY-94] Editors - Ed/Nano/Vi/Emacs..

Command line editors:

* nano, pico

super easy to use, press ctrl+x to exit, ctrl+k to cut text, and ctrl+u to uncut (paste)

* vi

Type `vimtutor` to see how it works, to quit use `ESC` then type `:` and then `q!`

* emacs

emacs is my favorite editor, in in fact I am writing this book using it. type `ctrl+x ctrl+c` to quit, and `ctrl+x ctrl+s` to save.

* ed

ed is super old editor, it is somewhat similar to xed.py that you wrote, its called 'line editor'. To quit use `q` or `Q` if you want to quit without saving, to print the contents of the file use `1,$n` which prints the lines from 1 to $, or you can print specific line with `1n` or `2n` where 1 or 2 is the linue number.

try this:

```
$ ed zzz
a
for i in range(10);
  print(i)
.
w
31
1,$n
1	for i in range(10);
2	  print(i)
q
```

`a` will append to the file, `w` will save the file, `1,$n` will print the contents, and `q` will quit. Commands like `a,i,d` (append,insert,delete) take line numbers as parameters as well. Use `man ed` to see the docs.

I don't think anyone uses `ed` anymore, at least not as a text editor, but sometimes its handy to know how to use it.

---

There are many many text editors, and some are better for you than others, but to me I dont really care, I want to type in my program and save it.. its not the end of the world if I use one or another editor.

So use the one you like most, but sometimes you will go on another computer and they wont have your editor there, so be be sure to be 'ok' with vim, nano or emacs, because they are on virtually any system.

## [DAY-95] Memory; Virtual Computer; Instructions; Strings; Lists


Memory.


Lets make a huuuuuge list.

```
memory = []
for i in range(1000000):
    memory.append(0)

```

Our memory looks like this:

```
[0,0,0,..............0,0,0,0....0,0,0,0,0]
```

Now we can make variables in this list of numbers, by addressing each variable with its index in the list, for exampke `x` can be at index 1000 and `y` can be at position 1001.


```
def add(a_address,b_address):
    return memory[a_address] + memory[b_address]

x_address = 1000
y_address = 1001
memory[x_address] = 5
memory[y_address] = 10

r = add(x_address,y_address)

print(r)
```

This is cheating though, because python uses its own memory to store the result from x and y, lets fix that:

```
def add(a_address,b_address,r_address):
    memory[r_address] = memory[a_address] + memory[b_address]

x_address = 1000
memory[x_address] = 5

y_address = 1001
memory[y_address] = 10

r_address = 1002
add(x_address,y_address,r_address)

print(memory[r_address])
```

This is how our memory looks like
```
[....0,0,0,5,10,15,0,...]
           ^ ^  ^
           | |  |
           x |  |
             y  |
                r

x at index 1000
y at index 1001
r at index 1002
```

The code above translates roughly to:

```
x = 5
y = 10
r = x + y
print(r)
```

How about strings? We can store strings by just defining how big the string is, and then follow with the characters of the string. You see how it is continous piece of memory.
```

h_address = 2000
memory[h_address] = 5
memory[h_address+1] = ord('h')
memory[h_address+2] = ord('e')
memory[h_address+3] = ord('l')
memory[h_address+4] = ord('l')
memory[h_address+5] = ord('o')

def xprint(address):
    l = memory[address]
    for i in range(l):
        # +1 is because of the length
        c = memory[address + 1 + i]
        print(chr(c), end = '')
    print('')
```


Strings with without length. We can also just say 'the string ends with 0' so start reading and stop when you see 0.

```

n_address = 3000
memory[n_address+0] = ord('h')
memory[n_address+1] = ord('e')
memory[n_address+2] = ord('l')
memory[n_address+3] = ord('l')
memory[n_address+4] = ord('o')

def nprint(address):
    for addr in range(address, len(memory)):
        c = memory[addr]
        if c == 0:
            break
        print(chr(c), end = '')
    print('')

nprint(n_address)

```

Now lets add a funciton to add two strings:

```


a_address = 4000
memory[a_address] = 5
memory[a_address+1] = ord('h')
memory[a_address+2] = ord('e')
memory[a_address+3] = ord('l')
memory[a_address+4] = ord('l')
memory[a_address+5] = ord('o')

b_address = 4006
memory[b_address] = 5
memory[b_address+1] = ord('w')
memory[b_address+2] = ord('o')
memory[b_address+3] = ord('r')
memory[b_address+4] = ord('l')
memory[b_address+5] = ord('d')

c_address = 7000

def xadd(a,b,dst):
    len_a = memory[a]
    len_b = memory[b]
    memory[dst] = len_a + len_b
    for i in range(len_a):
        c = memory[a + 1 + i]
        memory[dst + 1 + i] = c

    for i in range(len_b):
        c = memory[b + 1 +i]
        memory[dst + 1 + len_a + i] = c

xadd(a_address, b_address, c_address)
xprint(c_address)
```

You see, the list is just a list with 1 million numbers, but we decide what those numbers mean, if we are reading a string, we *know* that the first number represents the length of the string, so its just an integer, but we know that the other numbers are actually characters.

```
i_address = 3996
memory[i_address] = 9999

[....9999,0,0,0,5,104,101,108,108,111,5,119,111,114,108,100....]
     ^          ^                     ^
     i          this is a             this is b
  idx: 3996     idx: 4000             idx: 4006

```

The memory doesnt care, string integers, characters,, its all the same. It doesn't know where one array ends or begins. You just read and write to specific address and thats all it cares about. *WHERE* to read and write.

Think about what it means to remove a character from our string, if its the last character we can sinply reduce the lengthm but lets say we want to remove 'o' from 'world', that would mean something like:

```
world

* reduce the length to 4
* move r to the left
* move l to the left
* move d to the left

```

You see we had to do 4 things to remove 1 character, and imagine if the string is 10000 chars long and we want to remove the first one, we wikl have to do 999 things, moving each character to the left.


In the same time, it is super easy to go to specific character, if I want to print the 3rd char, I can just do memory[address + 1 + 3] and thats it, add 1 because of the length and then add however many characters i want to skip.

There are different way to store collections of things, Linked Lists are one example

```

[0, value]            # w
 |
[next_address, value] # o
 |
[next_address, value] # r
 |
[next_address, value] # l
 |
[0, value ]           # d
```

Arrays and Lists are very differentm arrays are *always* continous, like strings, actually string is just an array of characters. Lists however can be on scattered amongst the memory, and each element can point to the next one.

So with a linked list it is hard to get to position 3 for example, because we have to start from the top, and go down until we see 3 elements, so we have to do 3 things to get to position 3, or 1000 things to get to position 1000. In the same time if we want to remove something, we can simply make it disappear, by making the previous element point to the next one, e.g. make `o` point to `l`, and then `r` will disappear.


Our format will be (next element from the list, value)

```
memory[20000] = 30000
memory[20001] = 1

memory[30000] = 30500
memory[30001] = 2

memory[30500] = 30605
memory[30501] = 3

memory[30605] = 0
memory[30606] = 4
```

the memory now looks like this:

```
[ ....30000, 1, .... 30500, 2, .... 30605, 3, .... 0, 4, ...]
      ^              ^              ^              ^
      first          second         third          forth element
```


This is an example function that will print all the values in a linked list, following the links.

```
def lprint(start_address):
    done = False
    while not done:
        # check if this is the last element of the list
        done = memory[start_address] == 0

        # print the value at address + 1
        print(memory[start_address+1])

        # go to the next element from the list
        start_address = memory[start_address]

lprint(20000)
```

You see, having a flat area of memory is so powerfull! it doesnt know anything about what we store in it, so of course we can store pointers to other parts of the memory, we can have lists of lists of lists of lists that just point around, and of course we can have infinite loops, imagine a linked list where one of the elements points to a previous elemnent.

Check this out:
```
memory[20000] = 30000
memory[20001] = 1

memory[30000] = 20000
memory[30001] = 2

lprint(20000)
```

Inifinite loop! How cool is that!

```
1
2
1
2
1
2
1
2
1
2
1
2
1
2
1
2
```



Lets make a computer, it needs Memory and CPU, the CPU will read instructions from memory and produce results back in memory.

```
memory = []
for i in range(1000000):
    memory.append(0)


memory[1000] = 5  # a
memory[1001] = 10 # b
memory[1002] = 0  # result

# lets multiply a * b
# the code looks like this
# counter = b
# while counter > 0:
#     r = r + a
#     counter -= 1
# print(r)

# counter = b
memory[1003] = memory[1001]

# jump to position 10 if counter is 0
memory[0] = 4
memory[1] = 1003
memory[2] = 13

# r = r + a
memory[3] = 1
memory[4] = 1002
memory[5] = 1000
memory[6] = 1002


# since our add operation adds two things in memory, we
# need to store the value -1 somewhere to subtract it from the counter
#
# counter -= 1
memory[9999] = -1
memory[7] = 1
memory[8] = 1003
memory[9] = 9999
memory[10] = 1003

# go back to the if counter == 0 instruction
memory[11] = 5
memory[12] = 0

# print(r)
memory[13] = 3
memory[14] = 1002

# stop the program
memory[15] = 0

position = 0
while True:
    instruction = memory[position]
    print('instruction',instruction, 'position',position)
    # quit if instruction is 0
    if instruction == 0:
        break

    # add position+1 and position+2 and write result in position+3
    elif instruction == 1:
        a_address = memory[position+1]
        b_address = memory[position+2]

        r_address = memory[position+3]

        memory[r_address] = memory[a_address] + memory[b_address]
        position += 4

    # print position + 1
    elif instruction == 3:
        address = memory[position+1]
        print(memory[address])
        position+=2

    # if memory[position+1] is 0 jump to positon+2, else continue to position+3
    elif instruction == 4:
        address = memory[position+1]
        if memory[address] == 0:
            position = memory[position+2]
        else:
            position += 3

    # jump to value of position+1
    elif instruction == 5:
        position = memory[position+1]
```


start the computer and see the result!

```
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 1, 'position', 3)
('instruction', 1, 'position', 7)
('instruction', 5, 'position', 11)
('instruction', 4, 'position', 0)
('instruction', 3, 'position', 13)
50
('instruction', 0, 'position', 15)
```

Now lets get into variables from first principles, they are nothing but handy pointers to memory, that you can name yourself, and then you can access this memory by the name you chose.

This is the same program, but we are gonna use A, B, R, COUNTER and MINUS_1 as names for the specific addressess, and you can immidiately see how much cleaner the program looks. We will also name our instructions ADD, JUMP_IF_ZERO (or JZ), PRINT and HALT

```
...

# instructions
HALT = 0
ADD = 1
PRINT = 3
JUMP_IF_ZERO = 4
JUMP = 5


# variabnles
A = 1000
B = 1001
R = 1002
MINUS_1 = 9999
COUNTER = 1003


# program
memory[A] = 5  # A = 5
memory[B] = 10 # B = 5
memory[R] = 0  # R = 0
memory[COUNTER] = memory[B]  # COUNTER = B

# jump to position 10 if counter is 0
memory[0] = JUMP_IF_ZERO
memory[1] = COUNTER
memory[2] = 13

# r = r + a
memory[3] = ADD
memory[4] = R
memory[5] = A
memory[6] = R


# counter -= 1
memory[MINUS_1] = -1
# counter = counter + minus_1
memory[7] = ADD
memory[8] = COUNTER
memory[9] = MINUS_1
memory[10] = COUNTER

# go back to the if counter == 0 instruction
memory[11] = JUMP
memory[12] = 0

# print(r)
memory[13] = PRINT
memory[14] = R

# stop the program
memory[15] = HALT
...

```

The whole program is actually quite small:

```
[4, 1003, 13, 1, 1000, 1002, 1002, 1, 1003, 9999, 1003, 5, 0, 3, 1002, 0]
 ^                                                      ^
 jump to 13 if memory[1003] is zero                     jump to 0
```

## [DAY-95] Memory; Machine Code; Virtual Computer

It will be super nice if our multiply program can be used from multiple places from a bigger program:

```
...
r = multiply(5, 10)
print(r)
...
```

We can kind of do that, by just using jump, and carefully writing the multiply function in such a way, that when it is done, to jump back to where we called it. We also have to give it some values to work with, in our case 5 and 10.

We will use a simple list to append the values and the return address, and then pop them out in the right order to use them. Our multiply function has to know how many values to read and it must know which one of them is the return address. `[5, 10, ZZZ]` imagine ZZZ is the address where we should return after we have computed the result. And then the function will just do POP, POP, POP and know, first POP will be ZZZ, second pop will be one parameter, third pop will be another parameter. Do what it does with the parameters, and then append its result into the stack, then the caller must know to POP it.

It is called a stack because it is like a stack of things on top of each other (cards for example), you can append(push) one to the top, or remove one from the top (pop). When we pop() we will remove the last thing we push()ed.

If I push 1,2,3 then if i pop 3 times I will print 3 2 1

```
stack = [1,2,3]

print(stack.pop())
print(stack.pop())
print(stack.pop())
```

Here is our updated program, and computer:

```
memory = []
for i in range(1000000):
    memory.append(0)

HALT         = 0
ADD          = 1
PRINT        = 3
JUMP_IF_ZERO = 4
JUMP         = 5
PUSH         = 8
POP          = 9
SET          = 10

JUMPV        = 11 # same as jump, but jumps to the
                  # value of the address instead of the address itself
                  # so jumpv 9, will jump to the value of memory[9]

PUSHV        = 12 # same as jumpv but for push


# just used for debug
instruction_lookup = dict([
    (HALT         , 'HALT'),
    (ADD          , 'ADD'),
    (PRINT        , 'PRINT'),
    (JUMP_IF_ZERO , 'JUMP_IF_ZERO'),
    (JUMP         , 'JUMP'),
    (PUSH         , 'PUSH'),
    (POP          , 'POP'),
    (SET          , 'SET'),
    (PUSHV        , 'PUSHV'),
    (JUMPV        , 'JUMPV')
])

                  # pushv 9, will push memory[9] instead of 9
# constants addressess
# there is no such thing as constants though, we just think of them as such
MINUS_1 = 9999

# set "global" variable MINUS_1 to -1
memory[MINUS_1] = -1 # minus_1 = -1

# MAIN FUNCTION

# main function has only one variable, the MULTIPLY_RESULT
MULTIPLY_RESULT = 1000

# MULTIPLY_RESULT = multiply (5, 10)
memory[0] = PUSH            # |  |
memory[1] = 5               # ^  |
memory[2] = PUSH            #    |
memory[3] = 10              # >--+
memory[4] = PUSH            # >-------------+
memory[5] = 8               #               | after the function is called
memory[6] = JUMP            #               | jump to get the value
memory[7] = 198             #               | from the stack
memory[8] = POP             # <-------------+
memory[9] = MULTIPLY_RESULT #
memory[10] = PRINT
memory[11] = MULTIPLY_RESULT


####### MULTIPLY FUNCTION ######
# get the value of A
A = 9000
B = 9001
COUNTER = 9003
R = 9004
BACK_TO_ADDRESS = 9005

# get the value for where to return to
memory[198] = POP
memory[199] = BACK_TO_ADDRESS

# get the value for A
memory[200] = POP
memory[201] = A

# get the value for B
memory[202] = POP
memory[203] = B

# COUNTER = B (which is counter = 0 ; counter = counter + b)
# COUNTER = 0
memory[204] = SET
memory[205] = COUNTER
memory[206] = 0

# COUNTER = COUNTER + B
memory[207] = ADD
memory[208] = COUNTER
memory[209] = B
memory[210] = COUNTER

# the actual loop
memory[211] = JUMP_IF_ZERO
memory[212] = COUNTER
memory[213] = 224

# r = r + a
memory[214] = ADD
memory[215] = A
memory[216] = R
memory[217] = R

# since our add operation adds two things in memory, we
# need to store the value -1 somewhere to subtract it from the counter
#
# counter -= 1
memory[218] = ADD
memory[219] = COUNTER
memory[220] = MINUS_1
memory[221] = COUNTER

# go back to the if counter == 0 instruction
memory[222] = JUMP
memory[223] = 211

# return(r)
memory[224] = PUSHV
memory[225] = R

memory[226] = JUMPV
memory[227] = BACK_TO_ADDRESS

# start the computer from position 80, we will use positions up-to 80 for our function call stack
position = 0
stack = []
while True:
    instruction = memory[position]

    print(instruction_lookup[instruction], 'position',position, 'stack', stack)

    # quit if instruction is 0
    if instruction == HALT:
        break

    # add position+1 and position+2 and write result in position+3
    elif instruction == ADD:
        a_address = memory[position+1]
        b_address = memory[position+2]

        r_address = memory[position+3]

        memory[r_address] = memory[a_address] + memory[b_address]
        position += 4

    # print position + 1
    elif instruction == PRINT:
        address = memory[position+1]
        print(memory[address])
        position+=2

    # if memory[position+1] is 0 jump to positon+2, else continue to position+3
    elif instruction == JUMP_IF_ZERO:
        address = memory[position+1]
        if memory[address] == 0:
            position = memory[position+2]
        else:
            position += 3

    # jump to value of position+1
    elif instruction == JUMP:
        position = memory[position+1]

    elif instruction == JUMPV:
        position = memory[memory[position+1]]

    elif instruction == PUSH:
        stack.append(memory[position+1])
        position += 2

    elif instruction == PUSHV:
        stack.append(memory[memory[position+1]])
        position += 2

    elif instruction == POP:
        memory[memory[position+1]] = stack.pop()
        position += 2

    elif instruction == SET:
        memory[position+1] = memory[position+2]
        position += 3
```

We cheated a bit by using python's lists instead of our own list to do the stack. We could reserve some memory (e.g. 100000 to 200000) and just push and pop the values there, memory[100000] will just say how many elements we have in the stack, and PUSH will do `memory[[memory[100000]] = value, memory[100000] += 1`, and pop will do `memory[100000] -= 1` and use `memory[memory[100000]]` as value.

You see how powerfull are continous pieces of memory? Arrays and Lists are how computers are built!

Look. In reallity more things happen, and actually normal machine code is easier than this, you can store values in temporary places called registers, and access them really fast and nobody actually writes code like that, we use languages such as Assembler to help us, and using assemblers we built other languages, such as C, and with C we built others, such as python, and then with python we build whole systems, like instagram or dropbox. You can of course build instagram with machine code if you want, it will just take incredible amount of time, and will be gazillion times more buggy. C is good at some things that python is not, and the other way around.

The one thing you have to remember, is whatever language you are using, whatever program you are looking at, it must have some memory, and some way of modifying that memory, and execute instructions over it.

There is no magic, it is all built on this. Built with few numbers in a block of memory.


Lets examine the output of the program, you see how the stack is empty, then we add 5, 10, and then 8 which will be used from the function to go back to us.

```
PUSH position 0 stack-before [] stack-after [5]
PUSH position 2 stack-before [5] stack-after [5, 10]
PUSH position 4 stack-before [5, 10] stack-after [5, 10, 8]
JUMP position 6 stack-before [5, 10, 8] stack-after [5, 10, 8]
POP position 198 stack-before [5, 10, 8] stack-after [5, 10]
POP position 200 stack-before [5, 10] stack-after [5]
POP position 202 stack-before [5] stack-after []
SET position 204 stack-before [] stack-after []
ADD position 207 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
ADD position 214 stack-before [] stack-after []
ADD position 218 stack-before [] stack-after []
JUMP position 222 stack-before [] stack-after []
JUMP_IF_ZERO position 211 stack-before [] stack-after []
PUSHV position 224 stack-before [] stack-after [50]
JUMPV position 226 stack-before [50] stack-after [50]
POP position 8 stack-before [50] stack-after []
PRINT position 10 stack-before [] stack-after []
50
HALT position 12 stack-before []
```


We could do it the other way, first push the address to go back to, and then the values, which will be the same, we just have to decide, this is called a 'calling convention', convention is just the usuall way to do things. So each program on your computer obeys the calling convention, otherwise a chaos will arrive, imagine multiplying the return address by first paremeter and then returning to some random position in memory.

By now you can see how fragile this is, if one mistake is made, you can corrupt rest of the program, we can easilly write something into where the next instruciton is read, and make the computer halt, or go into infinite loop.

Sometimes we can find bugs in a program that we can exploit, if we can simply control the corruption, we can make it jump to somewhere where we have our own code, and then we can control what the program does.

## [DAY-96] Binary; ASCII; Memory

Lets spend a day on bits and bytes.

One bit is the minimum amount of information you can hold, it is either 1 or 0, on or off. If we have a variable that has to store the heads or tails value of a coin, we can store it in 1 bit, lets say 1 is heads, 0 is tails. To store the values of two coins we can use 2 bits.

```
0 # tails
1 # heads
```
2 possible

```
0 0 # both coins are tails
0 1 # second coin is heads
1 0 # first coin is heads
1 1 # both coins are heads
```

2 * 2 possible

We have 4 distinct values, in 2 bits, lets try 3 coins

```
000
001
010
011
100
101
110
111
```
2 * 2 * 2 possible

we have 8 distinct values in 3 bits, and in 4 bits we have 16 distinct values

```
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
```

2 * 2 * 2 * 2 possible

in 32 bits we can store 4294967295 distinct values! and in 64 bits we can store 18446744073709551615.

But what about if we want to store the value of a dice? Possible values are 1 2 3 4 5 6. We can do that in just 3 bits.

8 bits make a byte. Usually we need 1 bit of information for the sign of the number, is it - or +, so sometimes you will hear "signed integer" or "unsigned integer", and the difference is the unsigned integers get one more bit to work with, which is a big deal, if the integer is 4 bytes, that is 32 bits, the maximum possible numbmer for signed integer is 2147483647, and the minimum is -2147483647, but unsigned one is from 0 to 4294967295.

The reason is 2 * 2 * 2 * 2 * 2 * 2... 31 times is twice smaller than 2 * 2 * 2 * 2 ... 32 times.

We can also count in this system (called binary system) to make it represent numbers.

try this:

```
for i in range(255):
    print(i, ' -> ', format(i, '08b'))
```

in python format can take a number and print it as binary number:

```
0   ->  00000000
1   ->  00000001
2   ->  00000010
3   ->  00000011
4   ->  00000100
5   ->  00000101
6   ->  00000110
7   ->  00000111
8   ->  00001000
9   ->  00001001
10  ->  00001010
11  ->  00001011
12  ->  00001100
13  ->  00001101
14  ->  00001110
15  ->  00001111
16  ->  00010000
...
```

the rules to count in the binary system are the same in the decimal system, when you go from 9 to 10 you increase the number of digits, but here.. you havbe to do it many more because you habe only 0 and 1.

so you start with 0, then 1, then you are out of numbers, so you add one more and then ext one is 1 0, then 1 1 and then you are out of space again, and go 1 0 0, 1 0 1, 1 1 0, 1 1 1 and so on.

So if you need to store the number `x = 47917437`, which in binary is 10110110110010100101111101, you will need 27 bits of space. However there are more limitations, you can usually store only 4 or 8 bytes (so 32 or 64 bits) because of the way the computer is made, so we will just pad it with zeros, and what will get stored on the memory chip is 0000010110110110010100101111101, and python will know the address of that, so when you say 'a = x + 1' it will go to the specific address, read the value, add one to it, and store it back.


example if we want to store `5, h e l l o`, the computer memory might look like this:
```
       5               h                 e              l                    l               o
       5              104               101            108                  108             111

0,0,0,0,0,1,0,1, 0,1,1,0,1,0,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,1,1
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,
...
```

If we use 1 byte per character, ASCII actuaklly fitst in 7 bits (its called 7 bit ascii) as the maximum value is 127, but we store things aligned to 1 byte, the way processors are made, they have certain restrictions,m they cant just go and read/write at a specific bit position in the memory, so many times when we want to store 7 bits of data we need to use 8 bits, Unless we come with something to store in the extra bit, it will be just waste.

## [DAY-97] Lists; 

![game-97.png](./screenshots/game-97.png "game 97 screenshot")

Catch all the falling snakes.

Take this skeleton, and fill in the blanks.

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 300

falling = []
game_area = Rect(0,0,WIDTH,HEIGHT)
elf = Actor("c1")

elf.y = HEIGHT - 10
elf.x = WIDTH/2
game_over = False

def drop():
    f = Actor("snake")
    f.x = random.randint(0,WIDTH)
    f.y = random.randint(0, 150)
    falling.append(f)

def update():
    global game_over

    # move the elf left or right
    ...


    # detect the collisions between snakes and elf
    # and remove them if they collide
    ...


    # advance the snakes downwards
    ...


    # check if the snakes are outside of the game area, and set game over
    ...


    # add new snakes if there are less than 5 on the screen
    ...


def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')
        for f in falling:
            f.draw()

        screen.draw.rect(game_area, (255,0,0))
        elf.draw()

pgzrun.go()

```

This is one example of implementing it, can you think of another?

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 300

falling = []
game_area = Rect(0,0,WIDTH,HEIGHT)
elf = Actor("c1")

elf.y = HEIGHT - 10
elf.x = WIDTH/2
game_over = False

def drop():
    f = Actor("snake")
    f.x = random.randint(0,WIDTH)
    f.y = random.randint(0, 150)
    falling.append(f)

def update():
    global game_over

    # move the elf left or right
    if keyboard.left:
        elf.x = elf.x-5
    if keyboard.right:
        elf.x = elf.x+5


    # detect the collisions between snakes and elf
    # and remove them if they collide
    remove = []
    for f in falling:
        if f.colliderect(elf):
            remove.append(f)

    for r in remove:
        falling.remove(r)

    # advance the snakes downwards
    for f in falling:
        f.y += 1

    # check if the snakes are outside of the game area, and set game over
    for f in falling:
        if not f.colliderect(game_area):
            game_over = True

    # add new snakes if there are less than 5 on the screen
    if len(falling) < 5:
        drop()

def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')
        for f in falling:
            f.draw()

        screen.draw.rect(game_area, (255,0,0))
        elf.draw()

pgzrun.go()
```

Another possible implementation, this one uses `list()` to make a copy of the falling list and also has score and lives.

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 300

falling = []
game_area = Rect(0,0,WIDTH,HEIGHT)
elf = Actor("c1")

elf.y = HEIGHT - 10
elf.x = WIDTH/2
game_over = False
score = 0
lives = 5

def drop():
    f = Actor("snake")
    f.x = random.randint(0,WIDTH)
    f.y = random.randint(0, 150)
    falling.append(f)

def update():
    global game_over, score, lives


    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5

    for i in falling:
        i.y += 1

    for i in list(falling):
        if not i.colliderect(game_area):
            falling.remove(i)
            lives -= 1

    game_over = lives <= 0

    if len(falling) < 5:
        drop()

    for i in list(falling):
        if i.colliderect(elf):
            falling.remove(i)
            score += 1

def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')
        screen.draw.text("score: " + str(score) + " lives: " + str(lives), topleft=(10,10))

        for f in falling:
            f.draw()

        screen.draw.rect(game_area, (255,0,0))
        elf.draw()

pgzrun.go()
```


## [DAY-98] Lists; Read/Write File


![game-98-a.png](./screenshots/game-98-a.png "game 98-a screenshot")

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
colors = [
    [(255,0,0), Rect(0,0,40,40)],
    [(0,255,0), Rect(60,0,40,40)],
    [(0,0,255), Rect(120,0,40,40)],
]
color = None
pixels = []

def update():
    global color, pixels

    if keyboard.LEFT:
        elf.x -= 2
    if keyboard.RIGHT:
        elf.x += 2
    if keyboard.UP:
        elf.y -= 2
    if keyboard.DOWN:
        elf.y += 2

    if keyboard.Q:
        sys.exit(0)

    if keyboard.SPACE and color != None:
        pixels.append([
            color,
            Rect(elf.x,elf.y,40,40)
        ])

    if keyboard.C:
        pixels = []
        color = None

    if keyboard.D:
        drop = Rect(elf.x,elf.y,40,40)
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
        screen.draw.rect(Rect(elf.x,elf.y,40,40), color)

    elf.draw()
    screen.draw.text(str(len(pixels)), topleft=(10,10))

pgzrun.go()
```

Simple catch the flower game

![game-98-b.png](./screenshots/game-98-b.png "game 98-b screenshot")

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
flower = Actor("flower")

def update():
    if keyboard.LEFT:
        elf.x -= 5
    # add RIGHT/UP/DONW

    if keyboard.Q:
        sys.exit(0)

    # check if the elf collides the flower
    # and if it does, increment the score
    # and place the flower on some random place
    # ...

def draw():
    screen.fill('black')
    elf.draw()
    flower.draw()

    # show the score
    # ...
pgzrun.go()
```

Example implementation:

```
import pgzrun
import random
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
elf.x = WIDTH/2
elf.y = HEIGHT/2

flower = Actor("flower")
flower.x = 10
flower.y = 10
score = 0
def update():
    global score
    if keyboard.LEFT:
        elf.x -= 5
    if keyboard.RIGHT:
        elf.x += 5
    if keyboard.UP:
        elf.y -= 5
    if keyboard.DOWN:
        elf.y += 5

    if keyboard.Q:
        sys.exit(0)

    if elf.colliderect(flower):
        flower.x = random.randint(10,WIDTH-10)
        flower.y = random.randint(10,HEIGHT-10)
        score += 1

def draw():
    screen.fill('black')
    elf.draw()
    flower.draw()
    screen.draw.text(str(score), topleft=(10,10))

pgzrun.go()
```

Same program but with Load and Save

```
import pgzrun
import sys # for sys.exit()


HEIGHT = 300
WIDTH = 300

elf = Actor("c1")
colors = [
    [(255,0,0), Rect(0,0,40,40)],
    [(0,255,0), Rect(60,0,40,40)],
    [(0,0,255), Rect(120,0,40,40)],
]
color = None
pixels = []

def make_rect_around_actor(a):
    return Rect(a.x,a.y,40,40)
def update():
    global color, pixels

    if keyboard.LEFT:
        elf.x -= 2
    if keyboard.RIGHT:
        elf.x += 2
    if keyboard.UP:
        elf.y -= 2
    if keyboard.DOWN:
        elf.y += 2

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
## [DAY-99] Classes; Lists; Functions; Cartesian Coordinates

Today we talk about classes and instances.

Classes are a bit like the houses you buy in roblox, its just a recepie for a house, and when you buy it you can customize it.

If two people have houses made from the same blueprint, we call them instances, they are seperate entities, you can lock one and that does not mean the other is locked. One can have a couch the other one doesn't.

The blueprint or recipe we call 'class' and the real thing that comes out of it we call 'instance'.

The class can define functions, and those functions will take a magic `self` parameter, where `self` will be the instance. For example in roblox, the house probably has a function 'lock()' that does something like `self.is_locked = True`.

Those functions are called 'methods' and the instance is also called an object. A method is supposed to be a bit like a message to the object, `p.colliderect(r)` for example you can look at sending the message `colliderect` to the object `p` with parameter `r`. Or you can look at it just as a function with hidden `self` parameter. In the following example you can see a method `def colliderect(self,r)` in the Point class, and also a standalone function `def collidepoint(rect, point)` that just expects a rect and a point objects.


```
class Point:
    x = 0
    y = 0
    def __init__(self, name):
        self.name = name

    def print(self):
        print('point',self.x,self.y,self.name)

    def colliderect(self,r):
        return self.x > r.x and self.x < r.x + r.w and self.y > r.y and self.y < r.y + r.h

class Rect:
    x = 0
    y = 0
    w = 0
    h = 0
    def print(self):
        print('rect',self.x,self.y,self.w,self.h)


#
# |-----------------------+
# |                       |
# 6  +-------+            |
# |  |       |            |
# 4--|---x   |            |
# |  |   |   |            |
# 2--+-------+            |
# |  |   |   |            |
# +--2---6---9------------+
# 0,0
def collidepoint(rect, point):
    if point.x > rect.x and point.x < rect.x + rect.w and point.y > rect.y and point.y < rect.y + rect.h:
        return True
    else:
        return False

p = Point("blue") # instance
p.x = 6
p.y = 4

r = Rect() # instance
r.x = 2
r.y = 2
r.w = 7
r.h = 4

if collidepoint(r,p):
    print("COLLIDES")
    r.print()
    p.print()

p2 = Point("red")
p2.x = 10
p2.y = 10
if not collidepoint(r,p2):
    print("NO COLLISION")
    r.print()
    p.print()


if p.colliderect(r):
    print("p collides")
```

```
import pgzrun
import sys # for sys.exit()
import random

HEIGHT = 600
WIDTH = 600

elf = Actor("c1")
speed = 3
back = []
def update():
    global score
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.J:
        f = Actor('flower')
        f.x = elf.x
        f.y = elf.y
        back.append(f)

    if keyboard.M:
        f = open("save.txt", "w")
        for x in back:
            f.write(str(x.x))
            f.write(",")
            f.write(str(x.y))
            f.write("\n")
        f.close()
    if keyboard.L:
        f = open("save.txt", "r")
        for line in f.readlines():
            (x,y) = line.split(",") # 30,20
            a = Actor('flower')
            a.x = float(x)
            a.y = float(y)
            back.append(a)
        f.close()
    if keyboard.Q:
        sys.exit(0)

def draw():
    screen.fill('black')

    for i in back:
        i.draw()

    elf.draw()

pgzrun.go()
```

![game-99.png](./screenshots/game-99.png "game 99 screenshot")

simpler painting game:

```
import pgzrun
import sys # for sys.exit()
import random

HEIGHT = 600
WIDTH = 600

elf = Actor("c1")
speed = 3
back = []
def update():
    global score
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.J:
        f = Actor('flower')
        f.x = elf.x
        f.y = elf.y
        back.append(f)

    if keyboard.M:
        f = open("save.txt", "w")
        for x in back:
            f.write(str(x.x))
            f.write(",")
            f.write(str(x.y))
            f.write("\n")
        f.close()
    if keyboard.L:
        f = open("save.txt", "r")
        for line in f.readlines():
            (x,y) = line.split(",") # 30,20
            a = Actor('flower')
            a.x = float(x)
            a.y = float(y)
            back.append(a)
        f.close()
    if keyboard.Q:
        sys.exit(0)

def draw():
    screen.fill('black')

    for i in back:
        i.draw()

    elf.draw()

pgzrun.go()
```

## [DAY-100] Touch Typing; Lists

Day 100 party!

We will make another touch typing game

![game-100.png](./screenshots/game-100.png "game 100 screenshot")

```
import pgzrun
import random

HEIGHT = 400
WIDTH = 600

words = []
text = ''
game_over = False
beep = tone.create('A3', 0.5)

def move():
    global game_over
    for w in words:
        w[1]+= random.randint(10,15)
        if w[1] > HEIGHT:
            game_over = True

def add_word():
    common = ['a','about','all','also','and','as','at','be','because','but','by','can','come','could','day',
              'do','even','find','first','for','from','get','give','go','have','he','her','here','him','his',
              'how','i','if','in','into','it','its','just','know','like','look','make','man','many','me',
              'more','my','new','no','not','now','of','on','one','only','or','other','our','out','people',
              'say','see','she','so','some','take','tell','than','that','the','their','them','then','there',
              'these','they','thing','think','this','those','time','to','two','up','use','very','want','way',
              'we','well','what','when','which','who','will','with','would','year','you','your',
    ]
    words.append([random.randint(10,WIDTH-50), random.randint(10,HEIGHT/2), random.choice(common)])

def on_key_down(key, mod, unicode):
    global text
    if key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:-1]
    elif len(unicode) > 0 and ord(unicode) >= 65 and ord(unicode) <= 125:
        text += unicode
        for w in list(words):
            if w[2] == text:
                words.remove(w)
                text = ''
                beep.play()


def draw():
    if game_over:
        screen.fill('pink')
    else:
        screen.fill('black')

        for w in words:
            screen.draw.text(w[2], (w[0],w[1]), fontsize=20,fontname="437-win")

        screen.draw.text(text, (WIDTH/2,HEIGHT - 40), color=(255,0,0), fontsize=40,fontname="437-win")

for i in range(5):
    add_word()

clock.schedule_interval(add_word, 2)
clock.schedule_interval(move, 1)
pgzrun.go()
```


ghost!

```
import random
score = 0
while True:
    ghost = random.randint(1,3)
    choice = input('Pick a door from 1,2, or 3: ')
    if choice == str(ghost):
        print ('there is a ghost :O GAME OVER !!!')
        break
    else:
        score += 1
        print('lucky no gosht')
print('your score is ' + str(score))

```


## [DAY-101] Functions; Strings

invert a list

```
def invert(l):
    #...

print(invert([1,2,3]))
```

invert a string

```
def invert(s):
    #...

print(invert("hello"))
```

invert a number

```
def invert(n):
    #...

print(invert(123456))
```

Check if a string is a palindrome, a palindrome is a string that you can read backwards and it sounds the same.

```
Anna
civic
kayak
level
madam
mom
noon
racecar
radar
redder
refer
repaper
rotator
rotor
sagas
solos
stats
tenet
wow
Never odd or even.
We panic in a pew.
Won’t lovers revolt now?
Don’t nod.
Sir, I demand, I am a maid named Iris.
Don't nod.
I did, did I?
Step on no pets.
Eva, can I see bees in a cave?
Was it a cat I saw?
```

example:

```
while True:
    n = input("which string you want to check: )
    if is_palindrome(n):
        print(n + " is a palindrome")
    else:
        print(n + " is not a palindrome")
```

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

## [DAY-102] Touch Typing day
Whole day touch typing!

Modify the program to print some score and words per minute, and try to improve your score.

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
## [DAY-103] Read File; Command Line Arguments

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


## [DAY-104] Read File; Command Line Arguments; Dictionary

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

## [DAY-106] Read/Write File; Lists

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
## [DAY-107] Lists; Dictionaries

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

## [DAY-108] Dictionaries

count how many times each character appears in a string

```
line = "A quick brown fox jumps over the lazy dog"
count = {}
for s in line:
    if s not in count:
        count[s] = 1
    else:
        count[s] += 1

for s in count:
    print(count[s], s)
```

check if all characters from an alphabet are in a string

```
alphabet = {
    'a': True,
    'b': True,
    'c': True,
    'd': True,
    'e': True,
    'f': True,
    'g': True,
    'h': True,
    'i': True,
    'j': True,
    'k': True,
    'l': True,
    'm': True,
    'n': True,
    'o': True,
    'p': True,
    'q': True,
    'r': True,
    's': True,
    't': True,
    'u': True,
    'v': True,
    'w': True,
    'x': True,
    'y': True,
    'z': True,
    ' ': True,
}
line = "A quick brown fox jumps over the lazy dog"

for s in line:
    lower_case = s.lower()
    if lower_case not in alphabet:
        print(lower_case + " is not in the alphabet")
        break
```

are two strings equal

```
def equal(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

print(equal("hello","world"))
print(equal("hello","hello"))
print(equal("hello","roblox"))
```

are two lists of integers equal:

```
def equal(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

print(equal([1,2,3],[1,2,3,4]))
print(equal([1,2,3],[1,2,3]))
```

are two dictionaries equal

```
def equal(a,b):

    for k in a:
        if k not in b:
            return False
        if a[k] != b[k]:
            return False

    for k in b:
        if k not in a:
            return False
        if b[k] != a[k]:
            return False

    return True

print(equal({'a':'hello','b':'world'},{'a':'hello','b':'world'}))
print(equal({'a':'hello','b':'world'},{'a':'hello','b':'earth'}))
print(equal({'a':'hello','roblox': True},{'a':'hello', 'roblox': False}))
print(equal({'a':'hello','b':'world','roblox': True},{'a':'hello','b':'world'}))
```
## [DAY-109] Touch Typing Day

Touchtyping day!

## [DAY-110] Find Code on TikTok


![game-109.png](./screenshots/game-109.png "game 109 screenshot")

follow zippycode on tiktok https://www.tiktok.com/@zippycode
try some of their ideas, like:

```
from turtle import *
bgcolor('black')
n = 0
colormode(255)
while n < 200:
    right(n)
    forward(n*3)
    color(n,255-n,n%30*8)
    n+=1
```


```
from turtle import *
color('green')
speed(11)
i = 0
while True:
    circle(i*1.5)
    right(4)
    i+=1
```

## [DAY-111] Lists; Random
![game-110.png](./screenshots/game-110.png "game 110 screenshot")

```
import pgzrun
import random

WIDTH = 400
HEIGHT = 400
fox = Actor("c1")
fox.x = WIDTH/2
fox.y =HEIGHT/2

other = [
    Actor("c2", pos=(100,100)),
    Actor("c2", pos=(100,300)),
    Actor("c2",pos=(300,300)),
    Actor("c2",pos=(300,100))
]


def update():
    if keyboard.left:
        for o in other:
            o.x += 5
    if keyboard.right:
        for o in other:
            o.x -= 5
    if keyboard.up:
        for o in other:
            o.y += 5
    if keyboard.down:
        for o in other:
            o.y -= 5

    for o in list(other):
        if o.colliderect(fox):
            other.remove(o)
    if len(other) < 4:
        other.append(Actor("c2",pos=(random.randint(10,WIDTH-10), random.randint(10,HEIGHT-10))))

    for o in other:
        o.y -=1

def draw():
    screen.clear()
    screen.fill("deepskyblue")
    fox.draw()
    for o in other:
        o.draw()
pgzrun.go()
```

## [DAY-112] Use Simple Dictionary

Count the words in a song

```
song = """There once was a ship that put to sea
The name of the ship was the Billy of Tea
The winds blew up, her bow dipped down
O blow, my bully boys, blow (huh)
She had not been two weeks from shore
When down on her a right whale bore
The captain called all hands and swore
He'd take that whale in tow (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum (hey)
One day, when the tonguin' is done
We'll take our leave and go
Take our leave and go
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguin' is done
We'll take our leave and go
Before the boat had hit the water
The whale's tail came up and caught her
All hands to the side harpooned and fought her
When she dived down below (huh)
She had not been two weeks from shore
When down on her a right whale bore
The captain called all hands and swore
He'd take that whale in tow (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum (hey)
One day, when the tonguin' is done
We'll take our leave and go
Take our leave and go
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguin' is done
We'll take our leave and go
Soon may the Wellerman come
To bring us sugar and tea and rum (hey)
One day, when the tonguin' is done
We'll take our leave and go
Take our leave and go
Take our leave and go
"""

words = {}
word = ''
for c in song:
    if c == ' ' or c == '\n':
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
        word = ''
    else:
        word += c

for word in words:
    print(words[word],word)
```

This program has a bug, if the file does not end with empty line, it wont count the last word.

Print the length:

```
...
l = 0
for c in song:
    l += 1
print(l)
print(len(song))
```

## [DAY-113] Discover Pythontutor

use https://pythontutor.com/visualize.html with the folloowing code:

```
song = """Soon may the Wellerman come
To bring us sugar and tea and rum (hey)
One day, when the tonguin' is done
We'll take our leave and go
Take our leave and go
Soon may the Wellerman come
To bring us sugar and tea and rum (hey)
One day, when the tonguin' is done
"""

words = {}
word = ''
for c in song:
    if c == ' ' or c == '\n':
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
        word = ''
    else:
        word += c

for word in words:
    print(words[word],word)

```


![game-113-a.png](./screenshots/game-113-a.png "game 113-a screenshot")
![game-113-b.png](./screenshots/game-113-b.png "game 113-b screenshot")

try it with other programs as well.

## [DAY-114] Simple Turtle
![game-114.png](./screenshots/game-114.png "game 114 screenshot")

random walk

```
from turtle import *
from random import randint,choice

colors = ['red','deepskyblue','lawngreen']

screen = Screen()
width, height = screen.window_width(), screen.window_height()

pensize(5)
speed(20)

while True:
    pencolor(choice(colors))
    setheading(randint(0,360))
    forward(randint(1,100))
    (x,y) = pos()
    if x > width/2 or y > height/2 or x < -width/2 or y < -height/2:
        setpos(0,0)

```

## [DAY-115] Practical Coding, Control Roblox with python

![game-115.png](./screenshots/game-115.jpg "game 115 screenshot")

Control Roblox with python

NB: That might be considered cheating, even though its just for fun, so be ready to get your account banned.

First `pip install pyautogui` and `pip install pydirectinput`.

```
import pyautogui
import pydirectinput
import time

time.sleep(2)

while True:
    for key in ['w','a','s','d']:
        print('executing',key)
        pydirectinput.keyDown(key)
        time.sleep(1.6)
        pydirectinput.keyUp(key)
        time.sleep(0.5)
```

This is a simple program that presses w a s d, each for 1.6 seconds and then waits 0.5 seconds for the next one.

After you start the program, you have 2 seconds to click on Roblox otherwise the sequence will be wrong


## [DAY-116] Many Turtles

Many Turtles.

The ideas are borrowed from [Redisovering Logo with Bob the Turtle](https://notes.ayushsharma.in/2019/06/rediscovering-logo-with-bob-the-turtle), Ayush Sharma's amazing blog post!

![game-116-a.png](./screenshots/game-116-a.png "game 116-a screenshot")

```
import turtle

turtle.setup(width=800, height=800)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')
bob.speed(3000)

alice = turtle.Turtle(shape='turtle')
alice.color('lawngreen')
alice.speed(3000)

for i in range(500):

    bob.forward(i)
    bob.left(91)

    alice.backward(i)
    alice.right(91)

turtle.exitonclick()
```

even more turtles

![game-116-b.png](./screenshots/game-116-b.png "game 116-b screenshot")


```
import turtle

turtle.setup(width=800, height=800)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')
bob.speed(3000)

alice = turtle.Turtle(shape='turtle')
alice.color('lawngreen')
alice.speed(3000)


charlie = turtle.Turtle(shape='turtle')
charlie.color('deepskyblue')
charlie.speed(3000)

for i in range(500):

    bob.forward(i)
    bob.left(91)

    alice.backward(i)
    alice.right(91)

    charlie.forward(i)
    charlie.right(101)

turtle.exitonclick()
```

```
import turtle
turtle.setup(width=800, height=800)

bob = turtle.Turtle(shape='turtle')
bob.color('orange')

alice = turtle.Turtle(shape='turtle')
alice.color('lawngreen')
angle = 10
while True:
    alice.backward(20)
    bob.forward(20)
    alice.right(angle)
    bob.left(angle)
    angle += 1
```

Again this is the same as in roblox's houses, you have the blueprint of the house, and you can create an instance of it, and then you can modify it. so `turtle.Turtle()` creates an instance, and then you see, bob, alice and charlie have their own changes. In the same time they have the same functionality, like `forward` `up` and etc coming from the blueprint and each of those methods work on the instance itself.

## [DAY-117] Another Text Editor

![game-117.png](./screenshots/game-117.png "game 117 screenshot")

And lets discuss another text editor.

(if you are on windows make sure you `pip3 install windows-curses`)

Start super simple, what do we need to make a text editor? first we need to show the text being edited, and second we need to capture user input and modify this text.

First show some text:

```
import curses
import time

screen = curses.initscr()
screen.addstr(0, 0, "hello world",curses.A_NORMAL)
screen.refresh()

time.sleep(2)
```

Capture input and modify the text:

```
import curses

screen = curses.initscr()
text = ''
while True:
    screen.addstr(0, 0, text,curses.A_NORMAL)
    screen.refresh()

    c = screen.getch()
    text += chr(c)
```

In order to Read and Write the file we are editing, we need to have some control keys, like Ctrl+S to save, and Ctrl+C to quit without saving. Also we need to add support for backspace to be able to delete from the text string.

Hint: use `text += str(c)` to actually see the codes you need.

```
import curses
import sys

screen = curses.initscr()
curses.curs_set(2)

if len(sys.argv) != 2:
    print("usage:")
    print(sys.argv[0] + " filename")
    sys.exit(1)


text = ''
try:
    file = open(sys.argv[1],"r")
    text = file.read()
    file.close()
except:
    pass

status = 'file: ' + sys.argv[1]
while True:
    screen.clear()
    screen.addstr(0, 0, status + ' (len: ' + str(len(text)) + ')',curses.A_NORMAL)
    screen.addstr(2, 0, text,curses.A_NORMAL)
    screen.refresh()

    c = screen.getch()
    if c == 3:
        # quit Ctrl+C
        break

    if c == 19:
        # save Ctrl+S
        file = open(sys.argv[1],"w")
        file.write(text)
        file.close()
        status = 'file: ' + sys.argv[1]
        screen.addstr(0, 0, text,curses.A_NORMAL)
        continue
    if c == 8:
        # backspace
        if len(text) > 0:
            text = text[:len(text)-1]
        continue
    if (c < 127 and c > 30) or c == 10:
        text += chr(c)
        status = 'file: ' + sys.argv[1] + " (modified)"

```

## [DAY-118] Search Lyrics

Search for your favorite lyrics, dont forget to `pip3 install lyricsgenius`

```
import lyricsgenius
genius = lyricsgenius.Genius('get api key from genius.com')
genius.verbose = False
while True:
    artist = input("🔥 Artist: ")
    song_name = input("🔥 Song: ")
    song = genius.search_song(song_name, artist)
    if song == None:
        print(song_name + " / " + artist + " not found")
    else:
        print('-'  * 40)
        print(song.lyrics)
        print('-'  * 40)
```


## [DAY-119] Facial Recognition; Move 78

![game-119.png](./screenshots/game-119.png "game 119 screenshot")

Use https://github.com/ageitgey/face_recognition to see how easy it is to track people through a video stream only using 1 picture from them.

Recognize that if it is cheap and easy, it is done to you.

It will be done in the mall, to show you personalized ads, it will be done on the street to track where you go so they can sell you better things on tiktok.

They only need 1 picture.

If you are not paying, you are the product.

It is also not very easy to be tricked with mascara.


![game-119-a.png](./screenshots/game-119-a.png "game 119a screenshot")
![game-119-b.png](./screenshots/game-119-b.png "game 119b screenshot")
![game-119-c.png](./screenshots/game-119-c.png "game 119c screenshot")



even thought it was easy in 2014, https://www.theatlantic.com/technology/archive/2014/07/makeup/374929/


## [DAY-120] Program on your own form a book

Today you are on your own. We start with: https://www.amazon.de/-/en/DK/dp/1465461884 chapter 2, read it for 1 hour and make the programs and exercieses.

Write down your experience and what you struggle with.

Simple ping pong game

```
import pgzrun
import random

HEIGHT = 600
WIDTH = 600

elf = Actor('c1')
king = Actor('c2')
ball = Actor('bullet')

king.y = HEIGHT/2
elf.y = HEIGHT/2
elf.x = WIDTH-10
ball.x = WIDTH/2
ball.y = HEIGHT/2
d = 1
game_over = False
speed = 1
def update():
    global d,game_over,speed
    if keyboard.up:
            elf.y -= 5
    if keyboard.down:
            elf.y += 5
    if keyboard.S:
            king.y += 5
    if keyboard.W:
            king.y -= 5

    if ball.x < 0 or ball.x > WIDTH:
        game_over = True

    if d == 1:
        ball.x += speed
    else:
        ball.x -= speed

    if elf.colliderect(ball):
        d = 0
        ball.y = random.randint(10,HEIGHT-10)
        speed += 1
    if king.colliderect(ball):
        d = 1
        ball.y = random.randint(10,HEIGHT-10)
        speed += 1

def draw():
    screen.clear()
    screen.fill("deepskyblue")

    elf.draw()
    king.draw()
    ball.draw()

    if game_over:
        screen.fill('red')

pgzrun.go()
```

## [DAY-121] Scam Check List

Scams.. Scams everywhere.

Our phone numbers, names, address are everywhere we have registered to buy something, be it bol.com, amazon, some random website we bought fidgets from, etc. So people can find out your number and name also by stealing your friends's contact list, Overall you must assume the bad guys have your information, so when you receive a call or email or even people talk to you on the street, always think sus.

Follow this list:

* Always Think Sus
* Call your parents
* If you cant reach your parents, call adult you know
* If you cant reach adult you know, go and find a mother with a child, they are the safest to talk to.
* If you can not find any adult to help hang up.
* If you think it is serious and you must act, hang up, and *you* call wherever they claim to be calling from. For example if they say they are from your bank, or from roblox, or fortnite, you google and find a contact for your bank/fortnite and *you* call them and ask what is going on.

The scammers are very smart, and have a lot of experience to trick you into doing what they want, sometimes they will call claiming your parents are in trouble and you have to give them a credit card number, sometimes they will call to tell you you win the new iPhone if you just give them a credit card number. They are very inventive as well, so the best thing is just think sus.


## [DAY-122] Lists; Random; Mutate

Hide and Seek

Ask someone to count to 10, then you hide, and ask him to find you

![game-122-a.png](./screenshots/game-122-a.png "game 122a screenshot")


```
import pgzrun
import random
HEIGHT = 600
WIDTH = 600

elf = Actor('c1')
elf.x = 20
elf.y = random.randint(0,HEIGHT)

def update():
    if keyboard.UP:
        elf.y -= 5
    if keyboard.DOWN:
        elf.y += 5
    if keyboard.RIGHT:
        elf.x += 5
    if keyboard.LEFT:
        elf.x -= 5

def draw():
    elf.draw()

pgzrun.go()

```

![game-122-b.png](./screenshots/game-122-b.png "game 122b screenshot")

Practice walking over a list with `for i in range(len(x))` and `for item in x`.

```
import pgzrun
import random
HEIGHT = 600
WIDTH = 600

elf = Actor('c1')
king = Actor('c2')
elf.x = 20
elf.y = random.randint(0,HEIGHT)
king.y = random.randint(0,HEIGHT)
king.x = WIDTH-20

things = []

def add_new_obsticle(l):
    image = random.choice(["snake","bullet","flower","rock"])
    x = Actor(image)
    x.x = random.randint(0,WIDTH)
    x.y = random.randint(0,HEIGHT)
    l.append(x)

for i in range(10):
    add_new_obsticle(things)

def update():
    if keyboard.UP:
        elf.y -= 5
    if keyboard.DOWN:
        elf.y += 5
    if keyboard.RIGHT:
        elf.x += 5
    if keyboard.LEFT:
        elf.x -= 5

    if keyboard.W:
        king.y -= 5
    if keyboard.S:
        king.y += 5
    if keyboard.D:
        king.x += 5
    if keyboard.A:
        king.x -= 5

    for s in range(len(things)):
        if things[s].colliderect(elf):
            elf.image = things[s].image

    if king.colliderect(elf):
        king.image = "c3"
def draw():
    screen.fill('azure')
    king.draw()
    elf.draw()
    for thing in things:
        thing.draw()

pgzrun.go()
```


## [DAY-123] Lists; Callbacks

![game-123.png](./screenshots/game-123.png "game 123 screenshot")

a bit more complicated game

```
import pgzrun
import random
from itertools import cycle
WIDTH = 300
HEIGHT = 300
game_over = False
player = Actor("c1", pos=((WIDTH/2), (HEIGHT-16)), anchor=("center","bottom"))
obsticles = []

def jump_up(jumper):
    sounds.jump.play()
    animate(jumper, tween='decelerate', duration=0.3, pos=(jumper.x, jumper.y - 16),on_finished=lambda: jump_down(jumper))

def jump_down(jumper):
    animate(jumper, tween='accelerate', duration=0.3, pos=(jumper.x, HEIGHT-16))

def on_key_down(key):
    if key == keys.SPACE:
        jump_up(player)

def make_obsticles():
     for i in range(0, 5 - len(obsticles)):
        # check if colliding, add random + 20 to it
        actor = Actor(random.choice(["o1","o2","o3","o4","o5","o6","o7","o8","o9","o10","o11"]), anchor=("center","bottom"))
        actor.x = WIDTH + 40 + random.randint(10, WIDTH*2)
        actor.y = HEIGHT - 16
        while True:
            actor.x += random.randint(30, 50)
            conflict = False
            for o in obsticles:
                if o.colliderect(actor):
                    conflict = True
            if not conflict:
                break

        obsticles.append(actor)

def update():
    global game_over

    if len(obsticles) < 5:
        make_obsticles()

    for o in list(obsticles):
        # shrink the collision rects so the game is more fun to play
        if o.inflate(-4,-4).colliderect(player.inflate(-16,-16)):
            game_over = True

        # remove the obsticles out of screen
        o.x -= 2
        if o.x < -10:
            obsticles.remove(o)


# player animation
# we just change the image of the actor every 0.4 seconds
poses = cycle(["player/tiles-46","player/tiles-47","player/tiles-48","player/tiles-49","player/tiles-50","player/tiles-51"])
def make_actor_move():
    player.image = next(poses)
clock.schedule_interval(make_actor_move, 0.4)

def draw():
    screen.fill("black")
    player.draw()
    for o in obsticles:
        o.draw()

    for i in range(100):
        screen.blit('floor',(i * 16, HEIGHT - 16))

    if game_over:
        screen.fill("red")

pgzrun.go()

```
## [DAY-124] BMP format, Images; Encoding/Decoding

Images

The way we store image is very similar to the way we store text. It is just a bunch of bytes, but when we read them we decide to interpret them differently.

Open images/joshi-100.bmp and you will see: 

![joshi-100.bmp](./images/joshi-100.bmp "joshi") 

Now lets just read the bytes, and just show the numbers, starting at position 54, when we print new line every 106, and also we are gonna print every 4th byte.

first just print the bytes:


```
file = open("images/joshi-100.bmp","rb")
data = file.read()
file.close()

for b in data:
    print("%3d" % b,end='')
```

now lets print them in specific order:

```
file = open("images/joshi-100.bmp","rb")
data = file.read()
file.close()

width = 100
height = 106
offset = 54

for y in range(width):
    for x in range(height):
        off = offset + ((y * width + x) * 4)
        print("%3d" % data[off+2],end='')
    print()
```

![game-124.png](./screenshots/game-124.png "game 124 screenshot")


looks familiar!

The image itself actually contains information about how big it is, and where the data starts, it is specified in the bitmap format itself.


Here is the bitmap header information, copied from: http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm

| Name | Size | Offset | Description |
| - | - | - | - |
| **Header** | 14 bytes | | Windows Structure: BITMAPFILEHEADER |
| Signature | 2 bytes | 0000h | 'BM' |
| FileSize | 4 bytes | 0002h | File size in bytes |
| reserved | 4 bytes | 0006h | unused (=0) |
| DataOffset | 4 bytes | 000Ah | Offset from beginning of file to the beginning of the bitmap data |
| **InfoHeader** | 40 bytes | | Windows Structure: BITMAPINFOHEADER |
| Size | 4 bytes | 000Eh | Size of InfoHeader =40 |
| Width | 4 bytes | 0012h | Horizontal width of bitmap in pixels |
| Height | 4 bytes | 0016h | Vertical height of bitmap in pixels |
| Planes | 2 bytes | 001Ah | Number of Planes (=1) |
| Bits Per Pixel | 2 bytes | 001Ch | Bits per Pixel used to store palette entry information. This also identifies in an indirect way the number of possible colors. Possible values are:<br>1 = monochrome palette. NumColors = 1 <br>4 = 4bit palletized. NumColors = 16 <br>8 = 8bit palletized. NumColors = 256 <br>16 = 16bit RGB. NumColors = 65536<br>24 = 24bit RGB. NumColors = 16M |
| Compression | 4 bytes | 001Eh | Type of Compression <br>0 = BI\_RGB no compression <br>1 = BI\_RLE8 8bit RLE encoding <br>2 = BI\_RLE4 4bit RLE encoding |
| ImageSize | 4 bytes | 0022h | (compressed) Size of Image <br>It is valid to set this =0 if Compression = 0 |
| XpixelsPerM | 4 bytes | 0026h | horizontal resolution: Pixels/meter |
| YpixelsPerM | 4 bytes | 002Ah | vertical resolution: Pixels/meter |
| Colors Used | 4 bytes | 002Eh | Number of actually used colors. For a 8-bit / pixel bitmap this will be 100h or 256. |
| Important Colors | 4 bytes | 0032h | Number of important colors <br>0 = all |
| **ColorTable** | 4 \* NumColors bytes | 0036h | present only if Info.BitsPerPixel less than 8 <br>colors should be ordered by importance |
| Red | 1 byte | | Red intensity |
| Green | 1 byte | | Green intensity |
| Blue | 1 byte | | Blue intensity |
| reserved | 1 byte | | unused (=0) |
| repeated NumColors times |
| **Pixel Data** | InfoHeader.ImageSize bytes | | The image data

Now using the header information, we can get the width, height and data offset directly from there:

```
file = open("images/joshi-100.bmp","rb")
data = file.read()
file.close()

offset = int.from_bytes(data[10:14], byteorder='little')
width = int.from_bytes(data[18:22], byteorder='little')
height = int.from_bytes(data[22:26], byteorder='little')

for y in range(width):
    for x in range(height):
        off = offset + ((y * width + x) * 4)
        print("%3d" % data[off+2],end='')
    print()
```

You see when we read `data[10:14]` we want to skip `signature` (2 bytes), `file size` (4 bytes) and `reserved` (4 bytes) and read exactly 4 bytes after that.
And we can make 4 bytes into a integer with `int.from_bytes`. We will get into that later. For now the important thing to focus on is the format itself.

It has a header, followed up by data. This is very common method and you will see it in all kinds of places. Even in our virtual computer when we were storing the strings we used a similar method, the first byte was always the length of the string.


## [DAY-125] Lists; Dictionaries

![game-125-a.png](./screenshots/game-125-a.png "game 125 a screenshot")
![game-125-b.png](./screenshots/game-125-b.png "game 125 b screenshot")
![game-125-c.png](./screenshots/game-125-c.png "game 125 c screenshot")
![game-125-d.png](./screenshots/game-125-d.png "game 125 d screenshot")

Write code to destroy your enemies!

You have access to your `heroes` and `enemies` positions. When you collide you destroy each other.

```
import pgzrun
import random
from itertools import cycle

WIDTH=600
HEIGHT=600

enemies = []
heroes = []

text = """
for h in heroes:
    h.x += random.randint(-10,10)
    h.y += random.randint(-10,10)
"""

enemy_programs = cycle([
"""
i = 0
for e in enemies:
    e.x = i * 10
    e.y = i * 10
    i += 1
""",
"""
for e in enemies:
    e.x += random.randint(-10,10)
    e.y += random.randint(-10,10)
""",
"""
for e in enemies:
    (x,y) = random.choice(heroes)
    e.x = x
    e.y = y
"""
])

enemy_code = None

def reset():
    global heroes, enemies, enemy_code
    enemy_code = next(enemy_programs)
    enemies = []
    heroes = []
    for i in range(20):
        enemies.append(Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT), 10, 10))
        heroes.append(Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT), 10, 10))


def on_key_down(key, mod, unicode):
    global text, pause, score_words, score
    if key == keys.BACKSPACE:
        if mod == 1024 or mod == 256:
            text = ''
        if len(text) > 0:
            text = text[:-1]
    elif key == keys.SPACE:
        text += ' '
    elif key == keys.TAB:
        text += '  '        
    elif key == keys.RETURN:
        text += '\n'        
    elif len(unicode) > 0 and ord(unicode) >= 34 and ord(unicode) <= 126:
        text += unicode

def run_code():
    try:
        enemy_positions = []
        for e in enemies:
            enemy_positions.append((e.x, e.y))
        hero_positions = []
        for h in heroes:
            hero_positions.append((e.x, e.y))            
        exec(text, {"heroes": heroes,"random":random, "enemies": enemy_positions})
        exec(enemy_code, {"enemies": enemies, "random":random, "heroes": hero_positions})

        for h in list(heroes):
            collided = False
            for e in list(enemies):
                if e.colliderect(h):
                    enemies.remove(e)
            if collided:
                heroes.remove(h)                    
        if len(enemies) < 50:
            enemies.append(Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT), 10, 10))

        heroes.append(Rect(random.randint(0,WIDTH),random.randint(0,HEIGHT), 10, 10))
        if len(enemies) < 5:
            reset()

    except Exception as err:
        print(err)
        pass

reset()

clock.schedule_interval(run_code, 1)
def draw():
    screen.fill("black")

    screen.draw.text("heroes: " + str(len(heroes)) + " enemies: " + str(len(enemies)), (0, 0), align='left',fontname="437-win", fontsize=20)
    for (i,l) in enumerate(enemy_code.split('\n')):
        screen.draw.text(l, (0, (20 + (i * 16))), align='left',fontname="437-win", fontsize=14)


    for (i,l) in enumerate(text.split('\n')):
        screen.draw.text(l, (0, (HEIGHT - 200 + (i * 16))), align='left',fontname="437-win", fontsize=14)

    for e in enemies:
        screen.draw.rect(e, (255,0,0))
    for h in heroes:
        screen.draw.rect(h, (0,255,255))

pgzrun.go()
```

## [DAY-126] Read/Write File

![game-126.png](./screenshots/game-126.png "game 126 screenshot")


Save and load the position of the elf

Play hide and seek after that!


```
import pgzrun

HEIGHT = 600
WIDTH = 600

elf = Actor('c1')
elf.x = WIDTH/2
elf.y = HEIGHT/2

def update():
    if keyboard.UP:
        elf.y -= 5
    if keyboard.LEFT:
        elf.x -= 5
    if keyboard.RIGHT:
        elf.x += 5
    if keyboard.DOWN:
        elf.y += 5
    if keyboard.S:
        f = open('save','w')
        f.write('MAGIC HEADER\n' + str(elf.x) + '\n' + str(elf.y) + '\n')
        f.close()
    if keyboard.B:
        f = open("save","r")
        lines = f.readlines()
        if (lines[0].startswith('MAGIC HEADER')):
            elf.x = float(lines[1])
            elf.y = float(lines[2])
        f.close()

       
def draw():
    elf.draw()
pgzrun.go()
```
## [DAY-127] Callbacks; Schedule Interval

super short, make the actor walk

```
from itertools import cycle
import pgzrun

WIDTH=200
HEIGHT=200

elf = Actor("c1")
elf.x = WIDTH/2
elf.y = HEIGHT/2

poses = cycle(["player/tiles-46","player/tiles-47","player/tiles-48","player/tiles-49","player/tiles-50","player/tiles-51"])

def make_actor_move():
    elf.image = next(poses)
clock.schedule_interval(make_actor_move, 0.4)

def draw():
    screen.fill("black")
    elf.draw()

pgzrun.go()

```

## [DAY-128] Lists; CPU usage; Resources

![game-128.png](./screenshots/game-128.png "game 128 screenshot")


See how slow you can make your computer, by making it draw 100 000 actors 60 times per second.

See how slow it moves, open the activity monitor or the task manager to see how it eats all your resources.

After that chabnge it to 100 actors and see the difference.


```
import random
import pgzrun

WIDTH = 800
HEIGHT = 800

actors = []
for i in range(0, 100000):
    elf = Actor("c1")
    elf.x = WIDTH/2
    elf.y = HEIGHT/2
    actors.append(elf)


def update():
    if keyboard.UP:
        for i in range(0, len(actors)):
            a = actors[i]
            a.y -= i
    if keyboard.DOWN:
        for i in range(0, len(actors)):
            a = actors[i]
            a.y += i
    if keyboard.LEFT:
        for i in range(0, len(actors)):
            a = actors[i]
            a.x -= i
    if keyboard.RIGHT:
        for i in range(0, len(actors)):
            a = actors[i]
            a.x += i


def draw():
    screen.fill("black")
    for a in actors:
        a.draw()


pgzrun.go()
```
## [DAY-129] Eat your computer; Memory; CPU

consume one CPU on your computer

```
while True:
    x = 1
```

Open activity monitor/task manager and see how it will consume 100% of one CPU, your computer has more than one CPU, this code will totally consume one, and in a bit you will see the computer will get hot, and the fans will start spinning. This is because each cycle of the CPU requires energy. So when you consume 100% of the CPU it will consume the maximum possible energy, and every time you use energy something is lost, and the loss is radiated as heat, even when you run, and you sweat you can see heat coming out of you.

It might seem like `x = 1` is doing nothing, but it actually has to go to the memory address of the variable x and set it to value 1


Now, lets consume all the memory.

```
a = []
for i in range(10000000000):
    a.append(i)
```

This will create a list with 10000000000 items in it, in python the size of an integer is a bit bigger than you think, usually numbers are stored in 4 byte or 8 byte memory slots; so 10000000000 * 4 is approximately 40 gigabytes of memory, your computer has 16 or 32 gigabytes. If you let the program run long enough you will see how it grows, and it consumes more and more memory.

Now you might be surprised when it reaches your computer's max memory and it keeps going, and this is because your operating system will start taking memory out and writing it to your hard disk, this is called swapping. You will see your swap grow. If you wait long enough your computer will become slower and slower, and at some point it will be unusable.

## [DAY-130] turtle; lists; classes

![game-130.png](./screenshots/game-130.png "game 130 screenshot")

many turtles

```
import turtle
import random
colors = ['violet', 'turquoise', 'black', 
          'deepskyblue','lawngreen', 'seagreen ', 
          'royalblue', 'purple', 'red','orange']

turtles = []
for i in range(10):
    t = turtle.Turtle()
    t.color(random.choice(colors))
    t.speed(9000)
    turtles.append(t)


while True:
    for i in range(len(turtles)):
        t = turtles[i]
        t.setheading(random.randint(0,360))
        t.forward(10)
```

Lets practice making a new class, you see when we say Turtle() or Actor() we make a new instance of the class Turtle and the class Actor

The Class itself is like a blueprint of how to make a new instance of itself, for example lets make a class Point that has two properties, `x` and `y`

```
class Point:
    x = 0
    y = 0

points = []
for i in range(10):
    p = Point()
    p.x = i * 20
    p.y = i * 20
    points.append(p)

for p in points:
    print(p, p.x, p.y)
```

When you define a function in a class, you have access to special parameter, `self` which is the instance on which this function is called:

```
class Dog:
    name = ''
    def bark(self):
        print(self.name+' woof woof woof')

max = Dog()
max.name = 'Maxie'
max.bark()

rocky = Dog()
rocky.name = "Rocky"
rocky.bark()

```

There is also a special `__init__` function, called constructor that lets you pass parameters directly when you create the instance.

```
class Point:
    x = 0
    y = 0

    def __init__(self, x,y):
        self.x = x
        self.y = y

points = []
for i in range(10):
    p = Point(i * 10, i * 20)
    points.append(p)

for p in points:
    print(p, p.x, p.y)

```



## [DAY-131] Lists; Files; Dictionaries

Example dictionary, List and String

```
words = {}

words["some long key"] = True
words["x"] = 10

for k in words:
    print(k)
    print(words[k])


list_of_characters = ['a','b','c']

for i in range(len(list_of_characters)):
    print(i)
    print(list_of_characters[i])



s = "hello"
for i in range(len(s)):
    print(i)
    print(s[i])

```

You see how in the list and string we can address individual element or character by its index? In the dictionary we address things by their key, for example if i want to see the value of `some long key` I do `print(words["some long key"])`.

Now unrelated, but lets practice printing the first 100 numbers from a list.

```
a = []

for i in range(100):
    a.append(i)

for i in range(100):
    print(a[i])
```

Append to file, whatever command line agurments 1 and 2 are

```
import sys
f = open("account.txt", "a")

f.write(sys.argv[1] + " " + sys.argv[2] + "\n")

f.close()
```



## [DAY-132] Lists; Classes

![game-132.png](./screenshots/game-132.png "game 132 screenshot")

a tower defense game


```
import pgzrun
import random

WIDTH=1024
HEIGHT=576

towers = []
enemies = []
bullets = []
game_over = False
background = Actor("grass_template2", pos=(0,0), anchor=(0,0))

player = Actor("c1", pos=(WIDTH/2, HEIGHT/2), anchor=('center','bottom'))
lives = 100
cash = 100
current_wave = 1

class Tower:
    def __init__(self, image, x,y, size):
        self.actor = Actor(image, pos=(x,y), )
        self.rect = Rect((x-size/2,y-size/2), (size,size))
        self.color =  (random.randint(100,250),random.randint(100,250),random.randint(100,250))
    def shoot(self):
        for e in enemies:
            if e.colliderect(self.rect):
                b = Actor("bullet3")
                b.x = self.actor.x
                b.y = self.actor.y
                b.hit = False
                animate(b, pos=(e.x,e.y), tween='accelerate', on_finished=lambda: bullets.remove(b))
                bullets.append(b)
                break

    def colliderect(self,other):
        return self.actor.colliderect(other)
    def draw(self):
        self.actor.draw()
        #screen.draw.rect(self.rect,self.color)

def shoot():
    global cash
    for t in towers:
        t.shoot()
    for e in list(enemies):
        if e.image == 'exploded':
            enemies.remove(e)
            cash+=1

def new_wave():
    global current_wave
    for i in range(current_wave * 10):
        e = Actor("c3")
        e.y = HEIGHT
        e.x = random.randint(int(WIDTH/3), int(WIDTH-WIDTH/3))
        enemies.append(e)
    current_wave += 1

def on_key_down(key):
    global cash
    if key == keys.K_1:
        if cash >= 10:
            conflict = False
            for t in towers:
                if t.colliderect(player):
                    conflict = True

            if not conflict:
                t = Tower("tower_grass",player.x, player.y, 150)
                towers.append(t)
                cash -= 10

def update():
    global game_over
    if keyboard.UP:
        player.y -= 5
    if keyboard.DOWN:
        player.y += 5
    if keyboard.LEFT:
        player.x -= 5
    if keyboard.RIGHT:
        player.x += 5

    for e in enemies:
        if e.image != 'exploded':
            e.y -= random.randint(-1,2)
        for b in bullets:
            if b.colliderect(e):
                e.image = 'exploded'
                b.hit = True
                break
        if not background.colliderect(e):
            game_over = True
    pass


clock.schedule_interval(shoot, 1)
clock.schedule_interval(new_wave, 10)

new_wave()

def draw():
    screen.clear()
    if game_over:
        screen.fill('blue')
    else:
        background.draw()
        screen.draw.text("current_wave: " + str(current_wave) + ", cash: " + str(cash) + ", lives: " + str(lives), (5,0),fontname="437-win")   

        for b in bullets:
            if not b.hit:
                b.draw()

        for e in enemies:
            e.draw()

        for t in towers:
            t.draw()

        player.draw()

pgzrun.go()
```


## [DAY-133] Touch Typing; Lists

![game-133.png](./screenshots/game-133.png "game 133 screenshot")

Spend 15 minutes touch typing.

Add a path for the enemies to walk on.

The most important part is to think about, how would you follow a path, in this example we will follow a path by picking a next element to walk towards.

This is the most important part of the change, it is an what is called an algorithm, it is a sequence of steps to solve a problem. We can describe it in words: **find the current square you are colliding it, find which square is next in the list, start walking towards it**. Now lets write it down:

```

[...]

path = [
    Rect(0, HEIGHT/2, 50, 50),
    Rect(50, HEIGHT/2, 50, 50),

[...]

def update():

[...]

    for e in enemies:
        if e.image != 'exploded':
            destination = None
            for (i, p) in enumerate(path):
                if e.colliderect(p) and i < len(path) - 1:
                    destination = path[i+1]
                    break

            if destination != None:
                center_x = destination.x + 25
                center_y = destination.y + 25
                if e.x < center_x:
                    e.x += random.randint(0, 2)
                if e.x > center_x:
                    e.x -= random.randint(0, 2)
                if e.y > center_y:
                    e.y -= random.randint(0, 2)
                if e.y < center_y:
                    e.y += random.randint(0, 2)

[...]

```

```
import pgzrun
import random

WIDTH = 1024
HEIGHT = 576

towers = []
enemies = []
bullets = []
game_over = False
background = Actor("grass_template2", pos=(0, 0), anchor=(0, 0))


path_size = 50
path = [
    Rect(0, HEIGHT/2, 50, 50),
    Rect(50, HEIGHT/2, 50, 50),
    Rect(50, HEIGHT/2 + 50, 50, 50),
    Rect(100, HEIGHT/2 + 50, 50, 50),
    Rect(150, HEIGHT/2 + 50, 50, 50),
    Rect(200, HEIGHT/2 + 50, 50, 50),
    Rect(250, HEIGHT/2 + 50, 50, 50),
    Rect(250, HEIGHT/2 + 100, 50, 50),
    Rect(300, HEIGHT/2 + 100, 50, 50),
    Rect(350, HEIGHT/2 + 100, 50, 50),
    Rect(400, HEIGHT/2 + 100, 50, 50),
    Rect(450, HEIGHT/2 + 100, 50, 50),
    Rect(500, HEIGHT/2 + 100, 50, 50),
    Rect(500, HEIGHT/2 + 150, 50, 50),
    Rect(550, HEIGHT/2 + 150, 50, 50),
    Rect(600, HEIGHT/2 + 150, 50, 50),
    Rect(650, HEIGHT/2 + 150, 50, 50),
    Rect(650, HEIGHT/2 + 200, 50, 50),
    Rect(700, HEIGHT/2 + 200, 50, 50),
    Rect(750, HEIGHT/2 + 200, 50, 50),
    Rect(800, HEIGHT/2 + 200, 50, 50),
    Rect(850, HEIGHT/2 + 200, 50, 50),
    Rect(850, HEIGHT/2 + 150, 50, 50),
    Rect(850, HEIGHT/2 + 100, 50, 50),
    Rect(850, HEIGHT/2 + 50, 50, 50),
    Rect(850, HEIGHT/2 + 0, 50, 50),
    Rect(850, HEIGHT/2 - 50, 50, 50),
    Rect(850, HEIGHT/2 - 100, 50, 50),
    Rect(900, HEIGHT/2 - 100, 50, 50),
    Rect(950, HEIGHT/2 - 100, 50, 50),
    Rect(1000, HEIGHT/2 - 100, 50, 50),
    Rect(1050, HEIGHT/2 - 100, 50, 50),
    Rect(1100, HEIGHT/2 - 100, 50, 50),
]


player = Actor("c1", pos=(WIDTH/2, HEIGHT/2), anchor=('center', 'bottom'))
lives = 100
cash = 100
current_wave = 1


class Tower:
    def __init__(self, image, x, y, size):
        self.actor = Actor(image, pos=(x, y), )
        self.rect = Rect((x-size/2, y-size/2), (size, size))
        self.color = (random.randint(100, 250), random.randint(
            100, 250), random.randint(100, 250))

    def shoot(self):
        for e in enemies:
            if e.colliderect(self.rect):
                b = Actor("bullet3")
                b.x = self.actor.x
                b.y = self.actor.y
                b.hit = False
                animate(b, pos=(e.x, e.y), tween='accelerate',
                        on_finished=lambda: bullets.remove(b))
                bullets.append(b)
                break

    def colliderect(self, other):
        return self.actor.colliderect(other)

    def draw(self):
        self.actor.draw()
        screen.draw.rect(self.rect,self.color)


def shoot():
    global cash
    for t in towers:
        t.shoot()
    for e in list(enemies):
        if e.image == 'exploded':
            enemies.remove(e)
            cash += 1


def new_wave():
    global current_wave
    for i in range(10 + (current_wave * 2)):
        e = Actor("c3")
        e.y = HEIGHT/2+10
        e.x = 0
        enemies.append(e)
    current_wave += 1


def on_key_down(key):
    global cash
    if key == keys.K_1:
        if cash >= 10:
            conflict = False
            for t in towers:
                if t.colliderect(player):
                    conflict = True

            for p in path:
                if player.colliderect(p):
                    conflict = True

            if not conflict:
                t = Tower("tower_grass", player.x, player.y, 150)
                towers.append(t)
                cash -= 10


def update():
    global game_over
    if keyboard.UP:
        player.y -= 5
    if keyboard.DOWN:
        player.y += 5
    if keyboard.LEFT:
        player.x -= 5
    if keyboard.RIGHT:
        player.x += 5

    for e in enemies:
        if e.image != 'exploded':
            destination = None
            for (i, p) in enumerate(path):
                if e.colliderect(p) and i < len(path) - 1:
                    destination = path[i+1]
                    break

            if destination != None:
                center_x = destination.x + 25
                center_y = destination.y + 25
                if e.x < center_x:
                    e.x += random.randint(0, 2)
                if e.x > center_x:
                    e.x -= random.randint(0, 2)
                if e.y > center_y:
                    e.y -= random.randint(0, 2)
                if e.y < center_y:
                    e.y += random.randint(0, 2)

        for b in bullets:
            if b.colliderect(e):
                e.image = 'exploded'
                b.hit = True
                break
        if not background.colliderect(e):
            game_over = True
    pass


clock.schedule_interval(shoot, 1)
clock.schedule_interval(new_wave, 10)

new_wave()


def draw():
    screen.clear()
    if game_over:
        screen.fill('blue')
    else:
        background.draw()

        screen.draw.text("current_wave: " + str(current_wave) + ", cash: " +
                         str(cash) + ", lives: " + str(lives), (5, 0), fontname="437-win")

        for i in range(len(path)):
            p = path[i]
            screen.draw.filled_rect(p,(255,0,0))
            screen.draw.text(str(p.x), (p.x,p.y))
        for b in bullets:
            if not b.hit:
                b.draw()

        for e in enemies:
            e.draw()

        for t in towers:
            t.draw()

        player.draw()


pgzrun.go()
```



## [DAY-134] Lists; Methods

Upgrade our tower game, make it possible to:

* delete towers and get some money back
* be able to upgrade the tower's range

First we will store original `x`,`y` and `size` in the tower's instance, and then use it to increase its range.

Again pay attention when deleting from a list we are walking on (iterating on), we actually make a clone of the list and iterate over the clone, but remove items from the original list by value.

```
[...]

class Tower:
[...]
    def __init__(self, image, x, y, size):
        self.size = size
        self.x = x
        self.y = y
        self.actor = Actor(image, pos=(x, y))
        self.rect = Rect((x-size/2, y-size/2), (size, size))
        self.color = (random.randint(100, 250), random.randint(100, 250), random.randint(100, 250))

    def resize(self, bump):
        new_size = self.size + bump
        self.size = new_size
        self.rect = Rect((self.x-new_size/2, self.y-new_size/2), (new_size, new_size))
[...]

def on_key_down(key):
    global cash
    if key == keys.K_2:
        for t in towers:
            if t.colliderect(player):
                t.resize(5)
                cash -= 10
        
    if key == keys.D:
        for t in list(towers):
            if t.colliderect(player):
                cash += 15
                towers.remove(t)
[...]

```


## [DAY-134] If

![game-134.png](./screenshots/game-134.png "game 134 screenshot")

Relax day.

Make super simple game to draw with two players, because we dont clear the screen.

```
import pgzrun

HEIGHT = 800
WIDTH = 800

elf = Actor('c1')
king = Actor('c2')

def update():
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5
    if keyboard.UP:
        king.y -= 5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.LEFT:
        king.x -= 5
    if keyboard.RIGHT:
        king.x += 5


def draw():
    elf.draw()
    king.draw()

pgzrun.go()
```

## [DAY-135] Dictionary; For

[game-135](screenshots/game-135.mp3)


Make a morse code machine!

```
import pgzrun
import time

short = tone.create('A3', 0.3)
long = tone.create('D3', 0.7)

morse = {
    'a': [short, long],
    'b': [long, short, short, short],
    'c': [long, short, long, short],
    'd': [long, short, short],
    'e': [short],
    'f': [short, short, long, short],
    'g': [long, long, short],
    'h': [short, short, short, short],
    'i': [short, short],
    'j': [short, long, long, long],
    'k': [long, short, long],
    'l': [short, long, short, short],
    'm': [long, long],
    'n': [long, short],
    'o': [long, long, long],
    'p': [short, long, long, short],
    'q': [long, long, short, long],
    'r': [short, long, short],
    's': [short, short, short],
    't': [long],
    'u': [short, short, long],
    'v': [short, short, short, long],
    'w': [short, long, long],
    'x': [long, short, short, long],
    'y': [long, short, long, long],
    'z': [long, long, short, short]
}


def play(key):
    for t in morse[key]:
        t.play()
        time.sleep(1)
    time.sleep(1)


def on_key_down(key):
    if key == keys.A:
        play('a')
    if key == keys.B:
        play('b')
    if key == keys.C:
        play('c')
    if key == keys.D:
        play('d')
    if key == keys.E:
        play('e')
    if key == keys.F:
        play('f')
    if key == keys.G:
        play('g')
    if key == keys.H:
        play('h')
    if key == keys.I:
        play('i')
    if key == keys.J:
        play('j')
    if key == keys.K:
        play('k')
    if key == keys.L:
        play('l')
    if key == keys.M:
        play('m')
    if key == keys.N:
        play('n')
    if key == keys.O:
        play('o')
    if key == keys.P:
        play('p')
    if key == keys.Q:
        play('q')
    if key == keys.R:
        play('r')
    if key == keys.S:
        play('s')
    if key == keys.T:
        play('t')
    if key == keys.U:
        play('u')
    if key == keys.V:
        play('v')
    if key == keys.W:
        play('w')
    if key == keys.X:
        play('x')
    if key == keys.Y:
        play('y')
    if key == keys.Z:
        play('z')


def update():
    pass


def draw():
    pass


pgzrun.go()
```
## [DAY-136] For; Arrays; Memory

Lets make a super simple C program

Just to get familiar witht he syntax, it does not use indentation to group code, but {}, and also each variable has to have known type (size), e.g we have to tell the C compiler (compiler is a program that takes the text code and transforms it into machine code) that  `i` is of type `int` which on our computer is exactly 4 bytes long.

```
#include <stdio.h>
int main() {
    int sum = 0;
    for (int i = 0; i < 100; i++) {
        sum += 10;
    }

    printf("%d\n", sum);
}
```

When you execute `gcc -o foo foo.c` (if you save the program in foo.c), it will make the binary `foo`, do `cat foo` to see the actual binary made from the compiler. If you run `objdump -D foo` you will see the assembly code and the machine code corresponding to it.

`cat foo`:
```
????X? H__PAGEZERO?__TEXT@@__text__TEXT0?X0??__stubs__TEXT????__stub_helper__TEXT?????__cstring__TEXT????__unwind_info__TEXT??H???__DATA_CONST@@@@__got__DATA_CONST@?__DATA?@?@__la_symbol_ptr__DATA?__data__DA?H__LINKEDIT?@?"?? ?0?0h???H
                               P?? 
                                   /usr/lib/dyld9??
                                                   f:^?[c?υ02 

                                                              ?*(?0?
                                                                    8d
                                                                      /usr/lib/libSystem.B.dylib&`)h?UH??H???E??E??E??}?d??E???
?E??E???E???????u?H?=2??	?E?H??]??%r@L?q@AS?%a?h?????%d
0?44??4
       ??#Q@dyld_stub_binderQr?s@_printf?__mh_execute_header!main%?~??0?$ __mh_execute_header_main_printfdyld_stub_binder__dyld_privat
```

Because its a binary file, most of the bytes are not actually printable ASCII characters, you can use `hexdump` to see the byte's values:

`hexdump -C foo`

```
00000000  cf fa ed fe 07 00 00 01  03 00 00 00 02 00 00 00  |................|
00000010  10 00 00 00 58 05 00 00  85 00 20 00 00 00 00 00  |....X..... .....|
00000020  19 00 00 00 48 00 00 00  5f 5f 50 41 47 45 5a 45  |....H...__PAGEZE|
00000030  52 4f 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |RO..............|
00000040  00 00 00 00 01 00 00 00  00 00 00 00 00 00 00 00  |................|
00000050  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000060  00 00 00 00 00 00 00 00  19 00 00 00 d8 01 00 00  |................|
00000070  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
00000080  00 00 00 00 01 00 00 00  00 40 00 00 00 00 00 00  |.........@......|
00000090  00 00 00 00 00 00 00 00  00 40 00 00 00 00 00 00  |.........@......|
000000a0  05 00 00 00 05 00 00 00  05 00 00 00 00 00 00 00  |................|
000000b0  5f 5f 74 65 78 74 00 00  00 00 00 00 00 00 00 00  |__text..........|
000000c0  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
000000d0  30 3f 00 00 01 00 00 00  58 00 00 00 00 00 00 00  |0?......X.......|
000000e0  30 3f 00 00 04 00 00 00  00 00 00 00 00 00 00 00  |0?..............|
000000f0  00 04 00 80 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000100  5f 5f 73 74 75 62 73 00  00 00 00 00 00 00 00 00  |__stubs.........|
00000110  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
00000120  88 3f 00 00 01 00 00 00  06 00 00 00 00 00 00 00  |.?..............|
00000130  88 3f 00 00 01 00 00 00  00 00 00 00 00 00 00 00  |.?..............|
00000140  08 04 00 80 00 00 00 00  06 00 00 00 00 00 00 00  |................|

[...]

```

`objdump -D foo`
```
[...]
100003f30: 55                           pushq   %rbp
100003f31: 48 89 e5                     movq    %rsp, %rbp
100003f34: 48 83 ec 10                  subq    $16, %rsp
100003f38: c7 45 fc 00 00 00 00         movl    $0, -4(%rbp)
100003f3f: c7 45 f8 00 00 00 00         movl    $0, -8(%rbp)
100003f46: c7 45 f4 00 00 00 00         movl    $0, -12(%rbp)
100003f4d: 83 7d f4 64                  cmpl    $100, -12(%rbp)
100003f51: 0f 8d 17 00 00 00            jge     0x100003f6e <_main+0x3e>
100003f57: 8b 45 f8                     movl    -8(%rbp), %eax
100003f5a: 83 c0 0a                     addl    $10, %eax
100003f5d: 89 45 f8                     movl    %eax, -8(%rbp)
100003f60: 8b 45 f4                     movl    -12(%rbp), %eax
100003f63: 83 c0 01                     addl    $1, %eax
100003f66: 89 45 f4                     movl    %eax, -12(%rbp)
100003f69: e9 df ff ff ff               jmp     0x100003f4d <_main+0x1d>
[...]
```

`addl` meand `add`, `jmp` means jump and so forth. This is not important for now, the point is that `gcc` which is a popular C compiler, will take your code and make it into machine code.

Lets have another example:


FizzBuzz

```
#include <stdio.h>
int main() {
    for (int i = 0; i < 100; i++) {
        if (i % 15 == 0) {
            printf("fizzbuzz\n");
        } else if (i % 5 == 0) {
            printf("buzz\n");
        } else if (i % 3 == 0) {
            printf("fizz\n");
        } else {
            printf("%d\n",i);
        }
    }
}
```

What is your name?

```
#include <stdio.h>
int main() {
    char input[20] = {0};
    while(1) {
        printf("What is your name: ");
        scanf("%s",input);
        printf("\nHello %s\n",input);
    }
}
```

You see how we say `char input[20]` which means we habe 20 elements of type `char` pointed by the input variable, it is literally just a pointer to some memory, and we can use `input[1]` to go to the address `input` plus 1 byte. Same with `int x[10]`, if we do x[3], it will go to the address pointed by `x` and add 3 * 4 to it.

We can make interesting bugs like that, because nobody will check if we go and read somewhere outside of the defined array:


```
#include <stdio.h>
int main() {
    char input[20] = {0};
    int b = 5;
    while(1) {
        printf("What is your name: ");
        scanf("%s",input);
        printf("\nHello %s\n",input);

        for (int i = 0; i < 40; i++) {
            printf("  %d -> %d -> %c\n", i, input[i],input[i]);
        }
    }
}

```

You will see some garbage from element 20 to 39, because it will actually go and read beyond the input bounderioes.


## [DAY-137] For; File; If

Play with [words.txt](words.txt)

Open the file and print all the lines:

```
f = open("words.txt")
for line in f:
    print(line)
```

Remove the newline:

```
f = open("words.txt")
for line in f:
    word = line.strip()
    print(word)
```

Print only words with more than 10 characters:

```
f = open("words.txt")
for line in f:
    word = line.strip()
    if len(word) > 10:
        print(word)
```

Print only words starting with 'ab':

```
f = open("words.txt")
for line in f:
    word = line.strip()
    if word[0] == 'a' and word[1] == 'b':
        print(word)
```

Print words not containing a character

```
f = open("words.txt")
for line in f:
    word = line.strip()
    if 'e' not in word:
        print(word)
```

Avoid words containing multiple characters

```
f = open("words.txt")
def avoid(word, characters):
    for c in characters:
        for w in word:
            if w == c:
                return False
    return True

for line in f:
    word = line.strip()
    if avoid(word, ['a','b','c']):
        print(word)
```

Another implementation using 'char' in 'string':

```
f = open("words.txt")

def avoid(word, characters):
    for c in characters:
        for c in word:
            return False
    return True

for line in f:
    word = line.strip()
    if avoid(word, ['a','b','c']):
        print(word)
```

Spinning turtle

![game-137.png](./screenshots/game-137.png "game 137 screenshot")


```
import turtle as t
size = 10
t.speed(10000)
while True:
    t.right(150)
    t.forward(size)
    size += 1
```

![game-137-3.png](./screenshots/game-137-3.png "game 137-3 screenshot")

```
import turtle as t
size = 10
t.speed(10000)
while True:
    t.right(150)
    t.forward(size)
    if size % 2 == 0:
        t.color('cyan')
    else:
        t.color('magenta')
    size += 1

```

![game-137-4.png](./screenshots/game-137-4.png "game 137-4 screenshot")

```
import turtle as t
size = 1
t.speed(100000)
t.bgcolor('black')
t.hideturtle()
i = 0
while True:
    if i % 2 == 0:
        t.color('cyan')
    else:
        t.color('magenta')
    t.forward(i*3)
    t.left(91)
    i+=1
```
![game-137-2.png](./screenshots/game-137-2.png "game 137-2 screenshot")

```
from turtle import *
begin_fill()
color('red')
pensize(3)
left(48)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
done()
```

![game-137-1.png](./screenshots/game-137-1.png "game 137-1 screenshot")


```
from turtle import *
size = 1
speed(10000)
while True:
    if size % 2 == 0:
        color('blue')
    else:
        color('red')

    circle(size, size * 5)
    size += 1
```


## [DAY-138] For; File; If

Take it easy.

Count how many lines have exactly 5 characters

```
fi = open('words.txt')
n = 0
for line in fi:
    w = line.strip()
    if len(w) == 5:
        n += 1
print(n)
```

How many words have 7 and how many 5 characters?

```
fi = open('words.txt')
n = 0
x = 0
for line in fi:
    w = line.strip()
    if len(w) == 5:
        n += 1
    if len(w) == 7:
        x += 1 
print(n)
print(x)
```
## [DAY-139] While; List; Counter

First touchtype for 20 minutes.

Then do some chill turtle shapes.

![game-139-2.png](./screenshots/game-139-2.png "game 139-2 screenshot")

```
from turtle import *

speed(100000)
pencolor('cyan')
size = 66
while True:
    forward(size)
    left(size)
    size += 1
```

![game-139-1.png](./screenshots/game-139-1.png "game 139-1 screenshot")

```
from turtle import *

c = ['cyan','magenta']
dist = 20

hideturtle()
speed(11)

while True:
    color(c[dist%2])
    forward(dist)
    left(90)
    dist = dist-3
```




## [DAY-140] While; Turtle; Strings

Read the strings chapter in the Thinking Python book.

Then do some chill turtle shapes.

![game-140-1.png](./screenshots/game-140-1.png "game 140-1 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)

while True:
    for x in turtles:
        size = random.randint(10,300)
        extent = random.randint(0, 360)
        x.circle(size, extent=extent)

```


![game-140-2.png](./screenshots/game-140-2.png "game 140-2 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)



while True:
    for x in turtles:
        size = random.randint(10,300)
        for i in range(4):
            x.forward(size)
            x.right(90)

        x.circle(size)
```




![game-140-3.png](./screenshots/game-140-3.png "game 140-3 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)



while True:
    for x in turtles:
        size = random.randint(10,300)
        for i in range(4):
            x.forward(size)
            x.right(90)
```


![game-140-4.png](./screenshots/game-140-4.png "game 140-4 screenshot")

```
import turtle
import random
turtles = []
for i in range(5):
    a = turtle.Turtle()
    a.speed(10000)
    a.hideturtle()
    turtles.append(a)



while True:
    for x in turtles:
        size = random.randint(10,300)
        x.circle(size)
```


## [DAY-141] Wiki; API

Today we are going to make a small app that uses wikipedia. First install the wikipedia package:
```
pip3 install wikipedia
```

```
import wikipedia as wiki

while True:
    what = input("search> ")
    summary = wiki.summary(what)
    print(summary)
    print('*' * 40)
```

Will search wikipeadia the string you input, like this:

```
search> leonadro da vinci
Leonardo da Vinci (15 April 1452 – 2 May 1519) was an Italian polymath of...
[...]
search>
```

Lets do the same but with pygame:

![game-141.png](./screenshots/game-141.png "game 141 screenshot")

```
import wikipedia as wiki
import pgzrun

HEIGHT = 800
WIDTH = 800
text = ''
info = ''
def on_key_down(key, mod, unicode):
    global text, info
    if key == keys.BACKSPACE:
        if len(text) > 0:
            text = text[:-1]
    elif key == keys.RETURN:
        info = wiki.summary(text)
        text = ''

    elif len(unicode) > 0 and ord(unicode) >= 32 and ord(unicode) <= 126:
        text += unicode


def draw():
    screen.clear()
    screen.draw.text(info, (10,10), fontsize=18,fontname="437-win", width=WIDTH-20)
    screen.draw.text(text, (WIDTH/2,HEIGHT - 40), color=(255,0,0), fontsize=30,fontname="437-win")

pgzrun.go()
```

What does this do actually? How does the wikipedia module work? First thing you want to check is the documentation page, https://pypi.org/project/wikipedia/ and then you can also check the source code: https://github.com/goldsmith/Wikipedia

Next you would like to think, how would this python module download the data from wikipedia.

What it actually does, is it opens a web page, just a page that is specifically made to be easier to be read with programs, try to open: https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&explaintext=&titles=Dog which will be the page for `Dog`, you will see:

```
{"batchcomplete":"","query":{"pages":{"4269567":{"pageid":4269567,"ns":0,"title":"Dog","extract":"The dog or domestic dog
[...]
an end to the dinosaurs and the appearance of the first carnivoran...
[...]
Their personality traits include hypersocial behavior, boldnes
[...]
```

You can see the equivalent HTML page at https://en.wikipedia.org/wiki/Dog, The other page, which had structured data easier to read by python and any other programming language, is called API, Application Proggramming Interface. It just means that someone thought explicitly that their output will be read by programs and not people, and so they designed the interface that way. In the wikipedia example they return JSON.

JSON is data serialization format, its goal is to make it easy for programs to exchange data, for example I can have an array, or dictionary, and I want to make it easy for some other program to read it, so I use JSON to make it into text with special rules, and they can use their JSON decoder to make it into data.

```
>>> import json
>>> a = {"a":"b","c":3}
>>>
>>> print(json.dumps([1,2,a]))
[1, 2, {"a": "b", "c": 3}]
>>>
>>> d = json.loads('[1, 2, {"a": "b", "c": 3}]')
>>> d
[1, 2, {'a': 'b', 'c': 3}]
```


You see how it looks similar to the wikipedia API output, we will go in depth in the JSON format some times later, the point now is to just recognize that there is a whole world of APIs that are gluing the programs on your computer, and even the internet together so they can communicate. JSON is one of the most common serialization protocol, but there are many many more.


## [DAY-142] While


today is again, chill turtle art

ever growing circle

![game-142-1.png](./screenshots/game-142-1.png "game 142-1 screenshot")

```
from turtle import *
speed(0)
size = 0
hideturtle()
while True:
    size += 1
    circle(size)
```


evergrowing circle and also go into negative radius

![game-142-2.png](./screenshots/game-142-2.png "game 142-2 screenshot")


```
from turtle import *
speed(0)
size = 300
hideturtle()
while True:
    size -= 1
    circle(size)
```


stop when the bottom circle is the same as the top one

![game-142-3.png](./screenshots/game-142-3.png "game 142-3 screenshot")


```
from turtle import *
speed(0)
size = 300
hideturtle()
while True:
    size -= 1
    circle(size)
    if size < -300:
        break
done()
```

make the circles more edgy

![game-142-4.png](./screenshots/game-142-4.png "game 142-4 screenshot")


```
from turtle import *
import random
speed(0)
size = 300
hideturtle()
while True:
    #size -= 1
    circle(size, steps=random.randint(10,20))
    if size < -300:
        break
done()
```
## [DAY-143] Strings

Print the characters of a string one by one:

```
a = 'hello'
for i in a:
    print(i)
```

Print the characters and their index:

```
a = 'hello'
for i in range(0,len(a)):
    print(i, a[i])
```

Reverse the characters:

```
a = 'hey'
rev = ''
for i in range(0,len(a)):
    # i = 0
    # a[2 - 0] -> a[2] -> y
    # i = 1
    # a[2 - 1] -> a[1] -> e
    # i = 2
    # a[2 - 2] -> a[0] -> h
    print(i,a[len(a)-1-i])
    rev +=a[len(a)-1-i]
print(rev)
```

Google 'how to reverse a string in python'

```
a = 'hello'
b = a[len(a)::-1]
print(b)
```

check out the stackoverflow explanation at https://stackoverflow.com/questions/509211


Answer by Greg Hewgill, https://stackoverflow.com/users/893/greg-hewgill
```

It's pretty simple really:

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
There is also the step value, which can be used with any of the above:

a[start:stop:step] # start through not past stop, by step
The key point to remember is that the :stop value represents the first value that
 is not in the selected slice. So, the difference between stop and start is the 
 number of elements selected (if step is 1, the default).

The other feature is that start or stop may be a negative number, which means it 
counts from the end of the array instead of the beginning. So:

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
Similarly, step may be a negative number:

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

Python is kind to the programmer if there are fewer items than you ask for. For example, 
if you ask for a[:-2] and a only contains one element, you get an empty list instead of 
an error. Sometimes you would prefer the error, so you have to be aware that this may happen.

Relation to slice() object
The slicing operator [] is actually being used in the above code with a slice() object 
using the : notation (which is only valid within []), i.e.:

a[start:stop:step]
is equivalent to:

a[slice(start, stop, step)]

Slice objects also behave slightly differently depending on the number of arguments, 
similarly to range(), i.e. both slice(stop) and slice(start, stop[, step]) are 
supported. To skip specifying a given argument, one might use None, so that e.g. 
a[start:] is equivalent to a[slice(start, None)] or a[::-1] is equivalent to 
a[slice(None, None, -1)].

While the :-based notation is very helpful for simple slicing, the explicit use of 
slice() objects simplifies the programmatic generation of slicing.
```

## [DAY-144] Strings; Lists

Sum the ascii of the elements of a list.

```
a = ['h','e','l','l','o']
sum = 0
for i in a:
    sum += ord(a)

print(sum)
```

Print its index, and the letter with the corresponding ascii

```
a = ['h','e','l','l','o']
sum = 0
for i in range(len(a)):
    m = ord(a[i])
    print('index: ', i, a[i], '=', m)
    sum += m

print(sum)
```

Now do the same with a string

```
a = 'hello'
sum = 0
for i in range(len(a)):
    m = ord(a[i])
    print('index: ', i, a[i], '=', m)
    sum += m

print(sum)
```

See how lists and strings both have len() and are indexable, meaning you can go to a specific index a[i] and do something.

You can mutate (change) the list, meaning you can change its content

```
a = ['h','e','l','o']
a[2] = 'b'
print(a)
```

But you can not change a string inplace:

```
a = 'hello'
a[2] = 'b'
print(a)
```

You will get `TypeError: 'str' object does not support item assignment`. If you want to change a string, you have to make a new one and reasign the variable to point to the new string.

```
a = 'hello'

a = a[0:2] + 'b' + a[3:5]
```

See how we make completely new string, made up from the parts of the old string, and also the letter 'b' in the middle, and we make the variable `a` point to the new string.





## [DAY-145] While

More turtle

![game-145.png](./screenshots/game-145.png "game 145 screenshot")


```
import turtle as t
import random

t.bgcolor('black')
t.pensize(6)
t.speed(0)

size = 20
colors =['cyan','royalblue','lawngreen','red','purple','white','yellow']

while True:
    t.pencolor(random.choice(colors))
    t.circle(size)
    t.left(12)

    size += 1
```

![game-145-2.png](./screenshots/game-145-2.png "game 145-2 screenshot")


```
from turtle import *

size = 20
speed(0)
hideturtle()

while True:
    size += 5

    circle(size)
```

![game-145-3.png](./screenshots/game-145-3.png "game 145-3 screenshot")

```
import turtle as t 

size = 0
t.speed(0)

while True:
    t.forward(size)
    t.left(90)

    size += 1
```


Lets talk again about Memory.

```
a = 'hello'
print(len(a))
a += 'b'
print(len(a))
print(a[2])
```

First lets imagine a simplified representation of the string 'hello' in memory. 

Lets imagine the computer memory as a long line of numbered boxes, so we can go directly to specific box

```
[-------------------------------------------------------------------------]
 0                                                                       1024
```

Each of the boxes can contain value between 0 and 255, so in order to store our string, we need at least 5 boxes, one for each letter, the memory does not understand such thing as character, only numnbers between 0 and 255, that is why we have the ASCII table, to have a standard how to represent characters as numbers in a common way. So we will store `h` which is 104 and, `e` which is 101, etc

Lets say that python finds out some free memory at address 555, and we just store 104,101,108,108,111, The problem with that is that we dont know when the string actually ends, so either we have to read to the first `0`, or we have to store the length of the string, and usually you store the length. So we will store the number 5, which we know is the length, and then the ASCII characters.

```
[--------------5 104 101 108 108 111----------------------------------------------]
 0             ^                                                                 1024
               555
```

Now the variable `a` just points to box 555, when we do `len(a)` we can just read the number stored at this address, and when we do `a[1]` we can read the value at address `555 + 1 + 1` which will give us (101)


What happens now when we do `a += 'b'`, this is the same as `a = a + 'b'`, which means ok, lets make a new string, with size `6` copy the original string there, and then add `b` (which is 98 in ascii) to the end. So python will try to find a space in memory for at least 7 bytes (6 for the string, and one for the lenth), and do the copy.

```
[--------------5 104 101 108 108 111------6 104 101 108 108 111 98----------------]
 0             ^                          ^                                      1024
             555                         763  
```


Imagine the next free space in memory is on address 763, it will copy the data from address 556 to 560 to address 764 to 769, it will put `98` on address 770 and of course it will place the number `7` (the length of the new string), on address 763. And now we have a new string, it will just re-assign the variable `a` to point to 763 instead of 555. Now the string on address 555 is not referenecd by any variable, and if it is not used by anything else (e.g. a list that also points to it), it can be garbage collected, and memory can be marked as free.


Lets talk about this code:

```
a = 'he'
b = 'lo'
c = 6
d = [a,b,c]
print(d[1])
```

One way python could represent a list is very similar to a string, you have length, and just addressess of the elements


```
[---3 555 763 847-----------2 104 101 ----------------2 108 111 ------6-----------]
 0  ^                       ^                         ^               ^          1024
    125                    555                       763             847 
```


The variable d will point to address `125`, from there you have first element on address 555, second on 763 and third on 847, to do `print(d[1]`) means go to 125 + 1 + 1, and follow the pointer, so go to 555 ... and so on.

See there is a small problem because now python does not know if certain address contains a string, number or a list, so usually you need one more byte of information for the type of the object. Imagine 1 is for integer, 2 for string and 3 for list.

```
[---3 2 555 763 847-------2 2 104 101 --------------2 2 108 111 -----1 6----------]
 0  ^                     ^                         ^                ^           1024
    125                  555                       763               847 
```

ok now its eaier :) we know when we go to certain address of some data what to expect, so we know if we should print ascii or the number itself, or follow the reference to wherever it goes.   

## [DAY-146] While; Classes

Circles And Squares.

![game-146.png](./screenshots/game-146.png "game 146 screenshot")


```
import turtle as t

a = t.Turtle()
a.speed(0)
a.pencolor('fuchsia')

b = t.Turtle()
b.speed(0)
b.pencolor('mediumspringgreen')


c = t.Turtle()
c.speed(0)
c.pencolor('deepskyblue')

size = 30

while True:
    a.forward(size*2)
    a.left(90)
    b.forward(size*3)
    b.right(90)
    c.forward(size*4)
    c.right(90)
    c.circle(size+1)

    size += 2
```


![game-146-1.png](./screenshots/game-146-1.png "game 146-1 screenshot")


```
import turtle as t
import random

a = t.Turtle()
a.speed(0)

b = t.Turtle()
b.speed(0)

b.hideturtle()
a.hideturtle()

b.pensize(5)
a.pensize(4)

b.pencolor('chocolate')

b.right(90)
b.forward(300)

size = 0
for i in range(70):
    a.pencolor(random.choice(['red','orange','yellow','hotpink','magenta','deepskyblue','mediumspringgreen']))
    b.right(180)
    a.circle(size,extent=90)
    a.forward(10)
    a.right(5)
    size += 1
t.done()
```


## [DAY-147] While

Another flower

![game-147.png](./screenshots/game-147.png "game 147 screenshot")


```
import turtle as t

a = t.Turtle()
a.speed(0)
a.right(90)
a.forward(300)
a.hideturtle()

b = t.Turtle()
b.speed(0)
b.hideturtle()

def square(charlie, size):
    for i in range(4):
        charlie.forward(size)
        if i == 1:
            charlie.write(str(size))
        charlie.right(90)

size = 0
while True:
    square(b,size)
    b.right(9)
    size += 1
    if size > 125:
        break

t.done()
```

## [DAY-148] Money

Every time you use something, ask yourself how does the company that made it make money. How can it be so expensive or so cheap, or worse, how can it be free.


Most of the things you own and use are made by for-profit companies, for-profit means that the company tries to maximize its revenue and profit. This is in contrast with non-profit organizations, which does not try to make more money than it needs in order to function. For example Wikipedia is run by Wikimedia Foundation, which is a non profit organization.

Revenue means how much money comes in the company by selling its products, and profit means the revenue minus the expenses it has to produce the product. For example, if we have a company to make video games, and we pay ourselves 1000 euro in salary, and we sell each video game for 2 euro, then if we sell 600 video games, we will have 1200 euro in revenue, and 200 euro in profit: `1200 revenue - 1000 expense = 200 profit`.

The profit also taxed, so we have to pay some percent from the profit to the government, lets say its 10%, so from 200 euro profit, we will pay 20 euro to the government, it will use those money to pay its employees, and pay for health insurance, social insurance, build infrastructure, and maybe small percent of those will go to research and development projects, such as CERN (a huge 30 kilometer underground tunnel with magnets, that smashes protons together to see what happens when they collide with speeds closer to the speed of light) or the international space station.

After all that, we will be left with 180 euro profit. Almost every for-profit organization will try to maximize this number, for example one way we can increase this is if we try to reduce the expenses, imagine we pay less for the developers and we pay them 800 euro instead of 1000, then it seems we will get 400 euro in profit (or 360 after tax), but maybe those developers will make a worse game, so we wont eb able to sell 600 copies, and we sell 450, and then instead of getting 400 profit we get `900 revenue - 800 expense = 100 profit`, or 90 after tax.


Now think about what it means for something to be free, like Fortnite, or Roblox, or TikTok or Instagram, or when something is sold below its production cost, like the PlayStation 3.

Lets take the PlayStation as an example, they were selling the console for 600€, but it cost them 840€ to produce, why would they do that? First think how Sony makes money, each game you buy for 60€ Sony gets 30%, so 18€ goes to sony, when you buy 20 games through the year, which is what an average person spends on video games, they get 360€ profit, so in one year they will break even after 1 year, but people use the same video console for multiple years, so every consecutive year they get more and more profit.

So on the surface it might seem like Sony is making money on the console itself, but this is actually not true.

Lets go over Roblox, how do they make money? Every developer that makes a game there is taking a cut from all the robux spent by players, and Roblox is taking 75.5% of each transaction, so when you buy something for 10€ roblox gets 7.5€ and the developer gets 2.5€. Roblox is distributed through Apple's app store, how does Apple make money? they take 30% of all payments made oh the platform, so apple will take 30% as well, so the 10€ you pay, 3€ go to Apple, 5.3€ goes to Roblox and 1.7€ goes to the developers (the content creators of roblox).

Now there are other companies, such as Facebook, where they actually do not sell you anything, but they sell you to their customers. They are selling the fact that they can make you do something you did not intend to do, like buy a skateboard or buy karaoke machine, so they use that to sell it to for-profit corporations who make skateboards and karaoke machines.

In order for them to do that, they need to be very very precise with their predictions, what exactly they can make you do and when. That requires immense amount of data, so they have to track every possible thing. For example when you are walking, your phone has an accelerometer that can see how is the phone oriented in space so just by that they can see when you are walking to somebody, or when you are in the same mall with somebody, or are you in school? which people are in the same school because the basket you put your phones in is the same for all students in your class, etc. They must record every time you scroll a video, or you hesitate to scroll.

Facebook makes about 30 euros per month for each user they are selling.

Homework:

* Why do you think whatsapp is free?
* Why is primary education free?
* Why is google translate free?
* Why is google maps free?
* Why is google search free?
* Why is fortnite free?
* Why is youtube free?
* How is tocaboca making money?
* How are the youtube content creators making money?
* How does H&M make money?
* How does the government make money?

A good thing to think about is also why are some things so expensive, how can we have smartphones for 50€ and for 2000€, what is the difference, Apple's hardware is surely expensive but is the difference between 32G phone ans 128G phone really that much? Why are the airpods 200€ when there are better headphones for 100€. Apple's physical product is not just the product you are buying, you are also buying the apple brand, which is valued very highly by the people. So even if somebody makes "better" product physically, it is not better overall, and many people still prefer Apple.

It is important to think about the product sa s combination of things, the physical/virtual product, the experience, the story, the brand, the scarcity, the timing.. everything is important.

Interestingly Apple first makes money by selling you the devices, and secondly they make money from each in-app purchase you do on those devices (e.g. robux or fortnite money). Apple made 33 billion dollars from the app store alone.

How much can a company optimize its profits? Some companies are abusing humans in the other end of the world so the product is cheaper and more competitive. The moment one company does that, all other companies have no option but to do the same thing so they are competitive. Imagine H&M or C&A, how come a jacket costs 20€? and it comes in all the way from China, it is made, loaded on a ship, sailed for 1 month and came to Rotterdam, where it was put on a truck and then an employee unloaded it and put it on display in the Mall, where they have to pay at least 20000€ per month rent. How much does the cotton cost? How much it costs to be picked from the plants, and then made into fabric, sewed and packed? How can the jacket be 20€?

This is called 'race to the bottom', when one company discovers a way to make their products cheaper, the other companies have to immidiately adapt otherwise they will lose their customers. Imagine tomorrow a new company comes and starts selling jackets for 15€, then H&M has to figure out how to make them for 15€ instead of 20€. Maybe H&M will make a contract with Apple and put 'APPLE IS THE BEST' on their jackets and then reduce the cost to 15€, or it will find a way to reduce the amount of cotton it uses, or will come up with more innovative technology to make the sewing cheaper, or it will hire cheaper labor. Sometimes they will say, oh lets sell online so we dont have to pay 20000€ per month for rent in the mall.

The 'race to the bottom' is very interesting, because it seems its making things cheaper and faster, but it is also decreasing the salaries as much as it possibly can, the salaries of the very same people who are also buying products. So they actually have less money to buy products, which makes it even more important to build cheaper products. But there are certain minimums, like raw resources needed, for example how much ground you have to grow cotton on is fixed.

Another thing that H&M can do, is simply talk with C&A and agree that they wont sell jackets below 20€, regardless how much it costs them to make, so if someone finds a way to make them for 15€ they will just make 5€ more profit, because the consumers can only chose between 20€ jackets. Or they can buy all other manufacturers of jackets and start selling jackets for 60€ instead of 20, purely because they can. The government has rules about how companies can merge together, and is trying to protect its citizens from situations like that, but it is very very difficult thing to regulate.

A lot of people in the world work as much as it is required so they do not get fired, and their employers pay them the minimum so they dont quit. The relationship between worker and employer is very complicated. You will see when you grow up, you will have jobs that you hate, and jobs that you love. Be especially carefull with the jobs that you love. 

They say 'do what you love and never work a day in your life', but what they dont say, is that you are consuming that love, little by little, like an artist who is paid to draw something she thinks is ugly, she will need the money, and the real price the artist will pay is love. The love for your craft is not infinite. It is ok to hate your job, it is also ok to love your job.

You will study a lot of theories when you grow up, about how money flows, or how the free market works, or how the capitalist or socialist system is flawed, the most important thig to remember is to go back to first principles: `how is something made, who makes it and who profits from it`, and profit does not have to be money, could be anything that people value such as: comfort, status, fame, pride, etc.

You see those forces, of the companies competing to get cheaper, sometimes they forget.. why do people use their product, even worse, sometimes they forget what their product really is. And then a new company comes, like a candle in a dark night, usually its only few people, maybe 2 or 3, working from their parent's garage, that can see what those companies can not see anymore. This is called disrupting the market. When new force appears, previously unknown, and people rejoice. The big corporations grinding their wheels create the right conditions, the right pressure, so a diamond is formed.

You can be that person, that disrupts. Every time you create something that people want, you disrupt it a bit, and sometimes your creation will resonate with the people's frequency, this is called product market fit.


## [DAY-149] Creators, Consumers and Ideas

Every human in the world has brilliant ideas, multiple ideas per week. Most of the ideas are not good, but everyone has few great ideas per week. The problem is that nobody executes on those ideas, they just get forgotten and disappear. The execution of an idea is the real deal, the idea on its own is almost worthless. How many people do you think had the Fortnite idea before Epic games? Oh lets build Minecraft and Counter Strike together and booom Fortnite is born, I bet hundreds of developers thought about it, and many of them could've made it, but.. they didn't.

Today we will talk about why people do not make their ideas into being, and just forget them. There are usually many reasons, one of them is they think they cant make it, or they think its not good, or people wont like it. The problem is, it is extremely hard to evaluate an idea that is not obviously bad, withot putting a lot of effort and time into execution to actually see if it is worth it.

Lets just think outloud about some ideas:

* Ninja Fortnite where you die if you are seen
* Fifa Minecraft where you can build your field
* Neighbourhood Nintendo Switch game exchange library
* 1 year photo collage with your friends, one photo per day from 5 people joined in a video
* Dog meeting app, so you know when your dog's best friend is on a walk, so you can go together
* Neighbourhood book exchange platform
* make/write an augmented reality book
* AR minecraft
* AR lasertag

Those ideas came out just in few minutes. Now how would you decide which ones to buld? First, my advice is, build what you want to build **right now**. Just looking at this list, I could start working on AR minecraft right after I finish writing this sentence, just thinking about it it made me excited. However when you jump like that into execution of an idea, and you expect it to resonate with other people, you will be wrong most of the time, bencause your frequency is different than other people, so they might not like what you like.

If you want your product to be used by other people, you first have to carefully research if they would actually use and pay for what you are going to build. The process is as follows:

* have an idea
* build a super duper simple prototype that is totally broken, but good enough to illustrate the idea
* use your prototype for some time
* ask your friends to use your prototype
* delete the prototype and start from scratch
* build MVP - minimum viable product, which is a somewhat polished prototype that you can show to more people
* ask for money as soon as possible, nothing says that people like your product like them paying money for it.
* ask people if they like it, figure out what they do and dont like, and go back to change your MVP while you build on it
* keep iterating on the MVP while you are building features on it, and at some point it will become product, instead of minimum viable product

even more simplified

* step 1: build something [ with feedback ]
* step 2: ask for feedback
* step 3: ask for money if you can
* step 4: goto step 1

In most cases (but not all), there is no better signal than people paying for your product. In some rare cases, you may be so ahead of the market, or have an insight which is invisible to others, that people don't even know they would pay for your product yet. The key question here is 'who do you ask', 'who are your users', 'how many are they in the world', 'how many you can reach with ads/marketing', 'how much are they willing to pay'. There is a lot of skill into figuring the answers to those questions.

If you want to make your idea not fail, you have to put in the effort, work with designers, and artists to help you build the MVP or the proof of concept. It is really hard to say if ideas fail because they are bad, or because the creators did not do a good job making it.

It is unprecedented, how few people are needed for an idea to come to life, sometimes only 1 person, a good developer, or designer is enough to completely make the MVP. A lot of that is because in the last 50 years we have dramatically improved the programming languages and tools. From assembler to python, from paint to photoshop, the productivity of a single person now is like an army of people in 1991.

A single person can change the world, most of the people however wont even try. 95% of the content in the internet is made by 5% of the people. 95% of the games in roblox is made by 5% of the players. The 5% is where all the fun is, I promise you, its like a rollercoaster.


## [DAY-150] While; Classes

Circles And Squares.

![game-150.png](./screenshots/game-150.png "game 150 screenshot")

```
from turtle import *

bgcolor('black')

a = Turtle()
a.speed(0)
a.hideturtle()

b = Turtle()
b.speed(0)
b.hideturtle()

colorA = textinput('pencolor a',"what is your name?:")
colorB = textinput('pencolor b',"what is your name?:")

size = 0
while True:
    b.pencolor(colorB)
    b.forward(size*3)
    b.left(91)

    a.pencolor(colorA)
    a.forward(size*10)
    a.circle(size, 360)
    a.left(500)

    size += 1
```

More circles

![game-150-a.png](./screenshots/game-150-a.png "game 150-a screenshot")

```
import turtle as t
t.bgcolor('black')
t.hideturtle()
size = -300
t.speed(0)
while True:
    if size % 2 == 0:
        t.pencolor('cyan')
    else:
        t.pencolor('magenta')

    t.circle(size*3)
    size += 1
```


## [DAY-151] Classes; While

![game-151.png](./screenshots/game-151.png "game 151 screenshot")

First make a painting program where you can chose colors and draw rectangles

```
import pgzrun

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
x = 0
y = 0

color = None
drop = []
size = 40
def update():
    global color,size

    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.D:
        elf.x += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.C:
        screen.clear()

    if keyboard.SPACE and color != None:

        drop.append([color, Rect(elf.x, elf.y, size, size)])

    if keyboard.K_1:
        color = (255,0,0)
    if keyboard.K_2:
        color = (25,41, 88)

    if keyboard.K_8:
        size += 1
    if keyboard.K_9:
        size -= 1
def draw():
    screen.clear()
    elf.draw()

    for pixel in drop:
        screen.draw.rect(pixel[1],pixel[0])

    if color != None:
        screen.draw.rect(Rect(elf.x,elf.y,size,size), color)
pgzrun.go()
```

Same program but making a Pixel class instead of a list with color and rect.

```
import pgzrun

WIDTH = 800
HEIGHT = 800


class Pixel:
    def __init__(self, color, x, y, size):
        self.color = color
        self.rect = Rect(x,y,size,size)
    
    def draw(self):
        screen.draw.rect(self.rect, self.color)

elf = Actor('c1')
x = 0
y = 0

color = None
drop = []
size = 40
def update():
    global color,size

    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.D:
        elf.x += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.C:
        screen.clear()

    if keyboard.SPACE and color != None:
        pixel = Pixel(color, elf.x, elf.y, size)
        drop.append(pixel)

    if keyboard.K_1:
        color = (255,0,0)
    if keyboard.K_2:
        color = (25, 41, 88)

    if keyboard.K_8:
        size += 1
    if keyboard.K_9:
        size -= 1

def draw():
    screen.clear()
    elf.draw()

    for pixel in drop:
        pixel.draw()

    if color != None:
        screen.draw.rect(Rect(elf.x,elf.y,size,size), color)
pgzrun.go()
```

Go back in the book and re-read the class chapter.

Try out some ideas with a class, just to understand better what `self` is, for example play around with this Point class, try to add `move_right` or `move_up` methods.

```
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def move(self,x,y):
        self.x = x
        self.y = y

    def move_left(self):
        self.x -= 1

    def show(self):
        print(self.x, self.y)

    def equal(self, other_point):
        if self.x == other_point.x and self.y == other_point.y:
            return True

        return False


p1 = Point(10,20)
p2 = Point(30,40)
p3 = Point(10,20)

p3.move(50,60)
p1.show()

p2.show()

p3.move_left()
p3.show()

print(p3.equal(p1))
```

---

Completely unrelated and just for fun, make a triangle like pattern:

```
while True:
    for i in range(0,10):
        print(':3'* i)
    for i in range(10,0,-1):
        print(':D' * i)
```

Prints infinite sequence of smilies

```
:3
:3:3
:3:3:3
:3:3:3:3
:3:3:3:3:3
:3:3:3:3:3:3
:3:3:3:3:3:3:3
:3:3:3:3:3:3:3:3
:3:3:3:3:3:3:3:3:3
:D:D:D:D:D:D:D:D:D:D
:D:D:D:D:D:D:D:D:D
:D:D:D:D:D:D:D:D
:D:D:D:D:D:D:D
:D:D:D:D:D:D
:D:D:D:D:D
:D:D:D:D
:D:D:D
:D:D
:D

:3
:3:3
:3:3:3
:3:3:3:3
:3:3:3:3:3
:3:3:3:3:3:3
...
```


## [DAY-152] Lists

![game-152.png](./screenshots/game-152.png "game 152 screenshot")

Make 3 actors you can pick up and drop them wherever you hit SPACE.

```
import pgzrun

WIDTH = 500
HEIGHT = 500

king = Actor('c2')
elf = Actor('c1')
flower =  Actor('flower')
rock = Actor('rock')

king.x = 480
king.y = 125
flower.y = 380
flower.x = 480
rock.x = 480
rock.y = 250

drop = []

speed = 5
def update():
    global speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.D:
        elf.x += speed
    if keyboard.A:
        elf.x -= speed
    if keyboard.C:
        screen.clear()

    if elf.colliderect(king):
        elf.image=king.image
        speed = 2
    if elf.colliderect(rock):
        elf.image=rock.image
        speed = 1
    if elf.colliderect(flower):
        elf.image=flower.image
        speed = 10
    if keyboard.SPACE and elf.image != 'c1':
        a = Actor(elf.image)
        a.x = elf.x
        a.y = elf.y
        drop.append(a)

        elf.image='c1'
        speed = 5

def draw():
    screen.clear()
    elf.draw()
    king.draw()
    flower.draw()
    rock.draw()
    for d in drop:
        d.draw()

pgzrun.go()
```


## [DAY-153] Lists; Dictionaries

![game-153.png](./screenshots/game-153.png "game 153 screenshot")

Find Waldo, here are two different implementations of the game, one uses dictionaries and one doesnt.

In this game, one of the actors has his back turned, and the purpose of the game is to find them.

We are using this example to practice lists, using `for element in list` and `for i in range(len(list))`, and overusing iterating over the list to find a matching element.

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
elf.x = 400
elf.y = 400
drop = []

def on_key_down(key):
    if key == keys.SPACE:
        found = False
        for i in drop:
            if i.image == 'c2-back':
                found = True
        if not found:
            a = Actor('c2-back')
            a.x = random.randint(0,1500)
            a.y = random.randint(0,1500)
            drop.append(a)
        for i in range(100):
            a = Actor('c2')
            a.x = random.randint(0,2000)
            a.y = random.randint(0,2000)
            drop.append(a)
    if key == keys.P:
        for i in drop:
            if i.image == 'c2-back':
                i.x = random.randint(elf.x - 200,elf.x + 200)
                i.y = random.randint(elf.y - 200,elf.y + 200)

waldo_found = False
def update():
    global waldo_found
    if keyboard.W:
        for x in range(len(drop)):
            i = drop[x]
            i.y += 5
    if keyboard.S:
        for a in range(len(drop)):
            drop[a].y -= 5
    if keyboard.A:
        for i in drop:
            i.x += 5
    if keyboard.D:
        for i in drop:
            i.x -= 5
    for i in drop:
        if i.image == 'c2-back' and elf.colliderect(i):
            waldo_found = True

def draw():
    screen.fill('black')
    elf.draw()
    for i in drop:
        i.draw()
    if waldo_found == True:
        screen.draw.text(" YOU HAVE FOUND WALDO ", (10,10))

pgzrun.go()
```


A second implementation where we use a `waldo` variable so we dont have to scan the list of actors so many times, and also we move the elf instead of moving all the actors. And we use a dictionary with positions to try to avoid adding an actor close to already existing one.

```
import pgzrun
import random

WIDTH = 800
HEIGHT = 800

elf = Actor('c1')
elf.x = 400
elf.y = 400
drop = []
waldo = Actor('c2-back')
seen = {}
def on_key_down(key):
    if key == keys.SPACE:
        waldo.x = random.randint(0,WIDTH)
        waldo.y = random.randint(0,HEIGHT)
        place = str(int(waldo.x/50)) + "_" + str(int(waldo.y/100))
        seen[place] = True
        for i in range(100):
            x = random.randint(0,WIDTH)
            y = random.randint(0,HEIGHT)
            place = str(int(x/50)) + "_" + str(int(y/100))
            if place not in seen:
                a = Actor('c2')
                a.x = x
                a.y = y
                drop.append(a)
                seen[place] = True

waldo_found = False
def update():
    global waldo_found

    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x -= 5
    if keyboard.D:
        elf.x += 5

    if waldo.colliderect(elf):
        waldo_found = True

def draw():
    screen.fill('black')
    elf.draw()
    for i in drop:
        i.draw()
    waldo.draw()

    if waldo_found == True:
        screen.draw.text(" YOU HAVE FOUND WALDO ", (10,10))

pgzrun.go()
```
## [DAY-154] Classes


Pacman, make things move around, stop when they hit something

![game-154.png](./screenshots/game-154.png "game 154 screenshot")


```
import random
import pgzrun

WIDTH = 600
HEIGHT = 600
game_over = False
lives = 3
obsticles = [
    Rect(100,100,20,20),
    Rect(200,200,100,200),
]

class Mover:
    def __init__(self, image, x, y, direction):
        self.actor = Actor(image)
        self.direction = direction
        self.actor.x = x
        self.actor.y = y
        self.counter = 0

    def draw(self):
        self.actor.draw()

    def update(self):
        orig_x = self.actor.x
        orig_y = self.actor.y
        self.counter += 1
        if self.counter > 120 and self.actor.image == "c2":
            self.direction = random.choice(['up','down','left','right'])
            self.counter = 0

        if self.direction == 'up':
            self.actor.y -= 1
        if self.direction == 'down':
            self.actor.y += 1
        if self.direction == 'left':
            self.actor.x -= 1
        if self.direction == 'right':
            self.actor.x += 1
        
        if self.actor.x > WIDTH:
            self.actor.x = 0
        if self.actor.x < 0:
            self.actor.x = WIDTH
        if self.actor.y > HEIGHT:
            self.actor.y = 0
        if self.actor.y < 0:
            self.actor.y = HEIGHT 
        hit_wall = False
        for o in obsticles:
            if self.actor.colliderect(o):
                self.actor.x = orig_x
                self.actor.y = orig_y
                hit_wall = True
                break
        if hit_wall and self.actor.image == "c2":
            self.direction = random.choice(['up','down','left','right'])


pacman = Mover("c1", 10, 10, 'up')
movers = [pacman, 
  Mover("c2", 100, 40, 'up'),
  Mover("c2", 100, 50, 'up'),
  Mover("c2", 100, 60, 'up'),
  Mover("c2", 100, 70, 'up')
]

def update():
    global lives,game_over
    if keyboard.W:
        pacman.direction = 'up'
    if keyboard.S:
        pacman.direction = 'down'
    if keyboard.A:
        pacman.direction = 'left'
    if keyboard.D:
        pacman.direction = 'right'

    for m in movers:
        m.update()
    for o in movers:
        if pacman.actor.colliderect(o.actor) and o != pacman:
            lives -= 1
            pacman.actor.x = 0
            pacman.actor.y = 0
            
            if lives < 0:
                game_over = True

def draw():
    screen.fill('black')
    for o in obsticles:
        screen.draw.filled_rect(o,(255,0,0))
    screen.draw.text('lives: ' + str(lives), (10,10))
    if game_over == True:
        screen.fill('royalblue')
        screen.draw.text('GAME OVER YOU LOST',(10,10))
    for m in movers:
        m.draw()

pgzrun.go()
```

## [DAY-155] c++

First lets discuss a bit about the difference between `c++` and `python`. For example, lets examine what happens with the following program:

```
while True:
    print("hello world")
```
If you save it in the file `hello.py`, and you have to start it with `python hello.py`. Python is a program on its own, which will load the `hello.py` file and execute it line by line. The `python` program is called `interpreter` because it interprets the code, kind of like when you read a program, trying to find out what it does, you interpret the code in your head and evaluate it.

`c` and `c++` on the other hand are compiled languages, you need a program `gcc` for c and `g++` for c++ to transform your source code to machine code, that your computer will directly run, instruction by instruction, `gcc` and `g++` are compilers.

Lets start where everything starts, print "Hello World". Save the following program in a file `hello.cpp` (cpp for c plus plus).


```
#include <iostream>
using namespace std;

int main(void) {
	cout << "Hello World " << endl;
}
```

Now lets compile it, `g++ -o hello hello.cpp` will make a program `hello` that you will be able to execute by running `./hello` you see it is very different, you run directly `hello` which will make your computer execute its instructions one by one, which is very different than running python to load your `hello.py`, in the python case your computer is running the python executable which loads your `hello.py` and interprets it line by line.

`int main()` declares the `main` function, each c/c++ program must have a main() function, thats where your program starts, unlike python, where it starts from the top of the file. You can think of your processor jumping to the address of the main function in memory, as we spoke in the previous lessons, in the computer's memoruy code is data, and data is code.

`cout` means `character output` and `<<` means `pour into the cout` whatever follows, e.g. `cout << 5` will just print 5, `cout "hello"` will print hello, `cout << 5 << "hello"` will print 5hello, and `endl` inserts the newline character `\n`.

`using namespace std;` is similar to from `turtle import *`, we will get into it later

And very importantly you `c++` does not care about your spaces, the following program compiles just fine

```
#include <iostream>
using namespace std;int main(void) {cout << "Hello World " << endl;}
```

Each code block is surrounded by `{}` and each statement ends with `;` and thats it

Try out the following programs, and just experiment with them using your python knowledge. (hint: `int` means integer)

```
#include <iostream>

using namespace std;

int main(void) {
	int i = 1000;

	while(i) {
		if (i < 500) {
			cout << "HIII" << endl;
		} else {
			cout << "Hello World " << i << endl;
		}
		i--;
	}
}
```

```
#include <iostream>

using namespace std;

int main(void) {
	for (int i = 1000; i >= 0 ; i--) {
		if (i < 500) {
			cout << "HIII " << i << endl;
		} else {
			cout << "Hello World " << i << endl;
		}
	}
	return 0;
}
```

## [DAY-156] for; while

Write the same code with for and while loops.

```
#include <iostream>
using namespace std;
int main(void) {
	int x = 3;
	while(x < 3000000){
		cout << x  << endl;
		x = x+3;
	}
	return 0;
}
```

```
#include <iostream>
using namespace std;
int main(void) {
	for (int x = 0; x < 3000000; x = x + 3) {
		cout << x  << endl;
	}
	return 0;
}
```

<hr>

```
#include <iostream>
using namespace std;
int main(void) {
	for (int x = 10; x > 0; x = x - 1) {
		cout << x << endl;
	}
	return 0;
}
```

```
#include <iostream>
using namespace std;
int main(void) {
	int x = 10;
	while(x > 0){
		cout << x  << endl;
		x -= 1;
	}
	return 0;
}
```

<hr>

```
#include <iostream>
using namespace std;
int main(void) {
	int x = 0;
	while (x < 10) {
		cout << x << endl;
		x+=1;
	}
	return 0;
}
```

```
#include <iostream>
using namespace std;
int main(void) {
	for(int x = 0; x < 10; x += 1){
		cout << x << endl;
	}
	return 0;
}
```

## [DAY-157] strings; cin

Make love tester in python:

```
while True:
    sum = 0
    name1 = input('name 1: ')
    name2 = input('name 2: ')

    for i in range(len(name1)):
        sum += ord(name1[i])
    for i in range(len(name2)):
        sum += ord(name2[i])

    match = 1 + (sum % 100)
    print("love test result:")
    print(match)
```

Write the same program in c++:

```
#include <iostream>
using namespace std;
int main()
{
    while(1) {
        string name1;
        string name2;

        cout << "name1: ";
        cin >> name1;

        cout << "name2: ";
        cin >> name2;

        int sum = 0;
        for (int i = 0; i < name1.size(); i++) {
            sum += name1[i];
        }
        for (int i = 0; i < name2.size(); i++) {
            sum += name2[i];
        }

        int match = 1 + (sum % 100);
        cout << "love test result:" << endl;
        cout << match << endl;
    }
}
```

`cin` is `character input`, you can perform a read operation by geting data out of cin with `>>`. Both `cin` and `cout` are streams. We will talk more about it later. For now just remember `cin >> variable` will read from the input and put the value in `variable`, and `cout << variable` will print the value of the variable.



## [DAY-158] if; while

rock paper scissors again

```
import random
options = ['rock','paper','scissors']

while True:
    player = input(' '.join(options) + ': ')
    if player not in options:
        print("i dont know what to do with " + player)
        continue
    computer = random.choice(options)
    print(computer)
    if player == computer:
        print("its a tie!")
    if player == 'rock':
        if computer == 'paper':
            print('U lose the round')
        elif computer == 'scissors':
            print('U win this round')
    if player == 'paper':
        if computer == 'rock':
            print('U win this round')
        elif computer == 'scissors':
            print('U lose the round')
    if player == 'scissors':
        if computer == 'rock':
            print('U lose the round')
        elif computer == 'paper':
            print('U win this round')
```

sum things

```
data = ['hello','world','earth']
r = ''
for d in data:
  r += d
print(r)

data = [1,2,3]
r = 0
for d in data:
  r += d
print(r)

data = [[1,2],[3,4],[5,6]]
r = []
for d in data:
  r += d
print(r)
```

The pattern, start with an empty result, iterate over the list and append append to the result is very very common. Examine the above code and notice how the part where it adds to the result is the same regardless if the list is list of strings, integers or list of lists

## [DAY-159] strings; sizeof

Back to basics, how are strings layed out in memory, and how many bytes the primitive types occupy in memory:

```
#include <iostream>
using namespace std;
int main(void) {
    char c = 'a';
    int x = 'a';
    bool b = true;
    int sum = 0;
    long l = 1;
    short s = 1;
    float f = 0.555;
    double d = 0.4123123;
    long double ld = 0.123123;

    cout << "char" << sizeof(c) << endl;
    cout << "bool" << sizeof(b) << endl;
    cout << "int" << sizeof(sum) << endl;
    cout << "short" << sizeof(s) << endl;
    cout << "long" << sizeof(l) << endl;
    cout << "float" << sizeof(f) << endl;
    cout << "double" << sizeof(d) << endl;
    cout << "long double" << sizeof(ld) << endl;

    int ages[10]= {10,12,10,9,10,12,12,2,3,2};
    cout << sizeof(ages) << endl;;

    long double z[5] = {0,0,0,0,0};
    cout << sizeof(z) << endl;;

    char s1[10] = {'h','e','l','l','o','w','o','r','d','\0'};
    char s2[] = "helloword";
    
    cout << s1 << endl;
    cout << s2 << endl;
}
```
<hr>
argc and argv

```
#include <iostream>
using namespace std;
int main(int argc, char* argv[]) {
    cout << "Have " << argc << " arguments:" << endl;
    cout << "my name is: " << argv[0] << endl;
    for (int i = 0; i < argc; ++i) {
        cout << i << ": " << argv[i] << endl;
    }
    return 0;
}
```
Compile the the program above as `g++ -o xyz file.cpp`, and run it with `./xyz hello world "aaa bbbb cccc" ddd`. You see `g++` has a `main` function as well, and it has `argc` and `argv` as well.

<hr>
Formatting example:

```
#include <iostream>
#include <iomanip>
using namespace std;
int main(void) {
    for (int fahr=0; fahr<=100; fahr+=10){
        cout<< endl
        << setw(6)
        << setprecision(0)
        << fahr
        << setw(10)
        << setprecision(3)
        << 5.0/9.0 * (fahr-32.0);

    }
    cout << endl;
    return(0);
}
```

## [DAY-160] pointers

c/c++ pointes and arrays are sometimes confusing, we will come back to them multiple times, especially because strings are pointers to arrays of characters, it is important for the concept to "click". Do not worry if you dont get it at first (or at second, or at third) attempt.

There are two important operators '*' and '&', `int *pa = &a` means we have a pointer (`*`) to a variable of type `int` equal to the address (`&`) of variable `a`. The value of `pa` is just a number, it is literally the address of the memory where the value of `a` will be.

The most important concept is that `pa` is actually just a number, this is the actual value of `pa`, and with `*pa = 5` means, go to this place in memory and put 5 there, we can literally go anywhere in memory and put some value there.

Arrays are a continuous chunks of memory, `char b[10]` means `b` is a pointer to somewhere in memory where you hold `10` slots of type `char` which is 10 bytes. so `b` actually just holds the location of those 10 bytes. Thats right, `b` is a pointer, we can do `b[2] = 'a'` or `*(b + 2) = 'a'` they are the same thing, as `b[2]` means go to wherever `b` points to, and add 2 slots of `b`'s type, same as `*(b + 2)`.

Examine the following program:

```
#include <iostream>
using namespace std;
int main(int argc, char* argv[]) {
    int a = 7;
    int *pa = &a;

    *pa = 8;
    cout << a << endl;

    int b[8] = {10,11,12,13,14,15,16,17};
    cout << b << endl;
    cout << (b + 3) << endl;
    cout << *(b + 3) << endl;
    cout << b[3] << endl;

    return 0;
}
```


## [DAY-161] if; while; functions

Tic tac toe with 9 variables, one for each position of the grid.

This is how the gameplay should look:

```
  a b c
0 - - -
1 - - -
2 - - -
[x] enter position (row col): 0 a

  a b c
0 x - -
1 - - -
2 - - -
[0] enter position (row col): 0 b

  a b c
0 x 0 -
1 - - -
2 - - -
[x] enter position (row col): 1 a

  a b c
0 x 0 -
1 x - -
2 - - -
[0] enter position (row col): 1 b

  a b c
0 x 0 -
1 x 0 -
2 - - -
[x] enter position (row col): 2 a

  a b c
0 x 0 -
1 x 0 -
2 x - -
x wins!
```

And this is the code:

```
#include <iostream>
using namespace std;
void render(char g0, char g1, char g2, char g3, char g4, char g5, char g6, char g7, char g8) {
    cout << "  a b c" << endl;
    cout << "0 " << g0 << " " << g1 << " " << g2 << endl;
    cout << "1 " << g3 << " " << g4 << " " << g5 << endl;
    cout << "2 " << g6 << " " << g7 << " " << g8 << endl;
}

bool wins(char symbol, char g0, char g1, char g2, char g3, char g4, char g5, char g6, char g7, char g8) {
    if (g0 == symbol && g1 == symbol && g2 == symbol) {
        return true;
    }
    if (g0 == symbol && g3 == symbol && g6 == symbol) {
        return true;
    }
    if (g0 == symbol && g4 == symbol && g8 == symbol) {
        return true;
    }
    if (g1 == symbol && g4 == symbol && g7 == symbol) {
        return true;
    }    
    if (g2 == symbol && g5 == symbol && g8 == symbol) {
        return true;
    }
    if (g3 == symbol && g4 == symbol && g5 == symbol) {
        return true;
    }    
    if (g6 == symbol && g7 == symbol && g8 == symbol) {
        return true;
    }     
    if (g6 == symbol && g4 == symbol && g2 == symbol) {
        return true;
    }
    return false;
}


int main(void) {
    char g0,g1,g2,g3,g4,g5,g6,g7,g8;
    g0 = g1 = g2 = g3 = g4 = g5 = g6 = g7 = g8 = '-';
    char symbol = 'x';
    while(1) {
        render(g0,g1,g2,g3,g4,g5,g6,g7,g8);
        char row,col;
        cout << "[" << symbol <<  "] enter position (row col): ";
        cin >> row >> col;
        cout << endl;

        if (row == '0') {
            if (col == 'a') {
                g0 = symbol;
            }
            if (col == 'b') {
                g1 = symbol;
            } 
            if (col == 'c') {
                g2 = symbol;
            }                            
        }


        if (row == '1') {
            if (col == 'a') {
                g3 = symbol;
            }
            if (col == 'b') {
                g4 = symbol;
            } 
            if (col == 'c') {
                g5 = symbol;
            }                            
        }

        if (row == '2') {
            if (col == 'a') {
                g6 = symbol;
            }
            if (col == 'b') {
                g7 = symbol;
            } 
            if (col == 'c') {
                g8 = symbol;
            }                            
        }        
        if (wins(symbol,g0,g1,g2,g3,g4,g5,g6,g7,g8)) {
            render(g0,g1,g2,g3,g4,g5,g6,g7,g8);
            cout << symbol << " wins!" << endl;
            break;
        }

        if (symbol == 'x') {
            symbol = '0';
        } else {
            symbol = 'x';
        }        
    }
    return 0;
}
```


## [DAY-162] if; while; variables

Make Tic Tac Toe in python using 9 variables; Completely on your own.

> (this is the code that she wrote)

```
def board(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    print('  ',1,2,3)
    print('a ',a1,a2,a3)
    print('b ',b1,b2,b3)
    print('c ',c1,c2,c3)

def game():
    a1 = '-'
    a2 = '-'
    a3 = '-'
    b1 = '-'
    b2 = '-'
    b3 = '-'
    c1 = '-'
    c2 = '-'
    c3 = '-'


    xz = 'x'
    while True:
        board(a1,a2,a3,b1,b2,b3,c1,c2,c3)
        ask = input(xz + ' choose a number from 1,2,3 and a letter from a,b,c: ')
        if ask == 'a1':
            a1 = xz
        if ask == 'a2':
            a2 = xz
        if ask == 'a3':
            a3 = xz
        if ask == 'b1':
            b1 = xz
        if ask == 'b2':
            b2 = xz
        if ask == 'b3':
            b3 = xz
        if ask == 'c1':
            c1 = xz
        if ask == 'c2':
            c2 = xz
        if ask == 'c3':
            c3 = xz

        if a1 == xz and a2 == xz and a3 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if a3 == xz and b3 == xz and c3 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if a2 == xz and b2 == xz and c2 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if a1 == xz and b1 == xz and c1 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if c1 == xz and c2 == xz and c3 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if b1 == xz and b2 == xz and b3 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if c1 == xz and b2 == xz and a3 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if a1 == xz and b2 == xz and c3 == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break



        if xz == 'x':
            xz = '0'
        else:
            xz = 'x'

game()
```

Another way to write the same program, using few function.

```
def print_board(a1,a2,a3,b1,b2,b3,c1,c2,c3):
    print('  ',1,2,3)
    print('a ',a1,a2,a3)
    print('b ',b1,b2,b3)
    print('c ',c1,c2,c3)

def win(xz, a1,a2,a3,b1,b2,b3,c1,c2,c3):
    if a1 == xz and a2 == xz and a3 == xz:
        return True
    if a3 == xz and b3 == xz and c3 == xz:
        return True
    if a2 == xz and b2 == xz and c2 == xz:
        return True
    if a1 == xz and b1 == xz and c1 == xz:
        return True
    if c1 == xz and c2 == xz and c3 == xz:
        return True
    if b1 == xz and b2 == xz and b3 == xz:
        return True
    if c1 == xz and b2 == xz and a3 == xz:
        return True
    if a1 == xz and b2 == xz and c3 == xz:
        return True
    return False

def get_input(xz, a1,a2,a3,b1,b2,b3,c1,c2,c3):
    ask = input(xz + ' choose a number from 1,2,3 and a letter from a,b,c: ')
    if ask == 'a1':
        a1 = xz
    if ask == 'a2':
        a2 = xz
    if ask == 'a3':
        a3 = xz
    if ask == 'b1':
        b1 = xz
    if ask == 'b2':
        b2 = xz
    if ask == 'b3':
        b3 = xz
    if ask == 'c1':
        c1 = xz
    if ask == 'c2':
        c2 = xz
    if ask == 'c3':
        c3 = xz    
    return  a1,a2,a3,b1,b2,b3,c1,c2,c3

def game():
    a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = '-'
    xz = 'x'
    while True:
        print_board(a1,a2,a3,b1,b2,b3,c1,c2,c3)
        a1,a2,a3,b1,b2,b3,c1,c2,c3 = get_input(xz, a1,a2,a3,b1,b2,b3,c1,c2,c3)

        if win(xz, a1,a2,a3,b1,b2,b3,c1,c2,c3):
            print(xz + " WINS 🥳🥳🥳!!!")
            break

        if xz == 'x':
            xz = '0'
        else:
            xz = 'x'

game()
```

Now the game loop is very obvious:

* print the board
* get the input and modify the variables
* check if there is a winnner
* swap the symbol (from x to 0 and from 0 to x)

But in the same time, when you read the functions it is a bit confusing what is a1 a2 a3.. etc. This is ok for such a small program, either way works fine, but when programs grow you have to think about 'wait if someone is reading this function, will it make sense', 'will my variable names make sense to someone else'.



## [DAY-163] if; while; lists

Do the same tic tac toe but with a list instead of 9 variables

![game-163.png](./screenshots/game-163.png "game 163 screenshot")

> (this is the code that she wrote)

```
def board(g):
    print('  ',1,2,3)
    print('a ',g[0],g[1],g[2])
    print('b ',g[3],g[4],g[5])
    print('c ',g[6],g[7],g[8])

def game():
    g = ['-','-','-','-','-','-','-','-','-']

    xz = 'x'
    while True:
        board(g)
        ask = input(xz + ' choose a number from 1,2,3 and a letter from a,b,c: ')

        if ask == 'a1':
            g[0] = xz
        if ask == 'a2':
            g[1] = xz
        if ask == 'a3':
            g[2] = xz
        if ask == 'b1':
            g[3] = xz
        if ask == 'b2':
            g[4] = xz
        if ask == 'b3':
            g[5] = xz
        if ask == 'c1':
            g[6] = xz
        if ask == 'c2':
            g[7] = xz
        if ask == 'c3':
            g[8] = xz

        if g[0] == xz and g[1] == xz and g[2] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[3] == xz and g[4] == xz and g[5] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[6] == xz and g[7] == xz and g[8] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[1] == xz and g[4] == xz and g[7] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[0] == xz and g[3] == xz and g[6] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[2] == xz and g[5] == xz and g[8] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[0] == xz and g[4] == xz and g[8] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break
        if g[2] == xz and g[4] == xz and g[6] == xz:
            print(xz+ ' Wins 🥳🥳🥳')
            break

        if xz == 'x':
            xz = '0'
        else:
            xz = 'x'

game()
```

alternative way of writing this:

```
def board(g):
    print('  ',1,2,3)
    print('a ',g[0],g[1],g[2])
    print('b ',g[3],g[4],g[5])
    print('c ',g[6],g[7],g[8])

def check(g, xz, i1,i2,i3):
    if g[i1] == xz and g[i2] == xz and g[i3] == xz:
        return True
    return False

def game():
    g = ['-','-','-','-','-','-','-','-','-']

    xz = 'x'
    while True:
        # print the board
        board(g)

        # get the input and update the game board
        ask = input(xz + ' choose a number from 1,2,3 and a letter from a,b,c: ')
        index = 0
        if ask[0] == 'a':
            index = 0 + int(ask[1]) - 1 # convert a1 to index 0, a3 to index 3
        if ask[0] == 'b':
            index = 3 + int(ask[1]) - 1 # convert b1 to index 3 and b3 to index 5
        if ask[0] == 'c':
            index = 6 + int(ask[1]) - 1 # convert c1 to index 6 and c3 to index 8
        g[index] = xz

        # check if we have a winner
        # horizontal
        if check(g,xz,0,1,2) or check(g,xz,3,4,5) or check(g,xz,6,7,8):
            print(xz+ ' Wins 🥳🥳🥳')
            break
        # vertical
        if check(g,xz,1,4,7) or check(g,xz,0,3,6) or check(g,xz,2,5,8):
            print(xz+ ' Wins 🥳🥳🥳')
            break
        # diagonal
        if check(g,xz,0,4,8) or check(g,xz,2,4,6):
            print(xz+ ' Wins 🥳🥳🥳')
            break

        # swap the synmbol for the next turn
        if xz == 'x':
            xz = '0'
        else:
            xz = 'x'

game()
```

## [DAY-164] pointers

Write a program to prepare for the test tomorrow. Its a test of abbreviations, from abbreviation to meaning. Make a program to help you study, it should ask you for a abbreviation and then you should write its meaning.

```
t.z.t -> ten zijner tijd
v.l.n.r -> van links naar rechts
e.d -> en dergelijk
nr. -> nummer
zg. -> zogenaamd
Gebr. -> gebroeders
dr. -> doctor
s.v.p -> s'il vous plait
t.o.v -> ten opzichte van
nl. -> namelijk
N.B. -> Nota Bene
sr. -> senior
jr. -> junior
C -> Celsius
etc -> etcetra
t.a.v -> ter attentie van
P.S. -> postscriptum
B. en W. -> Burgemeesteren Wethouders
NL -> Nederland
v.a -> vanaf
drs -> doctorandes
```

The program will have 2 lists with the same amount of elements, you should pick a random index, ask the user to type the meaning for `abbreviations[i]` and compare it with `meaning[i]`

```
import random
def test(taal,toets):
    i = random.randint(0,len(taal)-1)
    f = input(taal[i]+ ': ')
    if f == toets[i]:
        print('corect')
    else:
        print("WRONG, one more try!")
        f = input(taal[i]+ ': ')
        if f == toets[i]:
            print('corect')
        else:
            print('better luck next time the correct answer was: '+toets[i])

short = ['t.z.t','v.l.n.r','e.d','nr.','zg.','Gebr.','dr.',
         's.v.p','t.o.v','nl.','N.B.','sr.','jr.','C',
         'etc','t.a.v','P.S.','B. en W.','NL','v.a','drs']

long = ['ten zijner tijd','van links naar rechts','en dergelijk',
        'nummer','zogenaamd','gebroeders','doctor',
        "s'il vous plait",'ten opzichte van','namelijk',
        'Nota Bene','senior','junior','Celsius',
        'etcetra','ter attentie van','postscriptum',
        'Burgemeesteren Wethouders','Nederland','vanaf','doctorandes']

for i in range(len(short)):
    print(short[i] + ' -> ' + long[i])

while True:
    test(short,long)
    test(long, short)
```

## [DAY-165] if; while

Another tic tac toe on your own

> (this is the code she wrote)

```
def board(g):
    print(' ',1,2,3)
    print('a',g[0],g[1],g[2])
    print('b',g[3],g[4],g[5])
    print('c',g[6],g[7],g[8])

g = ['-']*9
idk = 'x'
while True:
    board(g)
    l = input(idk + 'choose a number 1,2,3 and a letter a,b,c: ')

    if l == 'a1':
        g[0] = idk
    if l == 'a2':
        g[1] = idk
    if l == 'a3':
        g[2] = idk
    if l == 'b1':
        g[3] = idk
    if l == 'b2':
        g[4] = idk
    if l == 'b3':
        g[5] = idk
    if l == 'c1':
        g[6] = idk
    if l == 'c2':
        g[7] = idk
    if l == 'c3':
        g[8] = idk
    if g[0] == idk and g[1] == idk and g[2] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[3] == idk and g[4] == idk and g[5] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[6] == idk and g[7] == idk and g[8] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[0] == idk and g[3] == idk and g[6] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[1] == idk and g[4] == idk and g[7] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    if g[2] == idk and g[5] == idk and g[8] == idk:
        print(idk+ ' Won congratulations 🥳🥳🥳')
        break
    if g[2] == idk and g[4] == idk and g[6] == idk:
        print(idk+ 'Won congratulations 🥳🥳🥳')
        break
    if g[0] == idk and g[4] == idk and g[8] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break

    done = True
    for e in g:
        if e == '-':
            done = False
    if done:
        print('Its a tie')
        break

    if idk == 'x':
        idk = '0'
    else:
        idk = 'x'
    
board(g)
```

## [DAY-166] if; while

Write tic tac toe on your own but 4x4 instead of 3x3.

> (this is the code she wrote)

```
def board(g):
    print(' ',1,2,3,4)
    print('a',g[0],g[1],g[2],g[3])
    print('b',g[4],g[5],g[6],g[7])
    print('c',g[8],g[9],g[10],g[11])
    print('d',g[12],g[13],g[14],g[15])


g = ['-']*16
idk = 'x'
while True:
    board(g)
    l = input(idk + 'choose a number 1,2,3 and a letter a,b,c: ')

    if l == 'a1':
        g[0] = idk
    if l == 'a2':
        g[1] = idk
    if l == 'a3':
        g[2] = idk
    if l == 'a4':
        g[3] = idk

    if g[0] == idk and g[1] == idk and g[2] == idk and g[3] == idk:
        print(idk+' Won congratulations 🥳🥳🥳')
        break
    # ...

    if idk == 'x':
        idk = '0'
    else:
        idk = 'x'
    
board(g)
```

## [DAY-167] C; printf; scanf

We will use `printf` to display text and `scanf` to read text input from the user. First compile the following program, save it to a file `hello.c` and run `gcc -o hello hello.c` the C compiler we will use is called `gcc`, just as the C++ compiler we used was called `g++`, and the options are again `-o` for 'output file name' and then the source code file `hello.c`.

```
#include <stdio.h>

int main(void) {
    int age = 0;

    printf("How old are you: ");
    scanf("%d",&age);
    
    if (age > 10) {
        printf("you are a grownup\n");
    } else {
        printf("are you a little kid, %d %d %c\n", age, 102, 103);
    }
    return 0;
}
```

Now lets read it line by line, first we make a variable `age` of type `integer` with initial value of `0`, then we print "How old are you" using `printf`, and immidiately after tat we do `scanf("%d",&age)`, first we say to scanf that we are looking for a integer `%d` and then once it reads an integer to put it on memory where the variable `age` is located at. With the `&` symbol we take the memory address of the variable.

Then we compare if the age that the user entered is > 10, we print one thing, and if not we print `printf("are you a little kid, %d %d %c\n", age, 102, 103);` this will print the age itself (the first %d) will use the second parameter which is `age`, then the second %d will print 102, and then %c will print the ascii value of 103 (g).

Both printf and scanf's first argument is the formatting string, while it is printing or scanning the input, whenever it sees %d %c %f (digit, character, floating point number), it will read from the arguments you passed to it and do what you want, read or write depending if printf or scanf.

This is just the first steps towards C, dont worry if you dont get the `&` thing and the memory address, with some practice things will click and it will all make sense.

Lets say your coputer has only 30 bytes of memory:

```
00-09|..........|
10-19|0000......| int age at memory address 10, occupying 4 bytes
20-29|..........|
30-39|PPPPPPPPPP| the program itself
```

`&age` is the address of age, which is 10, its as simple as that, `scanf` gets the value 10 as the location in memory in which it should write down the number that it processed from the user input.

## [DAY-168] c; while; if

Rock paper scissors in C.


```
#include <stdio.h>
#include <stdlib.h>

#define ROCK 0
#define PAPER 1
#define SCISSORS 2

int main(void) {
    while (1) {
        int player;
        printf("rock(0) paper(1) scissors(2): ");
        scanf("%d", &player);

        int computer = rand() % 3;
        printf("player: %d, computer: %d\n", player, computer);

        if (computer == player) {
            printf("its a tie\n");
        } else {
            if (computer == ROCK && player == PAPER) {
                printf("player wins\n");
            }
            if (computer == ROCK && player == SCISSORS) {
                printf("computer wins\n");
            }
            if (computer == PAPER && player == ROCK) {
                printf("computer wins\n");
            }
            if (computer == PAPER && player == SCISSORS) {
                printf("player wins\n");
            }
            if (computer == SCISSORS && player == ROCK) {
                printf("player wins\n");
            }
            if (computer == SCISSORS && player == PAPER) {
                printf("computer wins\n");
            }
        }
    }
    return 0;
}
```

`#define ROCK 0` just makes the c compiler to replace ROCK with 0 wherever it sees it in the source code. 


`#include <stdlib.h>` is needed for the `rand` function, it returns an integer, but since we need a number from 0, 1, 2 we just do `rand() % 3`, which will take the reminder from the random number and 3.

Try this in python:

```
for i in range(100000):
    print(i, i % 3)
```

You will see:

```
0 0
1 1
2 2
3 0
4 1
5 2
6 0
7 1
8 2
9 0
10 1
11 2
12 0
13 1
14 2
15 0
16 1
17 2
18 0
19 1
20 2
21 0
22 1
23 2
24 0
25 1
26 2
27 0
28 1
29 2
30 0
31 1
32 2
33 0
34 1
35 2
36 0
37 1
38 2
39 0
40 1
41 2
42 0
43 1
44 2
45 0
46 1
47 2
48 0
49 1
50 2
51 0
52 1
53 2
54 0
...
```


## [DAY-169] c; while; if

Battle ship in C.

Arrays are continous block of memory, for example `int x[10]` creates 10 integers (4 bytes each, so 40 bytes block), you can access each element by its index from `x[0]` to `x[9]`, e.g. `x[2] = 5` will set the 3rd element to be equal to 5.

In C it is very easy to have multi dimensional arrays, simply say `int x[10][10]` and that creates 10x10 integers you can access by their row and column, we will use two dimensional array to store our boards for the battleship game. As usual, we use one hidden board with the ships and one display board with the guesses.

```
#include <stdio.h>
#include <stdlib.h>
#define SIZE 10
int main(void) {
    int hidden[SIZE][SIZE];
    int display[SIZE][SIZE];
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            hidden[i][j] = 0;
            display[i][j] = 0;
        }
    }

    // make 20 random ships
    for (int i = 0; i < 20; i++) {
        hidden[rand() % SIZE][rand() % SIZE] = 1;
    }

    while (1) {
        // print the display board
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                printf("%d ", display[i][j]);
            }
            printf("\n");
        }

        // get the row and column from the user
        int row, column;
        printf("row column> ");
        scanf("%d %d", &row, &column);

        // modify the display board depending if ship is 
        // found in the hidden board or not.
        if (hidden[row][column] == 1) {
            display[row][column] = 1;
        } else {
            display[row][column] = 2;
        }
    }
    return 0;
}
```
## [DAY-170] pointers

Watch "What Are Pointers? (C++)", by javidx9 on youtube. https://www.youtube.com/watch?v=iChalAKXffs


## [DAY-171] while; for; if; list

Build a chess game in 3 days.

* day 1, build the board, black and white squares, think carefully about the algorithm how to alternate between the colors
* day 2, build the basic movement, how to pick and drop a piece (use the pieces from https://joszs.itch.io/, they are licensed as CC 4.0 and are very very beautiful)
* day 3, polish the pieces, make it possible to take a piece
* todo: add queening the pawn code later
* todo: add restrictions to illegal moves

![game-171.png](./screenshots/game-171.png "game 171 screenshot")

> This is the code that we wrote together, it actually took 3 days, 30 minutes per day, with a some help from the parent, but in the end its a (almost) working chess game.

```
import pgzrun
HEIGHT = 800
WIDTH = 800

board = []

black = [
    Actor('chess/rook-black',anchor=(0,0), pos=(0,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(100,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(200,0)),
    Actor('chess/queen-black',anchor=(0,0), pos=(300,0)),
    Actor('chess/king-black',anchor=(0,0), pos=(400,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(500,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(600,0)),
    Actor('chess/rook-black',anchor=(0,0), pos=(700,0)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(0,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(100,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(200,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(300,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(400,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(500,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(600,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(700,100)),
]

white = [
    Actor('chess/pawn-white',anchor=(0,0), pos=(0,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(100,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(200,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(300,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(400,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(500,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(600,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(700,600)),
    Actor('chess/rook-white',anchor=(0,0), pos=(0,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(100,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(200,700)),
    Actor('chess/queen-white',anchor=(0,0), pos=(300,700)),
    Actor('chess/king-white',anchor=(0,0), pos=(400,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(500,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(600,700)),
    Actor('chess/rook-white',anchor=(0,0), pos=(700,700)),
]
x = 0
y = 0

block = 0
for i in range(1,65):
    if block % 2 == 0:
        board.append(Actor('chess/white',anchor=(0,0), pos=(x,y)))
    else:
        board.append(Actor('chess/black',anchor=(0,0), pos=(x,y)))

    block += 1
    x += 100
    if i != 0 and i%8 == 0:
        y += 100
        x = 0
        block+=3

pick_white = None
pick_black = None
elf = Actor("c1",ancor=(0,0))
king = Actor("c2")

def on_key_down(key):
    global pick_white,pick_black

    if key == keys.R and pick_white == None:
        # pick up the piece below
        for w in white:
            if elf.colliderect(w):
                pick_white = w 
    elif key == keys.R and pick_white != None:
        for b in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(b):
                for w in white:
                    if w != pick_white and b.colliderect(w):
                        return

                # snap the white piece to the board
                pick_white.x = b.x
                pick_white.y = b.y

                # take the black piece if there
                for bl in list(black):
                    if bl.colliderect(pick_white):
                        black.remove(bl)
                # drop it
                pick_white = None
                break
    if key == keys.P and pick_black == None:
        # pick up the piece below
        for b in black:
            if king.colliderect(b):
                pick_black = b 
    elif key == keys.P and pick_black != None:
        for b in board:
            if king.colliderect(b):
                # dont allow a drop if there is already a black piece there
                for l in black:
                    if l != pick_black and b.colliderect(l):
                        return

                # snap the black piece to the board
                pick_black.x = b.x
                pick_black.y = b.y

                # take the white piece if there
                for w in list(white):
                    if w.colliderect(pick_black):
                        white.remove(w)
                # drop it
                pick_black = None
                break

def update():
    global pick_white,pick_black
    speed = 2
   
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5  
    if keyboard.A:
        elf.x -= 5  
    if keyboard.D:
        elf.x += 5      
    if keyboard.UP:
        king.y -= 5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.LEFT:
        king.x -= 5
    if keyboard.RIGHT:
        king.x += 5
    
    # move the white piece with the elf
    if pick_white != None:
        pick_white.x = elf.x - 30
        pick_white.y = elf.y - 30
    # move the black piece with the king
    if pick_black != None:
        pick_black.x = king.x - 30
        pick_black.y = king.y - 30



def draw():
    screen.fill('deepskyblue')

    for b in board:
        b.draw()
    for b in black:
        b.draw()
    for w in white:
        w.draw()

    elf.draw()
    king.draw()

pgzrun.go()
```



## [DAY-172] if

Add Queening the Pawn functionality, which means when a white/black pawn reaches the of the board it turns into a queen. Think a bit what that means, for a white pawn it reaches the end of the board when its .y property is 0, and for a black pawn when its 700. The only thing left to do is to actually check if we are holding a pawn.


```
# ...
# shouldnt be able to drop if there is already white piece there
if elf.colliderect(b):
    for w in white:
        if w != pick_white and b.colliderect(w):
            return

    # snap the white piece to the board
    pick_white.x = b.x
    pick_white.y = b.y

    # take the black piece if there
    for bl in list(black):
        if bl.colliderect(pick_white):
            black.remove(bl)

    # Queening the Pawn:
    # pick_white.image is chess/pawn-white for the white pawn
    # set the pick_white.image to chess/queen-white if it reaches the black end of the board
    if pick_white.image == 'chess/pawn-white' and pick_white.y == 0:
        pick_white.image = 'chess/queen-white'
    
    # drop it
    pick_white = None
    break
# ...    
```

and respective for the black pawn:

```
# ...

    if pick_black.image == 'chess/pawn-black' and pick_black.y == 700:
        pick_black.image = 'chess/queen-black'
    
    # drop it
    pick_black = None    

# ...        
```

## [DAY-173] if; variables

Today we will make another rule, the pawns can not go backwards. Also we will cleanup the code a bit, and rename few variable so it is more readable, previously we had `for b in board` and then we were using `b.x` and etc, which was kind of confusing. We will rename it for `for square in board` and you will see how much more readable the code is.


First if we want to check if something is going backwards we have to compare its current position with the previous position. In our case this is quite simple, we will make two variables `x` and `y` and once we select which piece we will be moving we will store the piece's .x and .y properties into our `x` and `y` variables.

After we have the original position it is just a matter of checking at the time of placing the piece if it is a pawn and if the original y position is bigger or smaller than the new position, depending which way is forward, for the black pawns up is downwards (y is growing),  for white its upwards (y is decreasing).


This is the whole program again, because of the rename of some variables, it is easier to re-read it.

```
import pgzrun
HEIGHT = 800
WIDTH = 800

board = []

black = [
    Actor('chess/rook-black',anchor=(0,0), pos=(0,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(100,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(200,0)),
    Actor('chess/queen-black',anchor=(0,0), pos=(300,0)),
    Actor('chess/king-black',anchor=(0,0), pos=(400,0)),
    Actor('chess/bishop-black',anchor=(0,0), pos=(500,0)),
    Actor('chess/knight-black',anchor=(0,0), pos=(600,0)),
    Actor('chess/rook-black',anchor=(0,0), pos=(700,0)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(0,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(100,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(200,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(300,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(400,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(500,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(600,100)),
    Actor('chess/pawn-black',anchor=(0,0), pos=(700,100)),
]

white = [
    Actor('chess/pawn-white',anchor=(0,0), pos=(0,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(100,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(200,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(300,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(400,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(500,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(600,600)),
    Actor('chess/pawn-white',anchor=(0,0), pos=(700,600)),
    Actor('chess/rook-white',anchor=(0,0), pos=(0,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(100,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(200,700)),
    Actor('chess/queen-white',anchor=(0,0), pos=(300,700)),
    Actor('chess/king-white',anchor=(0,0), pos=(400,700)),
    Actor('chess/bishop-white',anchor=(0,0), pos=(500,700)),
    Actor('chess/knight-white',anchor=(0,0), pos=(600,700)),
    Actor('chess/rook-white',anchor=(0,0), pos=(700,700)),
]

x = 0
y = 0

block = 0
for i in range(1,65):
    if block % 2 == 0:
        board.append(Actor('chess/white',anchor=(0,0), pos=(x,y)))
    else:
        board.append(Actor('chess/black',anchor=(0,0), pos=(x,y)))

    block += 1
    x += 100
    if i != 0 and i%8 == 0:
        y += 100
        x = 0
        block+=3

pick_white = None
pick_black = None
elf = Actor("c1",ancor=(0,0))
king = Actor("c2")
x = 0
y = 0

def on_key_down(key):
    global pick_white,pick_black,x,y

    if key == keys.SPACE and pick_white == None:
        # pick up the piece below
        for w in white:
            if elf.colliderect(w):
                pick_white = w

                # store the original position
                x = w.x
                y = w.y
                
    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                for w in white:
                    if w != pick_white and square.colliderect(w):
                      return

                # pawns cant move backwards
                if pick_white.image == 'chess/pawn-white' and square.y > y:
                    return
                
                # snap the white piece to the board
                pick_white.x = square.x
                pick_white.y = square.y

                # take the black piece if there
                for b in list(black):
                    if b.colliderect(pick_white):
                        black.remove(b)

                # Queening the Pawn:
                # pick_white.image is chess/pawn-white for the white pawn
                # set the pick_white.image to chess/queen-white if it reaches the black end of the board
                if pick_white.image == 'chess/pawn-white' and pick_white.y == 0:
                    pick_white.image = 'chess/queen-white'
                
                # drop it
                pick_white = None
                break
    if key == keys.P and pick_black == None:
        # pick up the piece below
        for b in black:
            if king.colliderect(b):
                pick_black = b 

                # store the original position                
                y = b.y
                x = b.x
    elif key == keys.P and pick_black != None:
        for square in board:
            if king.colliderect(square):
                # dont allow a drop if there is already a black piece there
                for b in black:
                    if b != pick_black and square.colliderect(b):
                        return

                # pawns cant move backwards
                if pick_black.image == 'chess/pawn-black' and square.y < y:
                    return

                # snap the black piece to the board
                pick_black.x = square.x
                pick_black.y = square.y

                # take the white piece if there
                for w in list(white):
                    if w.colliderect(pick_black):
                        white.remove(w)
    
                # Queen the Pawn
                if pick_black.image == 'chess/pawn-black' and pick_black.y == 700:
                    pick_black.image = 'chess/queen-black'

                # drop it
                pick_black = None
                break

def update():
    global pick_white,pick_black
   
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5  
    if keyboard.A:
        elf.x -= 5  
    if keyboard.D:
        elf.x += 5      
    if keyboard.UP:
        king.y -= 5
    if keyboard.DOWN:
        king.y += 5
    if keyboard.LEFT:
        king.x -= 5
    if keyboard.RIGHT:
        king.x += 5
    
    # move the white piece with the elf
    if pick_white != None:
        pick_white.x = elf.x - 30
        pick_white.y = elf.y - 30

    # move the black piece with the king
    if pick_black != None:
        pick_black.x = king.x - 30
        pick_black.y = king.y - 30



def draw():
    screen.fill('deepskyblue')

    for square in board:
        square.draw()
    for b in black:
        b.draw()
    for w in white:
        w.draw()

    elf.draw()
    king.draw()

pgzrun.go()

```

## [DAY-174] if; list

The knight moves in shape L, so we have to make all other moves illegal.

First draw on a sheet of paper all possible moves, and 

![game-174.png](./screenshots/game-174.png "game 174 screenshot")

There are many ways you can implement this but we will focus on two, one with just if conditions, and one with a list of possible moves.

With if conditions, what we do is we set the move as bad (`good = False`), and then we check if it is actually one of the good moves we do `good = True`, in the end if its not a good move we return from the `on_key_press` function and the piece is not dropped on the square.

```
    elif key == keys.P and pick_black != None:
        for square in board:
            if king.colliderect(square):
                ...

                # knight can only move L shape
                if pick_black.image == 'chess/knight-black':
                    good = False
                    if square.x == x + 100 and square.y == y - 200:
                        good = True
                    elif square.x == x + 100 and square.y == y + 200:
                        good = True
                    elif square.x == x - 200 and square.y == y - 100:
                        good = True      
                    elif square.x == x - 200 and square.y == y + 100:
                        good = True                   
                    elif square.x == x - 100 and square.y == y + 200:
                        good = True
                    elif square.x == x + 200 and square.y == y + 100:
                        good = True
                    elif square.x == x + 200 and square.y == y - 100:
                        good = True
                    elif square.x == x - 100 and square.y == y - 200:
                        good = True
                    elif square.x == x and square.y == y:
                        good = True

                    if not good:
                        return
...                        
```

For the white pieces we will try the other approach, which checks if a the move is in a list of allowed moves. You can check if a list is in a list, e.g. `a = [[1,2],[3,4]]` you can just try `if [1,2] in a`, so we can simply build a list of possible moves, and check if the square we are dropping the piece on is one of those moves.

```
...
    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                ...

                # knight can only move L shape
                knight_possible = [
                    [x,y],
                    [x+100,y-200],
                    [x+100,y+200],
                    [x-200,y-100],
                    [x-200,y+100],
                    [x-100,y+200],
                    [x+200,y+100],
                    [x+200,y-100],
                    [x-100,y-200]
                ]
                if pick_white.image == 'chess/knight-white' and [square.x,square.y] not in knight_possible:
                    return
...
```


## [DAY-175] if

The pawn can only move 2 squares from starting position and 1 square otherwise, try to implement this rule by yourself.

> this is the code she wrote (including the comment)

```
...
                #if pawn.y ==  600:
                #pawn can only move 200:
                #else
                #pwan can move only 100
                if pick_white.image == 'chess/pawn-white':
                    if y == 600:
                        if y - square.y > 200:
                            return
                    if y != 600:
                        if y - square.y >100:
                            return

...

                if pick_black.image == 'chess/pawn-black':
                    if y == 100:
                        if square.y - y > 200:
                            return
                    if y != 100:
                        if square.y - y >100:
                            return
```

## [DAY-176] if

First rename x and y to pick_x and pick_y so things are clearer when you compare square.x with pick_x. Then come up with a way to limit the king's movements to only one square.

> this is the code she wrote

```
...
                if pick_black.image == 'chess/king-black':
                    if square.y - pick_y > 100 or square.y - pick_y < -100:
                        return
                    if square.x - pick_x > 100 or square.x - pick_x < -100:
                        return
...                        
```

## [DAY-177] if

The rook can move only vertically or horizontaly, meaning that either its x or y does not change. Try to code the rule by yourself. If you get stuck, try to do only vertical (x does not change) or horizontal (y does not change), and then think how to add the other direction.

Remember, always try the simple thing first.

> this is the code she wrote

```
...
                if pick_black.image == 'chess/rook-black':
                    if square.x != pick_x and square.y != pick_y:
                        return
...                        
```
## [DAY-178] if; absolute

Today we will do the rule for the bishop, since the bishop moves in diagonal. You see in the image that the diagonal means that both x and y change with the same absolute amount, lets say we want to move only one square, the possible values are: -1 -1, -1 1, 1 1, 1 -1, meaning move up and left (decrease y and decrease x), up and right (decrease y, increase x), down and right (increase y, indcrease x), down and left (increase y, decrease x). 

![game-178.png](./screenshots/game-178.png "game 178 screenshot")

Note that if you actually only care if the amount of steps away from the origin, the dirction does not matter. In math when we care about the absolute value of a number we just care about the amount of steps it would take to get from that number to zero, for example from -5 to zero it will take 5 steps, from 5 to zero it will also take 5 steps.

```
<--------------------|-------------------->
 -5  -4  -3  -2  -1  0   1   2   3   4   5
```

Imagine you walking from -5 to zero, or from 5 to zero both will take you 5 steps. So lets write a function that takes a number and if the number is negative we will just turn it into its positive value, as we only care about the amount of steps.


```
def abs(x):
    if x < 0:
        return x * -1
    return x
```

Now lets make the bishop rule. If the steps change in x is the same as the change in y then we must be moving in a diagonal, if not we refuse the move.


```
...

                if pick_white.image == 'chess/bishop-white':
                    # how much did the y change
                    d_y = pick_y - square.y

                    # how much did the x change
                    d_x = pick_x - square.x

                    # if they didnt change the same amount, then its illegal move
                    if abs(d_y) != abs(d_x):
                        return

...
```



## [DAY-179] if; for

Today we will do two more rules, one is the queen and one for the pawn. The queen can move like the rook and the bishop combined, so horizontally, vertically and diagonally. The pawn can move one step diagonally if she can take an enemy piece.

Lets start with the queen, as we already have the rook and bishop rules, it is quite easy, we just have to say 'if the move is not like the rook and not like the bishop then its illegal'.

```
                if pick_white.image == 'chess/rook-white':
                    if square.x != pick_x and square.y != pick_y:
                        return
                if pick_white.image == 'chess/bishop-white':
                    d_y = pick_y - square.y
                    d_x = pick_x - square.x
                    if abs(d_y) != abs(d_x):
                        return
                if pick_white.image == 'chess/queen-white':
                    d_y = pick_y - square.y
                    d_x = pick_x - square.x
                    if abs(d_y) != abs(d_x) and square.x != pick_x and square.y != pick_y:
                        return
...                        

```


The pawn is a bit more complicated, we need to check if the move is actually one step diagonally, and we also need to have a way to check if a piece is on specific position. We will make `is_on_square` function, that takes a position and a list and checks if any of the items of that list is on that position.

```
def is_on_square(x, y, pieces):
    for p in pieces:
        if p.x == x and p.y == y:
            return True

    return False

```


Now that we have the `is_on_square` function, we can simply check if the `y` of the square is exactly on top of the original position, and the `x` of the square is either one to the left or one to the right, which would mean either 1 square left diagonal or right diagonal, and then check if there is a black piece there, if it is allow the move.

![game-179.png](./screenshots/game-179.png "game 179 screenshot")


```
...
                if pick_white.image == 'chess/pawn-white':
                    # 1 or 2 squares
                    if pick_y == 600:
                        if pick_y - square.y > 200:
                            return
                    if pick_y != 600:
                        if pick_y - square.y > 100:
                            return

                    # pawn can only go left or right if theres someone
                    if pick_x != square.x:
                        ok = False
                        if pick_y - square.y == 100 and pick_x - square.x == 100 and is_on_square(square.x, square.y, black):
                            ok = True
                        if pick_y - square.y == 100 and pick_x - square.x == -100 and is_on_square(square.x, square.y, black):
                            ok = True

                        if not ok:
                            return
...
```

## [DAY-180] if

There is an important rule in chess, that many people dont know, En Passant (In Passing).

From Wikipedia (https://en.wikipedia.org/wiki/En_passant):

> En passant (French: [ɑ̃ paˈsɑ̃], lit. in passing) is a move in chess. It is a special pawn capture that can only occur immediately after a pawn makes a move of two squares from its starting square and provided that it could have been captured by an enemy pawn had it advanced only one square. The opponent captures the just-moved pawn "in passing" through the first square. The result is the same as if the pawn had advanced only one square and the enemy pawn had captured it normally.

> The en passant capture must be made on the very next turn or the right to do so is lost. En passant capture is a common theme in chess compositions.

> The en passant capture rule was added in the 15th century when the rule that gave pawns an initial double-step move was introduced. It prevents a pawn from using the two-square advance to pass an adjacent enemy pawn without the risk of being captured.


![game-180-a.png](./screenshots/game-180-a.png "game 180-a screenshot")
![game-180-b.png](./screenshots/game-180-b.png "game 180-b screenshot")
![game-180-c.png](./screenshots/game-180-c.png "game 180-b screenshot")

So its pretty nice rule, what we have to do is to remember each pawn that moves two squares and consider it possible en_passant, and then if the oponnent's pawn wants to move diagonally we will check if there is en_passant above(black)/below(white) and if there is we will capture it. If any move is made we will clear the en-passant

the code looks like this:

```
enpassant = None


def on_key_down(key):
    global pick_white, pick_black, pick_x, pick_y, enpassant

    ...
    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                ...
                if pick_white.image == 'chess/pawn-white':
                    # 1 or 2 squares
                    if pick_y == 600:
                        if pick_y - square.y == 200:
                            enpassant = pick_white

                        if pick_y - square.y > 200:
                            return
                    if pick_y != 600:
                        if pick_y - square.y > 100:
                            return
                    # if y > 200 first move:

                    # pawn can only go left or right if theres someone
                    if pick_x != square.x:
                        ok = False
                        if pick_y - square.y == 100 and pick_x - square.x == 100 and is_on_square(square.x, square.y, black):
                            ok = True
                        if pick_y - square.y == 100 and pick_x - square.x == -100 and is_on_square(square.x, square.y, black):
                            ok = True

                        if (pick_y - square.y == 100 and pick_x - square.x == 100) or (pick_y - square.y == 100 and pick_x - square.x == -100):
                            if enpassant != None and enpassant.image == 'chess/pawn-black':
                                if enpassant.x == square.x and enpassant.y == square.y + 100:
                                    black.remove(enpassant)
                                    ok = True

                        if not ok:
                            return

                    # pawns cant move backwards
                    if square.y > pick_y:
                        return
                    # Queening the Pawn:
                    # pick_white.image is chess/pawn-white for the white pawn
                    # set the pick_white.image to chess/queen-white if it reaches the black end of the board
                    if square.y == 0:
                        pick_white.image = 'chess/queen-white'
                ...
                # snap the white piece to the board
                pick_white.x = square.x
                pick_white.y = square.y
                if enpassant != pick_white:
                    enpassant = None
...
```

Notice how we set enpassant = pick_white if the pawn moves 2 squares (this will be used if the black pawn tries to capture), and later when we see that the pawn is moving diagonally we do:

```
if (pick_y - square.y == 100 and pick_x - square.x == 100) or (pick_y - square.y == 100 and pick_x - square.x == -100):
    if enpassant != None and enpassant.image == 'chess/pawn-black':
        if enpassant.x == square.x and enpassant.y == square.y + 100:
            black.remove(enpassant)
            ok = True
```

This basically checks if it is one square diagonal to the left or one square diagonal to the right, and if it is it checks if there is active enpassant and it is a black pawn, then it checks if it sits directly above the square we want to go to, and if it is we capture it and mark the move valid.


## [DAY-181] if

Add undo support. We need to store the piece's position when its picked up, the piece itself and its image (in case of Queening The Pawn) and we need to store those for every move, then if the key 'b' is pressed we need to take the last move and revert it, and so on.

A good strategy for that is to simply use a list, and each time we pick a piece we will append the position_x, position_y, image, actor and then when 'b' is pressed we will pop them out and set them to the actor in question.

```
...
back = []

def on_key_down(key):
    global pick_white, pick_black, pick_x, pick_y, pick_image, enpassant,back

    if key == keys.SPACE and pick_white == None:
        # pick up the piece below
        for w in white:
            if elf.colliderect(w):
                pick_white = w

                # store the original position
                pick_x = w.x
                pick_y = w.y
                pick_image = w.image

    elif key == keys.SPACE and pick_white != None:
        for square in board:
            # shouldnt be able to drop if there is already white piece there
            if elf.colliderect(square):
                # make sure the move is valid
                ...
                back.append(pick_image)
                back.append(pick_y)
                back.append(pick_x)
                back.append(pick_white)

                pick_white.x = square.x
                pick_white.y = square.y

                ...

    if key == keys.B:
        if len(back) != 0:
            actor = back.pop()
            x = back.pop()
            y = back.pop()
            image = back.pop()
            actor.x = x
            actor.y = y
            actor.image = image
...            
```

We are using the list like a stack, we add stuff to it and when we need we pop the top most items. You can see that we append image, y, x, actor but when we pop we get them in reverse order, because pop() removes the top most item from the ist, so we get back actor, x, y, image.


There is a fundamental limitation to this aproach, which is that we lose pieces that were taken, so if you undo they will just be gone.

## [DAY-182] look back

Today we will look back on some of the first programs you wrote.

Open our old files and read as many of them as you can.

## [DAY-183] Generalization

From today we will start to think before we code. You can see the game of chess we made, it kind of works but it is quite hard to add things to it, and to add new rules and etc. It is already around 500 lines of hard to read if statements.

We will do one week of exercises without writing code, just with pen and paper, where we will generalize, or try to extract the common attributes of things. We will think about how to think about things.

Lets start with an example. You know that `1 + 2` is the same as `2 + 1`, or `1 + 2 = 2 + 1`, same with `3 + 5 = 5 + 3`, this is quite intuitive, if you have two apples in one hand and one in the other, you have 3 apples irrelevant of which hand has 2 apples and which has 1. We can generalize that rule to `a + b = b + a`, meaning that any number `a` plus any number `b` is the same as wiriting `b+a`. It might seem like we did nothing here, just stated the obvious, but I will show you how powerful this generalization is.

At first we were thinkging of numbers, but with this generalization we can actually use expressions, for example `a = ((4838 + 8272) * 3)` and `b = ((7467 / 2) + 27838)` and still `a + b = b + a`, we can substitute `a` and `b`, so `((4838 + 8272) * 3) + ((7467 / 2) + 27838) = ((7467 / 2) + 27838) + ((4838 + 8272) * 3)`. We have higher level of reason, we are not confined to numbers anymore, but to whole expressions and expressions of expressions.

Lets talk now about what is needed to represent a chess piece. First we need its color, is it black or white, we need its kind (rook, bishop etc..), and its position x and y. Those are the properties of a piece. Each piece however can move in a different way, this is its behavior. Those are the two main things we have to think about, we can generalize thenm into 'what does the thing do' and 'how does the thing look'.

This week we will spend more time on examples about generalization and abstraction, and after that we will rewrite the chess game. It is very common to write something quick, and then rewrite it when you know how to actually think about it. The first time you code something is almost never good, purely because you still dont know how to represent the things in your program yet, even if you think a lot about it. In the real world you need to combine the both aproaches, of code and explore, and think carefully about how the pieces in your program talk to each other.

## [DAY-184] Generalization

> We (me and my daughter) have spent 30 minutes per day for the last week just talking about how to think about behavior and state. With all kinds of discussions, from tic tac toe, to stratego, to classess and lists and many more concepts. The talks were very open and unstructured, so it is hard to put them directly 1:1 in the book. I recommend you do the same. Spend time talking about how to think about your program, how the parts in it communicate, how you group the state, and how do you abstract behaviour. It is also important to think about how to think about problems in general, move one layer above practicality. Discuss patterns.




## [DAY-185] Generalization

Today we will build three different versions of snakes and ladders to illustrate different approaches.

We will use super small Snakes and Ladders game with the following rules:

* there are 9 squares, from 0 to 8
* 0 -> 0
* 1 -> 2
* 2 -> 2
* 3 -> 3
* 4 -> 2
* 5 -> 7
* 6 -> 0
* 7 -> 7
* 8 -> 8

1. While and If, most basic implementation. In this implementation if we do 99 squares or we want to render a board, or we want to make the game more interesting to roll the dice twice or something like that, everything will just explode in complexity.

```
player1 = 0
while True:
    print("player board position: ", player1)
    dice = int(input("dice roll> "))

    player1 += dice
    if player1 == 1:
        player1 = 3
    elif player1 == 4:
        player1 = 2
    elif player1 == 5:
        player1 = 7
    elif player1 == 6:
        player1 = 0

```

2. Think about the rules of the game and what is a bit more abstract way to think about the them. The only rule actually is: if you land on the square you move wherever the square says, could be 0 (stay there), +steps or -steps. This is an example implementation where we just keep the state of each square in a list, square index 1 moves you to index 3 and so on.

```
board = [
    0,
    2,   # 1 -> 3
    0,
    0,
    -2,  # 4 -> 2
    2,   # 5 -> 7
    -6,  # 6 -> 0
    0,
    0
]

player1 = 8
while True:
    print("player board index: ", player1)
    dice = int(input("dice roll> "))
    player1 += dice

    if player1 >= len(board) - 1:
        print("finished")
        break

    snake_or_ladder = board[player1]
    player1 += snake_or_ladder
```

The whole game is actually encoded in those two lines:

```
    snake_or_ladder = board[player1]
    player1 += snake_or_ladder
```

See how different this is? The size of the code is very similar in lines, but this version is so much easier to change and to extend. For example if we want to display the board, now we can just pass the board list to some `render` function and be done. This is actually not possible in the first version with the if conditions unless we almost duplicate the whole program.


3. There is one more thing we could do to simplify it a bit, and that is to split the board from the input. So that we could move it maybe in a separate file (board.py) if we want. Separating the user input from the board action is quite nice because now it will be super easy to add mouse click functionality, and board rendering.


```
class Board:
    def __init__(self):
        self.player = 0
        self.squares = [
            0,
            2,   # 1 -> 3
            0,
            0,
            -2,  # 4 -> 2
            2,   # 5 -> 7
            -6,  # 6 -> 0
            0,
            0
        ]

    def move(self, dice):
        position = self.player + dice
        if position >= len(self.squares) - 1:
            return True

        self.player += self.squares[position]
        return False

#################################################

b = Board()
while True:
    print("player board position: ", b.player)
    roll = int(input("dice roll> "))
    if b.move(roll):
        print('finished')
        break
```

## [DAY-186] If

Make snakes and ladders on your own with pygame zero.

![game-186-b.png](./screenshots/game-186-b.png "game 186-b screenshot")

> This is what she wrote. She just went and found 500x500 board so that its easy to compute the position of each square, and hardcoded the jumps.

```
import pgzrun
import random

HEIGHT = 500
WIDTH = 500

elf = Actor("c1")
elf.x = -25
elf.y = 475
game_over = False
board = Actor("snake-500")
def on_key_down(key):
    if key == keys.SPACE:
        elf.x += random.choice([50,100,150,200,250,300]) 
        if elf.x > 475 and elf.y == 25:
            elf.x = 25 
            elf.y = 25
        if elf.x > 475:
            elf.x -= 500 
            elf.y -= 50
        if elf.y == 375 and elf.x == 225:
            elf.y = 475 
            elf.x = 225
        if elf.y == 25 and elf.x == 25:
            elf.y = 175 
        if elf.y == 475 and elf.x == 125:
            elf.y = 225 
            elf.x = 25
        if elf.y == 325 and elf.x == 175:
            elf.y = 475 
            elf.x = 25
        if elf.y == 475 and elf.x == 275:
            elf.y = 375 
            elf.x = 325
        if elf.y == 175 and elf.x == 125:
            elf.y = 25 
            elf.x = 225
        if elf.y == 75 and elf.x == 325:
            elf.y = 225 
            elf.x = 325
        if elf.y == 25 and elf.x == 425:
            elf.y = 175 
            elf.x = 425
        if elf.y == 475 and elf.x == 425:
            elf.y = 175 
            elf.x = 425

def update():
    global game_over
    speed = 10

    if keyboard.UP:
        elf.y -= speed
    if keyboard.DOWN:
        elf.y += speed
    if keyboard.LEFT:  
        elf.x -= speed
    if keyboard.RIGHT:
        elf.x += speed
    
    if elf.x == 475 and elf.y == 25:
        game_over = True

def draw():
    board.draw()
    elf.draw()
    if game_over == True:
        screen.draw.text('YOU WIN CONGRATULATION',(100,100),color = (0,0,0))
pgzrun.go()
```
> she also made a grid to compute the positions of each square

![game-186-a.png](./screenshots/game-186-a.png "game 186-a screenshot")

## [DAY-187] If; While; Functions

Watch Programming for Advanced Beginners: Battleships - EP 1, from Robert Heaton (https://www.youtube.com/watch?v=Gi0Fdyhk1_0), and then watch it again and code with the author

## [DAY-188] OOP

Watch https://www.youtube.com/watch?v=JeznW_7DlB0 (Python Object Oriented Programming (OOP) - For Beginners
 from Tech With Tim)

## [DAY-189] Keyword Arguments; String Methods

Today you have to watch three videos:

* Python keyword arguments 🔑 by Bro Code - https://www.youtube.com/watch?v=Tu0lFBXQgPw
* Python string methods by Bro Code - https://www.youtube.com/watch?v=crw3rVFNwIM
* Python Object Oriented Programming (OOP) - For Beginners from Tech With Tim - https://www.youtube.com/watch?v=JeznW_7DlB0 (watch it again)



## [DAY-190] While

Make a web whatsapp bot that sends the same message in an infinite loop

* click on the chrome tab with whatsapp
* click on the search box
* searche for contact name (dad)
* clicks on the top result
* click on the message input field
* type 'hello world'
* click the send button

Using https://pyautogui.readthedocs.io/en/latest/ as a guide. There are many ways to read documentation, try to spend some time just brawsing through it. Another way is to go to the example section and see if you can find examples that can help you solve your problem.

This is a snippet with examples taken from pyautogui's page:

```
>>> import pyautogui

>>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
>>> screenWidth, screenHeight
(2560, 1440)

>>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
>>> currentMouseX, currentMouseY
(1314, 345)

>>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

>>> pyautogui.click()          # Click the mouse.
>>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
>>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

>>> pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
>>> pyautogui.doubleClick()     # Double click the mouse.
>>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

>>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
>>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

>>> with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
>>> # Shift key is released automatically.

>>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

>>> pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
```

> use `pyautogui.position()` to find the accurate positions for your screen.
```
import pyautogui
import time
while True:
    pyautogui.click(305,10)
    pyautogui.click(117,252)
    pyautogui.write('dad', interval=0.25)
    pyautogui.click(185, 395)
    pyautogui.write('hello world!', interval=0.20)
    pyautogui.click(935, 1132)
    time.sleep(1)
```

Have some fun with it pranking your parents :) _but not too much_.


## [DAY-191] While

Make another whatsapp bot, but this time send a very very long message.

```
import pyautogui
import time
import random
while True:
    pyautogui.click(305,10)
    pyautogui.click(117,252)
    pyautogui.write('dad', interval=0.25)
    time.sleep(1)
    pyautogui.click(185, 395)
    time.sleep(1)
    
    for i in range(3000):
        s = 'yo' * random.randint(1, 4)
        pyautogui.write(s + ' ')

    time.sleep(5)
    pyautogui.click(935, 1132)
```

this will send the message:

"yoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yo yo yoyo yoyo yo yoyo yoyo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yo yo yoyo yo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyo yoyo yoyo yo yo yoyo yoyoyoyo yo yoyo yo yoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yo yoyoyoyo yo yoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyo yo yo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyo yoyo yoyo yo yo yoyo yoyo yo yoyo yoyo yoyoyo yoyo yo yo yoyoyoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyo yo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yo yo yoyoyo yo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyo yo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yo yo yoyoyo yoyoyo yoyoyoyo yo yo yo yoyoyo yoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yo yo yoyo yoyoyoyo yo yo yoyoyo yo yoyoyo yoyoyoyo yo yoyo yoyoyo yoyo yoyoyo yo yo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yoyoyoyo yo yoyo yoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyoyo yo yoyo yo yoyo yoyoyoyo yo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yo yo yo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyoyo yo yo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyo yo yoyo yoyoyo yoyo yoyoyo yoyo yo yoyo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yo yoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyo yo yoyo yo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyo yoyoyo yoyo yoyo yoyo yoyo yo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yo yo yoyo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyo yo yoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yo yoyo yoyo yoyoyo yoyoyo yo yo yoyoyoyo yoyo yo yo yoyoyo yo yo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yo yo yo yoyoyo yo yoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yoyoyo yoyoyoyo yoyo yo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyo yo yoyoyo yoyoyo yo yoyoyoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yo yoyo yoyo yoyo yoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyo yoyoyoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yo yoyo yoyoyo yo yoyo yo yo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyo yoyo yo yoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyoyo yo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyo yoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yo yo yoyo yo yoyo yo yoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyo yoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yoyoyo yo yoyo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yo yoyoyo yo yoyo yoyoyo yoyo yoyo yo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyo yo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yo yoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yo yo yoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyo yo yo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyo yoyo yo yoyoyoyo yoyo yoyo yoyo yoyo yo yoyo yo yoyoyo yoyoyo yoyo yo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yo yo yo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyo yo yoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyo yoyoyo yo yoyoyo yo yoyo yoyoyoyo yoyoyo yo yoyoyo yo yoyoyoyo yo yoyo yoyoyo yoyo yoyoyo yo yo yo yo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yo yo yoyo yoyoyoyo yoyoyo yo yoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yo yoyo yoyoyo yoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyo yo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyo yo yoyoyoyo yoyoyo yoyoyo yo yo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yo yo yoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyoyoyo yo yo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyoyo yoyo yo yoyo yoyo yoyo yoyoyoyo yo yoyo yo yo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yoyoyo yo yo yo yoyo yo yoyoyoyo yoyo yoyo yoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyo yoyo yoyoyo yo yo yoyo yoyo yo yoyo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yo yo yoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyo yoyoyo yo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyo yoyo yoyoyoyo yo yoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyo yo yoyo yo yoyoyo yo yoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyo yo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yo yo yo yo yoyoyoyo yoyoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yo yo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyo yoyo yoyo yo yoyo yoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyo yo yo yoyoyo yo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yo yoyoyo yoyo yoyoyo yo yoyoyoyo yo yo yo yoyoyo yo yo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyo yo yo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yo yo yo yo yo yoyo yo yo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yo yo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yo yo yoyoyoyo yoyoyoyo yo yo yoyo yo yoyo yoyoyo yoyoyo yoyo yoyoyo yo yoyoyo yoyoyo yoyoyoyo yo yo yoyo yoyoyoyo yo yoyoyoyo yoyo yoyo yo yoyoyoyo yo yo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yoyo yo yo yoyoyoyo yoyoyo yoyo yoyo yo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yo yoyoyo yoyoyo yo yoyoyo yo yoyoyo yo yo yoyoyoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyo yo yo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yoyoyo yo yoyo yoyo yoyoyoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yo yoyo yoyoyoyo yoyoyo yo yoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yo yoyo yoyoyoyo yo yoyoyoyo yo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyo yoyoyo yo yoyo yoyoyoyo yo yoyo yoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyo yo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyoyo yo yoyo yoyoyo yo yoyo yoyoyo yo yo yoyoyoyo yo yoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yoyoyo yo yoyoyo yo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyo yoyo yo yo yoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyo yo yoyoyo yoyo yoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yo yo yoyoyo yoyoyo yo yoyo yoyo yoyoyoyo yo yoyo yoyo yoyoyo yoyoyoyo yo yo yoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyo yoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yo yoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yo yo yoyoyo yo yoyoyoyo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yo yoyo yoyo yo yoyo yo yoyoyoyo yoyo yo yoyoyo yoyoyoyo ypoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yo yoyo yoyoyo yoyoyo yoyo yoyo yo yoyoyo yoyoyoyo yo yoyo yo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyoyo yoyo yoyoyo yoyo yoyo yo yoyoyoyo yoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yo yoyo yoyoyoyo yo yo yoyoyo yoyo yoyo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yoyo yo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yo yoyo yoyoyo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyo yo yoyoyo yo yoyoyo yoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyoyo yo yoyo yo yoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yo yo yo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yo yoyo yoyoyo yo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyo yo yoyo yoyoyoyo yo yo yoyoyo yoyoyo yoyoyo yo yo yo yoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyo yo yoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyoyo yo yoyoyoyo yo yo yoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyo yo yoyoyo yoyoyo yoyo yoyo yo yo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yo yoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yo yoyoyo yoyo yo yoyoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yoyo yoyo yo yoyoyoyo yo yoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yoyo yoyoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyoyoyo yo yoyoyo yoyoyo yo yoyo yoyo yoyoyo yo yoyo yoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyoyoyo yo yoyo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yo yoyo yoyo yoyoyoyo yoyoyo yoyo yo yoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyo yoyoyoyo yo yo yoyoyoyo yo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyo yoyoyo yoyoyoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyo yo yoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyoyo yo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yo yoyo yoyoyoyo yo yoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyo yoyoyo yo yoyoyo yoyoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyo yoyoyo yo yoyoyoyo yoyoyo yo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yoyoyoyo yo yoyo yoyoyoyo yoyo yoyoyo yoyoyo yo yo yoyoyoyo yo yoyoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyo yoyo yoyo yoyoyo yoyoyo yoyo yoyo yoyoyoyo yo yoyo yo yoyo yo yo yo yoyo yo yoyoyoyo yo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yo yoyoyoyo yo yoyoyoyo yoyoyoyo yo yo yoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yoyoyoyo yoyo yo yo yoyo yoyoyoyo yoyoyoyo yo yo yoyoyo yoyoyoyo yo yoyoyoyo yo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yoyo yo yo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyo yoyoyo yoyoyo yoyo yo yo yoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yo yo yoyoyoyo yo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yoyoyoyo yoyoyo yo yoyo yoyo yo yoyo yoyoyoyo yo yoyo yo yoyo yoyoyoyo yoyoyoyo yo yo yoyoyo yo yoyoyo yoyo yoyoyoyo yoyo yoyo yo yoyo yo yoyo yoyoyoyo yo yoyoyo yo yoyoyoyo yo yoyoyoyo yo yo yoyo yoyoyoyo yo yo yo yoyoyo yo yo yoyo yoyo yoyoyo yoyo yo yoyoyo yo yoyo yoyoyoyo yoyo yo yoyoyo yoyoyo yoyo yoyo yoyoyo yo yoyo yo yoyo yoyoyo yoyoyo yoyoyoyo yoyo yo yoyoyoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yo yoyo yo yo yoyoyoyo yoyoyo yoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yo yoyoyo yo yoyoyo yo yoyoyoyo yoyo yo yo yoyoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yo yoyoyoyo yo yo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyoyo yoyoyo yoyo yoyoyo yoyoyo yoyo yo yo yoyo yoyoyoyo yoyoyoyo yoyo yoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyo yo yo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyo yoyo yo yoyoyoyo yo yoyoyoyo yoyoyo yoyo yoyo yoyoyoyo yoyoyoyo yoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyoyo yoyoyo yoyoyoyo yo yoyoyo yoyoyoyo yo yoyo yoyo yoyo yoyoyo yoyoyoyo yoyoyoyo yoyoyo yo yoyoyoyo yoyo yoyoyo yoyo yoyoyo yoyo yo yoyo yoyo yo yo yoyoyoyo yoyo yoyoyoyo yoyoyo yoyoyo yoyo yo yoyoyo yoyoyoyo yo yoyoyo yoyo yoyoyo yoyo yoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyoyo yoyoyoyo yoyoyoyo yoyo yoyoyo yoyo yo yo yo yoyoyoyo yoyo yo yo yoyoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yoyo yo yoyoyoyo yoyoyoyo yoyoyo yoyoyo yo yoyoyoyo yoyo yoyo yoyoyo yoyo yoyoyo yoyoyoyo yoyo yoyo yoyoyoyo yo yo yoyoyo yoyo yoyo yoyo yoyoyoyo yoyo yoyo yoyoyoyo yoyo yoyoyo yoyoyoyo yoyoyo yoyoyo yoyoyoyo yoyo yoyoyoyo yo yo yoyoyoyo yoyo yoyo yoyo yo yoyoyoyo yo yoyo yoyoyoyo yo yoyo yoyoyo yoyoyo yoyoyo"



## [DAY-192] Class; Methods


There are few ways to represent a rectangle, one is with one point plus width and height, e.g. top left point and width and height.


```
(the screen's y grows downwards, top left is 0,0)
    │       x=8                           x
────┼───────┬────────────────────────────────
    │       │
    │       │
 y=3├───────*──────────────────┐
    │       │##################│
    │       │##################│
    │       │##################│ height
    │       │##################│
    │       └──────────────────┘
    │              width
    │
    │
   y│
```

or you can store the position of two diagonal points, top left and bottom right (or top right and bottom left)

```
    │
    │       x=8              x=27         x
────┼───────┬──────────────────┬─────────────
    │       │                  │
    │       │                  │
 y=3├───────*──────────────────┤
    │       │##################│
    │       │##################│
    │       │##################│
    │       │##################│
 y=8├───────┴──────────────────*
    │
    │
   y│

```

In this example I chose the two points appriach as it I can just make a Point class and use it twice, but sometimes the first approach is more suitable. We want to make a Rect class that has a method to expand to include a point.

```
    │
    │       x=8              x=27   x=31    x
────┼───────┬──────────────────┬─────────────
    │       │                  │     .
    │       │                  │     .
 y=3├───────*──────────────────┤     .
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
    │       │##################│+++++.
 y=8├───────┴──────────────────*+++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
    │        ++++++++++++++++++++++++.
y=12│................................*
    │
    │
    │
   y│
```

> Pause here to think about how to approach this, use pen and paper to illustrate the approach.

The solutio is simply to move the topleft's x/y more left/up if they are bigger than the requested point, and move the bottomright's x/y if they are smaller than the requested point. This way the rectangle grows just enough to include the point.

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        if self.topLeft.y > point.y:
            self.topLeft.y = point.y
        if self.bottomRight.x < point.x:
            self.bottomRight.x = point.x
        if self.bottomRight.y < point.y:
            self.bottomRight.y = point.y

r = Rect(Point(10,10),Point(20,20))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(5,5))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,3))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
r.expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

Sometimes its handy to be able to chain method calls, so if the method returns an instance you can just call a method on the returned value.

```
class Rect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight


    def expand(self, point):
        if self.topLeft.x > point.x:
            self.topLeft.x = point.x
        ...
        return self

r = Rect(Point(10,10),Point(20,20))
r.expand(Point(5,5)).expand(Point(50,3)).expand(Point(50,100))
print(r.topLeft.x, r.topLeft.y,r.bottomRight.x, r.bottomRight.y)
```

## [DAY-193] Richard Buckland's computer


Richard Buckland's Higher Computing course is absolutely brilliant, you can watch it on youtube: https://www.youtube.com/watch?v=JA_G8XbVYug&list=PL6B940F08B9773B9F

In the beginning of the course he makes up an virtual 4 bit computer that we can program into useful things.

It has two registers, R0 and R1, 16 4 bit slots in (8 bytes) memory and 16 instructions we could use. Some of the instructions take 1 byte, some take 2 bytes

```
                      │ IP: instruction pointer
┌──────┐ ┌──────┐     │ IS: instruction store (current instruction)
│IP: 0 │ │IS: 0 │     │ R0: register 0
└──────┘ └──────┘     │ R1: register 1
┌──────┐ ┌──────┐     ├──────────────────────────────────────────────
│R0: 0 │ │R1: 0 │     │    0 halt
└──────┘ └──────┘     │    1 add R0 = R0 + R1
  0   1   2   3       │    2 subtract R0 = R0 - R1
┌───┬───┬───┬───┐     │    3 increment R0 R0 = R0 + 1
│ 0 │ 0 │ 0 │ 0 │     │    4 increment R1 R1 = R1 + 1
├───┼───┼───┼───┤     │    5 decrement R0 R0 = R0 - 1
│ 0 │ 0 │ 0 │ 0 │     │    6 decrement R1 R1 = R1 - 1
├───┼───┼───┼───┤     │    7 ring bell
│ 0 │ 0 │ 0 │ 0 │     │  8 X print data X
├───┼───┼───┼───┤     │  9 X load value of address X into R0
│ 0 │ 0 │ 0 │ 0 │     │ 10 X load value of address X into R1
└───┴───┴───┴───┘     │ 11 X store R0 into address X
 12  13  14  15       │ 12 X store R1 into address X
                      │ 13 X jump to address X
                      │ 14 X jump to address X if R0 == 0
                      │ 15 X jump to address X if R0 != 0
```

Example programs (also some are from the video lecture):

* print 7 and beep

```
┌───┬───┬───┬───┐
│ 8 │ 7 │ 7 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```


* beep 3 times

```
┌───┬───┬───┬───┐
│ 7 │ 7 │ 7 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```


* print 3

```
┌───┬───┬───┬───┐
│ 8 │ 3 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```



* what would this program do?

```
┌───┬───┬───┬───┐
│ 7 │ 10│ 3 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘ 
```


* beep and put 3 in R1

```
┌───┬───┬───┬───┐
│ 7 │ 10│ 15│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 3 │
└───┴───┴───┴───┘ 
```

* beep forever

```
┌───┬───┬───┬───┐
│ 7 │ 13│  0│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 3 │
└───┴───┴───┴───┘ 
```

* put the value 4 in R0, increment it and put it back in memory and print it

```
┌──────┐ ┌──────┐ 
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘ 
┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 8 │ 4 │ 0 │
└───┴───┴───┴───┘
```

Lets walk through each step of the program, you can see the IP(instruction pointer) has a pointer to which memory address it is executing now, and IS(instruction store) is the current instruction:

```
START               load addr 14 in R0  increment R0
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │   │IP: 0 │ │IS: 10│   │IP: 2 │ │IS: 3 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘  
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │   │R0: 4 │ │R1: 0 │   │R0: 5 │ │R1: 0 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘

┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 8 │ 4 │ 0 │   │ 0 │ 8 │ 4 │ 0 │   │ 0 │ 8 │ 4 │ 0 │
└───┴───┴───┴───┘   └───┴───┴───┴───┘   └───┴───┴───┴───┘



put R0 in addr 14   jump to addr 13      print 5
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│IP: 3 │ │IS: 11│   │IP: 5 │ │IS: 13│   │IP: 13│ │IS: 8 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘ 
┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐   ┌──────┐ ┌──────┐
│R0: 5 │ │R1: 0 │   │R0: 5 │ │R1: 0 │   │R0: 5 │ │R1: 0 │
└──────┘ └──────┘   └──────┘ └──────┘   └──────┘ └──────┘

┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐   ┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│   │  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │   │ 14│ 13│ 13│ 0 │ 
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │   │ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤   ├───┼───┼───┼───┤   ├───┼───┼───┼───┤
│ 0 │ 8 │ 5 │ 0 │   │ 0 │ 8 │ 5 │ 0 │   │ 0 │ 8 │ 5 │ 0 │
└───┴───┴───┴───┘   └───┴───┴───┴───┘   └───┴───┴───┴───┘


halt
┌──────┐ ┌──────┐ 
│IP: 15│ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 4 │ │R1: 0 │
└──────┘ └──────┘ 
┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 8 │ 5 │ 0 │
└───┴───┴───┴───┘
```

We can make a simpler to read language that we can easilly convert to machine code:
```
code  keyword   what it does
─────┼────────────────────────────────────
   0 │ halt      halt
   1 │ add       add R0 = R0 + R1
   2 │ sub       subtract R0 = R0 - R1
     │
   3 │ inc r0    increment R0 R0 = R0 + 1
   4 │ inc r1    increment R1 R1 = R1 + 1
   5 │ dec r0    decrement R0 R0 = R0 - 1
   6 │ dec r1    decrement R1 R1 = R1 - 1
     │ 
   7 │ ring      ring bell
     │
 8 X │ print     print X (whatever the next byte is)
     │
 9 X │ mov addr, r0  load value of address X into R0
10 X │ mov addr, r1  load value of address X into R1
     │
11 X │ mov r0, addr  store R0 into address X
12 X │ mov r1, addr  store R1 into address X
     │
13 X │ jmp addr   jump to address X
14 X │ je addr    jump to address X if R0 == 0
15 X │ jne addr   jump to address X if R0 != 0
```

now lets rewrite this program

```
┌──────┐ ┌──────┐ 
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘ 
┌───┬───┬───┬───┐
│  9│ 14│ 3 │ 11│
├───┼───┼───┼───┤
│ 14│ 13│ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 8 │ 4 │ 0 │
└───┴───┴───┴───┘
```

The same program looks like this:

```
0  mov 14, r0 # put value of addr 14 in r0
2  inc r0     # r0 += 1
3  mov r0, 14 # put r0's value in addr 14
5  jmp 13     # jump to addr 13
13 print      # print the next byte
15 halt       # halt
```

Which surely looks easier to read than `9 14 3 11 14 13 13 0 0 0 0 0 8 4 0`.

## [DAY-194] Self modifying programs

Make a program that prints the numbers from 12 to 1

![game-194.jpg](./screenshots/game-194.jpg "game 194 screenshot")


The instructions we will use are:

```
9X  - load value at address X to R0 (R0 = mem[x])
14X - jump to address if r0 == 0
11X - put value of R0 into memory address X (mem[x] = R0)
5   - decrement R0 (R0 -= 1)
13X - jump to address X
8X  - print X
```

And this is the program:

```
┌──────┐ ┌──────┐ 
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘  
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12|
└───┴───┴───┴───┘
```

Lets evaluate the program step by step:


```
9 15 - load the value of memory address 15 into R0
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 9 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

jump to address 12 if R0 == 0
┌──────┐ ┌──────┐
│IP: 2 │ │IS: 14│
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

place the value of R0 in address 7 (mem[7] = 12)
┌──────┐ ┌──────┐
│IP: 4 │ │IS: 11│
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

print 12

> this is the most important step of the program
> you see in the previous instruction (11 7), we modified the value 
> of the print instruction which is about to print the content of 
> the next byte, which was zero when our program started,
> but now it is filled with the current value of R0

┌──────┐ ┌──────┐
│IP: 6 │ │IS: 8 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 12│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

decrement R0 (R0 -= 1)
┌──────┐ ┌──────┐
│IP: 8 │ │IS: 5 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 11│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

jump to address 2
┌──────┐ ┌──────┐
│IP: 9 │ │IS: 13│
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 11│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 12│
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

---

> back from scratch, check if R0 is zero, if not it will put its value 
> as the second byte of the print instruction and then decrement it 
> until it reaches zero, at which point it will jump to address 12 and halt, 
> 

┌──────┐ ┌──────┐
│IP: 12│ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 9 │ 15│ 14│ 12│
├───┼───┼───┼───┤
│ 11│ 7 │ 8 │ 1 │
├───┼───┼───┼───┤
│ 5 │ 13│ 2 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 12│
└───┴───┴───┴───┘

```


## [DAY-195] loops


![game-195.jpg](./screenshots/game-195.jpg "game 195 screenshot")

![game-195-b.jpg](./screenshots/game-195-b.jpg "game 194-b screenshot")


* beep forever

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 7 │ 13│ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```

* print 6 forever

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 8 │ 6 │ 13│ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```

* print 0 1 2 3 4 5 6 7 8 ... forever

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 8 │ 0 │ 3 │ 11│
├───┼───┼───┼───┤
│ 1 │ 13│ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```


* if R0 == 0 print 6 else print 7

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 14│ 6 │ 8 │ 7 │
├───┼───┼───┼───┤
│ 13│ 8 │ 8 │ 6 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
├───┼───┼───┼───┤
│ 0 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```


## [DAY-196] loops

![game-196.jpg](./screenshots/game-196.jpg "game 196 screenshot")

* make a program that prints 0 15 1 14 2 13 3 12 4 11 5 10 ... 14 1

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 15│ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 11│ 5 │ 12│ 7 │
├───┼───┼───┼───┤
│ 8 │ 0 │ 8 │ 0 │
├───┼───┼───┼───┤
│ 5 │ 4 │ 14│ 15│
├───┼───┼───┼───┤
│ 13│ 0 │ 0 │ 0 │
└───┴───┴───┴───┘
```

we will start with initial state of R0 and R1 to 15 and 0, then we will put R0's value in memory address 5 and R1 in address 7, where they will become arguments to two print instructions, then we will decrement R0 and increment R1, after that we check if R0 is zero if it is we go to halt at address 15, if not we loop back to the beginning but now with updated values of R0 and R1

* jump to a jump

follow the jumps in this program

```
┌──────┐ ┌──────┐
│IP: 0 │ │IS: 0 │
└──────┘ └──────┘
┌──────┐ ┌──────┐
│R0: 0 │ │R1: 0 │
└──────┘ └──────┘
┌───┬───┬───┬───┐
│ 13│ 2 │ 13│ 12│
├───┼───┼───┼───┤
│ 13│ 14│ 13│ 10│
├───┼───┼───┼───┤
│ 13│ 4 │ 13│ 8 │
├───┼───┼───┼───┤
│ 13│ 6 │ 13│ 0 │
└───┴───┴───┴───┘
```


## [DAY-197] interpreter


We will make a small program, that can read the program state of our 4 bit computer and run it as it it is real, we will evaluate the input program and depending on the value of the instruction will do what it is said in the instruction set.


```
def cpu(IP, IS, R0, R1, memory):
    #    0 halt
    #    1 add R0 = R0 + R1, 2 subtract R0 = R0 - R1
    #    3 inc R0, 4 inc R1
    #    5 dec R0, 6 dec R1
    #    7 ring bell
    #  8 X print X
    #  9 X R0 = mem[X]
    # 10 X R1 = mem[X]
    # 11 X mem[X] = R0
    # 12 X mem[X] = R1
    # 13 X jump to address X
    # 14 X jump to address X if R0 == 0
    # 15 X jump to address X if R0 != 0

    while True:
        IS = memory[IP]
        print('instruction pointer:',IP,'instruction store:',IS)
        if IS == 0:
            break
        elif IS == 1:
            R0 = R0 + R1
            IP += 1
        elif IS == 2:
            R0 = R0 - R1
            IP += 1
        elif IS == 3:
            R0 += 1
            IP += 1
        elif IS == 4:
            R1 += 1
            IP += 1
        elif IS == 5:
            R0 -= 1
            IP += 1
        elif IS == 6:
            R1 -= 1
            IP += 1
        elif IS == 7:
            print("*** BEEP ***")
            IP += 1
        elif IS == 8:
            print("*** ", memory[IP+1], " ***")
            IP += 2
        elif IS == 9:
            R0 = memory[memory[IP+1]]
            IP += 2
        elif IS == 10:
            R1 = memory[memory[IP+1]]
            IP += 2
        elif IS == 11:
            memory[memory[IP+1]] = R0
            IP += 2
        elif IS == 12:
            memory[memory[IP+1]] = R1
            IP += 2
        elif IS == 13:
            IP = memory[IP + 1]
        elif IS == 14:
            if R0 == 0:
                IP = memory[IP + 1]
            else:
                IP += 2
        elif IS == 15:
            if R0 != 0:
                IP = memory[IP + 1]
            else:
                IP += 2

state = []
program = input('memory> ').split()
memory = [int(s) for s in program]
cpu(0,0,0,0, memory)
```

Try to run the above program and when it asks for input type `3 11 4 8 0 13 0`, this is will print 0 1 2 3 4 5 ..., by now you are probably used to seeing the program written as this:

```
    ┌────────┐ ┌────────┐
    │IP:  0  │ │IS:  0  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  0  │ │R1:  0  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │ 3  │ 11 │ 4  │ 8  │ 3
    ├────┼────┼────┼────┤
  4 │ 0  │ 13 | 0  │ 0  │ 7
    ├────┼────┼────┼────┤
  8 │ 0  │ 0  │ 0  │ 0  │ 11
    ├────┼────┼────┼────┤
 12 │ 0  │ 0  │ 0  │ 0  │ 15
    └────┴────┴────┴────┘  
```


Here you can also use a better version that helps you debug your programs and also reads them diectly from a file:

```
import sys

def ascii(state, highlight):
    center = []
    for (i, s) in enumerate(state):
        if i-4 in highlight:
            s = "_"+str(s)+"_"
        center.append(str(s).center(4))

    print("""
    ┌────────┐ ┌────────┐
    │IP: {0}│ │IS: {1}│
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0: {2}│ │R1: {3}│
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │{4}│{5}│{6}│{7}│ 3
    ├────┼────┼────┼────┤
  4 │{8}│{9}│{10}│{11}│ 7
    ├────┼────┼────┼────┤
  8 │{12}│{13}│{14}│{15}│ 11
    ├────┼────┼────┼────┤
 12 │{16}│{17}│{18}│{19}│ 15
    └────┴────┴────┴────┘  

""".format(*center))


def cpu(IP, IS, R0, R1, memory):
    """
                          │ IP: instruction pointer
    ┌──────┐ ┌──────┐     │ IS: instruction store, current instruction
    │IP: 0 │ │IS: 0 │     │ R0: register 0
    └──────┘ └──────┘     │ R1: register 1
    ┌──────┐ ┌──────┐     ├───────────────────────────────────────────
    │R0: 0 │ │R1: 0 │     │    0 halt
    └──────┘ └──────┘     │    1 add R0 = R0 + R1
      0   1   2   3       │    2 subtract R0 = R0 - R1
    ┌───┬───┬───┬───┐     │    3 increment R0 R0 = R0 + 1
    │ 0 │ 0 │ 0 │ 0 │     │    4 increment R1 R1 = R1 + 1
    ├───┼───┼───┼───┤     │    5 decrement R0 R0 = R0 - 1
    │ 0 │ 0 │ 0 │ 0 │     │    6 decrement R1 R1 = R1 - 1
    ├───┼───┼───┼───┤     │    7 ring bell
    │ 0 │ 0 │ 0 │ 0 │     │  8 X print data X
    ├───┼───┼───┼───┤     │  9 X load value of address X into R0
    │ 0 │ 0 │ 0 │ 0 │     │ 10 X load value of address X into R1
    └───┴───┴───┴───┘     │ 11 X store R0 into address X
     12  13  14  15       │ 12 X store R1 into address X
                          │ 13 X jump to address X
                          │ 14 X jump to address X if R0 == 0
                          │ 15 X jump to address X if R0 != 0
    """

    while True:
        IS = memory[IP]
        highlight = [IP]
        if (IS >= 8):
            highlight = [IP, IP+1]

        ascii([IP, IS, R0, R1, *memory], highlight)

        if IS == 0:
            break
        elif IS == 1:
            R0 = R0 + R1
            IP += 1
        elif IS == 2:
            R0 = R0 - R1
            IP += 1
        elif IS == 3:
            R0 += 1
            IP += 1
        elif IS == 4:
            R1 += 1
            IP += 1
        elif IS == 5:
            R0 -= 1
            IP += 1
        elif IS == 6:
            R1 -= 1
            IP += 1
        elif IS == 7:
            print("*** BEEP ***")
            IP += 1
        elif IS == 8:
            print("*** ", memory[IP+1], "***")
            IP += 2
        elif IS == 9:
            R0 = memory[memory[IP+1]]
            IP += 2
        elif IS == 10:
            R1 = memory[memory[IP+1]]
            IP += 2
        elif IS == 11:
            memory[memory[IP+1]] = R0
            IP += 2
        elif IS == 12:
            memory[memory[IP+1]] = R1
            IP += 2
        elif IS == 13:
            IP = memory[IP + 1]
        elif IS == 14:
            if R0 == 0:
                IP = memory[IP + 1]
            else:
                IP += 2
        elif IS == 15:
            if R0 != 0:
                IP = memory[IP + 1]
            else:
                IP += 2

        input()


if len(sys.argv) == 1 or ".prg" not in sys.argv[1]:
    print("usage: python3 ", sys.argv[0] + " file.prg")
    sys.exit(1)

f = open(sys.argv[1])
state = []
for line in f.readlines():
    if '#' in line:
        continue
    line = line.replace("│", " ")
    line = line.replace("_", " ")
    row = []
    for s in line.split():
        if s.isdigit():
            row.append(int(s))
    # remove first and last element in case its pasted from our output
    if len(row) == 6:
        row.pop(5)
        row.pop(0)
    if len(row) > 0:
        state += row
f.close()

instruction_pointer, instruction_store, r0, r1, *memory = state
cpu(instruction_pointer, instruction_store, r0, r1, memory)
```

Save a program as 'name.prg' and run it a `python3 interpreter.py name.prg`, then press enter for each step of the execution.

For example:

```
# print 1,2,3,1,2,3,1,2,3... forever
    ┌────────┐ ┌────────┐
    │IP:  0  │ │IS:  0 │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │ 8  │ 0  │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  
```

Will output of `python3 interpreter.py example.prg`:

```
    ┌────────┐ ┌────────┐
    │IP:  0  │ │IS:  12 │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │_12_│_3_ │ 8  │ 0  │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  




    ┌────────┐ ┌────────┐
    │IP:  2  │ │IS:  8  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │_8_ │_1_ │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  


***  1 ***


    ┌────────┐ ┌────────┐
    │IP:  4  │ │IS:  4  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  1  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │ 8  │ 1  │ 3
    ├────┼────┼────┼────┤
  4 │_4_ │ 5  │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  




    ┌────────┐ ┌────────┐
    │IP:  5  │ │IS:  5  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  3  │ │R1:  2  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │ 12 │ 3  │ 8  │ 1  │ 3
    ├────┼────┼────┼────┤
  4 │ 4  │_5_ │ 15 │ 12 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 15 │ 10 │ 14 │ 11
    ├────┼────┼────┼────┤
 12 │ 13 │ 0  │ 1  │ 3  │ 15
    └────┴────┴────┴────┘  


...

```



* print 15 then beep without using directly the beep instruction

```
#    0 halt
#    1 add R0 = R0 + R1
#    2 subtract R0 = R0 - R1
#    3 increment R0 R0 = R0 + 1
#    4 increment R1 R1 = R1 + 1
#    5 decrement R0 R0 = R0 - 1
#    6 decrement R1 R1 = R1 - 1
#    7 ring bell
#  8 X print X
#  9 X R0 = mem[X]
# 10 X R1 = mem[X]
# 11 X mem[X] = R0
# 12 X mem[X] = R1
# 13 X jump to address X
# 14 X jump to address X if R0 == 0
# 15 X jump to address X if R0 != 0
#
# print 15, then modify itself to beep without using the beep instruction
    ┌────────┐ ┌────────┐
    │IP:  0  │ │IS:  0  │
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0:  0  │ │R1:  0  │
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │ 9  │ 15 │ 10 │ 14 │ 3
    ├────┼────┼────┼────┤
  4 │ 1  │ 8  │ 15 │ 11 │ 7
    ├────┼────┼────┼────┤
  8 │ 9  │ 0  │ 0  │ 0  │ 11
    ├────┼────┼────┼────┤
 12 │ 0  │ 0  │ 4  │ 3  │ 15
    └────┴────┴────┴────┘  
```



## [DAY-198] coordinates

Make a cutes care game (like jumpscare but cute), the idea is to make a series of difficult challenges to make the user to concentrate on the game, and when they least expect it show them a cute corgi.

![game-198-a.jpg](./screenshots/game-198-a.jpg "game 198-a screenshot")

![game-198-c.jpg](./screenshots/game-198-c.png "game 198-b screenshot")

![game-198-b.jpg](./screenshots/game-198-b.png "game 198-c screenshot")


> This is the code she wrote, she struggled a bit with the isInside part, but I helped her out.

> Also important to google how to play sounds with pygamezero.

```
import ranom
import pgzrun
WIDTH=800
HEIGHT=800
elf = Actor("c1")
elf.x = 520
elf.y = 420
corgi = Actor("corgi")
data = [
    Rect(0,0,100,200),
    Rect(520,580, 300, 30),
    Rect(750,600, 30, 500),
    Rect(490,490, 50, 100),
    Rect(500,400, 200, 100),
]
def update():
    if keyboard.W:
        elf.y -= 2 
        elf.x += random.randint(-1,1)
    if keyboard.S:
        elf.y += 2
        elf.x += random.randint(-1,1)
    if keyboard.D:
        elf.x += 2 
    if keyboard.A:
        elf.x -= 2
    
    isInside = False
    for d in data:
        if elf.colliderect(d):
            isInside = True

    if not isInside:
        elf.x = 520 
        elf.y = 420

mouse_x = 0
mouse_y = 0
def on_mouse_move(pos):
    global mouse_x, mouse_y
    mouse_x = pos[0]
    mouse_y = pos[1]
    
def draw():
    screen.clear()
    for r in data:
        screen.draw.rect(r, (255,255,255))
    elf.draw()
    screen.draw.text("x: " + str(mouse_x) + " y: " + str(mouse_y), (20,20), color=(255,255,255))
    if elf.y > 780:
        corgi.draw()
        sounds.retro.play()

pgzrun.go()
```


## [DAY-199] coordinates

Add a blur around the cutescare game's actor so the game is more spooky

![game-199.png](./screenshots/game-199.png "game 199 screenshot")

Use images/fog.png which is a 2000x2000 black png with a transparent circle in the middle, we will use it to create "fog" around the player.

Read on https://pygame-zero.readthedocs.io/en/stable/builtins.html about how to anchor an actor so that the fog's x and y are actually at the center and not in the topleft.

Add a game level sound to make the game more fun, read in the pygame-zero docs how to loop a sound forever.

```
...
elf = Actor("c1")
elf.x = 520
elf.y = 420
...
fog = Actor("fog", anchor=("center","center"))

def update():
    ...
    if not isInside:
        elf.x = 520 
        elf.y = 420
    # move the fog's center to where the elf is 
    # so the elf is always in the center of the fog
    fog.x = elf.x
    fog.y = elf.y

...

sounds.level.play(-1)

def draw():
    screen.clear()
    for r in data:
        screen.draw.rect(r, (255,255,255))
    elf.draw()
    fog.draw()
    ...

pgzrun.go()
```



## [DAY-200] coordinates


Make a better maze

```
...

data = [
    Rect(0,0,100,200),
    Rect(20,200, 300, 30),
    Rect(267,226, 30, 500),
    Rect(408,678, 20, 200),
    Rect(23,659, 800, 20),
    Rect(429,101, 30, 500),
    Rect(299,356, 800, 20)
]

...
```

![game-200-a.png](./screenshots/game-200-a.png "game 200-a screenshot")


![game-200-b.png](./screenshots/game-200-b.png "game 200-b screenshot")

## [DAY-201] computers

Watch "The Computer Science Iceberg Explained (Part 1)" by Quabl - https://www.youtube.com/watch?v=H565avw-ufk

## [DAY-202] pointers

Watch "What Are Pointers? (C++)" by javidx9 again - https://www.youtube.com/watch?v=iChalAKXffs 


## [DAY-203] Strategy

Add multiple levels in your cutescare game, now you have only one level:

```
...

data = [
    Rect(0,0,100,200),
    Rect(20,200, 300, 30),
    Rect(267,226, 30, 500),
    Rect(408,678, 20, 200),
    Rect(23,659, 800, 20),
    Rect(429,101, 30, 500),
    Rect(299,356, 800, 20)
]

...
```

To make the game more interesting, add 2 more levels. First think a bit on your own how to do it then come back to the book.


```
...
level1 = [
    Rect(0,0,100,200),
    Rect(20,200, 300, 30),
    Rect(267,226, 30, 500),
    ...
]

level2 = [
    Rect(267,226, 30, 500),
    ...
]

level3 = [
    Rect(267,226, 30, 500),
    ...
]

current_level = level1


def update():
    global current_level
    
    if current_level == level1 and elf.x > 700 and elf.y > 700:
        current_level = level3
    
def draw():
    ....
    for d in current_level:
        ...
...
```

This pattern of having a 'current' thing is active from possible options is extremely common, you can see it everywhere in all kinds of program.

For example check out Google Chrome's tab bar, you have a current tab, when you click on some other one it changes it. As an exercise try to spot this pattern in the apps you use on your phone or computer.


## [DAY-204] money

Take a piece of paper and list all the apps installed on yout phone, then write down next to each one how they make money out of you.


|app|how it makes money|
|---|------------------|
|whatsapp|facebook using who you talk to and how often to show you more relevant ads|
|instagram|ads|
|duolingo|ads / subscription|
|spotify|ads / subscription|
|human resource machine|paid 7$|
|...|...|


## [DAY-205] fetch-decode-execute

Watch The Fetch-Execute Cycle: What's Your Computer Actually Doing - https://www.youtube.com/watch?v=Z5JC9Ve1sfI

Watch it 3 times and write it down.

## [DAY-206] client server

In order for computers to talk to each other we use the Internet Protocol, there are other ways to do it, but at the moment using the internet protocol is the most common one. The two computers talking to each other will need unique IP addresses. An IP address is just a 4 byte (32 bit) number, the minimum one is 0 and the maximum one is 4294967295. This is quite hard to remember, so we split the 32 bit number into 4x8 bit numbers, so for example the IP address of google.com is 2899945710, but this is super hard to read, if we split it into 4x8 bit numbers it looks like this: 172.217.168.238.

In another lesson we will discuss how the packet goes from computer to computer to get from your PC to google.com, it probably goes through 20 computers on its way.

Going back to the 32 bit number, lets start with something simple, 1 bit is as simple as an on/off switch, like the one controlling your lights.

One switch can either be on or off, so the possible configurations is 2 (0 or 1)

```
     .----------.
     |   ~ON~   |
     |   ____   |
     |  |.--.|  |
     |  ||  ||  |
     |  ||__||  |
     |  ||\ \|  |
     |  |\ \_\  |
     |  |_\[_]  |
     |          |
     |  ~OFF~   |
     '----------'
     (art by jgs)
```


Once we add a switch, the possible configurations double, however the previous ones were, we can have them either with the new switch on or off. So with 2 switches we have `00 01 10 11`


```
     .----------.      .----------.
     |   ~ON~   |      |   ~ON~   |
     |   ____   |      |   ____   |
     |  |.--.|  |      |  |.--.|  |
     |  ||  ||  |      |  ||  ||  |
     |  ||__||  |      |  ||__||  |
     |  ||\ \|  |      |  ||\ \|  |
     |  |\ \_\  |      |  |\ \_\  |
     |  |_\[_]  |      |  |_\[_]  |
     |          |      |          |
     |  ~OFF~   |      |  ~OFF~   |
     '----------'      '----------'
```


Adding third switch, the possible configurations doubles again `000 001 010 011 100 101 110 111`:

```
     .----------.      .----------.       .----------.
     |   ~ON~   |      |   ~ON~   |       |   ~ON~   |
     |   ____   |      |   ____   |       |   ____   |
     |  |.--.|  |      |  |.--.|  |       |  |.--.|  |
     |  ||  ||  |      |  ||  ||  |       |  ||  ||  |
     |  ||__||  |      |  ||__||  |       |  ||__||  |
     |  ||\ \|  |      |  ||\ \|  |       |  ||\ \|  |
     |  |\ \_\  |      |  |\ \_\  |       |  |\ \_\  |
     |  |_\[_]  |      |  |_\[_]  |       |  |_\[_]  |
     |          |      |          |       |          |
     |  ~OFF~   |      |  ~OFF~   |       |  ~OFF~   |
     '----------'      '----------'       '----------'
```

Going back to the IP address, one byte is just 8 switches, 4 bytes is 32 switches.

Now imagine 32 switches.. the possible amount of configurations is `2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2` or 4294967295.

So over the internet for any two computers to communicate they need their own 32 bit number, this btw is version 4 of the Internet Protocol, now we are in the process of adopting the new version 6 which has 128 bits for the IP address. Imagine 128 switches, the possible configurations are: 340282366920938463463374607431768211456, which is very very big number.


There are other few things needed in order to send messages between computers, and this is to be able to communicate with a specific program on the computer, for that we need a PORT, you can tell the operating system that when it recives a packet on specific port to send it to your program. We will use this in order to make a super simple chat program. The port is only 2 bytes (16 bits), so from 0 to 65535.

We will make a simple helper module, just copy paste the code for now, we will investigate it later.

Make a file 'multiplayer.py' and type the following code in it:

```
from socket import *
from threading import Thread

def server(ip, port,fn):
    t = Thread(target=listen, args=(ip,int(port),fn))
    t.start()
    t.join()

def listen(ip, port, fn):
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.bind((ip, port))
    while True:
        data, addr = sock.recvfrom(1024)
        r = fn(data.decode("utf-8"), addr)
        sock.sendto(r.encode("utf-8"), addr)


def send(ip, port, message):
    sock = socket(AF_INET,SOCK_DGRAM)
    sock.sendto(message.encode("utf-8"), (ip, int(port)))
    data, addr = sock.recvfrom(1024)
    return data.decode("utf-8")
```


Now make a server:

```
import multiplayer
import sys

messages = []
def incoming(text, sender):
    ip, port = sender
    if '>' in text:
        name, message = text.split("> ")
        if len(message) > 0:
            messages.append(text)
    return "\n".join(messages)

ip = sys.argv[1]
port = sys.argv[2]
print('listening on', 'ip:', ip, 'port:', port)

multiplayer.server(ip, port, incoming)
```

To see your ipaddress go to CMD and type `ipconfig`, on macos go to the terminal and type `ifconfig`, a computer can have multiple ip addresses, so use your parent to help you out. You will see `127.0.0.1`, you can use this ip address when you want to communicate with another program on the same computer, it is called the local host address.

Start the server with `python3 server.py 192.168.x.x 6500` we will use port 6500

Make a client:

```
import multiplayer
import sys

name = sys.argv[1]
ip = sys.argv[2]
port = sys.argv[3]

while True:
    my_message = input("message> ")
    all_messages = multiplayer.send(ip, port, name + "> " + my_message)
    print(all_messages)
```

Start the client on two computers with `python3 client.py server_ip 6500`, then when you type something and send a message, the server will reply to you with all messages it recived so far.

There is a lot of code you dont understand here, and this is totally ok, we will get back to it in the future. The important part to remember is that IP version 4 addresses are 32 bits, and the port is 16 bits, and IP address allows you to talk to a computer and a port allows you to talk to a program.


## [DAY-207] 0; 1; infinity; how to break things down

When you think about any solution to any problem, it is very important to think in context of zero, one and infinity (or one million if infinity is impractical).

Lets look at this code for rot13:

```
def rot13(c):
    n = ord(c) - ord('a')
    return chr(97 + ((n + 13) % 26))
```

This `97 + ((n + 13) % 26)` seems a bit intimidating, but if we set `n = 0` then `(n + 13) % 26` becomes `13 % 26` which is just 13, so the whole thing becomes 97+13, which is 110. To get `n=0` we need to pass 'a' as a parameter, so this function takes `a` and returns `chr(110)` which is `n`. See 0 is incredibly powerful, now lets try with 1, 97+14 is 111, so if we pass `b` as parameter, the function will return `o`. And for infinity, the biggest `n` we can have here is 25 or `ord('z') - ord('a')`, `(25+13)%26` is 12, 97+12 is `m`, so `a` goes to `n` and `b` goes to `o` and `z` goes to `m`.

Always check the bounderies of the code: 0,1 and ∞ are your friends.

In math as well, you can see how things break down when you use 0 or ∞, everytime you see something divided by a variable, try to make this variable 0.

```
x = [1,2,3]
average = sum(x)/len(x)
```

What happens when you have an empty list? What happens when the list has exactly 1 element? What happens when you have infinite elements in the list?

In any problem, try to reduce it to nothing, one and everything, and each of those steps will help you to understand it better.


Look at some old code we wrote in day 81:

```
image = [
    1,3,3,3,3,3,1,
    2,4,5,4,5,4,2,
    2,4,4,5,4,4,2,
    2,4,5,4,5,4,2,
    1,3,3,3,3,3,1,
]

width = 7

for (index, pixel) in enumerate(image):
    if index > 0 and index % width == 0:
        print('')

    if pixel == 1:
        print('+', end='')
    elif pixel == 2:
        print('|', end='')
    elif pixel == 3:
        print('-', end='')
    elif pixel == 4:
        print(' ', end='')
    elif pixel == 5:
        print('*', end='')
    else:
        print("dont know what to do with: " + str(pixel))
```

Think of width as 0 and make the image with only 1 pixel and look at the code again:

```
image = [1]

for (index, pixel) in enumerate(image):
    if pixel == 1:
        print('+', end='')
```

the code becomes incredibly trivial: `if you see the pixel value 1, print '+'`.

Go back through your previous programs, and re-read them when you set various things to 0 (or empty lists) or 1 (or lists with 1 element).


## [DAY-208] if; lists

Make a game where the player captures falling things, every time they catch a thing it starts falling from a random position again, every 5th catch the difficulty increases by increasing the number of falling things.

![game-208.png](./screenshots/game-208.png "game 208 screenshot")


> thats what she wrote

```
import pgzrun
import random

HEIGHT = 800
WIDTH = 800
score = 0
player = Actor("chess/white")

dots = [Actor("rock"),Actor("flower")]
player.y = 760
game_over = False

def update():
    global game_over,score
    if keyboard.A:
        player.x -= 15 #+ score
    if keyboard.D:
        player.x += 15 #+ score
    if player.x <0:
        player.x = 0
    if player.x >790:
        player.x = 790
    for d in dots:
        d.y += 4
        if player.colliderect(d):
            d.x = random.randint(50,700)
            d.y = random.randint(10,300)
            score += 1
            if score%5==0:
                n = Actor(random.choice(["rock", "flower"]))
                n.x = random.randint(50,700)
                n.y = random.randint(10,300)
                dots.append(n)

        if d.y >790:
            game_over = True

def draw():
    screen.fill("black")
    screen.draw.text(str(score), (10,10),color = (255,255,255))
    player.draw()
    for d in dots:
        d.draw()
    if game_over == True:
        screen.fill("deepskyblue")

pgzrun.go()
```

## [DAY-209] if; lists

Make each falling object have a different speed

> her initial idea was to just change the falling object's y with a random number

```
def update():
    ...
    for d in dots:
         d.y += random.randint(1,5)
         ...
```

> second idea she had was to use the index of the thing as its speed (up to 4)

```
def update():
    ...
    i = 1
    for d in dots:
         d.y += 1
         i += 1
         if i > 4:
             i = 1
         ...
```

> her third idea was somehow to use a speed defined outside of the update() loop, but she couldnt implement it so I helped a bit

```
dots = [[Actor("rock"), 3],[Actor("flower"), 2]]

def update():
    ...
    for d in dots:
        d[0].y += d[1]
        if player.colliderect(d[0]):
            d[0].x = random.randint(50,700)
            d[0].y = random.randint(10,300)
            score += 1
            if score%5==0:
                n = Actor(random.choice(["rock", "flower"]))
                n.x = random.randint(50,700)
                n.y = random.randint(10,300)
                dots.append([n, random.choice([1,2,3])])
    ...

def draw():
    ....
    for d in dots:
        d[0].draw()
    ....
```

This pattern, keeping multiple objects close together in a small group is very important, try to practice it with other things, for example think about how you would add special powers to the falling things (slow down time, increase the player's size, increase player size and speed up time, etc)

## [DAY-210] if; lists

add 3 special items to the game

* gold: move all balls back to starting position and slow them down to maximum speed 2
* elf: reduce the amount of balls by one
* king: add 5 more balls

> thats what she wrote

```
...
gold = Actor("c3")
king = Actor("c2")
elf = Actor("c1")
elf.x = random.randint(50,700)
king.x = random.randint(50,700)
gold.x = random.randint(50,700)
...

def update()
   ...
    if gold.colliderect(player):
        for d in dots:
            d[0].y = 0
            d[1].speed = random.randint(1,2)
        gold.y = 0
        gold.x = random.randint(50,700)

    if elf.colliderect(player):
        if len(dots) > 0:
            dots.pop()
        elf.y = 0
        elf.x = random.randint(50,700)

    if king.colliderect(player):
        for i in range(5):
            n = Actor(random.choice(["rock", "flower"]))
            n.x = random.randint(50,700)
            n.y = random.randint(10,300)
            dots.append([n,random.randint(1,3)])
        king.y = 0
        king.x = random.randint(50,700)
   ...

def draw():
   ...

   elf.draw()
   king.draw()
   gold.draw()
```

## [DAY-211] classes

This is the same game but with small tweaks, to the elf increases the player size, and the king decreases it, also the player speed varies.

Just try to read the code, it is a bit convoluted and objects are calling other objects and it is a bit intimidating, but focus on the `fall()` method and follow how it is used, then check the player `move_left()` and `move_right()`

```
import pgzrun
import random

HEIGHT = 800
WIDTH = 600

class Player:
    def __init__(self, w, h):
        self.speed = 15
        self.w = w
        self.h = h
        self.x = 0
        self.y = HEIGHT - (h + 10)

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > WIDTH-10:
            self.x = WIDTH-10

    def hit(self, someActor):
        playerRect = Rect(self.x, self.y, self.w, self.h)
        return someActor.colliderect(playerRect)

    def draw(self):
        r = Rect(self.x, self.y, self.w, self.h)
        screen.draw.filled_rect(r, color="red")

class FallingThing:
    def __init__(self, image):
        self.thing = Actor(image)
        self.speed = random.choice([1,1,2,2,3])
        self.start_from_top()

    def start_from_top(self):
        self.thing.x = random.randint(50,WIDTH-50)
        self.thing.y = random.randint(10,HEIGHT/4)
        self.speed = random.choice([1,2,2,3])

    def hit(self, player, falling):
        if player.hit(self.thing):
            if self.thing.image == 'c1':
                player.w *= 2

            elif self.thing.image == 'c2':
                player.w /= 2

            elif self.thing.image == 'c3':
                for d in falling:
                    d.start_from_top()

            player.speed += random.choice([-3,3])
            if player.speed < 0:
                player.speed = 1

            falling.append(FallingThing(random.choice(["rock", "flower"])))

            self.start_from_top()
            return True
        else:
            return False

    def fall(self):
        self.thing.y += self.speed
        return self.thing.y

    def draw(self):
        self.thing.draw()

score = 0
player = Player(100, 50)
falling = [
    FallingThing("c1"),
    FallingThing("c2"),
    FallingThing("c3"),
    FallingThing(random.choice(["rock", "flower"])),
    FallingThing(random.choice(["rock", "flower"])),
    FallingThing(random.choice(["rock", "flower"])),
    FallingThing(random.choice(["rock", "flower"]))
]
game_over = False

def update():
    global game_over, score

    if game_over:
        return

    if keyboard.A:
        player.move_left()
    if keyboard.D:
        player.move_right()

    for f in falling:
        if f.hit(player, falling):
            score += 1

        if f.fall() > HEIGHT:
            game_over = True

def draw():
    screen.fill("black")

    player.draw()
    for f in falling:
        f.draw()

    if game_over == True:
        screen.fill("deepskyblue")

    screen.draw.text(str(score), (10,10),color = (255,255,255))

pgzrun.go()
```

This is a different way of writing programs, splitting things into pieces that talk to each other through messages(methods), and those pieces contain state which might or might not be modified when they receive a message, like the player.x or the thing.y. It seems like the program is simpler than the previous way you wrote, but that is not exactly true, now in order to follow what is going on you have to jump from object to object, while previously you were just able to read from top to bottom of the update() function and see what is going on.

There are new ways, and old ways of writing programs, but the truth is, large scale software programming is difficult and also very new, it is only 60 years old, we still dont know how to do it, we dont know how to teach it. There are people that come and preach: 'use only functions dont mutate state', 'use only objects with state', there are the other ones with 'always strongly encapsulate your state', or 'you should be able to follow the code so it should be just a bunch of procedures', 'decouple the logic', 'separate your concerns', 'first write a test for your program before you write the program', 'you should always program with a programming buddy as two people think better than one', use a plastic duck to help you'..

So, relax, in the end of the day the computer will execute some instructions and show few pixels on the screen. Have some fun.



## [DAY-212] PICO-8 Follow Adventure Game Tutorial

[PICO-8](https://www.lexaloffle.com/pico-8.php) is a fantasy console (virtual computer), it costs one time 15$ to buy it, and then you can play and modify all the games and have access to their source code. You can also write your own games.

For the next week we will follow [PICO-8 Top-Down Adventure Game Tutorial](https://www.youtube.com/watch?v=J1wvvbVQ5zo&list=PLdLmU93eWisKpyk1WZywUSYAq5dkCPFIv) from [Dylan Bennett](https://www.youtube.com/channel/UCY3KFjwFe1DyZYxhwHbm7Ew).


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



## [DAY-220] lists

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


## [DAY-221] lists

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


## [DAY-222] lists

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


## [DAY-223] lists

![game-223.png](./screenshots/game-223.png "game 223 screenshot")

Make the boss shoot bullets in 4 directions

```
...
boss_bullets = []
bossIsAlive = False
...

def new_boss_bullet(x,y, where_to_go):
    #      KEY | VALUE
    #      ----+------
    #     image| "bullet"
    #        x | 47
    #        y | 27
    # direction| "right"

    b = Actor("bullet")
    b.x = x
    b.y = y
    b.direction = where_to_go

...
def update():
    global bossIsAlive
    ...
    if timer > 120:
        ...
        if bossIsAlive:
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"left"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"right"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"up"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y,"down"))

        timer = 0
    for m in list(monsters):
        ...
        if m.colliderect(bull):
            ...
            if counter > 20:
                bossIsAlive = True
                ...
    if bossIsAlive:
        for b in boss_bullets:
          if b.direction == "left":
              b.x -= speed
          if b.direction == "right":
              b.x += speed
          if b.direction == "up":
              b.y -= speed
          if b.direction == "down":
              b.y += speed

def draw():
    ...
    if bossIsAlive:
        boss.draw()
        for b in boss_bullets:
            b.draw()
```


Think about the objects in python like the tables in Lua, you can just add another row in the table, in our case we will add "direction" and we will put there the value we need.


## [DAY-224] lists

Make the boss die after being hit by 10 player bullets, and also make it so that the boss bullets kill the player if hit

```
...
bossHP = 100
...

def update():
    global bossHP
    ...
    if bossIsAlive:
        if boss.colliderect(elf):
            game_over = True
        for b in boss_bullets:
            if b.colliderect(elf):
                game_over = True
        if bull.colliderect(boss):
            bossHP -= 10
            bull.y = -100

            # move the boss a tiny amount
            boss.x += random.randint(-10,10)
            boss.y += random.randint(-10,10)

            if bossHP <= 0:
                bossIsAlive = False
        ...
```



## [DAY-225] functions

Make the elf bullet move in a random direction, reuse the code for moving the boss bullet

```
...
def move(speed,b):
    if b.direction == "left":
        b.x -= speed
    if b.direction == "right":
        b.x += speed
    if b.direction == "up":
        b.y -= speed
    if b.direction == "down":
        b.y += speed
    if b.direction == "diagonal_right":
        b.y += speed
        b.x += speed
...
def update():
    ...
    if keyboard.K_1:
        bull.direction= random.choice(['up','left','down','right', 'diagonal_right'])
    ...
    move(bullet_speed,bull)
    bullet_speed *= 1.06
    if bullet_speed > 20:
        bullet_speed = 1
    ...
    if bossIsAlive:
        for b in boss_bullets:
            move(1,b)
        ...
```

Our `move` function can work with **any** object that has the `direciton`, `x`  and `y` properties, it doesn't even care if its a bullet or a car.


## [DAY-226] lists

In the last few days we did few small refactors and improvements, e.g. improve the timer function to support multiple different seconds by using ever increasing number and checking if `timer % x_seconds == 0`. Split the code into `update_player`, `update_boss` etc, so that its easier to find the code.

Today's task is to make the player have 4 bullets instead of 1, and also increase the boss's bullet speed when he gets to low HP.

> This is how the code that we wrote together, she wrote most of it, but I helped as well. We spend a lot of time discussing patterns like having global timer that functions can check, or using a variable for a condition (e.g. if bossHP < 20 then speed = 4)


```
import random
import pgzrun
import math


def make_new_monster(x, y):
    monster = Actor("monster")
    monster.x = x
    monster.y = y
    return monster


def second(n):
    return (timer % math.floor((n * 60))) == 0


def new_boss_bullet(x, y, where_to_go):
    #      KEY | VALUE
    #      ----+------
    #     image| "bullet"
    #        x | 47
    #        y | 27
    # direction| "right"
    b = Actor("bullet")
    b.x = x
    b.y = y
    b.direction = where_to_go
    return b


elf = Actor("c1")
elf.y = 50
bullet_speed = 1
bull = []
bull.append(new_boss_bullet(-100, -10, "right"))
bull.append(new_boss_bullet(-100, -10, "left"))
bull.append(new_boss_bullet(-100, -10, "up"))
bull.append(new_boss_bullet(-100, -10, "down"))


WIDTH = 800
HEIGHT = 800
game_over = False
monsters_killed = 0

monsters = []
monster_speed_y = 1
for i in range(10):
    m = make_new_monster(i*100, 10)
    monsters.append(m)

boss = Actor("c2")
boss_bullets = []
bossIsAlive = False
bossHP = 100

timer = 1


def move(speed, b):
    if b.direction == "left":
        b.x -= speed
    if b.direction == "right":
        b.x += speed
    if b.direction == "up":
        b.y -= speed
    if b.direction == "down":
        b.y += speed
    if b.direction == "diagonal_right":
        b.y += speed
        b.x += speed


def update_player_bullet():
    global bullet_speed

    if keyboard.SPACE:
        for b in bull:
            b.x = elf.x+25
            b.y = elf.y + 5
        bullet_speed = 1
    if second(0.3):
        bullet_speed *= 1.20
        if bullet_speed > 20:
            bullet_speed = 1
    for b in bull:
        move(bullet_speed, b)


def update_player():
    global game_over
    if keyboard.W:
        elf.y -= 5
    if keyboard.S:
        elf.y += 5
    if keyboard.A:
        elf.x += -5
    if keyboard.D:
        elf.x += 5
    for b in bull:
        if elf.colliderect(b):
            game_over = True


def update_monsters():
    global game_over, monsters_killed, monsters

    for m in list(monsters):
        m.y += monster_speed_y
        if m.y > 795:
            m.y = 10

        if m.colliderect(elf):
            game_over = True
        for b in bull:
            if m.colliderect(b):
                if m in monsters:
                    monsters.remove(m)
                    monsters_killed += 1

    if second(5):
        m = make_new_monster(random.randint(10, 790), -10)
        monsters.append(m)


def reset_game():
    global game_over, timer, monsters
    game_over = False
    monsters = []
    for i in range(10):
        m = make_new_monster(i*100, 10)
        monsters.append(m)
    timer = 1
    elf.y = 500
    elf.x = 500


def update_boss():
    global game_over, bossIsAlive, monsters_killed, bossHP
    if bossIsAlive:
        for b in boss_bullets:
            if b.colliderect(elf):
                game_over = True
            for b in bull:
                if b.colliderect(boss):
                    bossHP -= 15
                    b.x = -100
                    b.y = -100
                    boss.x += random.randint(-10, 10)
                    boss.y += random.randint(-10, 10)
                    if bossHP <= 0:
                        bossIsAlive = False
                        boss.x = -1000
                        boss.y = -1000
                        monsters_killed = 0

        if second(3):
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "left"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "right"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "up"))
            boss_bullets.append(new_boss_bullet(boss.x, boss.y, "down"))

        boss_bullet_speed = 1
        if bossHP < 20:
            boss_bullet_speed = 5
        for b in boss_bullets:
            move(boss_bullet_speed, b)
    else:
        if monsters_killed > 1:
            boss.x = 400
            boss.y = 350
            bossIsAlive = True


def update():
    global timer
    update_player()
    update_player_bullet()
    update_monsters()
    update_boss()

    timer += 1

    if keyboard.R:
        reset_game()


def draw():
    screen.fill("white")
    elf.draw()
    for b in bull:
        b.draw()

    if bossIsAlive:
        boss.draw()
        for b in boss_bullets:
            b.draw()

    for m in monsters:
        m.draw()


pgzrun.go()
```

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

## [DAY-229] strings

Improve the game to print which character is different from the user input.

> We spent most of the time discussing strings and indexes, in the end that is what she wrote.

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

        for i in range(len(a)):
            if len(s) <= i:
                print(a[i] + " SORRY MISSING")
            else:
                if a[i] != s[i]:
                    print(a[i] + " != " + s[i])
                else:
                    print(a[i])
    else:
        print("CORRECT")
        a = select_words(scr)
        scr+=1

```

## [DAY-229] files; strings

![game-229.png](./screenshots/game-229.png "game 229 screenshot")

Make a game that draws with an image and you can save the image and load it. Copy the game from [day 99](https://github.com/jackdoe/programming-for-kids#day-99-classes-lists-functions-cartesian-coordinates) and think it through, google "how to split string in python". Play with the str.split in the python interpreter. Also think about what file.readlines() does.


```
import pgzrun
import sys # for sys.exit()
import random

HEIGHT = 600
WIDTH = 600

elf = Actor("elf")
speed = 3
back = []
def update():
    global score
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.J:
        f = Actor('bullet')
        f.x = elf.x
        f.y = elf.y
        back.append(f)

    if keyboard.M:
        f = open("save.txt", "w")
        for x in back:
            f.write(str(x.x))
            f.write(",")
            f.write(str(x.y))
            f.write("\n")
        f.close()
    if keyboard.L:
        f = open("save.txt", "r")
        for line in f.readlines():
            (x,y) = line.split(",") # 30,20
            a = Actor('bullet')
            a.x = float(x) # "40" 40
            a.y = float(y)
            back.append(a)
        f.close()
    if keyboard.Q:
        sys.exit(0)

def draw():
    screen.fill('black')
    for i in back:
        i.draw()

    elf.draw()

pgzrun.go()

```

## [DAY-230] dictionaries

![game-230.png](./screenshots/game-230.png "game 230 screenshot")

Make a drawing game that draws a circle with different size.

```
import pgzrun
import sys  # for sys.exit()
import random

HEIGHT = 600
WIDTH = 600

elf = Actor("elf")
speed = 3
back = []
radius = 5

def update():
    global score,radius
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed
    if keyboard.K_1:
        radius += 1
    if keyboard.K_2:
        radius -= 1
    if keyboard.J:
        f = {
            "x": elf.x, # x position
            "y": elf.y, # y position
            "color": [255, 0, 0], # color
            "radius": radius # current radius
        }

        back.append(f)

    if keyboard.Q:
        sys.exit(0)


def draw():
    screen.fill('black')

    screen.draw.circle(
        [elf.x,elf.y],  # position
        radius,         # radius
        [255,0,255]     # color
    )

    for circle in back:
        screen.draw.circle(
            [circle["x"], circle["y"]], # position
            circle["radius"],           # radius
            circle["color"]             # color
        )

    elf.draw()


pgzrun.go()
```


> Spend significant amount of time discussing the dictionaries, first start with static radius of 20 pixels, then add it as a variable that you can change.


## [DAY-231] dictionaries

![game-231.png](./screenshots/game-231.png "game 231 screenshot")

Continue to improve on the drawing program, add support for mutiple colos and filled/not filled circles, also organize your code with comments.


```
import pgzrun
import random
HEIGHT = 600
WIDTH = 600

elf = Actor("elf")
speed = 3
back = []
radius = 5
color = [255, 0, 0]
filled = True


def update():
    global radius, color, filled

    #######################################################
    # MOVEMENT
    #######################################################
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed

    #######################################################
    # FILLED NOT FILLED
    #######################################################
    if keyboard.F:
        filled = True
    if keyboard.G:
        filled = False

    #######################################################
    # COLOR AND RADIUS
    #######################################################
    # RADIUS
    if keyboard.K_9:
        radius += 1
    if keyboard.K_0:
        radius -= 1
    # COLORS
    if keyboard.K_1:
        color = [255, 0, 0]
    if keyboard.K_2:
        color = [0, 255, 0]
    if keyboard.K_3:
        color = [0, 0, 255]
    if keyboard.K_4:
        color = [255, 0, 255]
    if keyboard.K_5:
        color = [255, 255, 0]
    if keyboard.K_6:
        color = [0, 255, 255]
    if keyboard.K_7:
        color = [128, 128, 255]
    if keyboard.K_8:
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    #######################################################
    # ADD CIRCLES TO DRAW LATER
    #######################################################
    if keyboard.SPACE:
        f = {
            "x": elf.x,            # x position
            "y": elf.y,            # y position
            "color": color,        # [red, green, blue]
            "radius": radius,      # current radius
            "filled": filled
        }

        back.append(f)


def draw():
    screen.fill('white')

    for circle in back:
        if not circle["filled"]:
            # ...
            screen.draw.circle(
                [circle["x"], circle["y"]], # [x, y]
                circle["radius"],           # radius
                circle["color"]             # [red, green, blue]
            )
        else:
            screen.draw.filled_circle(
                [circle["x"], circle["y"]], # [x, y]
                circle["radius"],           # radius
                circle["color"]             # [red, green, blue]
            )

    screen.draw.circle(
        [elf.x, elf.y], # pos [x, y]
        radius,         # radius
        [255, 0, 255]   # color [red, green, blue]
    )

    elf.draw()


pgzrun.go()
```

## [DAY-232] dictionaries

![game-232.png](./screenshots/game-232.png "game 232 screenshot")

Add option to draw rectangles or circles


```
import pgzrun
import random
HEIGHT = 600
WIDTH = 600

elf = Actor("elf")
speed = 3
dict_to_draw = []
radius = 5
color = [255, 0, 0]
filled = True
userect = True

def update():
    global radius, color, filled,userect

    #######################################################
    # MOVEMENT
    #######################################################
    if keyboard.A:
        elf.x -= speed
    if keyboard.D:
        elf.x += speed
    if keyboard.W:
        elf.y -= speed
    if keyboard.S:
        elf.y += speed

    #######################################################
    # FILLED NOT FILLED, RECT NOT RECT
    #######################################################
    if keyboard.F:
        filled = True
    if keyboard.G:
        filled = False
    if keyboard.R:
        userect = True
    if keyboard.T:
        userect = False

    #######################################################
    # COLOR AND RADIUS
    #######################################################
    # RADIUS
    if keyboard.K_9:
        radius += 1
    if keyboard.K_0:
        radius -= 1
    # COLORS
    if keyboard.K_1:
        color = [255, 0, 0]
    if keyboard.K_2:
        color = [0, 255, 0]
    if keyboard.K_3:
        color = [0, 0, 255]
    if keyboard.K_4:
        color = [255, 0, 255]
    if keyboard.K_5:
        color = [255, 255, 0]
    if keyboard.K_6:
        color = [0, 255, 255]
    if keyboard.K_7:
        color = [128, 128, 255]
    if keyboard.K_8:
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    #######################################################
    # ADD CIRCLES TO DRAW
    #######################################################
    if keyboard.SPACE:
        f = {
            "x": elf.x,            # x position
            "y": elf.y,            # y position
            "color": color,        # [red, green, blue]
            "radius": radius,      # current radius
            "filled": filled,
            "userect":userect
        }

        dict_to_draw.append(f)


def draw():

    screen.fill('white')

    for element in dict_to_draw:
        if not element["filled"]:
            if not element["userect"]:
                screen.draw.circle(
                    [element["x"], element["y"]], # [x, y]
                    element["radius"],            # radius
                    element["color"]              # [red, green, blue]
                )
            else:
                baz = Rect([element["x"], element["y"]], [element["radius"], element["radius"]])
                screen.draw.rect(baz,element["color"])
        else:
            if not element["userect"]:
                screen.draw.filled_circle(
                    [element["x"], element["y"]], # [x, y]
                    element["radius"],            # radius
                    element["color"]              # [red, green, blue]
                )
            else:
                baz = Rect([element["x"], element["y"]], [element["radius"], element["radius"]])
                screen.draw.filled_rect(baz, element["color"])
    if userect:
        baz = Rect([elf.x, elf.y], [radius, radius])
        screen.draw.rect(baz,color)
    else:
        screen.draw.circle(
            [elf.x, elf.y],  # pos [x, y]
            radius,          # radius
            color            # color [red, green, blue]
        )

    elf.draw()


pgzrun.go()
```

## [DAY-233] scope

> Today I wrote some example programs on paper and we went through them, focusing on scope.

![game-233-a.jpeg](./screenshots/game-233-a.jpeg "game 233-a screenshot")
![game-233-b.jpeg](./screenshots/game-233-b.jpeg "game 233-b screenshot")
![game-233-c.jpeg](./screenshots/game-233-c.jpeg "game 233-c screenshot")

Another important subject we discussed was what acually happens when you do `x = [1,2,3]; some_list.append(x)`, how `[1,2,3]` exists separately from the variable.


Using [pythontutor.com](https://pythontutor.com/render.html#code=l%20%3D%20%5B%5D%0Adef%20abc%28%29%3A%0A%20%20%20%20x%20%3D%20%7B%22a%22%3A1%7D%0A%20%20%20%20l.append%28x%29%0A%20%20%20%20%0Aabc%28%29%0Aabc%28%29%0Aprint%28l%29&cumulative=false&curInstr=13&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) for the following code:


```
l = []
def abc():
    x = {"a":1}
    l.append(x)
    
abc()
abc()
print(l)
```

Step through it multiple times and look how the variable `x` disappears but the dictionary `{"a":1}` remains.

![game-233-d.png](./screenshots/game-233-d.png "game 233-d screenshot")
![game-233-e.png](./screenshots/game-233-e.png "game 233-e screenshot")





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


## [DAY-239] directories

Copy this program into a python file on your desktop, then run it

```
import os
import random

possible = ["a b c", "hello","world", "has space","maybe empty","empty","not empty"]

def md(p):
    one_of_five = ''
    for i in range(1,6):
        a = random.choice(possible)
        one_of_five= a
        os.makedirs(os.path.join(p,a), exist_ok=True)

    return one_of_five


p = os.path.join(".","secret mission")
for i in range(10):
    p = os.path.join(p, md(p))

with open(os.path.join(p, "password.txt"), "w") as f:
    f.write("the password is: " + str(random.randint(123123,477217972)* 31))
```

It will create a random tree of directories, and in one of them there will be a file named password.txt with a random password.

Use the command line to find the password, using the `dir` and `cd` commands (on macos/linux use `ls` and `cd`), use `type password.txt` on windows or `cat password.txt` on linux to see the contents of the file.


## [DAY-240] for


> we were camping and had an old introduction to C book, and decided to skim through some of the code

```
int i;
for (i = 1; i < 10; i++) {
    printf("%d\n",i)
}
```

a for loop in C has 3 parts separated by `;` (semi-colon)

The first part `i = 1` is the initialization part, it will be executed only once.

You can also write the above loop like this:

```
int i = 1;
for (; i < 10; i++) {
    printf("%d\n",i)
}

```

The second part `i < 10` is the condition, if the condition is true it will enter the loop and execute the block of code inside, otherwise it will continue with the code after the loop. If you dont put any condition in, it is always going to enter the loop turning it into infinite loop unless you break out of it. You can also write it like this:

```
for (i = 1; ; i++) {
    if (i >= 10) {
        break;
    }
    printf("%d\n",i)
}

```

The third part `i++` or `i+=1` is the `increment` part, it will be executed just after the code in the loop is finished and is about to go back to start, you can also write it like this:

```
for (i = 1; i < 10; ) {
    printf("%d\n",i)
    
    i++
}

```

You can see that each of the 3 parts are optional, you can write the same loop like this:

```
int i = 1;
for (;;) {
    if (i >= 10) {
        break;
    }
    printf("%d\n",i)
    i++
}

```


So you see having the 3 parts, `init; condition; increment` together with the `for` keyword makes it read nicer.


## [DAY-241] lists

![game-241.jpg](./screenshots/game-241.jpg "game 241 screenshot")


Make a line edittor that can add lines to a list, save this list to a file file and open a file and read the lines into the list.

It looks like this:

```
C:\Users\jackie\Desktop>python3 editor.py
> example file
========================================
0: example file
========================================
> with many lines
========================================
0: example file
1: with many lines
========================================
> save a.txt
a.txt saved!
>
^C (Ctrl + C)


C:\Users\jackie\Desktop>python3 editor.py
> open a.txt
========================================
0: example file
1: with many lines
========================================
>
```

Here are all the components you need:


```
* read the user input and add it into a list:
  lines = []
  while True:
      a = input("> ")
      lines.append(a)

* print list of lines with their line number, and
some header and footer of =====..x40:
  print("=" * 40)
  for i in range(len(lines)):
      print(str(i) + " " + lines[i])
  print("=" * 40)

* join list of lines into a string:
  lines = ["a","b","c"]
  s = "\n".join(lines)

  will make the string:
  a
  b
  c


* read the lines of a file:
  lines = []
  name = "hello.txt"
  with open(name, "r") as f:
      lines = f.read().splitlines()

* write list of lines to a file:
  name = "hello.txt"
  with open(name, "w") as f:
      f.write("\n".join(lines))


* check if string starts with the word "save"
  s = "save hello.txt"
  if s.startswith("save "):
      print("yes it does")

* split a string into two parts:
  s = "save hello.txt"
  a,b = s.split(" ")

  a is "save"
  b is "hello.txt"
```


Line editors seems silly, but they were the super useful in the 60s and 70s, in fact a lot of the operating systems and laguages back then were written in a line editor called `ed`, there are three fundamental components to make a computer usefful, `assembler` - a program that translate instructions into machine code, `editor` - a program that allows you to write files and a `shell` a program that allows you to start other programs and interact with them.

The C language was written in `ed`, the UNIX operating system was written by `ed` as well.


## [DAY-242] lists

Add the functionality to delete a line. This is how it should look:

```
python3 editor2.py
...
> haha amazing
========================================
000: hello
001: this
002: is
003: one
004: line
005: per
006: word
007: haha amazing
========================================
> d 2
========================================
000: hello
001: this
002: one
003: line
004: per
005: word
006: haha amazing
========================================
> d 4
========================================
000: hello
001: this
002: one
003: line
004: word
005: haha amazing
========================================
>
```

You will need the following:

```
* how to check if string starts with "d "
    if line.startswith("d "):
       print("yey")


* how to split a string
    line = "d 25"
    a,b = line.split(" ")
    # a is "d"
    # b is "25"

* how to convert string to a number:
    x = ["hello","this","is"]
    a = "5"
    n = int(a)

    # access the element at index n from the list x
    print(x[n])

* how to delete a item from a list
    x = ["hello","this","is"]

    # delete the element on index 1
    del x[1]

    # or you can use pop(1) to
    # remove and return the value at index 1
    a = x.pop(1)

    # or just use x.pop(1) if you dont care about
    # the element it is returning
    x.pop(1)


* if you try to access a list beyond its size it will
  crash, so you need to check if a number fits to be
  used as an index

    n = 5
    if n < len(lines):
       print("yey")
```


## [DAY-243] lists

Add goto line functionality.

```
* how to check if string starts with "goto "
    if line.startswith("goto "):
       print("yey")


* how to split a string
  .split(separator) is a method you call on the string
  it returns a list splitted by the separator
    line = "d 25"
    x = line.split(" ")
    x is a list ["d","25"]

  you can also use destructuring to directly assign
  the list into separate variables
    a,b = line.split(" ")
  a is "d"
  b is "25"


* how to convert string to a number:
    x = ["hello","this","is"]
    a = "5"
    n = int(a)

  access the element at index n from the list x
    print(x[n])

* insert into a list in a specific position

    a = ["hello","world"]
    x = 1
    a.insert(x, "beautiful")
    print(a)
  prints ['hello', 'beautiful', 'world']

  if you try to insert beyond the list size, it will
  just add it to the end

    x = 20
    a.insert(x, "zzz")
    print(a)
  prints ['hello', 'beautiful', 'world', 'zzz']


* string formatting
  python has 'f' strings, which are formatted strings

    i = 2
    print(f"hello {i:05}")
  prints 00002, so it will make sure it will occupy
  5 spaces, filling with 0, this is handy if you want
  to print things with the same width.

  e.g. lets say you have this lines:
  0: hello
  1: world
  ...
  9: good
  10: morning


  see how 'morning' is one space to the right, because 10
  has one more symbol than 9, so with print(f"{i:02}")
  it will look like this:

  00: hello
  01: world
  ...
  09: good
  10: morning



* example code:

    x = []
    # start at -1, because we always insert on the "next line"
    # and in the beginning the next line is going to be 0
    # so we need to start at -1
    position = -1
    while True:
        a = input("> ")
        if a == "goto 5":
            position = 5
        else:
            # insert at the next line
            position += 1
            x.insert(position, a)
            for line in x:
                print(line)



* example how to show which line we have the position on
  use f strings in your solution

    def printWithLineNumbers(a, position):
        print("=" * 40)
        for i in range(len(a)):
            if i == position:
                print("*" + str(i) + ": " + a[i])
            else:
                print(" " + str(i) + ": " + a[i])
        print("=" * 40)



```

How it should work:

```
python3 editor2.py
> hello
========================================
*000: hello
========================================
> this is a new
========================================
 000: hello
*001: this is a new
========================================
> file
========================================
 000: hello
 001: this is a new
*002: file
========================================
> with
========================================
 000: hello
 001: this is a new
 002: file
*003: with
========================================
> a lot
========================================
 000: hello
 001: this is a new
 002: file
 003: with
*004: a lot
========================================
> of information
========================================
 000: hello
 001: this is a new
 002: file
 003: with
 004: a lot
*005: of information
========================================
> goto 2
========================================
 000: hello
 001: this is a new
*002: file
 003: with
 004: a lot
 005: of information
========================================
> that i am writing in my new editor
========================================
 000: hello
 001: this is a new
 002: file
*003: that i am writing in my new editor
 004: with
 005: a lot
 006: of information
========================================
> d 4
========================================
 000: hello
 001: this is a new
 002: file
*003: that i am writing in my new editor
 004: a lot
 005: of information
========================================
> which is amazing and it can edit
========================================
 000: hello
 001: this is a new
 002: file
 003: that i am writing in my new editor
*004: which is amazing and it can edit
 005: a lot
 006: of information
========================================
> goto 6
========================================
 000: hello
 001: this is a new
 002: file
 003: that i am writing in my new editor
 004: which is amazing and it can edit
 005: a lot
*006: of information
========================================
> now i will append in the end of the file
========================================
 000: hello
 001: this is a new
 002: file
 003: that i am writing in my new editor
 004: which is amazing and it can edit
 005: a lot
 006: of information
*007: now i will append in the end of the file
========================================
>

```

## [DAY-242] lists

![game-242.jpg](./screenshots/game-242.jpg "game 242 screenshot")

> She was super tired after shool and training, so I had to help out a lot.

Make goto support `goto 7` to go to specific line index, and `goto hello` to go to the first line that contains the word `hello`


```
* check if a string is an integer:

  z = "helloo"
  if z.isdigit():
      print("Z IS A DIGIT")
  else:
      print("Z IS NOT A DIGIT")


* find the first line containing a string

  def find(where, what):
      for i in range(len(where)):
          if what in where[i]:
              return i
      return -1


  x = ['hello world', 'b' ,'hello']
  found = find(x, "b")
  if found >= 0:
     print(f"index {found} matching with value {x[found]}")
```


How it should look:

```
> hello
========================================
*000: hello
========================================
> world
========================================
 000: hello
*001: world
========================================
> this is hello
========================================
 000: hello
 001: world
*002: this is hello
========================================
> how can it be
========================================
 000: hello
 001: world
 002: this is hello
*003: how can it be
========================================
> blabla
========================================
 000: hello
 001: world
 002: this is hello
 003: how can it be
*004: blabla
========================================
> goto world
========================================
 000: hello
*001: world
 002: this is hello
 003: how can it be
 004: blabla
========================================
> goto 3
========================================
 000: hello
 001: world
 002: this is hello
*003: how can it be
 004: blabla
========================================
> z
========================================
 000: hello
 001: world
 002: this is hello
 003: how can it be
*004: z
 005: blabla
========================================
> goto world
========================================
 000: hello
*001: world
 002: this is hello
 003: how can it be
 004: z
 005: blabla
========================================
> m
========================================
 000: hello
 001: world
*002: m
 003: this is hello
 004: how can it be
 005: z
 006: blabla
========================================
>
```


Lookup the documentation for .split(" "), to see how to make "goto hello world" be split into ["goto", "hello world"] instead of ["goto","hello","world"] (hint, .split() takes two parameters, separator which in our case is " ", and maxsplit, which by default is -1, but you can limit how many times you want to split)


## [DAY-243] lists; strings

![game-243.jpg](./screenshots/game-243.jpg "game 243 screenshot")

> today was a 'write this code and lets go over it' kind of lesson

When adding a line, use the number of starting spaces from previous line this is super handy if you are writing python, or a presentation.

This is how it should look:

```

> hello
========================================
*000: hello
========================================
>    testing
========================================
 000: hello
*001:    testing
========================================
> another line
========================================
 000: hello
 001:    testing
*002:    another line
========================================
>
========================================
 000: hello
 001:    testing
 002:    another line
*003:
========================================
> and again
========================================
 000: hello
 001:    testing
 002:    another line
 003:
*004: and again
========================================
> goto 2
========================================
 000: hello
 001:    testing
*002:    another line
 003:
 004: and again
========================================
> zzz
========================================
 000: hello
 001:    testing
 002:    another line
*003:    zzz
 004:
 005: and again
========================================
>

```

use the following function which just iterates the characters of a string and counts spaces and breaks out if it sees the first non space

```
    def countSpaces(string):
        n = 0
        for character in string:
            if character == ' ':
                n += 1
            else:
                break
        return n

```

you need to use this function to modify the 'line' if we have a previous line and the current line has at least 1 character:

```

while True:
     line = input('> ')

     ...
     else:
         if pos >= 0 and pos < len(lines) and len(line) > 0:
              prev = lines[pos]
              prefix = (' ' * countSpaces(prev)) # n spaces
              line = prefix + line
```

## [DAY-244] files; strings

Create 1000 files 1.txt 2.txt etc.. each file should contain "hello\n" 500 times

```
MAKE BIG STRING:

  # make a string containing "hello\n" 500 times:
  a = "hello\n" * 500


WRITE TO A FILE:

  # with open and close
  name = "1.txt"
  f = open(name, "w")
  s = "hello\n"
  f.write(s)
  f.close()


  # or using `with` so it automatically closes the file:
  name = "1.txt"
  s = "hello\n"
  with open(name, "w") as f:
      f.write(s)
```

## [DAY-245] lists

We made a small test:

```
# insert 100000 random integers between 1 and 1000 in a list
# find the smallest number
# find the largest number

def find_smallest(x):
    n = 0

    # ...
    # code that finds the smallest

    return n



def find_largest(x):
    n = 0

    # ...
    # code that finds the largest

    return n


import random
numbers = []

for i in range(100000):
    # append random numbers between 1 and 1000 to the list


smallest = find_smallest(numbers)
largest = find_largest(numbers)

print(f"smallest: {smallest}, largest: {largest}")
```


After the test is done, google for 'how to find smallest/largest numbers from a ist in python' and see how the `min` and `max` functions work.



## [DAY-246] strings

```
# make a function to count how many times a given character
# appears in a string

def count(c, s):
    # .. count how many times `c` appears in `s`
    # example string s "hello"
    # example character c "l"
    return 0



n = count("l","hello")
print(f"character l appears {n} times")

# what would happen if we do: n = count(1, [1,2,3,4,1,5])

```

