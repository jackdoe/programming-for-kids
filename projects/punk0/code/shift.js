// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4,5]
// returns:
//   [2,3,4,5,0]
function shift(x) {
  let r = [];
  for (let i = 1; i < x.length; i++) {
    let v = x[i];
    r.push(v);
  }

  r.push(0);

  return r;
}

console.log(JSON.stringify(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
