function avg(x) {
    let sum = 0
    for (let v of x) {
        sum += v
    }
    return sum / x.length
}

console.log(avg([1, 2, 1, 1, 1, 3, 1]))
