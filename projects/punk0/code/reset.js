// Note: the reset() card can always be
// played, on top of any language.

// create a new list with the value
// 0,0,0,0
// returns:
function reset(x) {
  let r = [];

  for (let i = 1; i <= 4; i++) {
    r.push(0);
  }

  return r;
}

console.log(JSON.stringify(reset()));
