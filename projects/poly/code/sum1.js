// sum all the integers from a list
//   [1,2,3]
// returns:
//   6
function sum(x) {
    let s = 0
    for (let v of x) {
        s += v
    }

    return s
}

console.log(JSON.stringify(sum([1,1,2,3,3,4,1,2,7,1])))
