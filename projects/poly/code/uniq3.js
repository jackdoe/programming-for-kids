// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
function uniq(x) {
    // WARNING: modifies the original list
    x.sort()

    let r = []
    for (let v of x) {
        let l = r.length
        if (l == 0 || r[l-1] != v)
            r.push(v)
    }

    return r
}

console.log(JSON.stringify(uniq([1,1,2,3,3,4,1,2,7,1])))
