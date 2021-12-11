# The recipe or algorithm to
# concatenate two lists into a third
# one:
#  * make a new list
#  * append elements from listA
#  * append elements from listB
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

# [2,4,6].pop(1) removes the element
# at index 1 from the list and
# returns it, in this example it
# will return 4. And after that the
# list is modified to [2,6] and now
# 6 is at index 1
print(ab.pop(1) + ab.pop(1))
