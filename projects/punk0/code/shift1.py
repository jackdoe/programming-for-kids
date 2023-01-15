# shift the input list to the left,
# adding 0 at the end:
#   [1,2,3,4]
# returns:
#   [2,3,4,0]
def shift(x):
    # get a slice from the first element
    # onwards
    r = x[1:]

    # add 0 to the end
    r.append(0)
    
    return r


print(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
