# | computer memory      |
# |....1 3....1 6........| 0  - 21
# |....^......^..........| 22 - 43
# |....|......|..........| 44 - 65
# |....|......|..........| 66 - 87
# '----+------+----------'
#      |      |
# x ---+      |  x addr: 5
# y ----------+  y addr: 12
#
# x's value is stored somewhere in
# computer's memory (RAM), same as
# y's value.
#
# You can read and write the value
# as many times as you want. It will
# keep overwriting the memory at
# address 5.
x = 3
y = 6

x = 2
x = 4
x = 2

print(1 + x + y)
