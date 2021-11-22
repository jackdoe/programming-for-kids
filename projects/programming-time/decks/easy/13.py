# | computer memory        |
# |........................|
# |....2 1 55..............|
# |....^.......2 2 55 55...|
# |....|.......^...........|
# +----+-------+-----------+
#      |       |
# a ---+       |
# b -----------+
#
# 55 is the ASCII for the number 7
# To compare two strings, first
# you compare their length, and
# if its the same, you compare
# character by character.

a = '7'
b = '77'

if a == b:
  print(a)
else:
  print(b)
