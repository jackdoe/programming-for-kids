# | computer memory  |
# |..................|
# |....2 1 98........|
# |....^.............|
# |....|.............|
# +----+-------------+
#      |
# x ---+
#
# 98 is the ASCII for the letter
# 'b', len(string) returns the
# length of the string. So the
# computer will go to the memory
# where the variable x points, and
# skip the type(2 for string) slot
# and return the length stored next
# to it(1).

x = 'b'

print(len(x))
