# sort the list in descending order
#   [1,4,2,3]
# returns:
#   [4,3,2,1]
def sort_desc(x):
    # we can use the sorted() function
    # make a sorted copy

    # x.sort method mutates the list so
    # first we need to copy it and then
    # sort the copy
    r = []
    for v in x:
        r.append(v)

    r.sort(reverse=True)

    return r


print(sort_desc([1, 1, 2, 3, 3, 4, 1, 2, 7, 9]))
