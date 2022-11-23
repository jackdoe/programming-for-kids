# cube each number in the list
#   [1,2,3]
# returns:
#   [1,8,27]
def cube(x):
    r = []
    for v in x:
        r.append(v * v * v)

    return r

print(cube([1,1,2,3,3,4,1,2,7,1]))
