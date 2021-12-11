# roll the dice `n` times, joining
# the characters into a string
def random_string(n):
  s = ''
  for i in range(n):
    dice = ⚂
    s += chr(96 + dice)

  return s

# To check if two strings are
# equal to each other, first check
# the length, and then check the
# characters at each position.
def equal(a,b):
  if len(a) != len(b):
    return False

  for i in range(len(a)):
    if a[i] != b[i]:
      return False

  return True

x = random_string(2)
y = random_string(2)
print(x + " " +  y)
# or just use x == y, which will do
# the same algorithm as our equal()
if equal(x,y):
    print(x+y)
