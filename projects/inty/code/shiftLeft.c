// shiftLeft the value of x: move all
// the bits one position to the left and
// add 0 to the end
//
// for example:
//
// 00000111 -> 00001110     7 -> 14
// 00001110 -> 00011100    14 -> 28
// 00011100 -> 00111000    28 -> 56
// 00111000 -> 01110000    56 -> 112
// 01110000 -> 11100000   112 -> 224
// 11100000 -> 11000000   224 -> 192
// 11000000 -> 10000000   192 -> 128
// 10000000 -> 00000000   128 -> 0
uint8_t shiftLeft(uint8_t x) {
  // same as: x <<= 1
  x = x << 1;

  return x;
}
