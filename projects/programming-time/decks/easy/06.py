# | computer memory      |
# |......................| 0  - 21
# |...2 1 ⚂..............| 22 - 43
# |...^......1 ⚂.........| 44 - 65
# |...|......^...........| 66 - 87
# '---+------+-----------'
#     |      |
# x --+      |   x addr: 25
# y ---------+   y addr: 54
#
# 49 is the ASCII for the number 1
# (50 is for 2 and 51 is for 3..)
# If we have the string '2' and the
# number 50, python will not compare
# the ascii code 50 to the number
# 50, it will just say type 'string'
# is not the same as type integer ,
# so they cant be equal.

x = '⚂'
y = ⚂

if x == y:
  print('seven')
else:
  print(7)
