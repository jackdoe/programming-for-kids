# take a list of numbers
# and return an average
# floored, e.g:
#   [1,2]
# returns:
#   1
def avg(x):
    s = sum(x)
    l = len(x)

    return int(s/l)

print(avg([1,1,2,3,3,4,1,2,7,1]))

