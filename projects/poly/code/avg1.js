// take a list of numbers
// and return an average
// floored, e.g:
//   [1,2]
// returns:
//   1
function avg(x) {
    let sum = 0
    for (let v of x) {
        sum += v
    }

    return parseInt(sum / x.length)
}

console.log(JSON.stringify(avg([1,1,2,3,3,4,1,2,7,1])))
