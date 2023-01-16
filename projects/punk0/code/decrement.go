package main

import (
	"fmt"
)

// the player can specify
// which index to decrement
const DEC_INDEX = 0

// decrement the DEC_INDEX of a list,
// e.g. if DEC_INDEX is defined as 0:
//   [1,2,3,4]
// returns:
//   [0,2,3,4]
func decrement(x []int) []int {
	r := []int{}

	for i, v := range x {
		if i == DEC_INDEX {
			v--
		}
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", decrement([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
