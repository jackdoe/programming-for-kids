# The Euclidean algorithm calculates
# the greatest common divisor (gcd)
# of two numbers a and b. The
# greatest common divisor g is the
# largest number that divides both a
# and b without leaving a remainder.
# If a = 12 and b = 8, then gcd(a,b)
# or gcd(12,8) is 4. This algorithm
# is more than 2300 years old,
# written by Euclid in year 300BC.
# If gcd(a,b) = 1, then a and b are
# considered relatively prime, even
# though a and b might not be
# prime. This is one of the most
# important algorithms today, and it
# is used in almost all internet
# communication.

def gcd(a, b):
  while b != 0:
    tmp = b
    b = a % b
    a = tmp
  return a


x = ⚂
y = ⚂

print(gcd(x,y))
