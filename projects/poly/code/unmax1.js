// remove the all occurences of the
// largest integer in the list
//   [1,2,3,2,3,1]
// returns:
//   [1,2,2,1]
function unmax(x) {
    max = 0;
    for (let v of x) {
        if (v > max) {
            max = v;
        }
    }

    let r = []
    for (let v of x) {
        if (v != max) {
            r.push(v)
        }
    }

    return r
}

console.log(JSON.stringify(unmax([1,1,2,3,3,4,1,2,7,1])))
