#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int *data;
} list;

list unmax(list x) {
  list r = {0, malloc(x.len * 4)};
  int max = 0;
  for (int i = 0; i < x.len; i++) {
    int v = x.data[i];
    if (v > max) {
      max = v;
    }
  }
  
  for (int i = 0; i < x.len; i++) {
    int v = x.data[i];
    if (v != max) {
      r.data[r.len++] = v;
    }
  }
  return r;
}

int main(void) {
  list x = {
    .len = 5,
    .data = malloc(x.len*4),
  };
  x.data[0] = 9;
  x.data[1] = 3;
  x.data[2] = 3;
  x.data[3] = 5;
  x.data[4] = 7;

  list r = unmax(x);
  for (int i = 0; i < r.len; i++)
    printf("%d\n",r.data[i]);
}
