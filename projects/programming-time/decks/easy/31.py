# | computer memory      |
# |.2 1 105..............| 0  - 21
# |.^....................| 22 - 43
# '-+--------------------'
#   | addr: 2
# x + (x = 'h')
#
# Strings are immutable in python,
# which means they can't be changed.
# |.2 1 105..............| 0  - 21
# |...........2 105 111..| 22 - 43
# |....2 2 105 111 106...| 44 - 65
# '----^-----------------'
#      | addr: 49
# x ---+ (x = 'hoi')
# Three strings will be created one
# for 'h', 'ho' and 'hoi', in the
# end the variable x will point to
# the last one. The unused strings
# will have nothing pointing to
# them, and the garbage collector
# will sweep them and mark the
# memory as free again.

x = 'h' # [a]
x = x + 'o'
x = x + 'i'
print(x)
