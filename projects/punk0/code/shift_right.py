# shift to the input list to the left,
# adding 0 at the end:
#   [1,2,3,4]
# returns:
#   [2,3,4,0]
def shift_right(x):
    r = []

    # start with a zero
    r.append(0)

    # copy everything except the last
    # element
    for i in range(0, len(x)-1):
        v = x[i]
        r.append(v)

    return r


print(shift_right([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
