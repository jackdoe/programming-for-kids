package main

import "fmt"

// returns the biggest integer from a
// list, e.g.:
//   [1,2,3,2]
// returns:
//   3
func max(x []int) int {
	m := 0
	for _, v := range x {
		if v > m {
			m = v
		}
	}

	return m
}

func main() {
	fmt.Printf("%v\n", max([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
