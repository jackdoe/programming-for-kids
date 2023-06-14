// popcount x: return the number of 1
// bits in the value of x.
//
// for example:
//
// 1111 -> 4
// 1110 -> 3
// 0111 -> 3
// 1010 -> 2
// 0010 -> 2
// 0000 -> 0
uint4_t popcount(uint4_t x) {
    uint4_t c = 0;
    while(x != 0) {
      if ((x & 0b0001) > 0) {
        c++;
      }
      x = x >> 1;
    }

    /*
    same as:
      for (c = 0; x != 0; x = x >> 1)
          if (x & 1)
              c++;
    */

    return c;
}
