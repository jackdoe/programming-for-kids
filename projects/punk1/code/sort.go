package main

import (
	"fmt"
	"sort"
)

// sort the list in ascending order
//   [5,1,4,2,3]
// returns:
//   [1,2,3,4,5]
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
