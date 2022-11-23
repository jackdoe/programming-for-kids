#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  int len;
  int *data;
} list;

// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
list uniq(list x) {
  // worse case there are no duplicate
  // elements so we preallocate the full
  // original list length times 4 bytes
  // each integer
  list r = {0, malloc(x.len * 4)};
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
    .len = 9,
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
