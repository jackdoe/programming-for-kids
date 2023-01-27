// rotate the input list to the left
//   [1,2,3,4]
// returns:
//   [2,3,4,1]
function rotate_left(x) {
  let r = [];

  for (let i = 0; i < x.length; i++) {
    // go to the second element
    // then wrap around
    // example if x.len is 4:
    // (0 + 1) % 4 = 1
    // (1 + 1) % 4 = 2
    // (2 + 1) % 4 = 3
    // (3 + 1) % 4 = 0
    let len = x.length;
    let idx = (i + 1) % len;
    let v = x[idx];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(rotate_left([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
