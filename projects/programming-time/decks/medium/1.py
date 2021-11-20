def min(a):
  if len(a) == 0:
    return None

  s = a[0]
  for n in a:
    if n < s:
      s = n
  return s

print(min([3,2,4,3]))
