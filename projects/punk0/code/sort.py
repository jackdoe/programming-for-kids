# return a sorted copy of the list
#   [1,1,3,2,1]
# returns:
#   [1,1,1,2,3]
def sort(x):
    r = []
    for v in x:
        r.append(v)

    r.sort()

    return r


print(sort([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
