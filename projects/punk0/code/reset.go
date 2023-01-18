package main

import (
	"fmt"
)

// create a new list
// with the value 0,0,0,0
// (ignores the input)
// returns:
//   [0,0,0,0]
func reset(x []int) []int {
	r := []int{}
	for i := 1; i <= 4; i++ {
		r = append(r, 0)
	}
	return r
}

func main() {

	fmt.Printf("%v\n", reset([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
