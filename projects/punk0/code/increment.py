# increment the elements of a list
#   [1,2,3,4,5]
# returns:
#   [2,3,4,5,6]
def increment(x):
    r = []
    for v in x:
        r.append(v + 1)

    return r


print(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
