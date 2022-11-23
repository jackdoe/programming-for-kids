package main

import (
	"fmt"
	"sort"
)

// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
func uniq(x []int) []int {
	// WARNING: modifies the original list
	sort.Slice(x, func(i, j int) bool {
		return x[i] < x[j]
	})

	r := []int{}
	for _, v := range x {
		if len(r) == 0 || r[len(r)-1] != v {
			r = append(r, v)
		}
	}

	return r
}

func main() {
	fmt.Printf("%v\n", uniq([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
