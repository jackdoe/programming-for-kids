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

x = 0 # [@]
y = 1 # [@]

a = x == y
b = x > y
c = x < y
# brackets are important, first
# evaluate a, if its true then
# evaluate (b or c), and both a
# and (b or c) has to be true.
if a and (b or c):
  print(x)
else:
  print(y)
