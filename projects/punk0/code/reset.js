const N_PLAYERS = 3

// Note: the reset() card can always be
// played, on top of any language.

// create a new list depending on
// N_PLAYERS
// returns:
//   [0,0,0,0], or [-1,-1,1,1]
function reset() {
  let r = [];

  for (let i = 0; i < 4; i++) {
    let v = 0
    if (N_PLAYERS == 2) {
      if (i < 2) {
        v = -1
      } else {
        v = 1
      }
    }
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(reset()));
