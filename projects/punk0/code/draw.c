#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int len;
  int *data;
} list;

// the next player draws n % 5 cards
// where n is the first value from the
// list, and returns a reversed copy:
//   [7,2,3,4,5]
// returns
//   [5,4,3,2,7]
// prints:
//   draw 2 cards
list draw(list x) {
  int n = 0;

  if (x.len > 0) {
    n = x.data[0] % 5;
  }

  printf("draw %d cards\n", n);

  list r = {0, malloc(x.len * 4)};

  for (int i = 0; i < x.len; i++) {
    int v = x.data[x.len - 1 - i];
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
