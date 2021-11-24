# | computer memory      |
# |......................| 0  - 21
# |.............1 6......| 22 - 43
# |....1 2......^........| 44 - 65
# |....^........|........| 66 - 87
# '----+--------+--------'
#      |        |
#  a --+        |  a addr: 48
#  b -----------+  b addr: 35
#
# What does it mean for 'a' to be
# equal to 'b'?
#
# It means the value in memory
# where 'a' points to, is equal
# to the value where b points to
# the computer (CPU) itself has an
# instruction to compare two
# integers.

a = 2
b = 6

if a == b:
  print(a + b)
else:
  print(a * b)
