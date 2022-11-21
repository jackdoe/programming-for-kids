#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int *data;
} list;

list rld(list x) {
  list r = {0, malloc(x.len/2*4)};

  for (int i = 0; i < x.len; i+=2) {
    int c = x.data[i];
    int v = x.data[i+1];
    for (int j = 0; j < c; j++) {
      r.data[r.len++] = v;
    }
  }
  return r;
}

int main(void) {
  list x = {
    .len = 6,
    .data = malloc(x.len*4),
  };
  x.data[0] = 1;
  x.data[1] = 3;
  x.data[2] = 3;
  x.data[3] = 5;
  x.data[4] = 7;

  list r = rld(x);
  for (int i = 0; i < r.len; i++)
    printf("%d\n",r.data[i]);


    
}
