def unmax(x):
    m = max(x)
    r = []
    for v in x:
        if v != m:
            r.append(v)

    return r

print(unmax([1,2,43,1,1,1,1]))
