# rotate the input list to the right
#   [1,2,3,4,5]
# returns:
#   [5,1,2,3,4]
def rotate(x):
    r = []
    i = 0
    for v in x:
        # go to the last element and
        # then wrap around
        idx = (i + len(x) - 1) % len(x)
        v = x[idx]
        r.append(v)
        i += 1

    return r


print(rotate([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
