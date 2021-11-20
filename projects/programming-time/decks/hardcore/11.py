def fib(n):
  if n <= 1:
    return n
  else:
    a = fib(n-1)
    b = fib(n-2)
    return(a + b)

print(fib(5))
