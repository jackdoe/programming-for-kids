// the player can specify
// which index to decrement
const INC_INDEX = 0

// increment the INC_INDEX of a list,
// e.g. if INC_INDEX is set to 0:
//   [1,2,3,4]
// returns:
//   [2,2,3,4]
function increment(x) {
  let r = [];

  for (let i = 0; i < x.length; i++) {
    let v = x[i]
    if (i == INC_INDEX) {
      v++;
    }
    r.push(v);        
  }

  return r;
}

console.log(JSON.stringify(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
