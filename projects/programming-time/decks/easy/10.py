# return a random number between 1
# and 20
def random():
  dice = ⚂
  return dice

sum = 0
max = 0
n = 3
for i in range(n):
  value = random()
  sum += value
  if value > max:
    max = value

# the average of a series of items
# is the sum divided by the count
avg = sum / n

print(max - avg)
