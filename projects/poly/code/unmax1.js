function unmax(x) {
    max = 0;
    for (let v of x) {
        if (v > max) {
            max = v;
        }
    }

    let r = []

    for (let v of x) {
        if (v != max) {
            r.push(v)
        }
    }

    return r
}

console.log(unmax([1, 2, 1, 1, 1, 3, 1]))
