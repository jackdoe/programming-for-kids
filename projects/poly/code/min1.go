package main

import "fmt"

// returns the smallest integer from a
// list, e.g.:
//   [1,2,3,2]
// returns:
//   1
func min(x []int) int {
	m := 2147483647
	for _, v := range x {
		if v < m {
			m = v
		}
	}

	return m
}

func main() {
	fmt.Printf("%v\n", min([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
