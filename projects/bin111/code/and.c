// and x: return x AND 0b00001111
//
// binary AND operation
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
//     --------
//     00000011
//
uint8_t and(uint8_t x) {

  x = x & 0b00001111;

  return x;
}
