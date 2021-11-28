# | computer memory             |
# |.............................|
# |..1 6........................|
# |..^..........................|
# '--+--------------------------'
#    |
# x -+
#
# The global keyword allows the
# hello() function to access
# the same variable as defined
# outside.

def hello():
  global x
  x = 3

x = 6
hello()

print(x)
