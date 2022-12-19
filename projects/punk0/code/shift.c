#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// shift to the input list
// to the left, adding 0
// at the end
//   [1,2,3,4,5]
// returns:
//   [2,3,4,5,0]
list shift(list x) {
  list r = {0, malloc(x.len * 4)};

  for (int i = 1; i < x.len; i++) {
    int v = x.data[i];
    r.data[r.len++] = v;
  }

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
