# return a list of n numbers
# with values from 2 to n+1
# e.g
#   explode(10)
# returns:
#   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def explode(n):
    r = []
    for i in range(2, n + 2):
        r.append(i)

    return r


print(explode(11))
