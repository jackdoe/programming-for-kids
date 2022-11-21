def uniq(x):
   r = []
    for v in x:
        seen = False
        for v1 in r:
            if v == v1:
                seen = True

        if not seen:
            r.append(v)
    return r

print(uniq([1, 2, 1, 1, 1, 3, 1]))
