# | computer memory    |
# |....................|
# |....1 4... 5 1......|
# |....^......^........|
# '----+------+--------'
#      |      |
# x ---+      |
# y ----------+
#
# What is the value of 'x == 0'?
# It is either True or False,
# depending of the value of x,
# 4 == 4 is True, and 4 == 3 is
# False. True is stored as 1 in
# the memory, False is 0. This is
# called a boolean value, we also
# need to store its type(5).

x = 4 # [@]
y = x == 4

if y:
  print('x is four')
else:
  print('x is not four')

