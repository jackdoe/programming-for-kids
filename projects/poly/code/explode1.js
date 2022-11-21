function explode(n) {
    n = parseInt(n)
    r = []
    for (let i = 1; i < n+1; i++) {
        r.push(i)
        r.push(i)
    }
    return r
}

console.log(explode(10))
