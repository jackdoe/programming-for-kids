# the next player draws n % 5 cards
# where n is the first value from the
# list, and returns a reversed copy:
#   [7,2,3,4,5]
# returns
#   [5,4,3,2,7]
# prints:
#   draw 2 cards
def draw(x):
    n = 0

    if len(x) > 0:
        n = x[0] % 5

    print(f'draw {n} cards')

    r = []
    i = 0
    for v in x:
        v = x[len(x) - 1 - i]
        r.append(v)
        i += 1

    return r


print(draw([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
