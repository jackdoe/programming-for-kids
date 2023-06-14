// not x: return NOT x
//
// binary NOT operation
//
// NOT 0 -> 1
// NOT 1 -> 0
//
// for example:
//
// NOT 1011  
//     ----
//     0100
//
uint4_t not(uint4_t x) {
  
  x = ~x;

  return x;
}
