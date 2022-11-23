// cube each number in the list
//   [1,2,3]
// returns:
//   [1,8,27]
function cube(x) {
    r = []
    for (let v of x) {
        r.push(v * v * v)
    }

    return r
}

console.log(JSON.stringify(cube([1,1,2,3,3,4,1,2,7,1])))
