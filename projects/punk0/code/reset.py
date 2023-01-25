# Note: the reset() card can be played
# on top of any card.

# create a new list
# returns:
#   [0,0,0,0]
def reset():
    r = []

    for i in range(4):
        r.append(0)

    return r


print(reset())
