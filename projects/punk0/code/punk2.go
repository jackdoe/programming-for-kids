package main

import (
	"fmt"
)

// returns a copy of the list and print
// what happens next:
//   [1,2,3,4]
// returns
//   [1,2,3,4]
func punk2(x []int) []int {
	if len(x) >= 2 {
		n := x[2]
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
	fmt.Printf("%v\n", punk2([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
