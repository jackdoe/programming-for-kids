# | computer memory      |
# |....1 3....1 6........| 0  - 21
# |....^......^..........| 22 - 43
# |....|......|..........| 44 - 65
# |....|......|..........| 66 - 87
# '----+------+----------'
#      |      |
# a ---+      |  a addr: 5
# b ----------+  b addr: 12
#
# a's value is stored somewhere
# in computer's memory (RAM)
#
# you can read and write the value
# as many times as you want.
#

a = 3
b = 6

a = 2
a = 4
a = 2

print(1 + a + b)
