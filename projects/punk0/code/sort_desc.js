// sort the list in descending order
//   [1,4,2,3]
// returns:
//   [4,3,2,1]
function sort_desc(x) {
  // x.sort() mutates the array itsef
  // so we will copy it and sort the
  // copy
  let r = [];
  for (let v of x) {
    r.push(v);
  }

  r.sort();
  r.reverse()

  return r;
}

console.log(JSON.stringify(sort_desc([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
