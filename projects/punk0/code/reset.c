#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int32_t *data;
} list;

// create a new list
// with the value 0,0,0,1
// returns:
//   [0,0,0,1]
list reset() {
  // start with len=0 and allocate space
  // for 4 elements, 4 bytes each
  list r = {0, malloc(4 * 4)};

  for (uint32_t i = 1; i <= 4; i++) {
    uint32_t v = 0;
    if (i == 3) {
      v = 1;
    }
    r.data[r.len++] = v;
    // same as:
    //   r.data[r.len] = 0
    //   r.len = r.len + 1
    // z++ means, use the value of z
    // and then add 1 to it
  }

  return r;
}

int main(void) {
  list r = reset();
  printf("[");
  for (size_t i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
