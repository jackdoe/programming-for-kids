# | computer memory      |
# |.4 1 50...............| 0  - 21
# |.^...v................| 22 - 43
# |.|...1 1....1 ⚂.......| 44 - 65
# '-+----------^---------'
#   |          |
# odd          |
# x -----------+
#
# odd.append(x) will add reference
# to x's value in the end of 'odd'
# 
# |.4 2 50 56...........| 0  - 21
# |.^...v...\...........| 22 - 43
# |.|...1 1..`>1 ⚂......| 44 - 65
# '-+----------^--------'
#   |          | 
# odd          |
# x -----------+
# you see how odd[1] and the
# variable x point to the same place
odd = [1]
x = ⚂
if x % 2 == 0:
  x = x-1

odd.append(x)

print(odd[1])
