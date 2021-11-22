# | computer memory  |
# |..................|
# |....2 1 55..1 55..|
# |....^.......^.....|
# |....|.......|.....|
# +----+-------+-----+
#      |       |
# a ---+       |
# b -----------+
#
# 55 is the ASCII for the number 7
# Even though the raw values are
# the same, the types are not, so
# python knows that '7' is not 55.

a = '7'
b = 55

if a == b:
  print('seven')
else:
  print(7)
