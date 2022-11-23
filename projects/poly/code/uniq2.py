# deduplicate a list of integers
#   [1,1,3,2,1]
# returns:
#   [1,3,2]
def uniq(x):
    r = []
    seen = {}
    for v in x:
        if v not in seen:
            r.append(v)
            seen[v] = True

    return r

print(uniq([1,1,2,3,3,4,1,2,7,1]))

