# run length encode a list of
# integers by recording how many
# times a number is repeated, e.g.:
# [1,1,1,1,1,1,1] can be encoded as
# [1,7] (or 1 appears 7 times)
# [1,1,1,1,1,1,1,2,2,2,2] can be
# reduced to [1,7,2,4]
def compress(x):
  o = [x[0],0]

  for n in x:
    prev = o[len(o)-2]

    # if the current number is same
    # as the previous, increment the
    # count
    if n == prev:
      o[len(o)-1]+=1
    else:
      # if its a new number add a
      # new entry to the output with
      # count 1
      o.append(n)
      o.append(1)

  return o

dice = 1 + (⚂ % 2)
a = [1,1,1,1,1,1,1,1,1,1,dice,3,3]
print(compress(a))
