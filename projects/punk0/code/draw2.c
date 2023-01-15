#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int len;
  int *data;
} list;

// the next player draws list[0] cards
// and returns a copy of the list:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
// prints:
//   draw 1 cards
list draw(list x) {
  if (x.len > 0) {
    int n = x.data[0];
    if (n == 0) {
      printf("next player skips\n");
    } else {
      printf("draw %d cards\n", n);
    }
  }
  list r = {0};  // zeroed list struct
  for (int i = 0; i < x.len; i++) {
    // reallocate a new buffer with
    // 4 extra bytes in the end
    r.data = realloc(r.data, r.len * 4 + 4);
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

  list r = draw(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
