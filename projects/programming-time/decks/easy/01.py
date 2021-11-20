# | computer memory |
# |                 |
# |    0            |
# |    |            |
# '----+------------'
#      | 
# x ---+ 
#
# the variable x is stored some-
# where in memory.

x = 0

# .--<-----<---<------<-.
# v         #           |
while True: #           ^
  if x > 2: #           |
    break   #--->-->----+. break
            #           | \ out
  x = x + 1 #           |  \ of
            #           |   v
  # >--->------->--->---'   ' the
  # go back to the start   / loop
  #                       /
#<-----<------<------<---'

print(x)
