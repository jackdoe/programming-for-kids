# | computer memory           |
# |...........................|
# |..1 4........3 0 3 1..1 3..|
# |..^......1 0.^....1 0.^....|
# '--+------^---+----^---|----'
#    |      |   |    |   |
# a -+      |   |    |   |
# b ---------------------| b and x
# r --------+   |    |   | are
# range(b) -----+    |   | pointing
# i -----------------+   | to the
# x ---------------------+ same
#                          memory
# 
# When you pass parameters to a
# function, they are just like
# normal variables
def multiply(a,b):
  r = 0
  for i in range(a):
    r += b
  return r

x = ⚂
# or simply result = 4 * 3
result = multiply(4,x)

print(result)
