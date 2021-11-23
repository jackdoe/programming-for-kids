# | computer memory      |
# |..1 0.................| 0  - 20
# |..^..........3 0 3 1..| 21 - 41
# |..|....1 0...^........| 42 - 62
# |..|....^.....|........| 63 - 83
# |..|....|.....|........| 84 -104
# '--+----+-----+--------'
#    |    |     |
#    |    |     |  
# i -+    |     |  i:   addr 2
# sum ----+     |  sum: addr 50
# n ------------+  n:   addr 36
#
# range(start, stop, step) makes
# a sequence of numbers. e.g.
# range(0,3, 1) is sequence
# from 0 to 3 with step 1
# it stops before reaching the
# end so it will stop at 2.

sum = 0
n = range(0, 3, 1)
for i in n:
  sum += 0
  
print(sum)
