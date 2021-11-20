# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# ...

sum = 0

for i in range(10):
  if i % 2 == 1:
    sum += 1

print(sum)
