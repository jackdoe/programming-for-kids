# | computer memory      |
# |...2 2 104 105........| 0  - 20
# |...^..................| 21 - 41
# |...|..................| 42 - 62
# '---+------------------'
#     |   
# a --+ addr: 3
#
# strings are just a sequence
# of characters, but computers
# don't understand characters,
# so people came up with common
# way to put characters in memory
# we call it the ASCII standard:
# a  -> 97
# ...
# h  -> 104
# ...
# we also store the length of the
# string and its type(2), so
# print() knows when to stop.

a = 'hi'
print(a)

# this is not exactly the memory
# layout in python, but its close
