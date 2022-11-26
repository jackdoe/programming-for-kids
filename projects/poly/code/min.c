#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// returns the smallest integer from a
// list, or 1 if the list is empty, e.g.:
//   [2,3,2,4]
// returns:
//   2
int min(list x) {
  if (x.len == 0) {
    return 1;
  }
  int m = 2147483647;
  for (int i = 0; i < x.len; i++) {
    int v = x.data[i];
    if (v < m) {
      m = v;
    }
  }

  return m;
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

  printf("%d\n", min(x));
}
