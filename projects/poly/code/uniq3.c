#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int *data;
} list;

int cmp(const void *a, const void *b) {
    int av = *((int *)a);
    int bv = *((int *)b);
    return av - bv;
}
list uniq(list x) {
  list r = {
    .len = 0,
    .data = malloc(x.len * 4),
  };

  qsort (x.data, x.len, 4, cmp);
  
  for (int i=0; i<x.len;i++) {
    int v = x.data[i];
    int l = r.len;
    if (l == 0 || r.data[l-1] != v)
      r.data[r.len++] = v;
  }

  return r;
}

int main(void) {
  list x = {
    .len = 5,
    .data = malloc(x.len*4),
  };
  x.data[0] = 1;
  x.data[1] = 3;
  x.data[2] = 3;
  x.data[3] = 5;
  x.data[4] = 3;

  list r = uniq(x);
  for (int i = 0; i < r.len; i++)
    printf("%d\n",r.data[i]);
    
}
