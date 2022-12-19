package main

import (
	"fmt"
)

// returns new list, incrementing each
// element of the old one, e.g.:
//   [1,1,3,2,1]
// returns:
//   [2,2,4,3,2]
func increment(x []int) []int {
	r := []int{}
	for _, v := range x {
		r = append(r, v+1)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", increment([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
