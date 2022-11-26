#include <stdio.h>
#include <stdlib.h>

// halve the input, rounded down,
// never reaching 0, e.g.:
//   5
// returns:
//   2
int halve(int x) {
  int v = x / 2;
  if (v < 1) {
    v = 1;
  }

  return v;
}

int main(void) {
  printf("%d\n",halve(5));
}
