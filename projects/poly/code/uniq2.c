#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef struct list {
  int len; int *data;
} list;
int hash_find(list set, int k) {
  int bucket = (k * 31) % set.len;
  for (uint32_t i = bucket; ; i++) {
    int v = set.data[i % set.len];
    if (v == k || v == 0) return v;
  }
}
void hash_store(list set, int k) {
  int bucket = (k * 31) % set.len;
  for (int i = bucket; ; i++) {
    int idx = i % set.len;
    if (set.data[idx] == 0) {
      set.data[idx] = k; return;
    }
  }
}
list uniq(list x) {
  list r = {0, malloc(x.len * 4)};
  list s = {x.len * 10, malloc(s.len*4)};
  for (int i = 0; i < x.len; i++) {
    if (!hash_find(s, x.data[i])) {
      r.data[r.len++] = x.data[i];
      hash_store(s, x.data[i]);
    }
  }
  free(s.data);
  return r;
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
