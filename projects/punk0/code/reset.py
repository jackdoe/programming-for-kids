# Note: the reset() card can always be
# played, on top of any language.

# create a new list with the value
# 0,0,0,0
# returns:
def reset():
    r = []

    for i in range(4):
        r.append(0)

    return r


print(reset())
