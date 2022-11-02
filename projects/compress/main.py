import inspect
import json

image = """.....................................................................................................................................................................................................................@@,,,,,,,,,@@........................@,,,,,,,,,,,,,,,,@.....................@,,,,,,,,,,,,,,,,,,,@..................(,,,,,,,,,,,*,,,,,,,,@...............@@,,,,,,,,,,,,@,,,,,,,,@,,&@..........@/,,,,,,,,,,,,,,,,,@@@@%,,,,,,,@........@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@.......@,,,,,,,,,,,@,,,,,,,,,,,,,,,,,,,@.......@,,,,,,,,,,,@,,,,,,,,,,,,,,,,,,@..........@,,,,,,,,@@,,,,,,,,,,,,,,,,@..............@@@@@@%,,,,,,,,,,,,,,,,,,,,@............@,,,,,,,,,,,,,,,,,,@&,,,,,,,@............@,,,,,,,,,,,,,,,@,,,,,,,,,,@..............@@,,,,,,,,,,,,@,,,,,,,,,@.....................%,,,,,,,,,@/,,@@@........................@,,,,,,,,,,,,,(...........................@,,,,,,,,,,@..............................@,,,,,,,@...............................@,,,,@@................................@@/................................................................................................................................................................................................................................................................."""


CARD = 1
def card(x):
  global CARD
  print(f"CARD:{CARD}")
  CARD+=1
  for i in range(len(x)):
    if i > 0 and i % 40 == 0:
      print('')

    if x[i] != '\n':
      print(x[i],end='')
  print()

def card_str(x):
  global CARD
  print(f"CARD:{CARD}")
  CARD+=1
  print(x)
  print()


def card_list(x, title):
  global CARD
  print(f"CARD:{CARD}")
  CARD+=1
  print(title.center(39))
  print()
  print(f"size: {len(x)}".center(39))
  print()
  for i,v in enumerate(x):
      if (i > 0 and i % 10 == 0):
          print('')

      print(f"{v:>3}", end=' ')


  print()

def card_json(x, title):
  global CARD
  print(f"CARD:{CARD}")
  CARD+=1
  print(title.center(39))
  print('')
  print(json.dumps(x, sort_keys=False, indent=4))

    
def encode(x):
  sym = {}
  r = []

  for v in x:
    if v not in sym:
      # first time we see a symbol
      # we put it in the dictionary
      sym[v] = len(sym)

    # append the number of the symbol
    r.append(sym[v])

  # return both the list and the table
  return [r, sym]

def decode(x, sym):
  # invert keys and values from
  #   { ".": 1, "@": 2}
  # to
  #   {1: ".", 2: "@"}
  rs = {sym[k] : k for k in sym}
  r = ''

  for v in x:
    # lookup symbol from number
    r += rs[v] 

  return r

def rle(x):
  r = []
  for v in x:
    if len(r) == 0 or r[-2] != v:
      r.append(v)
      r.append(0)
    if v == r[-2]:
      r[-1] += 1
  return r

def rld(x):
  r = []

  for i in range(0, len(x), 2):
    for k in range(x[i+1]):
      r.append(x[i])

  return r

def squeeze(x, n):
  r = []

  for i in range(0, len(x), n):
    avg = sum(x[i:i+n])/n
    r.append(int(avg))

  return r


def unsqueeze(x, n):
  r = []

  for v in x:
    for i in range(n):
      r.append(v)

  return r


def invert(x):
  # [1,1,3,0,0]
  # becomes
  # [2,2,0,3,3]
  r = []

  m = max(x)
  for v in x:
    r.append(m - v)

  return r
    
def bw(x):
  # make everything "black and white"
  # [2,7,0,0] -> [1,1,0,0]
  r = []

  for v in x:
    if v == 0:
      r.append(0)
    else:
      r.append(1)

  return r


def blur(x):
  s = squeeze(x, 3)
  return unsqueeze(s,3)


def delta(x):
  r = [x[0]]

  for i in range(1, len(x)):
    current = x[i]
    prev = x[i-1]
    d = current - prev
    r.append(d)

  return r

def undelta(x):
  r = [x[0]]

  for i in range(1, len(x)):
    r.append(x[i] + r[-1])

  return r

import inspect

