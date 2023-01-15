#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct list {
  int len;
  int *data;
} list;

// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
list shift(list x) {
  // start with len=4 and allocate space
  // for x.len elements, 4 bytes each
  list r = {x.len, malloc(x.len * 4)};

  // zero the allocated memory
  memset(r.data, 0, r.len * 4);

  // copy x.len*4-4 bytes from x.data+1
  // to r.data, note that x.data is of
  // type int, so x.data+1 is adding
  // size of int (4) to x.data
  memcpy(r.data, x.data+1, x.len*4 - 4);

  // note: we dont have to add zero in
  // the end because the laste element
  // is already zero due to the early
  // memset
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

  list r = shift(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
