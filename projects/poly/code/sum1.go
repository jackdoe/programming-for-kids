package main

import "fmt"

// sum all the integers from a list
//   [1,2,3]
// returns:
//   6
func sum(x []int) int {
	s := 0
	for _, v := range x {
		s += v
	}

	return s
}

func main() {
	fmt.Printf("%v\n", sum([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
