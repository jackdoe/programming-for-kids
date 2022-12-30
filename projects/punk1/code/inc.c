#include <stdio.h>
#include <stdlib.h>

// increment the input, e.g.:
//   5
// returns:
//   6
int increment(int x) {
  int v = x + 1;
  return v;
}

int main(void) { printf("%d\n", increment(5)); }
