package main

import "fmt"

// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
func uniq(x []int) []int {
	r := []int{}
	for _, v := range x {
		seen := false
		for _, v1 := range r {
			if v1 == v {
				seen = true
			}
		}

		if !seen {
			r = append(r, v)
		}
	}

	return r
}

func main() {
	fmt.Printf("%v\n", uniq([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
