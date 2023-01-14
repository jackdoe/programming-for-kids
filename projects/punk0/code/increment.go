package main

import (
	"fmt"
)

// increment the elements of a list
//   [1,2,3,4]
// returns:
//   [2,3,4,5]
func increment(x []int) []int {
	r := []int{}

	// algorithm:
	//   for each value of the input list
	//   add value+1 to the output list
	for _, v := range x {
		r = append(r, v+1)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", increment([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
