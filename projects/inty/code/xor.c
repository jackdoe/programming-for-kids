// binary XOR with 0b10101010
// 0 XOR 0 -> 0
// 0 XOR 1 -> 1
// 1 XOR 0 -> 1
// 1 XOR 1 -> 0
//
// for example:
//
//     10000111 
// XOR 10101010
//    ----------
//     00101101
uint8_t xor(uint8_t x) {
  // same as: x = x ^ 170
  // same as: x = x ^ 0b10101010
  // same as: x ^= 170
  // same as: x ^= 0b10101010

  x = x ^ 0b10101010;

  return x;
}
