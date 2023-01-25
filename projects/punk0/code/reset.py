# Note: the reset() card can be played
# on top of any card.

# create a new list with the value
# 0,0,0,0
# returns:
def reset():
    r = []

    for i in range(4):
        r.append(0)

    return r


print(reset())
