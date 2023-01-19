// create a new list
// with the value 0,0,0,1
// returns:
//   [0,0,0,1]
function reset(x) {
  let r = [];
  for (let i = 1; i <= 4; i++) {
    let v = 0;
    if (i == 3) {
      v = 1;
    }
    r.push(v);
  }

  return r;
}

console.log(JSON.stringify(reset()));
