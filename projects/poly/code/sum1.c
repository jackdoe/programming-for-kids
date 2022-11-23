#include <stdio.h>
#include <stdlib.h>

typedef struct list {
  int len;
  int *data;
} list;

// sum all the integers from a list
//   [1,2,3]
// returns:
//   6
int sum(list x) {
  int s = 0;
  for (int i = 0; i < x.len; i++) {
    s += x.data[i];
  }

  return s;
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
  
  printf("%d\n", sum(x));
}
