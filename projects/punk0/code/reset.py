# create a new list
# with the value 1,2,3,4
# (ignores the input)
# returns:
#   [1,2,3,4]
def reset(x):
    r = []
    # start from 1, upto but not
    # including 5
    for i in range(1, 5):
        r.append(i)

    return r


print(reset([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
