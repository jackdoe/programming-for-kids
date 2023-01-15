// reverse the input list
//   [1,2,3,4]
// returns:
//   [4,3,2,1]
function reverse(x) {
  let r = [];
  for (let i = 0; i < x.length; i++) {
    // example if len is 4:
    // 4 - 1 - 0 = 3
    // 4 - 1 - 1 = 2
    // 4 - 1 - 2 = 1
    // 4 - 1 - 3 = 0
    let v = x[x.length - 1 - i];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(reverse([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
