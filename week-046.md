## [DAY-330] html

Make 5 webpages with image, link to a website some title, description and a list of items

> this is an example page she made, this exercise actually took 5-6 days, she made one page every few days

![game-330.png](./screenshots/game-330.png "game 330 screenshot")

Upload them to the server your parents bought with scp then ssh into it and move the files to the right directory so they are visible from http://x.x.x.x/page.html




## [DAY-331] for; input

Rewrite this card from our [https://punkjazz.org/programming-time](programming-time) game from python to c:

```
# Welcome to the haunted house!
# ⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂⌂
# 
#     ___
#   _/ @@\   +--0--+ +--1--+ +--2--+
#  ( \  O/__ |     | |     | |     |
#   \    \__)|*    | |*    | |*    |
#   /     \  |     | |     | |     |
#  /      _\ |     | |     | |     |
# `"""""``   +-----+ +-----+ +-----+
# (ghost art
#  by jgs)
#
#
# There are 3 doors.
# Behind one of the doors there is a
# ghost.
#
# Roll the dice until your door is
# different from the ghost's door.
while True:
  ghost_door = ⚂ % 3
  your_door = ⚂ % 3

  if your_door == ghost_door:
    print("RUUUNNN!!")
  else:
    print("phew! no ghost!")
    break
```


those are two example C programs that you can read to draw inspiration from:

```
// printf, scanf come from here:
#include <stdio.h>

// random() comes from here:
#include <stdlib.h>

int main(void) {
    int a = random();

    printf("the random number is: %d\n",a);

    return 0;
}

```

and

```
// printf, scanf come from here:
#include <stdio.h>

int main(void) {
  int b = 0;

  printf("enter number: ");
  scanf("%d",&b);

  printf("the number you entered is is: %d\n",b);

  return 0;
}

```


## [DAY-332] unix


Play the [bandit war game](https://overthewire.org/wargames/bandit/) level 0 to 7:

* https://overthewire.org/wargames/bandit/bandit0.html
* https://overthewire.org/wargames/bandit/bandit1.html
* https://overthewire.org/wargames/bandit/bandit2.html
* https://overthewire.org/wargames/bandit/bandit3.html
* https://overthewire.org/wargames/bandit/bandit4.html
* https://overthewire.org/wargames/bandit/bandit5.html
* https://overthewire.org/wargames/bandit/bandit6.html
* https://overthewire.org/wargames/bandit/bandit7.html

Read the instructions carefully, try to not use chatgpt, but if you get stuck its better to use it to unblock yourself.

## [DAY-333] unix

In order to understand how arguments are passed to your program, read chapter [18.1 from Beej's C guide](https://beej.us/guide/bgc/html/split/the-outside-environment.html#command-line-arguments) and implement the program to print the sum of the command line arguments.


## [DAY-334] unix

> make a file somewhere on another computer (e.g. /etc/hidden/data.txt) with specific size, and fill it with random data, and mid-way put some word like 'helloworld', in my case the file was 18348672 bytes long

On the computer a.b.c.d (your parent will yell you the ip address) there is a file somewhere in the filesystem which is exactly 18348672, login to the computer with ssh (your parent will give you username and password) and use the `find` command to find it, then use the programs `cat` and `grep` to print only the lines the contain the word hello

> find / -size 18348672c # finds the file, then `cat /etc/hidden/data.txt | grep hello`, explain about how one program's output becomes another program's input

## [DAY-335] unix

Make a small python program on your computer that reads the file /etc/hidden/data.txt and prints only the lines that start with the word hello, then use `scp` to copy it to the other computer and then use `ssh` to log into it and execute your program.


```
f = open("/etc/hidden/data.txt","r")
lines = f.readlines()
for l in lines:
    if l.startswith("hello"):
        print(l)
f.close()

```

> I specifically encouraged using list of all lines instead of a stream at this stage because streams of bytes are actualy quire strange concept, while lists are more natural


## [DAY-336] unix

Make a program that prints only the lines that are exactly 5 characters, use `nano` on the remote computer to edit the program from the previous day.

```
f = open("/etc/hidden/data.txt","r")
lines = f.readlines()
for l in lines:
    if len(l) == 5:
        print(l)
f.close()
```


## [DAY-337] unix

Make a program that prints only the lines that are exactly 5 characters and start with 'h', use `nano` on the remote computer to edit the program from the previous day.

```
f = open("/etc/hidden/data.txt","r")
lines = f.readlines()
for l in lines:
    if len(l) == 5 and l.startswith("h"):
        print(l)
f.close()
```


## [DAY-338] unix

Make a program that counts the lines that are exactly 5 characters and start with 'h', use `nano` on the remote computer to edit the program from the previous day.

```
f = open("/etc/hidden/data.txt","r")
lines = f.readlines()
n = 0
for l in lines:
    if l.startswith("h"):
        n += 1
f.close()
print(n)
```

Now do the same with unix pipes, `cat /etc/hidden/data.txt | grep ^h | wc -l`


## [DAY-339] unix

> generate a file with few thousand name,age,country entries, I used chatgpt to generate it, you can get it from: [names.csv](names.csv), and upload it to the server.

```
Ava,51,UK
William,49,USA
Michael,24,Australia
Ava,20,USA
Emma,48,USA
James,64,Brazil
David,34,Japan
Olivia,46,India
Michael,62,Canada
Ava,41,India
Ava,63,Brazil
Emma,65,Australia
James,18,Japan
Olivia,26,UK
Michael,34,Canada
John,53,Brazil
Michael,35,Germany
Emma,52,Brazil
William,46,Brazil
James,61,USA
...
```

Write a program that prints only the names column, use the python cheatsheet to see how to use the 'split' method of the string object.

```
f = open("names.csv","r")
lines = f.readlines()
n = 0
for l in lines:
    s = l.split(",")
    print(s[0])
f.close()
```

> now use `cat names.csv | cut -f 1 -d ,` to show an example of using the `cut` command.


## [DAY-340] split

Download the file [covid-test-cases.csv](covid-test-cases.csv) which is from https://www.ecdc.europa.eu/en/publications-data/covid-19-testing and has the following format:

```
country,country_code,year_week,level,region,region_name,new_cases,tests_done,population,testing_rate,positivity_rate,testing_data_source
Austria,AT,2020-W01,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W02,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W03,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W04,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W05,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W06,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W07,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W08,national,AT,Austria,NA,NA,8978929,NA,NA,NA
Austria,AT,2020-W09,national,AT,Austria,12,NA,8978929,NA,NA,NA
Austria,AT,2020-W10,national,AT,Austria,115,NA,8978929,NA,NA,NA
Austria,AT,2020-W11,national,AT,Austria,874,NA,8978929,NA,NA,NA
Austria,AT,2020-W12,national,AT,Austria,3046,NA,8978929,NA,NA,NA
Austria,AT,2020-W13,national,AT,Austria,5098,NA,8978929,NA,NA,NA
Austria,AT,2020-W14,national,AT,Austria,3114,NA,8978929,NA,NA,NA
Austria,AT,2020-W15,national,AT,Austria,1838,NA,8978929,NA,NA,NA
Austria,AT,2020-W16,national,AT,Austria,686,NA,8978929,NA,NA,NA
Austria,AT,2020-W17,national,AT,Austria,450,NA,8978929,NA,NA,NA
Austria,AT,2020-W18,national,AT,Austria,309,NA,8978929,NA,NA,NA
Austria,AT,2020-W19,national,AT,Austria,260,NA,8978929,NA,NA,NA
Austria,AT,2020-W20,national,AT,Austria,324,NA,8978929,NA,NA,NA
Austria,AT,2020-W21,national,AT,Austria,264,NA,8978929,NA,NA,NA
Austria,AT,2020-W22,national,AT,Austria,195,NA,8978929,NA,NA,NA
Austria,AT,2020-W23,national,AT,Austria,228,NA,8978929,NA,NA,NA
Austria,AT,2020-W24,national,AT,Austria,172,NA,8978929,NA,NA,NA
Austria,AT,2020-W25,national,AT,Austria,248,NA,8978929,NA,NA,NA
Austria,AT,2020-W26,national,AT,Austria,334,NA,8978929,NA,NA,NA
Austria,AT,2020-W27,national,AT,Austria,640,NA,8978929,NA,NA,NA
Austria,AT,2020-W28,national,AT,Austria,597,NA,8978929,NA,NA,NA
Austria,AT,2020-W29,national,AT,Austria,784,NA,8978929,NA,NA,NA
Austria,AT,2020-W30,national,AT,Austria,872,NA,8978929,NA,NA,NA
Austria,AT,2020-W31,national,AT,Austria,792,NA,8978929,NA,NA,NA
Austria,AT,2020-W32,national,AT,Austria,721,NA,8978929,NA,NA,NA
Austria,AT,2020-W33,national,AT,Austria,1461,NA,8978929,NA,NA,NA
Austria,AT,2020-W34,national,AT,Austria,1908,NA,8978929,NA,NA,NA
Austria,AT,2020-W35,national,AT,Austria,1943,NA,8978929,NA,NA,NA
Austria,AT,2020-W36,national,AT,Austria,2263,NA,8978929,NA,NA,NA
Austria,AT,2020-W37,national,AT,Austria,3995,NA,8978929,NA,NA,NA
Austria,AT,2020-W38,national,AT,Austria,5215,NA,8978929,NA,NA,NA
Austria,AT,2020-W39,national,AT,Austria,4661,NA,8978929,NA,NA,NA
Austria,AT,2020-W40,national,AT,Austria,5602,NA,8978929,NA,NA,NA
Austria,AT,2020-W41,national,AT,Austria,7487,124663,8978929,1388.394985638042,6.005791614191861,TESSy COVID-19
Austria,AT,2020-W42,national,AT,Austria,9898,129647,8978929,1443.9027193555044,7.634576966686464,TESSy COVID-19
Austria,AT,2020-W43,national,AT,Austria,18262,158997,8978929,1770.7791207615073,11.485751303483713,TESSy COVID-19
Austria,AT,2020-W44,national,AT,Austria,31613,167926,8978929,1870.223052214802,18.825554113121257,TESSy COVID-19
Austria,AT,2020-W45,national,AT,Austria,44772,199567,8978929,2222.6147461462274,22.434570845881332,TESSy COVID-19
Austria,AT,2020-W46,national,AT,Austria,47837,215044,8978929,2394.9849698109874,22.245214932757946,TESSy COVID-19
...
```

Print the sum of all covid cases:

```
total = 0

f = open("covid-test-cases.csv","r")
lines = f.readlines()
f.close()

lines = lines[1:] # ignore the first line

for l in lines:
    s = l.split(",")
    if s[6] != "NA":
        total += int(s[6])

print(total)
```
