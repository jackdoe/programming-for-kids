function rle(x) {
    let r = []
    for (let v of x) {
        // use tmp var because
        // of card space
        let l = r.length
        if (l == 0 || r[l-1] != v) {
            r.push(0)
            r.push(v)
        }
        // fetch length again
        // because of push
        r[r.length-2] += 1
    }
    return r
}

console.log(rle([2,2,2,2,3,3,3,1]))
