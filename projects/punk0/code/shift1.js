// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
function shift(x) {
  // get a slice from the first element
  // onwards
  let r = x.slice(1);

  // append 0 to the end
  r.push(0);

  return r;
}

console.log(JSON.stringify(shift([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
