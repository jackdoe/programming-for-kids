def uniq(x):
    r = []
    seen = {}
    
    for v in x:
        if v not in seen:
            r.append(v)
            seen[v] = True
    return r

print(uniq([1, 2, 1, 1, 1, 3, 1]))

