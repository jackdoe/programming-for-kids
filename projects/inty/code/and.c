// binary AND with 0b00001111
//
// 0 AND 0 -> 0
// 0 AND 1 -> 0
// 1 AND 0 -> 0
// 1 AND 1 -> 1
//
// for example:
//
//     11000011
// AND 00001111
//    ----------
//     00000011
uint8_t and(uint8_t x) {
  // same as: x = x & 15
  // same as: x = x & 0b00001111
  // same as: x &= 15
  // same as: x &= 0b00001111

  x = x & 0b00001111;

  return x;
  
}
