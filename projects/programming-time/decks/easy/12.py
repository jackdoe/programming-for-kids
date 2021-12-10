# n = 3 will print this
# x
# xx
# xxx
# xx
# x

n = ⚂

# range(start, stop, step)
forward = range(1, n, 1)
for i in forward:
  # in python you can multiply
  # string by number
  # 'ab' * 4 -> 'abababab'
  # it just repeats the string
  # so 'x' * i, when `i` is 1 will
  # be just 'x' but when `i` is 2
  # it will be 'xx' ans so on.
  print('x' * i)

# range can also go backwards
# start at n, up to 0, adding -1 on
# every step
back = range(n, 0, -1)
for i in back:
  print('x' * i)
  
