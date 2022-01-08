# Prime number is a number that is
# divisible, without remainder, only
# by itself and 1 (e.g. 2, 3, 5, 7,
# 11). To check the remainder use
# the modulo operator %. For example
# 5 is a prime number:
#  5 % 1 is 0 (reminder of 5/1 is 0)
#  5 % 2 is 1 (reminder of 5/2 is 1)
#  5 % 3 is 2 (reminder of 5/3 is 2)
#  5 % 4 is 1 (reminder of 5/4 is 1)
#  5 % 5 is 0 (reminder of 5/5 is 0)
def is_prime(n):
  # 0 and 1 are not prime
  if n == 0 or n == 1:
    return False
  # check if the number is divisible
  # by any number from 2 to n
  for x in range(2,n):
    # if there is no reminder that
    # means it is divisible, and it
    # is not a prime
    if n % x == 0:
      return False
  return True

n = ⚂
if is_prime(n):
  print('prime')
else:
  print('not a prime')
