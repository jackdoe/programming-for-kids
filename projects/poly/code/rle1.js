// RunLength Encode a list of numbers
// in the format count, value:
// e.g.
//   [1,1,1,1,1,1,3,3]
// returns:
//   [6,1,2,3]
function rle(x) {
    let r = []
    for (let v of x) {
        let l = r.length
        if (l == 0 || r[l-1] != v) {
            r.push(0)
            r.push(v)
        }

        r[r.length-2] += 1
    }
    return r
}

console.log(JSON.stringify(rle([1,1,2,3,3,4,1,2,7,1])))
