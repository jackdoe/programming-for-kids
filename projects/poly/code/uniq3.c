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

// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
list uniq(list x) {
  // WARNING: modifies the original list
  qsort(x.data, x.len, 4, cmp);
  
  list r = {0, malloc(x.len * 4)};
  for (int i=0; i<x.len;i++) {
    int v = x.data[i];
    int l = r.len;
    if (l == 0 || r.data[l-1] != v) {
      r.data[r.len++] = v;
    }
  }

  return r;
}

int main(void) {
  list x = {
    .len = 10,
    .data = malloc(x.len*4),
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

  
  list r = uniq(x);
  printf("[");
  for (int i = 0; i < r.len; i++) {
    printf("%d",r.data[i]);
    if (i != r.len - 1) {
      printf(" ");
    }
  }
  printf("]\n");    
}
