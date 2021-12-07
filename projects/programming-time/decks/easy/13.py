# | computer memory          |
# |..........................|
# |....2 1 ⚂.................|
# |....^.......2 3 49 49 49..|
# |....|.......^.............|
# +----+-------+-------------+
#      |       |
# x ---+       |
# y -----------+
#
# To compare two strings, first you
# compare their length, and if its
# the same, you compare character by
# character.  In this case, it wont
# even compare the characters,
# because the length is not the
# same.

x = '⚂'
y = '111'

if x == y:
  print(x)
else:
  print(y)
