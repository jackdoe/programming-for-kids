package main

import "fmt"

func unmax(x []int) []int {
	max := 0
	for _, v := range x {
		if v > max {
			max = v
		}
	}
	r := []int{}

	for _, v := range x {
		if v != max {
			r = append(r, v)
		}
	}

	return r
}

func main() {
	fmt.Printf("%v", unmax([]int{1, 2, 1, 1, 1, 3, 1}))
}
