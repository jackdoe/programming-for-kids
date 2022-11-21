function uniq(x) {
    let r = []
    let seen = {}
    for (let v of x) {
        if (!seen[v]) {
            r.push(v)
            seen[v] = true
        }
    }
    return r
}

console.log(uniq([1, 2, 1, 1, 1, 3, 1]))
