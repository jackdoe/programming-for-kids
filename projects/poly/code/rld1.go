package main

import "fmt"

func rld(x []int) []int {
	r := []int{}

	for i := 0; i < len(x); i += 2 {
		for j := 0; j < x[i]; j++ {
			r = append(r, x[i+1])
		}
	}
	return r
}

func main() {
	fmt.Printf("%v", rld([]int{1, 3, 6, 5, 2, 3}))
}
