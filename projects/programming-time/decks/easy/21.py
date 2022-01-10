# Delta encoding is a way to store a
# sequence by storing the
# differences between the elements.
# For example [1,2,3,5] can be
# represented as [1,2-1,3-2,5-3] or
# [1,1,1,2].
def delta(x):
  result = [x[0]]

  # start from 1 because we already
  # have x[0] in the output
  for i in range(1,len(x)):
    current = x[i]
    prev = x[i-1]
    d = current - prev
    result.append(d)

  return result

a = [1, 2, 3, 4, 5, 6, ⚂ % 10]
encoded = delta(a)

print(encoded)

# python has built-in `sum` function
# that sums the integers from a list
avg = sum(encoded) / len(encoded)
print(avg)
