#                | y
#  y > 0   , - ~ | ~ - ,       y > 0
#  x < 0 '       |       ' ,   x > 0
#    ,           |           ,
#   ,     2      |    1       ,
#  ,             |             ,
#--|-------------|-------------|---
# -x             |             +x
#   ,     3      |    4       ,
#    ,           |           ,
#      ,         |        , '
#  y < 0 ` - , _ | _ ,  '
#  x < 0         |-y         y < 0
#                            x > 0
#
def quadrant(x,y):
  if y > 0 and x > 0:
    return 1
  elif y < 0 and x > 0:
    return 4
  elif y < 0 and x < 0:
    return 3
  elif y > 0 and x < 0:
    return 2
  else:      # origin
    return 0 # x = 0, y = 0

point_x = ⚂ - 10
point_y = ⚂ - 10

print(quadrant(point_x,point_y))
