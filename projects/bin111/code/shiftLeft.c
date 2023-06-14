// shiftLeft the value of x: move all
// the bits one position to the left and
// add 0 at the end
//
// for example:
//
// 00000111 -> 00001110
// 00001110 -> 00011100
// 00011100 -> 00111000
// 00111000 -> 01110000
// 01110000 -> 11100000
// 11100000 -> 11000000
// 11000000 -> 10000000
// 10000000 -> 00000000
uint8_t shiftLeft(uint8_t x) {

  x = x << 1;

  return x;
}
