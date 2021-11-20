# | computer memory |
# |.................|
# |....1 0..........|
# |....^............|
# +----+------------+
#      |
#      |
# a ---+
# 
# a = a + 1 means the computer
# has to read the current value
# of 'a', add 1 to it, and store
# it back to 'a'

a = 0

a = a + 1

a += 1
# += is shortcut for a = a + 1

print(a)
