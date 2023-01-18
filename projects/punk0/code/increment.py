# the player can specify
# which index to decrement
INC_INDEX = 0

# increment the INC_INDEX of a list,
# e.g. if INC_INDEX is set to 0:
#   [1,2,3,4]
# returns:
#   [2,2,3,4]
def increment(x):
    r = []

    for i in range(len(x)):
        v = x[i]
        if i == INC_INDEX:
            v += 1
        r.append(v)

    return r


print(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
