// rotate the input list to the right
//   [1,2,3,4]
// returns:
//   [4,1,2,3]
function rotate_right(x) {
  let r = [];

  for (let i = 0; i < x.length; i++) {
    // go to the last element and
    // then wrap around
    // example if len is 4:
    // (0 + 4 - 1) % 4 = 3
    // (1 + 4 - 1) % 4 = 0
    // (2 + 4 - 1) % 4 = 1
    // (3 + 4 - 1) % 4 = 2
    let len = x.length;
    let idx = (i + len - 1) % len;
    let v = x[idx];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(rotate_right([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
