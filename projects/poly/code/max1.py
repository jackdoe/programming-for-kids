# returns the biggest integer from a
# list, e.g.:
#   [1,2,3,2]
# returns:
#   3
def max(x):
    m = 0
    for v in x:
        if v > m:
            m = v

    return m

print(max([1,1,2,3,3,4,1,2,7,1]))
