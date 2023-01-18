// create a new list
// with the value 0,0,0,0
// returns:
//   [0,0,0,0]
function reset(x) {
  let r = [];
  for (let i = 1; i <= 4; i++) {
    r.push(0);
  }

  return r;
}

console.log(JSON.stringify(reset()));
