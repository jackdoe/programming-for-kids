#include <stdio.h>
#include <stdint.h>

#include <stdlib.h>
typedef struct list {
  size_t len;
  int32_t *data;
} list;

// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
list shift_left(list x) {
  // start with len=0 and allocate space
  // for x.len elements, 4 bytes each
  list r = {0, malloc(x.len * 4)};

  // copy everything after the first
  // element
  for (size_t i = 1; i < x.len; i++) {
    int32_t v = x.data[i];
    r.data[r.len++] = v;
  }

  // append 0 to the end
  r.data[r.len++] = 0;
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

  list r = shift_left(x);
  printf("[");
  for (size_t i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
