package main

import (
	"fmt"
)

// the player can specify
// which index to decrement
const INC_INDEX = 0

// increment the INC_INDEX of a list,
// e.g. if INC_INDEX is defined as 0:
//   [1,2,3,4]
// returns:
//   [2,2,3,4]
func increment(x []int) []int {
	r := []int{}

	for i, v := range x {
		if i == INC_INDEX {
			v++
		}
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", increment([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
