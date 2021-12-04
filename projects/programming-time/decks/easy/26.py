# | computer memory      |
# |....2 2 49............| 0  - 21
# |....^......1 2........| 22 - 43
# |....|......^ 1 1......| 44 - 65
# |....|......|.^...1 3..| 66 - 87
# '----+------+-+---^----'
#      |      | |   |
# a ---+      | |   |
# b ----------+ |   |
# int(a) -------+   |
# int(a) + b -------+ addr: 83
# print's param-----+ addr: 83
#
# Everything happens in memory.
# int(a) has to be computed, and
# placed somewhere in memory, then
# int(a)+b has to be computed and
# placed somewhere in memory and
# then print will get a paremeter
# pointing where the result of
# int(a)+b is stored.
#
# int('1') makes the string 1
# to the integer 1

a = '1'
b = 2
print(int(a) + b)
