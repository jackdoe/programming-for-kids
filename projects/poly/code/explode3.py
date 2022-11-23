# return a list of N numbers
# with values from 2 to n*2
# e.g
#   explode(10)
# returns:
#   [2,4,6,8,10,12,14,16,18,20]
def explode(n):
    r = []
    for i in range(1,n+1):
        r.append(i*2)

    return r


print(explode(11))
