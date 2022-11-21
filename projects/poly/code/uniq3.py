def uniq(x):
    r = []

    x.sort()
    
    for v in x:
        l = len(r)
        if l == 0 or r[l-1] != v:
            r.append(v)

    return r

print(uniq([1, 2, 1, 1, 1, 3, 1]))

