// decrement x: return x - 1
//
// if x is 0 it underflows and wraps
// arround, so 0 - 1 becomes 255
//
// in binary:
// 00000000 - 000000001 = 11111111
// in decimal:
// 0 - 1 = 255
uuint8_t decrement(uint8_t x) {
  // same as: x -= 1
  // same as: x--

  x = x - 1;

  return x;
}
