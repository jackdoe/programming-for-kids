# | computer memory |
# |.................|
# |....1 0..........|
# |....^............|
# +----+------------+
#      |
#      |
# x ---+
# 
# x = x + 1 means the computer has
# to read the current value of x,
# add 1 to it, and store it back to
# x's location in memory

x = 0

x = x + 1

# += is shortcut for x = x + 1
x += 1

print(x)
