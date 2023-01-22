#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int32_t *data;
} list;

int N_PLAYERS = 3;
// Note: the reset() card can always be
// played, on top of any language.

// create a new list depending on
// N_PLAYERS
// returns:
//   [0,0,0,0], or [-1,-1,1,1]
list reset() {
  // start with len=0 and allocate space
  // for 4 elements, 4 bytes each
  list r = {0, malloc(4 * 4)};
  for (uint32_t i = 0; i < 4; i++) {
    int32_t v = 0;
    if (N_PLAYERS == 2) {
      if (i < 2) {
        v = -1;
      } else {
        v = 1;
      }
    }
    r.data[r.len++] = v;
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
