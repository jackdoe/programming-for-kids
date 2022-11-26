# return a new list without the first
# element, e.g.:
#   [1,2,3,2,3,1]
# returns:
#   [2,3,2,3,1]
def rest(x):
    n = 0
    r = []
    for v in x:
        if n > 0:
            r.append(v)
        n += 1

    return r


print(rest([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
