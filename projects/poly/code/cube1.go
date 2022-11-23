package main

import "fmt"

// cube each number in the list
//   [1,2,3]
// returns:
//   [1,8,27]
func cube(x []int) []int {
	r := []int{}
	for _, v := range x {
		r = append(r, v*v*v)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", cube([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
