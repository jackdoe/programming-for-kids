// returns the first element from a list
// or 1 if the list is empty, e.g.:
//   [2,3,2]
// returns:
//   2
function first(x) {
  let f = 1;
  if (x.length > 0) {
    f = x[0];
  }

  return f;
}

console.log(JSON.stringify(first([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
