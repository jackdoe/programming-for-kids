# a,b = [1,2] is the same as a=1,b=2
# called Destructuring, it can be
# used in the for loop while
# destructuring each point, e.g. x,y
# in case of [1,6] will be x=1,y=6

points = [
  [1,6],
  [4,5],
  [8,17],
  [3,2],
  [12,14],
  [6,20],
  [1,11],
  [2,11],
  [19,6],
]

pos_x = ⚂
pos_y = ⚂
found = False
for x,y in points:
  if x == pos_x and y == pos_y:
    found = True

if found:
  print(str(pos_x)+' '+str(pos_y))
else:
  print('missing')
