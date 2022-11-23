# remove the all occurences of the
# largest integer in the list
#   [1,2,3,2,3,1]
# returns:
#   [1,2,2,1]
def unmax(x):
    m = max(x) 

    r = []
    for v in x:
        if v != m:
            r.append(v)

    return r

print(unmax([1,1,2,3,3,4,1,2,7,1]))
