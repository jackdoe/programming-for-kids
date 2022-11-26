#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int len;
  int *data;
} list;

// return a list of n numbers
// with decreasing values from n to 1
// e.g:
//   explode(10)
// returns:
//   [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list explode(int n) {
  list r = {0, malloc(n * 4)};
  for (int i = 0; i < n; i++) {
    int v = n - i;
    r.data[r.len++] = v;
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
