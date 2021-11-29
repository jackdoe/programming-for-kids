# The area of rectangle is its width
# times its height.
# For example:
#
#        ######
#   3    ######
# height ######
#          6
#        width
#
# so the amount of area the rectangle
# occupies its 3 rows 6 pieces each,
# so 6 + 6 + 6, or 3 * 6

def area(width, height):
  a = width * height
  return a

rect_width = 3
rect_height = 6

r = area(rect_width, rect_height)

print(r)
