#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int len;
  int *data;
} list;

// return a list of n numbers
// with values from 2 to n+1
// e.g
//   explode(10)
// returns:
//   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list explode(int n) {
  list r = {0, malloc(n * 4)};
  for (int i = 2; i <= n+1; i++) {
    r.data[r.len++] = i;
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
