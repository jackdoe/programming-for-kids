// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
function shift(x) {
  let r = [];

  // copy everything after the first
  // element
  for (let i = 1; i < x.length; i++) {
    let v = x[i];
    r.push(v);
  }

  // append 0 to the end
  r.push(0);

  return r;
}

console.log(JSON.stringify(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
