package main

import "fmt"

// the player can specify a different
// value when they play the card, can be
// zero, it must not be negative
const ROT = 1

// rotate the input list to the left ROT
// steps, e.g. if ROT = 1
//   [1,2,3,4]
// returns:
//   [2,3,4,1]
func rotate_left(x []int) []int {
	r := []int{}

	for i := 0; i < len(x); i++ {
		// go to the ROT element
		// then wrap around
		// example if x.len is 4
		// and ROT is 1:
		// (0 + 1) % 4 = 1
		// (1 + 1) % 4 = 2
		// (2 + 1) % 4 = 3
		// (3 + 1) % 4 = 0
		idx := (i + ROT) % len(x)
		v := x[idx]
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", rotate_left([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
