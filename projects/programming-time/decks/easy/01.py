# | computer memory      |
# |......................| 0  - 21
# |..1 3.................| 22 - 43
# |..^...................| 44 - 65
# '--+-------------------'
#    |  
# x -+
#
# the variable x is stored some-
# where in memory (addr 24), its
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
