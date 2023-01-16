# decrement the first of a list
#   [1,2,3,4]
# returns:
#   [0,2,3,4]
def decrement(x):
    r = []

    for i in range(len(x)):
        v = x[i]
        if i == 0:
            v--
        r.append(v)

    return r


print(decrement([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
