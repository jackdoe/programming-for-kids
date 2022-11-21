function uniq(x) {
    let r = []
    for (let v of x) {
        let seen = false
        for (let v1 of r) {
            if (v == v1) {
                seen = true
            }
        }
        if (!seen) {
            r.push(v)
        }
    }
    return r
}

console.log(uniq([1, 2, 1, 1, 1, 3, 1]))
