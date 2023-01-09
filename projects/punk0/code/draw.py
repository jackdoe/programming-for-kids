# the next player draws list[0] cards
# and returns a copy of the list:
#   [1,2,3,4]
# returns
#   [1,2,3,4]
# prints:
#   draw 1 cards
def draw(x):
    n = 0

    if len(x) > 0:
        n = x[0]
        if n == 0:
            print('next player skips')
        else:
            print(f'draw {n} cards')

    r = []

    for v in x:
        r.append(v)

    return r


print(draw([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
