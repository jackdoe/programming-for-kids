# a - b
# subtract 1 from a b times
def subtract(a,b):
  while b > 0:
    a -= 1
    b -= 1
  return a

# a//b
# divide without reminder (floor)
# how many times you can subtract b
# from a?
def divide(a,b):
  n = 0
  while a > 0:
    a = subtract(a,b)
    n += 1
  return n

# math.log(a,b)
# logarighm of a with base b
# how many times you can divide a by
# b?
def log(a,b):
  n = 0
  while a > 1:
    a = divide(a,b)
    n += 1
  return n
base = [2,4,32][⚂ % 3]
print(log(1024,base))
