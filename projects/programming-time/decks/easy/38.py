#            ▲y        │x=5
#            │         │
#           6│    B    │     C
#           5│         │         y=4
#───────────4┼─────────P────────────
#           3│         │
#           2│    A    │     D
#           1│         │
#────────────┼─────────┼───────────▶
#           0│ 1 2 3 4 5 6 7 8 9   x
#            │         │
#            │         │

x0 = 5
y0 = 4

x,y = [⚂,⚂]

# assume dice can roll only > 0
if x == x0 and y == y0:
  print("P")
elif x < x0 and y < y0:
  print("A")
elif x < x0 and y > y0:
  print("B")
elif x > x0 and y > y0:
  print("C")
elif x > x0 and y < y0:
  print("D")
else:
  print("on a line")
