// return a list of n numbers
// with decreasing values from n to 1
// e.g:
//   explode(10)
// returns:
//   [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
function explode(n) {
  r = [];
  for (let i = 0; i < n; i++) {
    let v = n - i;
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(explode(11)));
