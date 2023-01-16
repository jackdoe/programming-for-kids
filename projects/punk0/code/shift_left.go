package main

import "fmt"

// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [2,3,4,0]
func shift_left(x []int) []int {
	r := []int{}

	// copy everything after the first
	// element
	for i := 1; i < len(x); i++ {
		v := x[i]
		r = append(r, v)
	}

	// append 0 to the end
	r = append(r, 0)

	return r
}

func main() {
	fmt.Printf("%v\n", shift_left([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
