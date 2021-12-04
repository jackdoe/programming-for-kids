# | computer memory             |
# |.............................|
# |..2 1 49.....................|
# |..^..2 2 49 49 ..............|
# |..|..^.......................|
# |..|..|...2 3 49 49 49........|
# |..|..|...^...................|
# '--+--+---+-------------------'
#    |  |   |
# x -+  |   |
# y ----+   |
# z --------+
# w --------+ w and z point to same
#             place in memory
#
# Adding two strings makes another
# string. This is called:
# concatenating strings.
    
x = '1'
y = '11'
z = x + y
w = z
print(w)
