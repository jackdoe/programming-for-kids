cards = []


cards.append([2, """
def min(a):
  if len(a) == 0:
    return None

  s = a[0]
  for n in a:
    if n < s:
      s = n
  return s

print(min([3,2,4,3]))
"""])

cards.append([2, """
def max(a):
  if len(a) == 0:
    return None

  m = a[0]
  for n in a:
    if n > m:
      m = n
  return m

print(max([1,2,4,3]))
"""])


cards.append([2, """
def avg(a):
  sum = 0
  for n in a:
    sum += n
  return sum/len(a)

print(avg([2,2,4,4]))
"""])

cards.append([2, """
x = 0

for i in range(2):
  for j in range(3):
    x += 1

print(x)
"""])


cards.append([2, """
# sometimes things 
# are not as they seem

def sum(a,b):
  return a * b

x = sum(1,2)

print(sum(x, sum(2,3)))
"""])

cards.append([2, """
# 1 + 2 = 3
# 3 + 3 = 6
# ...

sum = 0

for i in range(5):
  sum += i

print(sum)
"""])


cards.append([2, """
a = [1,2,0,1]
sum = 0

for n in a:
  sum += n

print(sum)
"""])

cards.append([2, """
a = [6,-2,-1,1]
sum = 0

for n in a:
  sum += n

print(sum)
"""])

cards.append([2, """
a = [1,2,3]
r = 0

for n in a:
  r *= n

print(r)
"""])


cards.append([2, """
a = ['7','8','9']
x = ''

for c in a:
  x += c

print(x)
"""])

cards.append([2, """
a = ['8','9']
x = '7'

for c in a:
  x += c

print(x)
"""])


cards.append([2, """
a = ['2','1','1']
x = a.pop()

for c in a:
  x += c

print(len(x))
"""])

cards.append([2, """
# ' '.join([1,2,3])
#   -> "1 2 3"

a = ['7','8','9']

print(''.join(a))
"""])

cards.append([2, """
# you can index into
# a string, just as
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

a = "hello world"

print(ord(a[7]))
"""])

cards.append([2, """
# time.time() gives
# the amount of seconds
# since midnight 1st of
# Jan 1970 in Greenwich.
# 
# e.g. at the time this
# card is made:
# 1635787548.417151

import time

now = time.time()
print(str(now)[0])
"""])

cards.append([2, """
# int('2') makes the 
# string 2 to the 
# integer 2

a = '1'
b = 2
c = 3

r = 0
for i in range(c):
  r += int(a) + b

print(r)
"""])


cards.append([2, """
# you can index into
# a string, just as 
# lists
#
# s = "abc"
# s[0] is 'a'
# s[1] is 'b'
# s[2] is 'c'

a = 'hello world'

m = 0

for i in range(len(a)):
  if a[i] == 'o':
    m += 1

print(m)
"""])


cards.append([2, """
a = "world"
b = ['h','e','llo']

print(len(a[0] + b[2]))
"""])

cards.append([2, """
def mul(a,b):
  r = 0
  for i in range(b):
    r += a
  return r

print(mul(2,3))
"""])

cards.append([2, """
i = 0
while 1 == 1:
  i += 1
  if i > 5:
    break

print(i)
"""])


cards.append([2, """
i = 0
while 1 == 1:
  i += 1
  if i > 5:
    break
print(i)
"""])

cards.append([2, """
a = [4,5,6]
b = [1,2,3]
c = [*a, *b]

print(len(c))
"""])

cards.append([2, """
a = []
a.append(1)
a.append(2)

b = a.pop()

print(b)
"""])

cards.append([2, """
b = '4321'
a = [b[0],b[1],b[2],b[3]]

print(a[3])
"""])

cards.append([2, """
a = []
while True:
  a.append(1)
  if len(a) > 5:
    break

print(len(a))
"""])

cards.append([2, """
a = "h2llo"
b = 3

a += str(b)

print(a[len(a)-1])
"""])

cards.append([2, """
phones = {
    "Jack": 5551212,
    "John": 5556622,
    "Jill": 555621
}

s = phones["Jack"]
print(str(s)[0])
"""])

cards.append([3, """
a = [ord('c'),
   -ord('b'),
   ord('a')]

r = ord('d')

for c in a:
  r -= c

print(r)
"""])