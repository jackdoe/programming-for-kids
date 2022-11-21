function uniq(x) {
    let r = []
    x.sort()
    for (let v of x) {
        let l = r.length
        if (l == 0 || r[l-1] != v)
            r.push(v)
    }
    return r
}

console.log(uniq([2, 1, 2, 1, 1, 1, 3, 1]))
