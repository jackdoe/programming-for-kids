package main

import (
	"fmt"
)

const N_PLAYERS = 3

// Note: the reset() card can always be
// played, on top of any language.

// create a new list
// returns:
//   [0,0,0,0]
func reset() []int {
	r := []int{}

	for i := 0; i < 4; i++ {
		v := 0
		if N_PLAYERS == 2 {
			if i < 2 {
				v = -1
			} else {
				v = 1
			}
		}
		r = append(r, v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", reset())
}
