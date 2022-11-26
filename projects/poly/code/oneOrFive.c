#include <stdio.h>
#include <stdlib.h>

// return 1 if the number is bigger than 5
// return 5 if otherwise, e.g.:
//   3
// returns:
//   5
int oneOrFive(int x) {
  if (x > 5) {
    return 1;
  }
  return 5;
}

int main(void) { printf("%d\n", oneOrFive(5)); }
