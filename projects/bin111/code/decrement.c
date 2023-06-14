// decrement x: return x - 1
// WARNING: integer underflow
//          0 - 1 = 15
//
// Two's Compliment:
// a - b = a + ~b + 1
// a - b = a + NOT b + 1
//
// for example:
//
//    a = 0011, b = 0001
//   ~b = 1110, ~b + 1 = 1111
//   
//   0011
// + 1111
//   ----
//  10010  is truncated to 0010
//         as we have only 4 bits
uint4_t decrement(uint4_t x) {

  x = x - 1;

  return x;
}
