// binary OR with 0b11110000
//
// 0 OR 0 -> 0
// 0 OR 1 -> 1
// 1 OR 0 -> 1
// 1 OR 1 -> 1
//
// for example:
//
//    00000011 
// OR 11110000
//    ----------
//    11110011
uint8_t or(uint8_t x) {
  // same as: x = x | 240
  // same as: x = x | 0b11110000
  // same as: x |= 240
  // same as: x |= 0b11110000
  
  x = x | 0b11110000;

  return x;
}
