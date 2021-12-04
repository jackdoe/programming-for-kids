# | computer memory      |
# |.4 3 69 108 78........| 0  - 21
# |.^../...|...|.........| 22 - 43
# |.|.v....|...v.........| 44 - 65
# |.|.1 9..|...1 7.......| 66 - 87
# |.|......v.............| 88 -109
# |.|......2 2 104 105...| 110-131
# '-+--------------------'
#   |
# x-+  addr: 2
#
# Lists are just ordered sequence
# of items, each pointing to some
# location in memory.

x = [9,'hi',7] # [@],[@],[@]

# print the first element from the
# list
print(x[0])
