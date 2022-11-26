# returns the first element from a list
# or 1 if the list is empty, e.g.:
#   [2,3,2]
# returns:
#   2
def first(x):
    f = 1
    if len(x) > 0:
        f = x[0]

    return f


print(first([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
