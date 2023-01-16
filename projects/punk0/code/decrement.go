package main

import (
	"fmt"
)

// decrement the first of a list
//   [1,2,3,4]
// returns:
//   [0,2,3,4]
func decrement(x []int) []int {
	r := []int{}

	for i, v := range x {
		if i == 0 {
			v--
		}
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", decrement([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
