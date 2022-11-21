def rle(x):
  r = []
  for v in x:
    if len(r) == 0 or r[-1] != v:
      r.append(0)
      r.append(v)
    r[-2] += 1

  return r


print(rle([2,2,2,2,2,2,2]))
