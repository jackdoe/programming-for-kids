# return a list of n times
# the number n + 1
# e.g
#   explode(5)
# returns:
#   [6, 6, 6, 6, 6]
def explode(n):
    r = []
    for i in range(n):
        r.append(n + 1)

    return r


print(explode(11))
