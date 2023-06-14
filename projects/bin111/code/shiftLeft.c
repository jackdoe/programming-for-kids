// shiftLeft the value of x: move all
// the bits one position to the left and
// add 0 at the end
//
// for example:
//
// 0111 -> 1110
// 1110 -> 1100
// 1100 -> 1000
// 1000 -> 0000
// 0000 -> 0000
uint4_t shiftLeft(uint4_t x) {

  x = x << 1;

  return x;
}
