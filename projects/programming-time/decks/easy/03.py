# | computer memory      |
# |....1 3....1 6........| 0  - 20
# |....^......^..........| 21 - 41
# |....|... ..|..........| 42 - 62
# |....|......|..........| 63 - 83
# '----+------+----------'
#      |      |
# a ---+      | a addr: 5
# b ----------+ b addr: 12
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
