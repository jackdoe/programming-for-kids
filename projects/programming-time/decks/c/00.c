// we need stdio.h for printf()
#include <stdio.h>

int main(void) {
  // int means number between
  // -2,147,483,648 to 2,147,483,647
  int dice = ⚂;

  // char means number betwen
  // -128 and 127
  char c = 97 + dice;

  // strings in C are arrays of
  // characters ending with the null
  // character \0 we can have array
  char word[3] = {c, c, '\0'};

  // %d means print integer
  printf("%d\n",dice);

  // you see `char` is just a number
  // we can print it as character or
  // as an integer %d or %c, and %s
  // means print from wherever the
  // `word` points in memory until
  // the first \0
  printf("%d or %c or %s\n",
         c, 
         c, 
         word);
}
