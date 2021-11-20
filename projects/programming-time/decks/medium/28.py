a = [ord('c'),
   -ord('b'),
   ord('a')]

r = ord('d')

for c in a:
  r -= c

print(r)
