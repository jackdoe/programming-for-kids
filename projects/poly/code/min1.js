// returns the smallest integer from a
// list, e.g.:
//   [1,2,3,2]
// returns:
//   1
function max(x) {
    m = 2147483647;
    for (let v of x) {
        if (v < m) {
            m = v;
        }
    }

    return m;
}

console.log(JSON.stringify(max([1,1,2,3,3,4,1,2,7,1])))
