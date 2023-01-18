// the player can specify a different
// value when they play the card, can be
// zero, it must not be negative
const ROT = 1

// rotate the input list to the left ROT
// steps, e.g. if ROT = 1
//   [1,2,3,4]
// returns:
//   [2,3,4,1]
function rotate_left(x) {
  let r = [];

  for (let i = 0; i < x.length; i++) {
    // go to the ROT element then wrap
    // around example if x.len is 4 and
    // ROT is 1:
    // (0 + 1) % 4 = 1
    // (1 + 1) % 4 = 2
    // (2 + 1) % 4 = 3
    // (3 + 1) % 4 = 0
    let idx = (i + ROT) % x.length;
    let v = x[idx];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(rotate_left([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
