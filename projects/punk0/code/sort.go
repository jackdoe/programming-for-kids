package main

import (
	"fmt"
	"sort"
)

// return a sorted copy of the list
//   [1,1,3,2,1]
// returns:
//   [1,1,1,2,3]
func sortL(x []int) []int {
	r := []int{}
	for _, v := range x {
		r = append(r, v)
	}

	sort.Slice(r, func(i, j int) bool {
		return r[i] < r[j]
	})

	return r
}

func main() {

	fmt.Printf("%v\n", sortL([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
