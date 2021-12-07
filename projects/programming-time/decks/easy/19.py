# | computer memory             |
# |.............................|
# |..1 ⚂........................|
# |..^..........................|
# '--+--------------------------'
#    |
# x -+
#
# The global keyword allows the
# hello() function to access
# the same variable as defined
# outside.
# So after the function runs, the
# value will change, because x is
# global.

def hello():
  global x
  x = 3

x = ⚂
hello()

print(x)
