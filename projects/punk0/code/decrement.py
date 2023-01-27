# the player can specify
# which index to decrement
DEC_INDEX = 0
 
# decrement the DEC_INDEX of a list,
# e.g. if DEC_INDEX is set to 0:
#   [1,2,3,4]
# returns:
#   [0,2,3,4]
def decrement(x):
    r = []

    for i in range(len(x)):
        v = x[i]
        if i == DEC_INDEX:
            v -= 1
        r.append(v)

    return r


print(decrement([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
