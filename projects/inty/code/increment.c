// increment x: return x + 1
//
// if x is 255 it overflows and wraps
// arround, so 255 + 1 becomes 0
//
// in binary:
// 11111111 + 000000001 = 00000000
// in decimal:
// 255 + 1 = 0
uint8_t increment(uint8_t x) {
  // same as: x += 1
  // same as: x++
  x = x + 1;

  return x;
}


