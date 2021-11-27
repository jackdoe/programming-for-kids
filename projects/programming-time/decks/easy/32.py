# to see if something is contained
# in a list, we go over each
# element in the list, and see if
# its equal to the element we are
# looking for.
# pretty similar to how you would
# find needle in a haystack.
def contains(haystack, needle):
  for x in haystack:
    if x == needle:
      return True

  return false

a = [7,2,5,8]
b = 5

# or just use 'if b in a' 
if contains(a, b):
  print(b)
else:
  print(b * b)

