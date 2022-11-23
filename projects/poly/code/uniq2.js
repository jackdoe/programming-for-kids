// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
function uniq(x) {
    let r = []
    let seen = {}
    for (let v of x) {
        if (!seen[v]) {
            r.push(v)
            seen[v] = true
        }
    }

    return r
}

console.log(JSON.stringify(uniq([1,1,2,3,3,4,1,2,7,1])))
