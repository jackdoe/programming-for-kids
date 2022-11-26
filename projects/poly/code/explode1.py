# return a list of n numbers
# with decreasing values from 2 + n down
# e.g:
#   explode(10)
# returns:
#   [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def explode(n):
    r = []
    for i in range(n):
        r.append(2 + n - i)

    return r


print(explode(11))
