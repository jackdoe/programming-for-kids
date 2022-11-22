function rand(max) {
    let r = Math.random() * (max-1)
    return Math.floor(r);
}

function explode(n) {
    r = []

    for (let i = 0; i < n; i++) {
        r.push(rand(20))
    }

    return r
}

console.log(explode(10))
