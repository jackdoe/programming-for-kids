def explode(n):
    n = int(n)
    r = []
    for i in range(1,n+1):
        r.append(i)
        r.append(i)

    return r


print(explode(10))
