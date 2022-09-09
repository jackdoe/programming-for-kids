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
