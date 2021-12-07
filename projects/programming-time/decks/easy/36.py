# Concatenate two lists into a new
# list is very similar to
# concatenating two strings.
#  * make a new list
#  * append elements from listA
#  * append elements from listB
# however you might also decide
# just to append all elements from
# listB into the back of listA
# this however will change listA
# and sometimes you don't want that.
def concat(listA, listB):
  r = []

  for element in listA:
    r.append(element)

  for element in listB:
    r.append(element)

  return r

a = [⚂,⚂]
b = [⚂,⚂]

ab = concat(a,b)

print(ab.pop(1) + ab.pop(1))
