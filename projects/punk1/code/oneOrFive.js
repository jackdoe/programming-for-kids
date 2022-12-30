function oneOrFive(x) {
  if (x > 5) {
    return 1;
  }
  return 5;
}

console.log(JSON.stringify(oneOrFive(5)));
