// Returns the number of 1 bits in the
// value of x.
//
// for example:
// 11110000 -> 4    240 -> 4
// 10101010 -> 4    170 -> 4
// 00000011 -> 2      3 -> 2
// 10000000 -> 1    128 -> 1
// 01111111 -> 7    127 -> 7
// 11111111 -> 8    255 -> 8
uint8_t popcount(uint8_t x) {
    uint8_t c = 0;
    while(x != 0) {
      if ((x & 0b00000001) > 0) {
        c++;
      }
      x >>= 1;
    }
    /*
    same as:
      for (c = 0; x != 0; x >>= 1)
          if (x & 1)
              c++;
    */

    return c;  
}
