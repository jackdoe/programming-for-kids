package main

import (
	"fmt"
)

// Note: the reset() card can be played
// on top of any card.

// create a new list
// returns:
//   [0,0,0,0]
func reset() []int {
	r := []int{}

	for i := 0; i < 4; i++ {
		r = append(r, 0)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", reset())
}
