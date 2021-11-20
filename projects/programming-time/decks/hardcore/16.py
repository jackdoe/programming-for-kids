# series converge to pi
# pi = 4 - 4/3 + 4/5 - 4/7 + 4/9 ...
k = 1
s = 0
for i in range(1000):
  if i % 2 == 0:
    s += 4/k
  else:
    s -= 4/k
  k += 2
   
print(int(s))
