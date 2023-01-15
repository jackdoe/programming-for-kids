package main

import (
	"fmt"
)

// the next player draws list[0] cards
// and returns a copy of the list:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
// prints:
//   draw 1 cards
func draw(x []int) []int {
	if len(x) > 0 {
		n := x[0]
		if n == 0 {
			fmt.Printf("next player skips\n")
		} else {
			fmt.Printf("draw %d cards\n", n)
		}

	}

	// make a slice with
	// preallocated len(x) slots
	r := make([]int, len(x))
	for i := range x {
		r[i] = x[i]
	}
	return r
}

func main() {
	fmt.Printf("%v\n", draw([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
