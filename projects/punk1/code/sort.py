# sort the list in ascending order
#   [5,1,4,2,3]
# returns:
#   [1,2,3,4,5]
def sort(x):
    r = []
    for v in x:
        r.append(v)

    r.sort()

    return r


print(sort([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
