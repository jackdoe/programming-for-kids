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