card_str(f"""{'COMPRESSION AND INFORMATION'.center(40)}
                                        
[color:red]                     &@%(*/%@#*         [/color]
[color:red]             .#.,(,@,,,,,,,,,,/&*(.     [/color]
[color:red]           (,&,*,,@,,,,,*&,,,,,,,,*%&(  [/color]
[color:red]          //%,,,,,*@*,,,*%(*,,,,,,,,,*@/[/color]
[color:red]       ..(@@/,,,,,,,,,//,,,,,,,,,,,,,*/&[/color]
[color:red]&#, #*&#,,,,,,,,,,,,,,,,,,,,,(&&%,,,,,,@[/color]
[color:red]&@**,,,,,,,,*,,,,,,,,,,,,,,,%/,,,,,,,*#,[/color]
[color:red] %&#*,,,,,((,**,%*,,,,,,,,,,#(*,,,,,,@,.[/color]
[color:red]   &&&,,,,@,,,,,,,,,,,,,,,,,,,/@@@&,#   [/color]
[color:red]      /&&&*@*,,,,,,,@#*,,,,,,/&/        [/color]
[color:red]           *,(&@@#*# #,*##( **          [/color]
                                        

The original Akatsuki cloud represented
justice and fairness. Later however it
began to represent the rain of blood
that fell in Amegakure during its wars.

This game is a game of information.

How can we represent information as
compact as possible.

What is the smallest amount of symbols
we need in order to still think of
Akatsiku when we see the image?

""")

card_str(f"""{'GAME RULES'.center(40)}

This game is more of a puzzle, you can
play it alone, or with friends, but
remember to start with the easy and
obvious cards.

Remember that it is actually very
difficult to do what you are about to
do, so do not get discouraged. 


> 1. WATCH NARUTO IF YOU HAVENT

> 2. PICK AN IMAGE CARD

> 3. FIND THE ENCODING CARD
     MATCHING THE OUTPUT IMAGE

> 4. IF YOU ARE HAVING FUN GOTO 2

> 5. WATCH Hunter x Hunter or One Piece

""")

card_str(f"""{'WHAT IS AN IMAGE'.center(40)}

Images are just an array of pixels, a
pixel is just a dot of color, your
monitor probably has more than 2,073,600
pixels.

Each pixel has 3 one byte numbers:

    red: from 0 to 255
    green: from 0 to 255
    blue: from 0 to 255

For example, we could have 2 pixel image

[
   [255,0,0],
   [0,0,255]
]

In this game we will use text symbols to
represent pixels, but the idea is the
same. Each card has 40 columns and 31
rows, so we can use symbols to represent
1240 pixels.

Like this tree:
  *
 ***
*****
  |

""")



card_str(f"""{'ENCODE AND DECODE'.center(40)}

First we will transform our text image
into something we can use, like a list
of numbers. We will encode each symbol
from the image with a number, and we
will create a symbol table so we can use
it to decode the image later. 
For example, having this 7x8 image:
                .......
                ...*...
                ..***..
                .*****.
                ...|...
                .......
The first symbol we see is [color:red].[/color], we 
will give it the number 0, next is
[color:red]*[/color], so this will be number 1, and then
last we see [color:red]|[/color], which will be number 2

Our symbol table will look like this:

        {"{'[color:red].[/color]': 0, '[color:red]*[/color]': 1, '[color:red]|[/color]': 2}"}

and our encoded image would look like:
                0000000
                0001000
                0011100
                0111110
                0002000
                0000000
""")

card_str(f"""{'ENCODE AND DECODE'.center(40)}

{inspect.getsource(encode)}
{inspect.getsource(decode)}
""")


card_str(f"""{'RUNLENGTH ENCODING'.center(40)}
Lets flatten this image to how it
actually looks as a list of numbers:
                0000000
                0001000
                0011100
                0111110
                0002000
                0000000
becomes:
[
  [color:red]0,0,0,0,0,0,0,0,0,0[/color],[color:blue]1[/color],[color:magenta]0,0,0,0,0[/color],[color:green]1,1,1[/color],
  [color:maroon]0,0,0[/color],[color:purple]1,1,1,1,1[/color],[color:pink]0,0,0,0[/color],[color:orange]2[/color],[color:royalblue]0,0,0,0,0,0,[/color]
  [color:royalblue]0,0,0,0[/color]
]

There is [color:red]a lot[/color] of repetition in this
list, so we can just write how many
times each number appears in the
sequence:

[
  [color:red]0,10[/color],[color:blue]1,1[/color],[color:magenta]0,5[/color],[color:green]1,3[/color],[color:maroon]0,3[/color],[color:purple]1,5[/color],[color:pink]0,4[/color],[color:orange]2,1[/color],[color:royalblue]0,10[/color]
]

meaning, [color:red]0 repeats 10 times[/color], [color:blue]then 1 [/color]
[color:blue]repeats 1 time[/color], and again [color:magenta]0 repeating[/color]
[color:magenta]5 times[/color].. etc

This is called RunLength Encoding. To
decode simply do the reverse operation.
""")


card_str(f"""{'RUNLENGTH ENCODING'.center(40)}

# run length encode a list of numbers
# from:
#   [1,1,1,1,1,1,1,2] 
# to:
#   [1,7,2,1]

{inspect.getsource(rle)}
# run length decode
# from:
#   [1,7,2,1]
# to:
#   [1,1,1,1,1,1,1,2]
{inspect.getsource(rld)}
""")

