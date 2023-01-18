# create a new list
# with the value 0,0,0,0
# returns:
#   [0,0,0,0]
def reset():
    r = []
    # start from 1, upto but not
    # including 5
    for i in range(1, 5):
        r.append(0)

    return r


print(reset())
