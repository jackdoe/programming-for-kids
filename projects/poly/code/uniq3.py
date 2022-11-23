# deduplicate a list of integers
#   [1,1,3,2,1]
# returns:
#   [1,3,2]
def uniq(x):
    #WARNING: modifies the original list
    x.sort()

    r = []    
    for v in x:
        l = len(r)
        if l == 0 or r[l-1] != v:
            r.append(v)

    return r

print(uniq([1,1,2,3,3,4,1,2,7,1]))

