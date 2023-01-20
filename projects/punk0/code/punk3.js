// returns a copy of the list and print
// what happens next:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
function punk3(x) {
  if (x.length >= 3) {
    let n = x[3];
    if (n == 0) {
      console.log("next player skips");
    } else if (n < 0) {
      console.log(`play ${-n} cards`);
    } else {
      console.log(`draw ${n} cards`);
    }
  }

  let r = [];
  for (let v of x) {
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(punk3([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
