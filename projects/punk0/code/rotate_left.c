#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef struct list {
  size_t len;
  int32_t *data;
} list;

// rotate the input list to the left
//   [1,2,3,4]
// returns:
//   [2,3,4,1]
list rotate_left(list x) {
  // start with len=0 and allocate space
  // for x.len elements, 4 bytes each
  list r = {0, malloc(x.len * 4)};

  for (size_t i = 0; i < x.len; i++) {
    // go to the second element
    // then wrap around
    // example if x.len is 4:
    // (0 + 1) % 4 = 1
    // (1 + 1) % 4 = 2
    // (2 + 1) % 4 = 3
    // (3 + 1) % 4 = 0
    size_t idx = (i + 1) % x.len;
    int32_t v = x.data[idx];
    r.data[r.len++] = v;
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
  x.data[n++] = 9;

  list r = rotate_left(x);
  printf("[");
  for (size_t i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
