package main

import (
	"fmt"
)

// create a new list
// with the value 0,0,0,0
// returns:
//   [0,0,0,0]
func reset() []int {
	r := []int{}
	for i := 1; i <= 4; i++ {
		r = append(r, 0)
	}
	return r
}

func main() {
	fmt.Printf("%v\n", reset())
}
