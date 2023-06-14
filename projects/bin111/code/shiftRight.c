// shiftRight x: move all
// the bits one position to the right
// and add 0 at the start
//
// for example:
//
// 11100000 -> 01110000
// 01110000 -> 00111000
// 00111000 -> 00011100
// 00011100 -> 00001110
// 00001110 -> 00000111
// 00000111 -> 00000011
// 00000011 -> 00000001
// 00000001 -> 00000000
uint8_t shiftRight(uint8_t x) {

  x = x >> 1;

  return x;
}

