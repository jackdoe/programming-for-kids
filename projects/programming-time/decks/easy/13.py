# | computer memory          |
# |..........................|
# |....2 1 ?.................|
# |....^.......2 3 49 49 49..|
# |....|.......^.............|
# +----+-------+-------------+
#      |       |
# x ---+       | NB: ? is 96+⚂
# y -----------+
#
# To compare two strings, first you
# compare their length, and if its
# the same, you compare character by
# character.  In this case, it won't
# even compare the characters,
# because the length is not the
# same.

x = chr(96+⚂)
y = '111'
if x == y:
  print(x)
else:
  print(y)