card_str(f"""{'DELTA ENCODING'.center(40)}
Lets look at a list of numbers:

[1, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

If we runlength encode this list it will
blow up, most elements appears only once
[
  1,1,3,2,4,1,5,1,6,1,7,1,8,1,9,1,
  10,1,11,1,12,1
]
However we can encode the difference
between each element, so 
[
  1, # first element is 1
  2, # 3 - 1
  0, # 3 - 3
  1, # 4 - 3
  ...
]
This is called delta encoding, we encode
the the difference (the delta).

So the list becomes very repetitive:
[1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Now we can runlength encode it:
[1, 1, 2, 1, 0, 1, 1, 9]
To go back to the original list first we
need to delta decode, and then to
runlength decode.
""")



card_str(f"""{'DELTA ENCODING'.center(40)}

# delta encode a list of numbers
# from:
#   [1,2,3,4,5]
# to:
#   [1,1,1,1,1]
{inspect.getsource(delta)}

# delta decode a list of numbers
# from:
#   [1,1,1,1,1]
# to:
#   [1,2,3,4,5]
{inspect.getsource(undelta)}

""")

card_str(f"""{'REDUCE INFORMATION'.center(40)}
Going back to our tree:

                .......
                ...*...
                ..***..
                .*****.
                ...|...
                .......

How would it look if we try to squeeze
it in fewer pixels? For example take
every 2 pixels and average them together
and then explode it back:

00 00 00 0    0 0 0 0    00 00 00 0
00 01 00 0    0 0 0 0    00 00 00 0
00 11 10 0    0 1 0 0    00 11 00 0
01 11 11 0    0 1 1 0    00 11 11 0
00 02 00 0    0 1 0 0    00 11 00 0
00 00 00 0    0 0 0 0    00 00 00 0

Then if we draw it again:
                .......
                .......
                ..**...
                ..****.
                ..**...
                .......
Its ugly, but it .. kind of looks like
the original tree :) if you squint
really hard.
""")



card_str(f"""{'REDUCE INFORMATION'.center(40)}

# average every n elements
# from:
#  [1,2,4,4,9,5] with n=2
# to:
#  [1,4,7]
{inspect.getsource(squeeze)}

# explode the elements
# from:
#   [1,4,7] with n=2
# to:
#   [1,1,4,4,7,7]
{inspect.getsource(unsqueeze)}

""")


card_str(f"""{'FILTERS'.center(40)}

You can do all kinds of manpulations
of the image data. 

An example is Black And White filter:

  for every pixel
     if the pixel is not zero
       set the pixel to WHITE
     else
       set the pixel to BLACK

Simple Blur filter:
  
  for every block of 8x8 pixels
    replace them with their
    average
     
Invert filter:
  for each pixel:
    set it to the opposite
    e.g. ORANGE <-> BLUE
         RED <-> GREEN
         WHITE <-> BLACK

In our example we use simplified
versions of those filters, but the
fundamental idea is the same.

Take the pixels and manipulate them.
""")


card_str(f"""{'FILTERS'.center(40)}

{inspect.getsource(blur)}
{inspect.getsource(invert)}
{inspect.getsource(bw)}
""")



encoded, sym = encode(image)

card(image)
card(encoded)
card_json(sym, "SYMBOL TABLE")
card_list(rle(encoded), 'rle(encoded)')

blurred = blur(encoded)

card(blurred)
card(decode(blurred, sym))

card_list(rle(blurred), 'rle(blur(encoded))')



for s in [5, 20, 40]:
    card_list(squeeze(encoded, s),f"squeeze(encoded,{s})")
    card_list(rle(squeeze(encoded, s)),f"rle(squeeze(encoded,{s}))")
    card_list(rle(bw(squeeze(encoded, s))),f"rle(bw(squeeze(encoded,{s})))")
    card(decode(unsqueeze(squeeze(encoded, s),s), sym))

for s in [5, 20, 40]:
    card_list(squeeze(blurred, s),f"squeeze(blur(encoded),{s})")
    card_list(rle(squeeze(blurred, s)),f"rle(squeeze(blur(encoded),{s}))")
    card_list(rle(delta(squeeze(blurred, s))),f"rle(delta(squeeze(blur(encoded)),{s}))")
    card(decode(unsqueeze(squeeze(blurred, s),s), sym))


black_and_white = bw(encoded)
card(black_and_white)
card(decode(black_and_white, sym))
card_list(rle(black_and_white), 'rle(bw(encoded))')

inv_black_and_white = invert(bw(encoded))
card(inv_black_and_white)
card(decode(inv_black_and_white, sym))
card_list(rle(inv_black_and_white), 'rle(invert(bw(encoded)))')


black_and_white_blur = bw(blurred)
card(black_and_white_blur)
card(decode(black_and_white_blur, sym))
card_list(rle(black_and_white_blur), 'rle(bw(blur(encoded)))')


card(invert(encoded))
card(decode(invert(encoded), sym))



#card_list(rle(delta(black_and_white)),f"rle(delta(bw(encoded)))")



#print(json.dumps(sym, sort_keys=False, indent=4))
