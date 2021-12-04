# | computer memory        |
# |........................|
# |....2 1 55..............|
# |....^.......2 2 55 55...|
# |....|.......^...........|
# +----+-------+-----------+
#      |       |
# x ---+       |
# y -----------+
#
# 55 is the ASCII for the number 7
# To compare two strings, first
# you compare their length, and
# if its the same, you compare
# character by character.

x = '7' # [@]
y = '77' # [@]

if x == y:
  print(x)
else:
  print(y)
