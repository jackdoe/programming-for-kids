package main

import (
	"fmt"
	"sort"
)

// sort the list in ascending order
//   [1,4,2,3]
// returns:
//   [1,2,3,4]
func sort_asc(x []int) []int {
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

	fmt.Printf("%v\n", sort_asc([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
