# Basic division:
# We start subtracting 'b' from 'a'
# until 'a' becomes smaller than 0
# then we calculate the remainder
def divide(a,b):
  reminder = 0
  multiple = 0

  while a > 0:
    a -= b
    if a < 0:
      # we need to calculate
      # the remainder now,
      # try it on paper with 4/3
      reminder = b+a
    else:
      multiple += 1

  return [multiple, reminder]

# or simply reminder = 4 % 3
#           multiple = int(4/3)
pizza = ⚂
pieces = ⚂
m,rem = divide(pizza,pieces) 
print(rem)
