# what do the symbols mean
#   == means 'is equal'
#   > means 'greater than'
#   < means 'less than'
# people get confused by < and > but
# its quite easy, imagine a
# crocodile: ..,---*< so < is its
# mouth, so you can see which number
# the crocodile will eat
# 3 ..,---*< 5 (3 is smaller than 5)
# 5 >*---,.. 3 (5 is bigger than 3)
# remember: the crocodile always
# eats the bigger number.

x = ⚂
y = ⚂

a = x == y
b = x > y
c = (x - 5) < y
# brackets are important, first
# evaluate a, if its false then
# evaluate (b and c)
if a or (b and c):
  print(x)
else:
  print(y)
