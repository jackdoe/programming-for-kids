// sort the list in ascending order
//   [5,1,4,2,3]
// returns:
//   [1,2,3,4,5]
function sort(x) {
  let r = [];
  for (let v of x) {
    r.push(v);
  }

  r.sort();

  return r;
}

console.log(JSON.stringify(sort([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
