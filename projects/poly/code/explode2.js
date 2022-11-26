// return a list of n numbers
// with values from 2 to n+1
// e.g
//   explode(10)
// returns:
//   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
function explode(n) {
  r = [];
  for (let i = 2; i <= n+1; i++) {
    r.push(i);
  }

  return r;
}

console.log(JSON.stringify(explode(11)));
