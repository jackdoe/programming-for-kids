def max(a):
  if len(a) == 0:
    return None

  m = a[0]
  for n in a:
    if n > m:
      m = n
  return m

print(max([1,2,4,3]))
