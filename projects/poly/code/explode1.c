#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct list {
  size_t len;
  int *data;
} list;

// return a list of N numbers
// with values from 1 to n/2
// e.g
//   explode(10)
// returns:
//   [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
list explode(int n) {
  list r = {0, malloc(n * 4)};
  for (int i = 1; i <= n; i++) {
    r.data[r.len++] = (i + 1) /2;
  }
  return r;
}

int main(void) {
 list r = explode(33);
 for (int i = 0; i < r.len; i++)
   printf("%d\n",r.data[i]);
}
