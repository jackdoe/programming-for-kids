# return a list of N numbers
# with values from 1 to n/2
# e.g
#   explode(10)
# returns:
#   [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
def explode(n):
    r = []

    for i in range(1,n+1):
        v = int((i+1)/2)
        r.append(v)

    return r


print(explode(10))
