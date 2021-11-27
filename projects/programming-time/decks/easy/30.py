# | computer memory      |
# |.4 1 50...............| 0  - 21
# |.^...v................| 22 - 43
# |.|...1 7.1 8..........| 44 - 65
# '-+-------^------------'
#   |       | 
# a +       |
# b --------+
#
# a.append(b) will add reference
# to b's value in the end of 'a'
# 
# |.4 2 50  54...........| 0  - 21
# |.^...v...v............| 22 - 43
# |.|...1 7.1 8..........| 44 - 65
# '-+-------^------------'
#   |       | 
# a +       |
# b --------+

a = [7]
b = 8

a.append(b)

print(a[1])