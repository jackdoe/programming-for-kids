# | computer memory             |
# |.............................|
# |..1 6........................|
# |..^..........................|
# '--+--------------------------'
#    |
# a -+
#
# The global keyword allows the
# hello() function to access
# the same variable as defined
# outside.

def hello():
  global a
  a = 3

a = 6
hello()

print(a)
