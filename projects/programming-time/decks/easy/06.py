# | computer memory      |
# |......................| 0  - 21
# |...2 1 55.............| 22 - 43
# |...^......1 7.........| 44 - 65
# |...|......^.,,........| 66 - 87
# '---+------+-----------'
#     |      |
# a --+      |   a addr: 25
# b ---------+   b addr: 54
#
# 49 is the ASCII for the number 1
# (50 is for 2 and 51 is for 3..)
# But when you compare string to
# number in python, it will not
# compare 55 to 7, it will just
# say 'string' is not the same
# as number, so they cant be
# equal.

a = '7'
b = 7

if a == b:
  print('seven')
else:
  print(7)
