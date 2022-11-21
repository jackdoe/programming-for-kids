package main

import "fmt"

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
	fmt.Printf("%v", uniq([]int{1, 2, 1, 1, 1, 3, 1}))
}
