// return a list of N numbers
// with values from 1 to n
// e.g
//   explode(10)
// returns:
//   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
function explode(n) {
    r = []
    for (let i = 1; i <= n; i++) {
        r.push(i)
    }

    return r
}

console.log(JSON.stringify(explode(11)))
