package main

import "fmt"

// deduplicate a list of integers
//   [1,1,3,2,1]
// returns:
//   [1,3,2]
func uniq(x []int) []int {
	r := []int{}
	seen := map[int]bool{}
	for _, v := range x {
		if !seen[v] {
			r = append(r, v)
			seen[v] = true
		}
	}

	return r
}

func main() {
	fmt.Printf("%v\n", uniq([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
