def is_prime(n):
  if n == 0 or n == 1:
    return False
  for x in range(2,n):
    if n%x == 0:
      return False

  return True

if is_prime(9):
    print(1)
elif is_prime(7):
    print(2)
else:
    print(3)
