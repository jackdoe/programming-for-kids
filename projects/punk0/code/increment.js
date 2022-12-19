// returns new list, incrementing each
// element of the old one, e.g.:
//   [1,1,3,2,1]
// returns:
//   [2,2,4,3,2]
function increment(x) {
  let r = [];
  for (let v of x) {
    r.push(v + 1);
  }

  return r;
}

console.log(JSON.stringify(increment([1, 1, 2, 3, 3, 4, 1, 2, 7, 1])));
