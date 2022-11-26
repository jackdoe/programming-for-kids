package main

import "fmt"

// return a new list without the first
// element, e.g.:
//   [1,2,3,2,3,1]
// returns:
//   [2,3,2,3,1]
func rest(x []int) []int {
	r := []int{}
	for i := 1; i < len(x); i++ {
		r = append(r, x[i])
	}

	return r
}

func main() {
	fmt.Printf("%v\n", rest([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
