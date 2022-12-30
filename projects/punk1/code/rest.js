// return a new list without the first
// element, e.g.:
//   [1,2,3,2,3,1]
// returns:
//   [2,3,2,3,1]
function rest(x) {
  let r = [];
  for (let i = 1; i < x.length; i++) {
    r.push(x[i]);
  }

  return r;
}

console.log(JSON.stringify(rest([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
