package main

import "fmt"

// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
func shift(x []int) []int {
	r := make([]int, len(x))

	// copy everything after the first
	// element
	for i := 1; i < len(x); i++ {
		r[i-1] = x[i]
	}

	// make() in Go creates a new
	// slice with all elements set
	// to zero, so there is no need
	// to add zero to the end
	return r
}

func main() {
	fmt.Printf("%v\n", shift([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
