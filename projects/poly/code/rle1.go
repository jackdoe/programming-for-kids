package main

import "fmt"

func rle(x []int) []int {
	r := []int{}

	for _, v := range x {
		if len(r) == 0 || r[len(r)-1] != v {
			r = append(r, 0)
			r = append(r, v)
		}
		r[len(r)-2] += 1
	}

	return r
}

func main() {
	fmt.Printf("%v", rle([]int{1, 1, 1, 1, 3, 1}))
}
