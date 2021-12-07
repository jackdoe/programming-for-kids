# | computer memory      |
# |...2 2 ⚂ ⚂............| 0  - 21
# |...^..................| 22 - 43
# |...|..................| 44 - 66
# '---+------------------'
#     |   
# x --+ addr: 3
#
# Strings are just a sequence
# of characters, but computers
# don't understand characters,
# so people came up with common
# way to put characters in memory
# we call it the ASCII standard:
#
# use ord('a') to get the ASCII of
# a character, and chr(97) to make
# a number into a character.
#
# ord('a')  -> 97
# chr(97)   -> 'a'
#
# We also store the length of the
# string and its type(2), so
# print() knows when to stop.

# for example x = '5' + chr(97+8)
x = '⚂' + chr(96 + ⚂)
print(x)
