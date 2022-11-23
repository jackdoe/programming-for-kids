// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
function uniq(x) {
    let r = []
    for (let v of x) {
        let seen = false
        for (let v1 of r) {
            if (v == v1) {
                seen = true
            }
        }

        if (!seen) {
            r.push(v)
        }
    }

    return r
}

console.log(JSON.stringify(uniq([1,1,2,3,3,4,1,2,7,1])))
