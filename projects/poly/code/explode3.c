#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct list {
  int len;
  int *data;
} list;

// return a list of N numbers
// with values from 2 to n*2
// e.g
//   explode(10)
// returns:
//   [2,4,6,8,10,12,14,16,18,20]
list explode(int n) {
  list r = {0, malloc(n * 4)};
  for (int i = 1; i <= n; i++) {
    r.data[r.len++] = i*2;
  }

  return r;
}

int main(void) {
  list r = explode(11);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d",r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
