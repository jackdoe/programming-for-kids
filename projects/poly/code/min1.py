# returns the smallest integer from a
# list, e.g.:
#   [1,2,3,2]
# returns:
#   1
def min(x):
    m = 2147483647
    for v in x:
        if v < m:
            m = v

    return m

print(min([1,1,2,3,3,4,1,2,7,1]))
