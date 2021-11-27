# | computer memory      |
# |.2 1 105..............| 0  - 21
# |.^....................| 22 - 43
# '-+--------------------'
#   | addr: 2
# a + (a = 'h')
#
# Strings are immutable in python,
# which means they can't be changed.
#     (a = a + 'i')
# | computer memory      |
# |.2 1 105..............| 0  - 21
# |.........2 2 105 106..| 22 - 43
# '---------^------------'
#           | addr: 31
# a --------+
#
# New string will be created for
# 'h' + 'i', and the variable 'a'
# will point to it.
# the old string will have nothing
# pointing to it, and the garbage
# collector will sweep it and mark
# the memory as free again.

a = 'h'
a = a + 'i'
print(a)
