# sum all the integers from a list
#   [1,2,3]
# returns:
#   6
def sum(x):
    s = 0
    for v in x:
        s += v

    return s

print(sum([1,1,2,3,3,4,1,2,7,1]))

