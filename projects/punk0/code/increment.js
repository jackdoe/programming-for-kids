// increment the elements of a list
//   [1,2,3,4]
// returns:
//   [2,3,4,5]
function increment(x) {
  let r = [];

  // algorithm:
  //   walk over each value of the input
  //   and add value+1 in the new list
  for (let v of x) {
    r.push(v + 1);
  }

  return r;
}

console.log(JSON.stringify(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
