// return a list of N numbers
// with values from 2 to n*2
// e.g
//   explode(10)
// returns:
//   [2,4,6,8,10,12,14,16,18,20]
function explode(n) {
    r = []
    for (let i = 1; i <= n; i++) {
        r.push(i*2)
    }

    return r
}

console.log(JSON.stringify(explode(11)))
