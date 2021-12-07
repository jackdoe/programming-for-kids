# a.pop() removes the last element
# from the list and returns it to
# the caller.
#
# a = [1,2,3]
# b = a.pop()
# 
# 'a' will become [1,2]
# and 'b' will be 3
#
# pop() also takes an argument where you can specify which index to remove
# e.g.
# a = [1,2,3]
# b = a.pop(1)
# a.pop(1) will remove index 1, so
# 'a' will become [1,3], and 'b'
# will be 2

dice_rolls = [
  ⚂,
  ⚂,
  ⚂,
]

roll3 = dice_rolls.pop()
roll2 = dice_rolls.pop()
roll1 = dice_rolls.pop()

print(roll3 - roll1)
