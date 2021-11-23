# You can break out of a while
# loop, whenever you want.
# You can also break out of for
# loops.

a = 5
while True:
  if True:
    break

  a += 1
  
for i in range(1000):
  if True:
    break
  a += 1  

print(a)
