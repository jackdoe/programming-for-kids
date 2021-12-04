# | computer memory  |
# |..................|
# |....2 1 55..1 55..|
# |....^.......^.....|
# |....|.......|.....|
# +----+-------+-----+
#      |       |
# x ---+       |
# y -----------+
#
# 55 is the ASCII for the number 7
# Even though the raw values are
# the same, the types are not, so
# python knows that '7' is not 55.
# To get the ASCII code of a
# character use ord(x), or if you
# want to go the other way around,
# use chr(y) to go from ASCII code
# to character.

x = '7' # [@]
y = 55  # [@]

if x == y:
  print('seven')
else:
  print(7)
