#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;
// passed to qsort
int cmp(const void *a, const void *b) {
  int av = *((int *)a);
  int bv = *((int *)b);
  return av - bv;
}

// return a sorted copy of the list
//   [1,1,3,2,1]
// returns:
//   [1,1,1,2,3]
list sort(list x) {
  list r = {0, malloc(x.len * 4)};
  for (int i = 0; i < x.len; i++) {
    int v = x.data[i];
    r.data[r.len++] = v;
  }

  qsort(r.data, r.len, 4, cmp);

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

  list r = sort(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
