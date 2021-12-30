# A square root of a number is a
# value that, when multiplied by
# itself, gives the number. Example:
# 4*4 = 16, so a square root of 16
# is 4. Newton's method of finding
# the square root of x:
# root = (x + (n / x))/2 where x
# is any guess which can be assumed
# to be n or 1.
#
# We will run the algorithm 10 times
# to get good approximations
def sqrt(x):
  n = x
  for i in range(10):
    x = (x + (n / x))/2.0
  return x


squares = [100,1024,25,16,4,9]

x = squares[⚂ % len(squares)]
print(sqrt(x))
