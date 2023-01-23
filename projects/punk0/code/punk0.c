#include <stdint.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct list {
  size_t len;
  int32_t *data;
} list;

// returns a copy of the list and print
// what happens next:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
list punk0(list x) {
  if (x.len >= 1) {
    int n = x.data[0];
    if (n == 0) {
      printf("next player skips\n");
    } else if (n < 0) {
      printf("play %d cards\n",-n);
    } else {
      printf("draw %d cards\n", n);
    }
  }
  // start with len=0 and allocate space
  // for x.len elements, 4 bytes each
  list r = {0, malloc(x.len * 4)};
  for (size_t i = 0; i < x.len; i++) {
    r.data[r.len++] = x.data[i];
  }

  return r;
}

int main(void) {
  list x = {
      .len = 10,
      .data = malloc(x.len * 4),
  };

  int n = 0;
  x.data[n++] = 1;
  x.data[n++] = 1;
  x.data[n++] = 2;
  x.data[n++] = 3;
  x.data[n++] = 3;
  x.data[n++] = 4;
  x.data[n++] = 1;
  x.data[n++] = 2;
  x.data[n++] = 7;
  x.data[n++] = 1;

  list r = punk0(x);
  printf("[");
  for (size_t i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
