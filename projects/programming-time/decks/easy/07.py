# | computer memory      |
# |......................| 0  - 21
# |.............1 6......| 22 - 43
# |....1 2......^........| 44 - 65
# |....^........|........| 66 - 87
# '----+--------+--------'
#      |        |
#  x --+        |  x addr: 48
#  y -----------+  y addr: 35
#
# What does it mean for x to be
# equal to y?
#
# It means the value in memory where
# x points to, is equal to the value
# where y points to. The computer
# (CPU) itself has an instruction to
# compare two integers.

x = 2 # [@]
y = 6 # [@]

if x == y:
  print(x + y)
else:
  print(x * y)
