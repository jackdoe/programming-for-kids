function rld(x) {
    let r = []
    for (let i=0; i<x.length; i+=2) {
        for (let j = 0; j < x[i]; j++) {
            r.push(x[i+1])
        }
    }
    return r
}

console.log(rld([2,2,1,3,6,7]))
