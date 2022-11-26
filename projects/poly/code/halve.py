# halve the input, rounded down,
# never reaching 0, e.g.:
#   5
# returns:
#   2
def halve(x):
    v = int(x / 2)
    if v < 1:
        v = 1

    return v


print(halve(5))
