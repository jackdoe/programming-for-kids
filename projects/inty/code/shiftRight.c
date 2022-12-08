// shiftRight the value of x: move all
// the bits one position to the right
// and add 0 at the start
//
// for example:
//
// 11100000 -> 01110000   224 -> 112
// 01110000 -> 00111000   112 -> 56
// 00111000 -> 00011100    56 -> 28
// 00011100 -> 00001110    28 -> 14
// 00001110 -> 00000111    14 -> 7
// 00000111 -> 00000011     7 -> 3
// 00000011 -> 00000001     3 -> 1
// 00000001 -> 00000000     1 -> 0
uint8_t shiftRight(uint8_t x) {
  // same as: x >>= 1
  x = x >> 1;

  return x;
}
