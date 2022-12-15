// or x: return x OR 0b11110000
//
// binary OR operation
//
// 0 OR 0 -> 0
// 0 OR 1 -> 1
// 1 OR 0 -> 1
// 1 OR 1 -> 1
//
// for example:
//
//    01000011
// OR 11110000
//   ----------
//    11110011
uint8_t or(uint8_t x) {

  x = x | 0b11110000;

  return x;
}
