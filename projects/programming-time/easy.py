cards = []

cards.append("""
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

for i in range(3):
  if i % 2 == 1:
    print(i)
""")

cards.append("""
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

sum = 0

for i in range(10):
  if i % 2 == 1:
    sum += 1

print(sum)
""")

cards.append("""
a = {
  "x": 10,
  "y": 20,
  "z": 5
}

a["k"] = 8

print(a["x"] + a["k"])
""")

cards.append("""
i = 0
while i < 3:
  i += 1

print(i)
""")


cards.append("""
i = 0
while True:
  i += 1
  if i > 3:
    break
print(i)
""")


cards.append("""
a = 'hello world'

print(len(a))
""")


cards.append("""
a = 'hello world'
b = a[2:5]

print(len(b))
""")


cards.append("""
a = 'hello world'
b = a[:2]

print(len(b))
""")


cards.append("""
a = 'hello world'
b = a[0:2] + a[6:9]

print(len(b))
""")


cards.append("""
def hello():
  return 'world'

a = hello()

print(len(a))
""")


cards.append("""
def world():
  return 'world'

def hello():
  return 'hello'

a = hello() + world()

print(len(a))
""")


cards.append("""
a = 'hello world'
b = a[2:]

print(len(b))
""")



cards.append("""
# 
# len('abc') -> 3
#

b = 8

print(len('hi' * b))
""")

cards.append("""
a = '1'
b = '11'

print(a + b)
""")

cards.append("""
# ASCII
#  a -> 97
#  ...
#  o -> 111
#  ...

print(ord('q'))
""")

cards.append("""
# ASCII
#  a -> 97
#  ...
#  c -> 99
#  ...

print(ord(chr(111)))
""")

cards.append("""
print(5)
""")

cards.append("""
# ASCII
#  A -> '65'
#  B -> '66'
#  ..

b = ord('C') - 90

print(b)
""")


cards.append("""
sum = 0

for i in range(5):
  sum += i

print(sum)
""")

cards.append("""
a = '7'
b = '8'
c = '9'

print(a + b + c)
""")

cards.append("""
x = {
  'a': 'hello',
  'b': 'world'
}

r = x['a'] +  x['b'] 
print(len(r))
""")

cards.append("""
# str(1) makes the
# integer 1 to the 
# string 1

a = '1'
b = 2

print(a + str(b))
""")


cards.append("""
# int('2') makes the 
# string 2 to the 
# integer 2

a = '1'
b = 2

print(int(a) + b)
""")

cards.append("""
# 5 / 2 is 2
# and 1 remainder
#
# 7 / 2 is 3
# and 1 remainder
# 
# 11 / 4 is 2
# and 3 remainder
# 11 % 4 is 3

print(99 % 10)
""")


cards.append("""
while True:
  break

print(5)
""")

cards.append("""
a = '7798'
b = 2

if b > 2:
  b -= 1

print(a[b])
""")


cards.append("""
a = '7798'
b = 2

if b < 2 or b == 2:
  b -= 1

print(a[b])
""")


cards.append("""
a = '7798'
b = 2
c = 3
if b < 2 and c >= 3:
  b -= 1

print(a[b])
""")

cards.append("""
a = ['7',2,'5',9]
b = 2

b += 1

print(a[b])
""")

cards.append("""
a = ['7',2,'5',9]
a.pop()
a.pop()

print(a[len(a)-1])
""")

cards.append("""
b = '4321'

print(b[len(b) - 1])
""")

cards.append("""
x = [1,2,3,4]

print(x[len(x)-2])
""")


cards.append("""
x = [1,2,3,4]

print(x[3] - x[1])
""")

cards.append("""
x = 0
for i in range(len('a')):
  x += 11

print(x)
""")

cards.append("""
x = 0
while x < 10 or x < 5:
  x += 1

print(x)
""")


cards.append("""
text = "hello 1 2 3"
s = text.split(" ")

print(s[1])
""")

cards.append("""
a = \"""hello
this
is
a
multiline
string
\"""

lines = a.split('\\n')
print(len(lines))
""")


cards.append("""
a,b,c = [1,2,3]

print(c)
""")


cards.append("""
a,b,c = [1,2,3]

print(len(str(c)))
""")