#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int *data;
} list;

list uniq(list x) {
  list r = {
    .len = 0,
    .data = malloc(x.len * 4),
  };

  for (int i=0; i<x.len;i++) {
    int seen = 0;
    for (int j = 0;j<r.len;j++) {
      if (r.data[j] == x.data[i]) {
        seen = 1;
      }
    }
    if (!seen) {
      r.data[r.len++] = x.data[i];
    }
  }
  return r;
}

int main(void) {
  list x = {
    .len = 3,
    .data = malloc(3*4),
  };
  x.data[1] = 3;
  x.data[2] = 2;

  list r = uniq(x);
  for (int i = 0; i < r.len; i++)
    printf("%d\n",r.data[i]);
    
}
