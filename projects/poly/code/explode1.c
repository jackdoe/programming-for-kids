#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef struct list {
  size_t len;
  int *data;
} list;

//
// takes a float N and returns
// a list with floor(N) * 2 elements
// from 1 to floor(N)
//
list explode(float nf) {
  int n = (int) nf;
  
  list r = {0, malloc(n * 2 * 4)};
  for (int i = 1; i <= n; i++) {
    r.data[r.len++] = i;
    r.data[r.len++] = i;    
  }
  return r;
}

int main(void) {
 list r = explode(30.1);
 for (int i = 0; i < r.len; i++)
   printf("%d\n",r.data[i]);
}
