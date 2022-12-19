# returns new list, incrementing each
# element of the old one, e.g.:
#   [1,1,3,2,1]
# returns:
#   [2,2,4,3,2]
def increment(x):
    r = []
    for v in x:
        r.append(v + 1)

    return r


print(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
