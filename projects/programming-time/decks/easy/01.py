# | computer memory      |
# |......................| 0  - 20
# |..1 3.................| 21 - 41
# |..^...................| 84 -104
# '--+-------------------'
#    |
# x -+ 
#
# the variable x is stored some-
# where in memory (addr 23), its
# type, 1 for integer, and value 3

x = 3
# .--<-----<-----<----<-.
# v         #           |
while True: #           ^
  if x > 4: #           |
    break   #--->-->----+. break
            #           | \ out
  x = x + 1 #           |  \ of
            #           |   v
  # >--->------->--->---'   ' the
  # go back to the start   / loop
  #                       /
#<-----<------<------<---'

print(x)
