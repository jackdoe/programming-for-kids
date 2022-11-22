import random

def explode(n):
    r = []

    for i in range(n):
        v = random.randint(0,20)
        r.append(v)

    return r


print(explode(10))
