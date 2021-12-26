# a list where we will keep all the
# rolls
rolls = []

# the modulo operator % gets the
# reminder of a division, 4 % 3
# means divide 4 by 3 and take the
# remainder, so 4%3 is 1, 15 % 4 is
# 3 as 4 fits 15 3 times until is
# 12, and 3 is left as remainder.
n = (⚂ % 4)
if n < 2:
  n = 2

# start from i = 0 up to, but
# excluding, n, increase `i` with 2
# at each step
for i in range(0, n, 2):
  # roll the dice every time
  rolls.append(⚂)

# sort the list in ascending order
# that means [3,1,2,5] will become
# [1,2,3,5]
rolls.sort()

# print the element at index 0
print(rolls[0])
