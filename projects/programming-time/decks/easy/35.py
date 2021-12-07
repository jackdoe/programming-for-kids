# Destructuring (card 041) is very
# handy to also expand lists in for
# loops as well. In this case the
# inner list will be unpacked in the
# variables x and y.

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
