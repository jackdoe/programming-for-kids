# | computer memory          |
# |..........................|
# |....3 1 2 66..............|
# |....^.....v...............|
# |....|.....|...............|
# |....|......`-> 2 104 105..|
# |....|.....................|
# '----+---------------------'
#      |
# a ---+
#
# lists are just sequence of
# items, some can be inline
# and some can point to other
# places in memory

a = [1,2,'hi']

# print the first element from 'a'
print(a[0])
