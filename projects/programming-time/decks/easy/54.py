class Rect:
  def __init__(self, x, y, w, h):
    self.x = x # topleft X
    self.y = y # topleft Y
    self.w = w # width
    self.h = h # height

  # Check if a point is contained in
  # the rect.
  # See if the x is bettween left
  # most and right of the rect, and
  # if y is between top and bottom.
  def contains(self, x, y):
    x_left = self.x
    x_right = self.x + self.w
    y_top = self.y
    y_bottom = self.y - self.h
    if x > x_left and x < x_right:
      if y > y_bottom and y < y_top:
        return True
    return False    

box = Rect(10,10,5,8)

pos_x = ⚂
pos_y = ⚂

if box.contains(pos_x, pos_y):
  print('inside')
else:
  print('outside')
