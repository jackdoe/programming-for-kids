// remove the all occurences of the
// smallest integer in the list
//   [1,2,3,2,3,1]
// returns:
//   [2,3,2,3]
function unmin(x) {
  min = 2147483647;
  for (let v of x) {
    if (v < min) {
      min = v;
    }
  }

  let r = [];
  for (let v of x) {
    if (v != min) {
      r.push(v);
    }
  }

  return r;
}

console.log(JSON.stringify(unmin([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
