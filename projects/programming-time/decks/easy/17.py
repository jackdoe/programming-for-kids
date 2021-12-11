# lists are just a ordered sequence
# of things, they can also contain
# other lists
image = [
  [1,0,0,0,1],
  [0,1,0,1,0],
  [0,0,1,0,0],
  [0,1,0,1,0],
  [1,0,0,0,1],
]

# height is the number of rows
height = len(image)
# we assume image is rectangle
width = len(image[0])

# image[0] returns a list, so
# image[0][1] will return the second
# element from the first row
image[⚂ % height][⚂ % width] = 2

for row in image:
  for pixel in row:
    if pixel == 0:
      print(' ', end='')
    elif pixel == 1:
      print('@', end='')
    else:
      print('#', end='')
  # print new line after every row
  print('')
