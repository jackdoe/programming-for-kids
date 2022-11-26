// halve the input, rounded down,
// never reaching 0, e.g.:
//   5
// returns:
//   2
function halve(x) {
  let v = parseInt(x / 2);
  if (v < 1) {
    v = 1
  }

  return v;
}

console.log(JSON.stringify(halve(5)));
