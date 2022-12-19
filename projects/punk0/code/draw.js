// the next player draws N % 5 cards
// where N is the first value from the
// list, and returns a reversed copy:
//   [1,2,3,4,5]
// returns
//   [5,4,3,2,1]
// prints:
//   draw 1 cards
function draw(x) {
  let n = 0;

  if (x.length > 0) {
    n = x[0] % 5;
  }

  console.log("draw " + n + " cards");

  let r = [];

  for (let i = 0; i < x.length; i++) {
    let v = x[x.length - 1 - i];
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(draw([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
