# Prime numbers are numbers
# divisable without remainder only
# by themselves and one, to check
# the remainder use the modulo
# operator % e.g. 6 % 5 is 1
def is_prime(n):
  # 0 and 1 are not prime
  if n == 0 or n == 1:
    return False

  # check if the number is divisable
  # by any number from 2 to n
  for x in range(2,n):
    # if there is no reminder that
    # means it is divisable, and it
    # is not a prime
    if n % x == 0:
      return False

  return True

n = ⚂
if is_prime(n):
  print('prime')
else:
  print('not a prime')
