def decompress(x):
  o = []
  l = len(x)
  for i in range(0,l,2):
    n = x[i+1]

    for k in range(n):
      o.append(x[i])

  return o

a = [1, 4, 2, 1, 3, 4]
print(decompress(a)[2])
