# returns new list, doubling each
# item, e.g.:
#   [1,2,3,4,5]
# returns:
#   [2,4,6,8,10]
def doubleList(x):
    r = []
    for v in x:
        r.append(v*2)

    return r


print(doubleList([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
