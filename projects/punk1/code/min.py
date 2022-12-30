# returns the biggest integer from a
# list, or 1 if the list is empty
# e.g.:
#   [1,2,3,2]
# returns:
#   3
def min(x):
    if len(x) == 0:
        return 1

    m = 2147483647
    for v in x:
        if v < m:
            m = v

    return m


print(min([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
