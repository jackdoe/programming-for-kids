// the player can specify
// which index to decrement
const DEC_INDEX = 0

// decrement the DEC_INDEX of a list,
// e.g. if DEC_INDEX is set to 0:
//   [1,2,3,4]
// returns:
//   [0,2,3,4]
function decrement(x) {
  let r = [];

  for (let i = 0; i < x.length; i++) {
    let v = x[i]
    if (i == DEC_INDEX) {
      v--;
    }
    r.push(v);        
  }

  return r;
}

console.log(JSON.stringify(decrement([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
