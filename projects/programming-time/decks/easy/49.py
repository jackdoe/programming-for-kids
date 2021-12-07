# | computer memory      |
# |......................| 0  - 21
# |......................| 22 - 43
# |......................| 44 - 65
# |......................| 66 - 87
# |....2 1 194 174.......| 88 -109
# |....^.................| 110-131
# '----+-----------------'
#      |
# b----+   b addr: 92
#
# UTF8:
# it is a very simple format, the
# first byte dictates how long is
# the sequence of bytes for one
# character.
# 
# first byte:
#  > 240  4 bytes sequence
#  > 224  3 bytes sequence
#  > 192  2 bytes sequence
#  < 128  1 byte (ASCII fits here)
# even though ® is 2 bytes in memory
# its length is 1

b = '®'
print(len(b) * ⚂)
