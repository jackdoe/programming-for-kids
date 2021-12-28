# To reverse a list you can make
# a new list with the elements
# inserted in the opposite order.
# 
# length starts from 1, e.g.
# a = [] has length of 0
# a = [9] has length of 1
# but the index starts from 0
# so a[0] is the first element
# of 'a' (9)
#
# in this small function we are
# getting the back element by doing
# x[length - 1] to get to the end
# index, and then subtract 'i' from
# it.
def reverse(x):
  le = len(x)
  result = []

  for i in range(le):
    element = x[le - 1 - i]
    result.append(element)
  return result

a = [⚂,⚂,⚂]    # another quick way
b = reverse(a) # to reverse a list
c = a[::-1]    # or string is to
print(b)       # use [::-1] negative
print(c)       # slice step
