# | computer memory |
# |.................|
# |....2 1 49..1 1..|
# |....^.......^....|
# |....|.......|....|
# +----+------+----+
#      |       |
# a ---+       |
# b -----------+
#
# 49 is the ASCII for the number 1
# (50 is for 2 and 51 is for 3..)
# But when you compare string to
# number in python, it will not
# compare 49 to 1, it will just
# say 'string' is not the same
# as number, so they cant be
# equal.

a = '1'
b = 1

if a == b:
  print(7)
else:
  print(3)

