// return a sorted copy of the list
//   [1,1,3,2,1]
// returns:
//   [1,1,1,2,3]
function sort(x) {
  let r = [];
  for (let v of x) {
    r.push(v);
  }

  r.sort();

  return r;
}

console.log(JSON.stringify(sort([1, 1, 2, 3, 3, 4, 1, 2, 7, 9])));
