// increment x: return x + 1
// WARNING: integer overflow
//          15 + 1 = 0

// binary addition:
//   0 + 0 = 0
//   0 + 1 = 1
//   1 + 0 = 1
//   1 + 1 = 10 (carry the 1)
//
// for example:
//
//    0011 
//  + 0001 
//    -----
//    0100
// 
uint4_t increment(uint4_t x) {

  x = x + 1;

  return x;
}


