# a+b
# add 1 to a, b times
def add(a,b):
  while b > 0:
    a += 1
    b -= 1
  return a

# a*b
# add a to a, b times
def multiply(a,b):
  r = 0
  while b > 0:
    r = add(r,a)
    b -= 1
  return r

# a**b
# a to the power of b
# multiply a by a, b times
def pow(a,b):
  r = 1 # a**0 is 1
  while b > 0:
    r = multiply(r,a)
    b -= 1
  return r

x = 1 + ⚂
y = ⚂ % 5
xy = pow(x,y)
print(xy)
