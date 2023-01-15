#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// create a new list
// with the value 1,2,3,4
// (ignores the input)
// returns:
//   [1,2,3,4]
list reset(list x) {
  // start with len=0 and allocate space
  // for 4 elements, 4 bytes each
  list r = {0, malloc(4 * 4)};

  for (int i = 1; i <= 4; i++) {
    r.data[r.len++] = i;
    // same as:
    //   r.data[r.len] = i
    //   r.len = r.len + 1
    // z++ means, use the value of z
    // and then add 1 to it
  }
  // Note: The first element of an array
  // is at index 0, but length counts
  // from 1. For example, list with 1
  // element has length 1 and you access
  // it at index 0.
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

  list r = reset(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
