package main

import (
	"fmt"
)

// returns a copy of the list and print
// what happens next:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
func punk3(x []int) []int {
	if len(x) >= 3 {
		n := x[3]
		if n == 0 {
			fmt.Printf("next player skips\n")
		} else if n < 0 {
			fmt.Printf("play %d cards\n", -n)
		} else {
			fmt.Printf("draw %d cards\n", n)
		}
	}

	r := []int{}
	for i := range x {
		r = append(r, x[i])
	}
	return r
}

func main() {
	fmt.Printf("%v\n", punk3([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
