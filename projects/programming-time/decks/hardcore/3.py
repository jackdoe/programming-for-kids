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
