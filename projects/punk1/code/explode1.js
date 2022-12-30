// return a list of n numbers with
// increasing value from 1 to n but if n
// is less than 3, then it returns from
// 1 to 6 e.g:
//   explode(10)
// returns:
//   [1,2,3,4,5,6,7,8,9,10]
function explode(n) {
  r = [];
  if (n < 3) {
    n = 6;
  }
  for (let i = 1; i <= n; i++) {
    r.push(i);
  }

  return r;
}

console.log(JSON.stringify(explode(11)));
