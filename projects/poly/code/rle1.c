#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int *data;
} list;

list rle(list x) {
  list r = {0, malloc(x.len * 4 * 2)};

  for (int i = 0; i < x.len; i++) {
    int v = x.data[i];
    int l = r.len;
    if (l == 0 || r.data[l-1] != v) {
      r.data[r.len++] = 0;
      r.data[r.len++] = v;
    }
    r.data[r.len-2] += 1;
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
  x.data[4] = 7;

  list r = rle(x);
  for (int i = 0; i < r.len; i++)
    printf("%d\n",r.data[i]);


    
}
