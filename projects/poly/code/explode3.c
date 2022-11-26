#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int len;
  int *data;
} list;

// return a list of n times
// the number n + 1
// e.g
//   explode(5)
// returns:
//   [6, 6, 6, 6, 6]
list explode(int n) {
  list r = {0, malloc(n * 4)};
  for (int i = 0; i < n; i++) {
    r.data[r.len++] = n + 1;
  }

  return r;
}

int main(void) {
  list r = explode(11);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
