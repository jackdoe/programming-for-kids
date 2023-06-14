// shiftRight x: move all
// the bits one position to the right
// and add 0 at the start
//
// for example:
//
// 1110 -> 0111
// 0111 -> 0011
// 0011 -> 0001
// 0001 -> 0000
// 0000 -> 0000
uint4_t shiftRight(uint4_t x) {

  x = x >> 1;

  return x;
}

