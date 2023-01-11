# rotate the input list to the right
#   [1,2,3,4]
# returns:
#   [4,3,2,1]
def rotate(x):
    r = []
    i = 0
    for v in x:
        # go to the last element and
        # then wrap around
        # example if len is 4:
        # (0 + 4 - 1) % 4 = 3
        # (1 + 4 - 1) % 4 = 0
        # (2 + 4 - 1) % 4 = 1
        # (3 + 4 - 1) % 4 = 2
        idx = (i + len(x) - 1) % len(x)
        v = x[idx]
        r.append(v)
        i += 1

    return r


print(rotate([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
