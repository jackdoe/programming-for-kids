# Binary search is a way to search
# more efficienty a sorted list.
# Imagine the list [1,2,3,4,5,6] and
# you are looking for 5, you just
# check the middle element if it is
# bigger than 5 you search in the
# right half, if not you try the
# left part, and then the half of
# the half, and so on.
def search(data, key):
  start = 0
  end = len(data) - 1
  mid = 0
  while start <= end:
    mid = int((end + start) / 2)
    if data[mid] < key:
      # look in the right half
      start = mid + 1
    elif data[mid] > key:
      # look in the left half
      end = mid - 1
    else:
      return mid

  return  -1
a = [1,3,4,7,9,11,12,13,14,19,20]
idx = search(a, ⚂)
if idx == -1:
  print("not found")
else:
  print("found at:" + str(idx))
