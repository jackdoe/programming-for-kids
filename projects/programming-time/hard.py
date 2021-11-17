cards = []

cards.append("""
# ASCII:
#  a -> 97
#  b -> 98
#  ...
#  z -> 122

a = 'acd'
sum = 0

for c in a:
  sum += ord(c)

print(sum % 100)
""")

cards.append("""
a = [1,2,3]
b = [3,4,5]

i = 0
for x in a:
  b[i] = x
  i += 1

print(b[2])
""")

cards.append("""
# ASCII
#  0 -> 48
#  1 -> 49
#  ...
#  9 -> 57
#  ...

b = ['9','3']
f = ['3','4']
l = ''

for i in b:
  l += i
for i in f:
  l += i

print(ord(l[3]) -
    ord(l[1]))
""")



cards.append("""
# You can override
# keys in dictionaries

a = ['1','1','1','2']
b = {}
for x in a:
  b[x] = True

r = ''
for k in b:
  r += k

print(r)
""")


cards.append("""
# you can index into
# a string, just as 
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

# Split a string into
# a list of strings:
# "a b".split(" ")
# makes ["a","b"]

a = "hello world"
b = a.split(" ")

print(ord(b[1][1]))
""")

cards.append("""
memory = []
for i in range(10000):
  memory.append(0)

memory[800] = 3
memory[801] = 97
memory[802] = 98
memory[803] = 99
memory[804] = 48

def show(m, addr):
  l = m[addr]
  for i in range(l):
    c = m[addr+i+1]
    print(chr(c))

show(memory, 800)
""")



cards.append("""
class Point:
  x = 0
  y = 0

a = Point()
a.x = 5
a.y = 10

b = Point()
b.x = 3
b.y = 1

print(a.x - b.x + b.y)
""")

cards.append("""
class Actor:
  x = 0
  y = 0

player = Actor()

def update():
  player.x += 1
  player.y += 1

def draw():
  print(player.x)
  print(player.y)

while True:
  update()
  draw()

  break
""")

cards.append("""
# ASCII
#  0 -> 48
#  1 -> 49
#  ...

b = ['1','3']

r = ord(b[1])-ord(b[0])

print(r)
""")

cards.append("""
# Dictionary keys
# can be integers as 
# well

b = {}
b[1] = 5
b[2] = 6
x = 0
for k in b:
  x += k

print(x)
""")


cards.append("""
def fib(n):
  if n <= 1:
    return n
  else:
    a = fib(n-1)
    b = fib(n-2)
    return(a + b)

print(fib(5))
""")


cards.append("""
def compress(x):
  o = [x[0],0]

  for n in x:
    p = o[len(o)-2]

    if n == p:
      o[len(o)-1]+=1
    else:
      o.append(n)
      o.append(1)

  return o

a = [1,1,1,1,2,3,3,3,3]
print(compress(a)[1])
""")


cards.append("""
def decompress(x):
  o = []
  l = len(x)
  for i in range(0,l,2):
    n = x[i+1]

    for k in range(n):
      o.append(x[i])

  return o

a = [1, 4, 2, 1, 3, 4]
print(decompress(a)[2])
""")


cards.append("""
def delta(x):
  o = [x[0]]
  l = len(x)

  for i in range(1,l):
    p=x[i]
    c=x[i-1]

    o.append(p-c)

  return o

a = [1, 2, 3, 4, 5 ,6]
print(delta(a)[3])
""")


cards.append("""
def is_prime(n):
  if n == 0 or n == 1:
    return False
  for x in range(2,n):
    if n%x == 0:
      return False

  return True

if is_prime(9):
    print(1)
elif is_prime(7):
    print(2)
else:
    print(3)
""")


cards.append("""
# series converge to pi
# pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 ...
k = 1
s = 0
for i in range(1000):
  if i % 2 == 0:
    s += 4/k
  else:
    s -= 4/k
  k += 2
   
print(int(s))
""")