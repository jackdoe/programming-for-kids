package main

import "fmt"

func uniq(x []int) []int {
	r := []int{}
	seen := map[int]bool{}

	for _, v := range x {
		s := seen[v]
		if !s {
			r = append(r, v)
			seen[v] = true
		}
	}

	return r
}

func main() {
	fmt.Printf("%v", uniq([]int{1, 2, 1, 1, 1, 3, 1}))
}
