// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
function shift(x) {
  let r = [];

  // start with a zero
  r.push(0);

  // copy everything except the last
  // element
  for (let i = 0; i < x.length-1; i++) {
    let v = x[i];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
