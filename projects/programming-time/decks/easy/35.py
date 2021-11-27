# Destructuring (card 041) is very
# handy to also expand lists in
# for loops as well.
# In this case the inner list will
# be unpacked in the variables x
# and y

points = [[0,1],[1,2],[3,2]]

for x,y in points:
  if x == 3 and y == 2:
    print(x)

