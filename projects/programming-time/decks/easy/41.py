# Compute Euler's number
# e = 1 + 1/1 + 1/2 + 1/(1*2*3) + …
def compute_e(end):
  e = f = 1.0
  for i in range(2, end):
    e += 1.0 / f
    f *= i # compute the factorial
           # incrementally
  return e

# Compute pi
# Leibniz's formula to compute pi
# pi = 4 – 4/3 + 4/5 – 4/7 + 4/9 – …
def compute_pi(end):
  pi = 0
  n = 4
  d = 1
  for i in range(1,end):
    # alternate between -1 and 1
    # (2 * (0 % 2)) - 1 = -1
    # (2 * (1 % 2)) - 1 = 1
    # (2 * (2 % 2)) - 1 = -1
    # (2 * (3 % 2)) - 1 = 1
    sign = (2*(i % 2)) - 1
    pi += sign * n/d
    d += 2
  return pi

e = compute_e(7 + ⚂ % 3)
pi = compute_pi(11 + ⚂ % 3)
print(e,pi)
