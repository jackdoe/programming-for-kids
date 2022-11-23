# RunLength Encode a list of numbers
# in the format count, value:
# e.g.
#   [1,1,1,1,1,1,3,3]
# returns:
#   [6,1,2,3]
def rle(x):
  r = []

  for v in x:
    if len(r) == 0 or r[-1] != v:
      r.append(0)
      r.append(v)

    r[-2] += 1

  return r


print(rle([1,1,2,3,3,4,1,2,7,1]))
