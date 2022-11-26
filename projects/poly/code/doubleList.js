// returns new list, doubling each
// item, e.g.:
//   [1,2,3,4,5]
// returns:
//   [2,4,6,8,10]
function doubleList(x) {
  let r = [];
  for (let v of x) {
    r.push(v * 2);
  }

  return r;
}

console.log(JSON.stringify(doubleList([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
