# | computer memory      |
# |...2 2 104 105........| 0  - 21
# |...^..................| 22 - 43
# |...|..................| 44 - 66
# '---+------------------'
#     |   
# x --+ addr: 3
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

x = 'hi' # [a]
print(x)

# this is not exactly the memory
# layout in python, but its close
