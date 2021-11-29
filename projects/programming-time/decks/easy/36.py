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

a = [1,2]
b = [3,4]

c = concat(a,b)

print(len(c))
