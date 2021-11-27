# | computer memory      |
# |......................| 0  - 21
# |....2 1 55............| 22 - 43
# |....^......1 55.......| 44 - 65
# |....|......^.,,.......| 66 - 87
# '----+------+----------'
#      |      |
# a ---+      |  a addr: 26
# b ----------+  b addr: 54
#
# 49 is the ASCII for the number 1
# (50 is for 2 and 51 is for 3..)
# But when you compare string to
# number in python, it will not
# compare 55 to 55, it will first
# compare the types, and in this
# case it will see that string is
# not equal to integer, even though
# the ASCII for '7' is 55

a = '7'
b = 55

if a == b:
  print('fifty five')
else:
  print(7)