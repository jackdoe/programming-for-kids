# sums all integers from a list
def sum(data):
  r = 0
  for element in data:
    r += element
  return r

# average value means the sum of the
# elements divided by the amount of
# elements. avg([2,4,6]) means: (2 +
# 4 + 6) / 3 which is 4.  In your
# school class if you have 5
# children with ages [9,8,10,9,9],
# the average age is 9, you can
# check:
#   9 + 8 + 10 + 9 + 9 = 45
#   45 / 5 = 9
def avg(data):
  n = sum(data)
  # `len` is a builtin function
  # that python provides, that
  # returns the length of a list or
  # string, e.g. len([1,2]) is 2 and
  # len('abc') is 3
  l = len(data)

  # sum / amount of elements
  return n/l

average = avg([⚂,⚂,⚂])
print(average)
