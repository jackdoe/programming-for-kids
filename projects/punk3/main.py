import itertools
import inspect


def sort_asc(x):
    """
    return a sorted copy of the list
    in ascending order
    [2,1,4,3]
    [1,2,3,4]
    """

    # we can use the sorted() function
    # make a sorted copy or copy the
    # list and use the sort method on
    # the copy

    r = []

    # x.sort method mutates the list so
    # first we need to copy it
    for v in x:
        r.append(v)

    r.sort()

    return r

def sort_desc(x):
    """
    return a sorted copy of the list
    in descending order
    [2,1,4,3]
    [4,3,2,1]
    """

    # we can use the sorted() function
    # make a sorted copy or copy the
    # list and use the sort method on
    # the copy

    r = []
    # x.sort method mutates the list so
    # first we need to copy it
    for v in x:
        r.append(v)

    r.sort(reverse=True)

    return r

def reverse(x):
    """
    return a reversed copy the list
    [1,2,3,4]
    [4,3,2,1]
    """

    r = []
    i = 0
    for v in x:
        # last index - i
        v = x[len(x) - 1 - i]
        r.append(v)
        i += 1

    return r

def rotate(x):
    """
    return a rotated copy of the list
    [1,2,3,4]
    [4,1,2,3]
    """
    r = []
    i = 0
    for v in x:
        # go to the last element and
        # then wrap around
        idx = (i + len(x) - 1) % len(x)
        v = x[idx]
        r.append(v)
        i += 1

    return r

def swap_pairs(x):
    """
    return a copy of the list
    where each 2 elements are swapped
    [1,2,3,4]
    [2,1,4,3]
    """

    r = []
    # FIXME: it ignores the last element
    # if the list has odd number of
    # elements, so [1,2,3] -> [2,1]
    for i in range(0, len(x)-1, 2):
        r.append(x[i+1])
        r.append(x[i])
    return r


def swap_first_and_last(x):
    """
    return a copy of the list
    where the first and last
    elements are swapped
    [1,2,3,4]
    [4,2,3,1]
    """

    r = []
    for v in x:
        r.append(v)

    if len(r) < 2:
        return r

    tmp = r[0]
    r[0] = r[len(r)-1]
    r[len(r)-1] = tmp

    return r

CARD = 1

def card_meta(id, lang):
  color = 'black'
  bgcolor = 'white'
  theme = 'friendly'
#  color = '#ffcc00' # amber apple2
#  bgcolor = 'black'
#  theme='punk0'
  font='BlockZone'
  fontSize='25px'

  if lang == "c":
    color = '#ffcc00' # amber apple2
    bgcolor = '#000000'
    theme='gptamber'


  if lang == "go":
    color = '#0f0200' # green apple2
    bgcolor = '#ffffff'
    theme='gptwhite'


  if lang == "python":
    color = '#0f0200' # green apple2
    bgcolor = '#ffffff'
    theme='gptwhite'


  if lang == "javascript":
    color = '#fffdff'
    bgcolor = '#c40f42'
    theme="gptredzz" #next(possible["javascript"])
    
  return f"CARD:{id}:{lang}:{theme}:{bgcolor}:{color}:{color}:{font}:{fontSize}"
  
  
  
#color = '#ffb000' # amber
#color = '#33ff33' # green

#color = '#ffcc00' # amber apple2
#bgcolor = 'black'
#theme='doom-one2'
#

  
#color = '#ffcc00' # amber apple2
#bgcolor = 'black'
#theme='doom-one2'
  
def card_str(title, x, lang):
  global CARD
  print(card_meta(CARD,lang))

  CARD+=1

  n = int((32/2)) - int((len(x.split('\n'))) / 2)
  print(f"{title.center(40)}")
  print('\n' * (n-1), end='')
  print(x)
  print()




fn = ['sort_asc','sort_desc','reverse','rotate','swap_pairs', 'swap_first_and_last']

possible = {}
for r in range(1,len(fn)+1):
  for perm in itertools.permutations(fn,r):
      for rr in range(4,5):
          for inp in itertools.permutations([1,2,3,4],rr):
              x = list(inp)
              for f in perm:
                  x = eval(f + '(x)')
              k = f'{x}'
              if k in possible:
                  possible[k] += 1
              else:
                  possible[k] = 1
    
#          print(f"{list(inp)} -> {x}\t\t{perm}")



found = {}
for r in range(4,5):
  for p in itertools.permutations([1,2,3,4],r):
      x = f'{list(p)}'
      if x not in possible:
          print(f"{x} missing")
          pass
      else:
          found[x] = True
  

card_str('PUNK0',f"""
function cards in the middle

players play input and output cards so
program runs correctly

input, output in the middle

players are building a program to
produce this output given the input

""", '')


for i in range(4):
    card_str('sort_asc',inspect.getsource(sort_asc), 'python')
    card_str('sort_desc',inspect.getsource(sort_desc), 'python')
    card_str('reverse',inspect.getsource(reverse), 'python')
    card_str('rotate',inspect.getsource(rotate), 'python')
    card_str('swap_pairs',inspect.getsource(swap_pairs), 'python')
    card_str('swap_first_and_last',inspect.getsource(swap_first_and_last), 'python')


keys = []
for k in found:
    keys.append(eval(k))

keys.sort()
for k in keys:
    card_str('INPUT/OUTPUT',f"{k}".center(40),'')


while CARD <=55:
    card_str('INPUT/OUTPUT',f"[1, 2, 3, 4]".center(40),'')

#print(CARD)


