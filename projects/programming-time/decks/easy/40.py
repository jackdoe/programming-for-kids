# you can have multiline strings
# in python with """ instead of "
#
# '\n' is the new line character.
# so you can split by it.

a = """hello
this
is
a
multiline
string
"""

lines = a.split('\n')
print(len(lines))
