# You can break out of a while
# loop, whenever you want.
# You can also break out of for
# loops.

a = ⚂
b = ⚂
while True:
  if b > a:
    break

  b += 1
  
for i in range(1000):
  if a > b:
    break

  a += 1

print(a + b)
