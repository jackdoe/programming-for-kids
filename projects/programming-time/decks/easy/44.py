# | computer memory      |
# |....4 3 74 79 60......| 0  - 21
# |....^...|..\...v......| 22 - 43
# |....|...v...v...1 3...| 44 - 65
# |....|...1 1..1 2......| 66 - 87
# '----+-----------------'
#      |  b and a point to the same
#      |  place.
# a ---+    a addr: 4
# b ---+    b addr: 4
#
# when you set b[0] to 4, it will
# replace the value of the integer
# at address 74 with 4 instead of 1
# and since 'a' points to the same
# list as 'b', a[0] will be the same
# as b[0], which is the integer at
# address 74, and its value is 4

a = [1,2,3]
b = a

b[0] = 4

print(a[0])

