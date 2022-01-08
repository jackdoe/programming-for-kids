# return the dice roll
def pick():
  return ⚂

a = [pick(), pick(), pick()]

# Sorting a list is quite common,
# the list object has a method
# `sort`, that sorts in-place, so it
# will just modify the list itself,
# without returning anything. This
# is called mutating, like the
# teenage mutant ninja turtles, they
# changed from turtles to ninja
# turtles, so they mutated.  After
# that the list will be sorted in
# ascending order (smaller numbers
# first).
a.sort()

# reverse() does what it says,
# inplace it will reverse the list,
# it takes first and last elements
# and swaps them, then the second
# and pre-last, and so on. Again
# mutating the list.
a.reverse()

print(a[0])
