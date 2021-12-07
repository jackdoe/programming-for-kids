# | computer memory            |
# |............................|
# |..2 2 ⚂ ⚂.......1 ⚂.........|
# |..^.............^...........|
# +--+-------------|-----------+
#    |             |
# x -+             |
# y ---------------+
#
# x[0] gets the first character of
# the string pointed by the variable
# x
#
# ord('a') returns the ASCII code
# for the character a, which is 97

x = chr(96+⚂) + chr(96+⚂)
y = ord(x[0])

print(y)
