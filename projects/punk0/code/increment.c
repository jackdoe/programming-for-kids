#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// increment the elements of a list
//   [1,2,3,4]
// returns:
//   [2,3,4,5]
list increment(list x) {
  // start with len=0 and allocate space
  // for x.len elements, 4 bytes each
  list r = {0, malloc(x.len * 4)};
  // algorithm:
  //   walk over each value of the input
  //   and add value+1 in the new list
  for (int i = 0; i < x.len; i++) {
    // get the i-th element from the
    // input and add 1 to it
    int v = x.data[i] + 1;
    // store it as the next element in
    // the output list
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
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
