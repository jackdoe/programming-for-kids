#include <stdio.h>
#include <stdlib.h>

int oneOrFive(int x) {
  if (x > 5) {
    return 1;
  }
  return 5;
}

int main(void) { printf("%d\n", oneOrFive(5)); }
