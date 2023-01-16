#include <stdio.h>
#include <stdint.h>

#include <stdlib.h>
typedef struct list {
  size_t len;
  int32_t *data;
} list;
// passed to qsort
int cmp(const void *a, const void *b) {
  int av = *((int *)a);
  int bv = *((int *)b);
  return av - bv;
}

// sort the list in ascending order
//   [1,4,2,3]
// returns:
//   [1,2,3,4]
list sort_asc(list x) {
  // qsort will mutate the array itself
  // so first we will copy it, and
  // then sort the copy
  list r = {0, malloc(x.len * 4)};
  for (size_t i = 0; i < x.len; i++) {
    int32_t v = x.data[i];
    r.data[r.len++] = v;
  }
  // sort r.data, with r.len elements
  // 4 bytes each using the cmp function
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

  list r = sort_asc(x);
  printf("[");
  for (size_t i = 0; i < r.len; i++) {
    printf("%d", r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");
}
