# concatenate two strings
# into a result
def concat(a,b):
  result = ''

  for char in a:
    result += char

  for char in b:
    result += char

  return result

# chr(`x`) returns the ascii
# character for code `x`
#
# chr(97) returns 'a'
# chr(98) returns 'b'
# chr(99) returns 'c'
# ...
x = chr(96 + ⚂) + chr(96 + ⚂)
y = 'llo'

# in python you can also concatenate
# strings by doing `r = x + y`
r = concat(x,y)

print(r)
