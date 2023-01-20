# returns a copy of the list and print
# what happens next:
#   [1,2,3,4]
# returns
#   [1,2,3,4]
def punk3(x):
    if len(x) >= 3:
        n = x[3]
        if n == 0:
            print('next player skips')
        elif n < 0:
            print(f'play {-n} cards')
        else:
            print(f'draw {n} cards')

    r = []
    for v in x:
        r.append(v)

    return r


print(punk3([1, 1, 2, 3, 3, 4, 1, 2, 7, 1]))
