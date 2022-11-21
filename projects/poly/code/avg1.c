#include <stdio.h>
#include <stdlib.h>
typedef struct list {
  size_t len;
  int *data;
} list;
//
// take a list of numbers
// and return an average
// it will return NaN if
// the list length is 0
//
float avg(list x) {
  float sum = 0;
  for (int i = 0; i < x.len; i++) {
    sum += x.data[i];
  }

  return sum/x.len;
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

  printf("%f\n",avg(x));

    
}
