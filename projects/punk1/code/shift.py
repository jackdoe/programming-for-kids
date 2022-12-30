# shift to the input list to the left,
# adding 1 at the end:
#   [1,2,3,4,5]
# returns:
#   [2,3,4,5,1]
def shift(x):
    r = []
    for i in range(1, len(x)):
        v = x[i]
        r.append(v)

    r.append(1)
    return r


print(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
