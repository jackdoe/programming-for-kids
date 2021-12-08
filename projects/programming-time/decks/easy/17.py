# | computer memory             |
# |.............................|
# |..2 1 ?......................|
# |..^..2 2 ? ?.................|
# |..|..^.......................|
# |..|..|...2 3 ? ? ?...........|
# |..|..|...^...................|
# '--+--+---+-------------------'
#    |  |   |
# x -+  |   | NB: ? is 96+⚂
# y ----+   |
# z --------+
# w --------+ w and z point to same
#             place in memory
#
# Adding two strings makes another
# string. This is called:
# concatenating strings.
    
x = chr(96+⚂)
y = chr(96+⚂) + chr(96+⚂)
z = x + y
w = z
print(w)
