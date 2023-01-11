// the next player draws list[0] cards
// and returns a copy of the list:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
// prints:
//   draw 1 cards
function draw(x) {
  if (x.length > 0) {
    let n = x[0];
    if (n == 0) {
      console.log("next player skips");
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

console.log(JSON.stringify(draw([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
