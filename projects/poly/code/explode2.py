# return a list of N numbers
# with values from 1 to n
# e.g
#   explode(10)
# returns:
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def explode(n):
    r = []
    for i in range(1,n+1):
        r.append(i)

    return r


print(explode(11))
