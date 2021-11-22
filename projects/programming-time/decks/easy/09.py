# | computer memory    |
# |....................|
# |....1 4... 5 1......|
# |....^......^........|
# '----+------+--------'
#      |      |
# a ---+      |
# b ----------+
#
# What is the value of 'a == 0'?
# It is either True or False,
# depending of the value of 'a',
# 4 == 4 is True, and 4 == 3 is
# False. True is stored as 1 in
# the memory, False is 0. This is
# called a boolean value, we also
# need to store its type(5).

a = 4
b = a == 4

if b:
  print('a is four')
else:
  print('a is not four')

