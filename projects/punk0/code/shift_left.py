# shift the input list to the left,
# adding 0 at the end:
#   [1,2,3,4]
# returns:
#   [2,3,4,0]
def shift_left(x):
    r = []

    # copy everything after the first
    # element
    for i in range(1, len(x)):
        v = x[i]
        r.append(v)

    # append 0 to the end
    r.append(0)
    return r


print(shift_left([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
