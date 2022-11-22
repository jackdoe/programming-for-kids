// return a list of N numbers
// with values from 1 to n/2
// e.g
//   explode(10)
// returns:
//   [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
function explode(n) {
    r = []

    for (let i = 1; i <= n; i++) {
        let v = parseInt((i+1)/2)
        r.push(v)
    }

    return r
}

console.log(explode(10))
