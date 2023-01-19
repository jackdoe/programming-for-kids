#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// rotate the input list to the right
//   [1,2,3,4]
// returns:
//   [4,1,2,3]
list rotate_right(list x) {
  // start with len=0 and allocate space
  // for x.len elements, 4 bytes each
  list r = {0, malloc(x.len * 4)};

  for (int i = 0; i < x.len; i++) {
    // go to the last element and
    // then wrap around
    // example if x.len is 4:
    // (0 + 4 - 1) % 4 = 3
    // (1 + 4 - 1) % 4 = 0
    // (2 + 4 - 1) % 4 = 1
    // (3 + 4 - 1) % 4 = 2
    int idx = (i + x.len - 1) % x.len;
    int v = x.data[idx];
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

  list r = rotate_right(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
