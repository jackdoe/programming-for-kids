package main

import "fmt"

// shift to the input list to the right,
// adding 0 at the end:
//   [1,2,3,4]
// returns:
//   [0,1,2,3]
func shift_right(x []int) []int {
	r := []int{}

	// start with a zero
	r = append(r, 0)

	// copy everything except the last
	// element
	for i := 0; i < len(x)-1; i++ {
		v := x[i]
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", shift_right([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
