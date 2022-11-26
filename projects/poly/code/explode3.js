// return a list of n times
// the number n+1
// e.g
//   explode(5)
// returns:
//   [6, 6, 6, 6, 6]
function explode(n) {
  r = [];
  for (let i = 0; i < n; i++) {
    r.push(n + 1);
  }

  return r;
}

console.log(JSON.stringify(explode(11)));
