# remove the all occurences of the
# smallest integer in the list
#   [1,2,3,2,3,1]
# returns:
#   [2,3,2,3]
def unmin(x):
    m = min(x)

    r = []
    for v in x:
        if v != m:
            r.append(v)

    return r


print(unmin([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
