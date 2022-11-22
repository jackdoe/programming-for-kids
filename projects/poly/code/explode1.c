#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct list {
  size_t len;
  int *data;
} list;
//
// fill a list with N random
// integers
//
list explode(int n) {
  list r = {0, malloc(n * 4)};
  for (int i = 0; i < n; i++) {
    r.data[r.len++] = rand() % 20;
  }
  return r;
}

int main(void) {
 list r = explode(30);
 for (int i = 0; i < r.len; i++)
   printf("%d\n",r.data[i]);
}
