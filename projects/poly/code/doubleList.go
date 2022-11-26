package main

import (
	"fmt"
)

// returns new list, doubling each
// item, e.g.:
//   [1,2,3,4,5]
// returns:
//   [2,4,6,8,10]
func doubleList(x []int) []int {
	r := []int{}
	for _, v := range x {
		r = append(r, v*2)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", doubleList([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
