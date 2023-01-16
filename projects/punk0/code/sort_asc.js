// sort the list in ascending order
//   [1,4,2,3]
// returns:
//   [1,2,3,4]
function sort_asc(x) {
  // x.sort() mutates the array itsef
  // so we will copy it and sort the
  // copy
  let r = [];
  for (let v of x) {
    r.push(v);
  }

  r.sort();

  return r;
}

console.log(JSON.stringify(sort_asc([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
