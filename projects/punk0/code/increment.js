// increment the elements of a list
//   [1,2,3,4]
// returns:
//   [2,3,4,5]
function increment(x) {
  let r = [];
  for (let v of x) {
    r.push(v + 1);
  }

  return r;
}

console.log(JSON.stringify(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
