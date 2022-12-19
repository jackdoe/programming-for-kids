package main

import "fmt"

// shift to the input list to the left,
// adding 0 at the end:
//   [1,2,3,4,5]
// returns:
//   [2,3,4,5,0]
func shift(x []int) []int {
	r := []int{}
	for i := 1; i < len(x); i++ {
		v := x[i]
		r = append(r, v)
	}

	r = append(r, 0)

	return r
}

func main() {
	fmt.Printf("%v\n", shift([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 9}))
}
