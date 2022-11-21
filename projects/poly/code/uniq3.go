package main

import (
	"fmt"
	"sort"
)

func uniq(x []int) []int {
	r := []int{}
	sort.Slice(x, func(i, j int) bool {
		return x[i] < x[j]
	})

	for _, v := range x {
		if len(r) == 0 || r[len(r)-1] != v {
			r = append(r, v)
		}
	}

	return r
}

func main() {
	fmt.Printf("%v", uniq([]int{1, 2, 1, 1, 1, 3, 1}))
}
