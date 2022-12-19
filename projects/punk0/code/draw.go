package main

import (
	"fmt"
)

// the next player draws n % 5 cards
// where n is the first value from the
// list, and returns a reversed copy:
//   [7,2,3,4,5]
// returns
//   [5,4,3,2,7]
// prints:
//   draw 2 cards
func draw(x []int) []int {
	n := 0

	if len(x) > 0 {
		n = x[0] % 5
	}

	fmt.Printf("draw %d cards\n", n)

	r := []int{}
	for i := 0; i < len(x); i++ {
		v := x[len(x)-1-i]
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", draw([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
