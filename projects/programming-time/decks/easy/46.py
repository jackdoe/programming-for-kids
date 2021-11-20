# | computer memory |
# |.................|
# |....0...1........|
# |....^...^........|
# +----+---+--------+
#      |   |
# a ---+   |
# b -------+
#
# What is 'a == 0'? Well == means
# compare, but what is the value
# of it? In python if comparison's
# value is True or False, so
# 1 == 1 is True, and 1 == 0 is
# False. True is usually stored
# as 1 in the memory. False is 0.
#
# if True/False:
#   ...

a = 0
b = a == 0
if b:
  a = 1

print(a)
