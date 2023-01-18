#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int32_t *data;
} list;

// the player can specify
// which index to decrement
size_t INC_INDEX = 0;

// increment the INC_INDEX of a list,
// e.g. if INC_INDEX is set to 0:
//   [1,2,3,4]
// returns:
//   [2,2,3,4]
list increment(list x) {
  // start with len=0 and allocate space
  // for x.len elements, 4 bytes each
  list r = {0, malloc(x.len * 4)};

  for (size_t i = 0; i < x.len; i++) {
    int32_t v = x.data[i];
    if (i == INC_INDEX) {
      v++;
    }

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
  x.data[n++] = 1;

  list r = increment(x);
  printf("[");
  for (size_t i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
