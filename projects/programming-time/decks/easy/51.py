# | computer memory      |
# |..1 0.................| 0  - 21
# |..^..........3 0 20 1.| 22 - 43
# |..|....1 18..^........| 44 - 65
# |..|....^.....|........| 65 - 87
# |..|....|.....|........| 88 -109
# '--+----+-----+--------'
#    |    |     |
#    |    |     |  
# i -+    |     |         i: addr 2
# 18 -----+     |        18: addr 51
# range(20) ----+ range(20): addr 35
#
# How does 'range(20)' know when its
# done? The range object has some
# memory to keep its current number.
# In our case on address 36.
# So it can just keep updating it
# until it reaches the stop value.
# Another way to write it:
#   n = 0
#   stop = 20
#   while n < stop:
#     if n > 18:
#       print(n)
#     n += 1
for i in range(20):
  if i > 18:
    print(i)
