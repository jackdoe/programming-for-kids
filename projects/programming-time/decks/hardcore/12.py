def compress(x):
  o = [x[0],0]

  for n in x:
    p = o[len(o)-2]

    if n == p:
      o[len(o)-1]+=1
    else:
      o.append(n)
      o.append(1)

  return o

a = [1,1,1,1,2,3,3,3,3]
print(compress(a)[1])
