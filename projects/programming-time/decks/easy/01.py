# | computer memory |
# |.................|
# |....1 2..........|
# |....^............|
# '----+------------'
#      | 
# x ---+ 
#
# the variable x is stored some-
# where in memory, its type (1 for
# integer) and value (2)

x = 2

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
