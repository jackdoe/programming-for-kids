// increment x: return x + 1
// WARNING: integer overflow
//          255 + 1 = 0

// binary addition:
//   0 + 0 = 0
//   0 + 1 = 1
//   1 + 0 = 1
//   1 + 1 = 10 (carry the 1)
//
// for example:
//
//    00000011 
//  + 00000001 
//    ---------
//    00000100
// 
uint8_t increment(uint8_t x) {

  x = x + 1;

  return x;
}


