# rotate the input list to the left
#   [1,2,3,4]
# returns:
#   [2,3,4,1]
def rotate_left(x):
    r = []

    i = 0
    for v in x:
        # go to the second element
        # then wrap around
        # example if x.len is 4:
        # (0 + 1) % 4 = 1
        # (1 + 1) % 4 = 2
        # (2 + 1) % 4 = 3
        # (3 + 1) % 4 = 0
        idx = (i + 1) % len(x)
        v = x[idx]
        r.append(v)
        i += 1

    return r


print(rotate_left([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
