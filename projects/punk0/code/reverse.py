# reverse the input list
#   [1,2,3,4]
# returns:
#   [4,3,2,1]
def reverse(x):
    r = []
    i = 0
    for v in x:
        v = x[len(x) - 1 - i]
        r.append(v)
        i += 1

    return r


print(reverse([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
