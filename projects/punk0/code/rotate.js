// rotate the input list
// to the right, e.g.:
//   [1,2,3,4,5]
// returns:
//   [5,1,2,3,4]
function rotate(x) {
  let r = [];

  for (let i = 0; i < x.length; i++) {
    // go to the last element and
    // then wrap around
    let len = x.length;
    let idx = (i + len - 1) % len;
    let v = x[idx];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(rotate([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
