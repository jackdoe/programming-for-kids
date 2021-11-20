def avg(a):
  sum = 0
  for n in a:
    sum += n
  return sum/len(a)

print(avg([2,2,4,4]))
