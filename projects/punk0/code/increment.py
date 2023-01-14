# increment the elements of a list
# without mutating the original list
#   [1,2,3,4]
# returns:
#   [2,3,4,5]
def increment(x):
    r = []

    # algorithm:
    #   for each value of the input list
    #   add value+1 to the output list

    for v in x:
        r.append(v + 1)

    return r


print(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
