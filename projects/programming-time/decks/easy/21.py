# | computer memory            |
# |............................|
# |..2 2 104 105...1 104.......|
# |..^.............^...........|
# +--+-------------|-----------+
#    |             |
# x--+             |
# b----------------+
#
# x[0] gets the first character
# of the string pointed by the
# variable x
#
# ord('a') returns the ASCII code
# for a, which is 97

x = 'hi'
b = ord(x[0])

print(b)
