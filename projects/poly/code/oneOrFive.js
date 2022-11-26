// return 1 if the number is bigger than 5
// return 5 if otherwise, e.g.:
//   3
// returns:
//   5
function oneOrFive(x) {
  if (x > 5) {
    return 1;
  }
  return 5;
}

console.log(JSON.stringify(oneOrFive(5)));
