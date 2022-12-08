// binary NOT operation
//
// NOT 0 -> 1
// NOT 1 -> 0
//
// for example:
//
// NOT 11000011 
//    ----------
//     00111100
uint8_t not(uint8_t x) {
  x = ~x;

  return x;
}
