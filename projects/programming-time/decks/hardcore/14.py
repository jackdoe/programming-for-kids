def delta(x):
  o = [x[0]]
  l = len(x)

  for i in range(1,l):
    p=x[i]
    c=x[i-1]

    o.append(p-c)

  return o

a = [1, 2, 3, 4, 5 ,6]
print(delta(a)[3])
