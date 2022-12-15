// decrement x: return x - 1
// WARNING: integer underflow
//          0 - 1 = 255
//
// Two's Compliment:
// a - b = a + ~b + 1
//
// for example:
//
//    a = 00000011, b = 00000001
//   ~b = 11111110, ~b + 1 = 11111111
//   
//   00000011
// + 11111111
//   --------
//  100000010  is truncated to 00000010
//             as we have only 8 bits
uint8_t decrement(uint8_t x) {

  x = x - 1;

  return x;
}
